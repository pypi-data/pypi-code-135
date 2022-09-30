from enum import Enum
import json
import os
import logging
import threading
from typing import Optional
import copy

import botocore.exceptions
import torch
import torch.distributed as dist

import boto3

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

class BreezeState:
    def __init__(self):
        self.sampler = None
        self.loader = None
        self.model = None
        self.optimizer = None
        self.scheduler = None
        self.job_id = os.environ.get('LATTICE_RUN_ID', None)
        self.checkpoint_bucket = os.environ['LATTICE_CHECKPOINT_ENDPOINT']
        self.steps_per_checkpoint = int(os.environ['LATTICE_STEPS_PER_CHECKPOINT'])
        self.batch_size = 0
        self.world_size = dist.get_world_size()
        self.rank = dist.get_rank()

        checkpoint_endpoint_str = os.environ['LATTICE_CHECKPOINT_ENDPOINT']
        self._backend = get_checkpoint_backend(checkpoint_endpoint_str)
        # Right now we do not do anything special with the different backends
        # Just assume that it is S3
        self.checkpoint_bucket, self._path_name = parse_s3_endpoint(checkpoint_endpoint_str)
        self._base_key = f'{self._path_name}/{self.job_id}/checkpoint'

        logging.info('Creating s3')
        self.s3 = boto3.client('s3')

        self.total_epochs = int(os.environ['total_epochs'])
        self.actual_epoch = 0
        self.actual_step = 0
        self.epoch = 0
        self.step = 0
        self.trained_indices = 0

        self.upload_lock = threading.Lock()
        logging.info(f"BreezeState created for job {self.job_id}")

    def load_ref(self, sampler, loader, model, optimizer, scheduler: Optional = None):
        self.sampler = sampler
        self.loader = loader
        self.model = model
        self.optimizer = optimizer
        self.scheduler = scheduler

    def find_and_load_state(self):
        try:
            response = self.s3.get_object(Bucket=self.checkpoint_bucket, Key=f"{self._base_key}/ckpt.index")
            ckpt_info = json.loads(response['Body'].read())

            epoch = ckpt_info['epoch']
            step = ckpt_info['step']
            object_key = f"{self._base_key}/epoch_{epoch}_step_{step}.pt"
            logging.info(f"Found checkpoint for epoch {epoch} and step {step}")
            with open('/tmp/load_cp.pt', 'wb') as cp_data:
                self.s3.download_fileobj(
                    self.checkpoint_bucket,
                    object_key,
                    cp_data
                )
            state = torch.load('/tmp/load_cp.pt')

            self.actual_epoch = epoch
            self.actual_step = step
            self.trained_indices = state['trained_indices']
            self.sampler.trained_indices = self.trained_indices
            self.model.load_state_dict(state['model'])
            self.optimizer.load_state_dict(state['optimizer'])

            logging.info('Load checkpoint successful')
        except botocore.exceptions.ClientError:
            logging.info(f'No checkpoints found. Starting from scratch')
            return

    def preserve_state(self):
        if self.actual_step % self.steps_per_checkpoint == 0 and self.actual_step != 0:
            state = {
                'epoch': self.actual_epoch,
                'step': self.actual_step,
                'trained_indices': self.trained_indices,
                'model': self.model.state_dict(),
                'optimizer': self.optimizer.state_dict()
            }
            t = threading.Thread(target=self._preserve_state_worker,
                                 args=(state, self.actual_epoch, self.actual_step))
            t.start()

    def _preserve_state_worker(self, state, epoch, step):
        # skip upload if another thread is uploading
        # to avoid queueing upload tasks and miss the most recent checkpoint at preemption
        if self.upload_lock.locked():
            return
        state_copy = copy.deepcopy(state)
        self.upload_lock.acquire()
        logging.debug(f"Saving state to file")
        torch.save(state_copy, '/tmp/current_state.pt')

        logging.debug(f"Uploading state to s3")
        with open("/tmp/current_state.pt", "rb") as cp_data:
            self.s3.upload_fileobj(cp_data, self.checkpoint_bucket,
                                   f"{self._base_key}/epoch_{epoch}_step_{step}.pt")

        d = {'step': step, 'epoch': epoch}
        logging.debug('Setting index file')
        self.s3.put_object(Body=json.dumps(d), Bucket=self.checkpoint_bucket, Key=f"{self._base_key}/ckpt.index")
        self.upload_lock.release()

    def forward(self):
        self.step += 1
        self.actual_step += 1
        self.trained_indices += self.batch_size * self.world_size
        logging.info("Step: %d, Trained indices: %d", self.actual_step, self.trained_indices)
        if self.rank == 0:
            self.preserve_state()
