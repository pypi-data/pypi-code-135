from importlib.resources import path
import boto3
import botocore.exceptions
import copy
from enum import Enum
import json
import logging
import os
from typing import Any, Dict
import types
from typing import Iterator

import torch
import pytorch_lightning as pl
from pytorch_lightning.trainer.states import TrainerFn
from pytorch_lightning.callbacks import Callback
from pytorch_lightning.utilities.types import STEP_OUTPUT
from pytorch_lightning.overrides.distributed import DistributedSamplerWrapper

class CheckpointBackend(Enum):
    S3 = 1

def get_checkpoint_backend(endpoint_str):
    if endpoint_str.startswith('s3://'):
        return CheckpointBackend.S3
    else:
        raise NotImplementedError("Currently only S3 checkpoints are supported. Please provide a checkpoint endpoint of the form 's3://bucket/path/'")

# Assumption: if using S3 backend, endpoint_str starts with "s3://"
def parse_s3_endpoint(endpoint_str):
    # Find the index of the first '/' character AFTER "s3://"
    path_index = endpoint_str[5:].find('/') + 5
    bucket_name = endpoint_str[5:path_index]
    path_name = endpoint_str[path_index + 1:]
    if path_name.endswith('/'):
        path_name = path_name[:-1]

    return bucket_name, path_name

class ElasticityProvider(Callback):
    def __init__(self, batch_size):
        self._rdzv_id = os.environ.get('LATTICE_RUN_ID', None)
        assert self._rdzv_id is not None, "Make sure there is a rdzv id set through Lattice"

        self._every_n_steps = os.environ.get('LATTICE_STEPS_PER_CHECKPOINT', None)
        assert self._every_n_steps is not None
        self._every_n_steps = int(self._every_n_steps)

        checkpoint_endpoint_str = os.environ.get('LATTICE_CHECKPOINT_ENDPOINT', None)
        assert checkpoint_endpoint_str is not None, "Please provide a checkpoint endpoint to the ElasticityProvider through the `LATTICE_CHECKPOINT_ENDPOINT` environment variable"
        self._backend = get_checkpoint_backend(checkpoint_endpoint_str)
        # Right now we do not do anything special with the different backends
        # Just assume that it is S3
        self._bucket, self._path_name = parse_s3_endpoint(checkpoint_endpoint_str)
        self._s3 = boto3.client('s3')

        self._base_s3_key = f'{self._path_name}/{self._rdzv_id}/checkpoint'

        self._batch_size = batch_size

    def _increment_values(self, d: Dict):
        for k in d.keys():
            if not isinstance(d[k], dict):
                continue

            for state_key in d[k].keys():
                d[k][state_key] += 1

    def _fix_batch_alignment(self, loop_state_dict):
        """
            Fix discrepancy between saved checkpoint step
            and Progress state step
        """
        fit_loop_state = loop_state_dict['fit_loop']
        fit_loop_state['epoch_loop.state_dict']['_batches_that_stepped'] += 1

        self._increment_values(fit_loop_state['epoch_loop.batch_progress'])
        self._increment_values(fit_loop_state['epoch_loop.scheduler_progress'])
        self._increment_values(
            fit_loop_state['epoch_loop.batch_loop.optimizer_loop.optim_progress']['optimizer']['step'])
        self._increment_values(
            fit_loop_state['epoch_loop.batch_loop.optimizer_loop.optim_progress']['optimizer']['zero_grad'])

        return loop_state_dict

    def _wrap_sampler(self, sampler: DistributedSamplerWrapper):
        # DistribuedSamplerWrapper inherited from DistributedSampler
        def init(self):
            self.is_altered = True

            self.epoch = 0
            self.remaining_indices = []
            self.processed_num = 0
            self.loaded_epoch = -1

            self.reset()

        def set_epoch(self, epoch):
            """Sets the epoch for this sampler.

            When `shuffle=True`, this ensures all replicas use a different random ordering
            for each epoch.

            Will clear and reset the `processed_indices` for the next epoch. It is important
            that this is called at the end of the epoch (not the beginning) to ensure that
            partially completed epochs do not reprocess samples.

            Args:
                epoch: Epoch number.
            """
            self.epoch = epoch
            if self.epoch == self.loaded_epoch:
                return
            self.processed_num = 0
            self.reset()

        def record_batch(self, batch_idx, batch_size):
            """Record the number of processed samples."""
            self.processed_num += batch_size * self.num_replicas

        def load_state_dict(self, state_dict):
            self.epoch = state_dict["epoch"]
            self.loaded_epoch = state_dict["epoch"]
            self.processed_num = state_dict["processed_num"]
            self.reset(override=True)

        def state_dict(self):
            return dict(
                epoch=self.epoch,
                processed_num=self.processed_num
            )

        def __iter__(self) -> Iterator:
            if not hasattr(self, "is_altered"):
                self.dataset.reset()
                return (self.dataset[index] for index in super(DistributedSamplerWrapper, self).__iter__())
            # remaining_indices set in reset()
            return iter(self.remaining_indices)

        def __len__(self):
            return self.num_samples

        def reset(self, override=False):
            if self.epoch == self.loaded_epoch and not override:
                return

            # Exclude any samples we have already processed this epoch
            all_indices = list(self.dataset[index] for index in super(DistributedSamplerWrapper, self).__iter__())
            self.remaining_indices = all_indices[self.processed_num // self.num_replicas:]

        sampler.init = types.MethodType(init, sampler)
        sampler.set_epoch = types.MethodType(set_epoch, sampler)
        sampler.record_batch = types.MethodType(record_batch, sampler)
        sampler.load_state_dict = types.MethodType(load_state_dict, sampler)
        sampler.state_dict = types.MethodType(state_dict, sampler)
        sampler.reset = types.MethodType(reset, sampler)
        DistributedSamplerWrapper.__iter__ = __iter__
        DistributedSamplerWrapper.__len__ = __len__

        sampler.init()

    def _find_and_load_state(self, trainer: "pl.Trainer", pl_module: "pl.LightningModule"):
        try:
            response = self._s3.get_object(Bucket=self._bucket, Key=f'{self._base_s3_key}/ckpt.index')
            ckpt_info = json.loads(response['Body'].read())

            epoch = ckpt_info['epoch']
            step = ckpt_info['step']
            object_key = f'checkpoint/epoch_{epoch}_step_{step}.pt'
            logging.info(f'Found checkpoint for epoch {epoch} and step {step}')
            with open('/tmp/load_cp.pt', 'wb') as cp_data:
                self._s3.download_fileobj(
                    self._bucket,
                    object_key,
                    cp_data
                )

            state = torch.load('/tmp/load_cp.pt')

            fit_loop = trainer.fit_loop
            batch_loop = fit_loop.epoch_loop.batch_loop
            if pl_module.automatic_optimization:
                batch_loop.optimizer_loop.optim_progress.optimizer.step.total.completed = step
            else:
                batch_loop.manual_loop.optim_step_progress.total.completed = step

            fit_loop.epoch_progress.current.completed = epoch
            fit_loop.epoch_progress.current.processed = epoch

            assert trainer.state.fn is not None
            state_dict = state.get("loops")
            if state_dict is not None:
                if trainer.state.fn in (TrainerFn.FITTING, TrainerFn.TUNING):
                    state_dict = self._fix_batch_alignment(state_dict)
                    fit_loop.load_state_dict(state_dict["fit_loop"])
                elif trainer.state.fn == TrainerFn.VALIDATING:
                    trainer.validate_loop.load_state_dict(state_dict["validate_loop"])
                elif trainer.state.fn == TrainerFn.TESTING:
                    trainer.test_loop.load_state_dict(state_dict["test_loop"])
                elif trainer.state.fn == TrainerFn.PREDICTING:
                    trainer.predict_loop.load_state_dict(state_dict["predict_loop"])

            pl_module.load_state_dict(state['model'])
            pl_module.optimizers().load_state_dict(state['optim'])
            trainer.train_dataloader.sampler.load_state_dict(state['sampler'])

            logging.info('Load checkpoint successful')
        except botocore.exceptions.ClientError:
            logging.info(f'No checkpoints found. Starting from scratch')
            return

    def on_train_start(self, trainer: "pl.Trainer", pl_module: "pl.LightningModule") -> None:
        # code.interact(local=locals())
        if trainer.train_dataloader.sampler is not None and isinstance(trainer.train_dataloader.sampler,
                                                                       DistributedSamplerWrapper):
            self._wrap_sampler(trainer.train_dataloader.sampler)
        self._find_and_load_state(trainer, pl_module)

    def _preserve_state_worker(self, epoch, step, state_dict) -> None:
        logging.debug('Saving to file')
        sd_copy = copy.deepcopy(state_dict)
        torch.save(sd_copy, '/tmp/current_state.pt')

        logging.debug('Uploading to S3...')
        with open('/tmp/current_state.pt', 'rb') as cp_data:
            self._s3.upload_fileobj(
                cp_data, self._bucket,
                f'{self._base_s3_key}/epoch_{epoch}_step_{step}.pt'
            )

        d = {'step': step, 'epoch': epoch}
        logging.debug('Setting index file')
        self._s3.put_object(Body=json.dumps(d),
                            Bucket=self._bucket, Key=f'{self._base_s3_key}/ckpt.index')

    def _preserve_state(self, trainer: "pl.Trainer", pl_module: "pl.LightningModule", epoch: int = -1,
                        step: int = -1) -> None:
        if trainer.global_rank != 0:
            return

        epoch = trainer.current_epoch if epoch == -1 else epoch
        step = trainer.global_step if step == -1 else step

        all_state = {
            'loops': trainer._checkpoint_connector._get_loops_state_dict(),
            'model': pl_module.state_dict(),
            'optim': pl_module.optimizers().state_dict(),
            'sampler': trainer.train_dataloader.sampler.state_dict(),
            'step': step,
            'epoch': epoch,
        }

        self._preserve_state_worker(epoch, step, all_state)

    def on_train_batch_end(self, trainer: "pl.Trainer", pl_module: "pl.LightningModule", outputs: STEP_OUTPUT,
                           batch: Any, batch_idx: int) -> None:
        trainer.train_dataloader.sampler.record_batch(trainer.global_step, self._batch_size)

        if trainer.global_step % self._every_n_steps == 0:
            self._preserve_state(trainer, pl_module)

    def on_epoch_end(self, trainer: "pl.Trainer", pl_module: "pl.LightningModule") -> None:
        # When this is first called there is no sampler or dataloader which will raise
        # an AttributeError so ignore the first time
        try:
            # trainer.train_dataloader.sampler.reset()
            if trainer.current_epoch != 0 and trainer.global_step != 0:
                self._preserve_state(trainer, pl_module, trainer.current_epoch + 1, 0)
        except AttributeError:
            return
