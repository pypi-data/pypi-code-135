'''


'''
import logging
import os
import shutil
from copy import deepcopy as dcopy

import torch
import torch.optim as optim
import torch.utils.data as D

import tools # since T is used as a variable in this module, refrain from "import tools as T"
import tools.torch
import tools.modules

from . import validation as V
from . import utils as U
from . import plot as P

__all__ = [
'Node'
]

# %%
log = logging.getLogger(__name__)

# %%
class Node:
    '''Local Node for training'''
    def __init__(self, model, dataset=None, cfg_train={}, criterion=None, model_dir=None, node_dir=None, validation=None, earlystopper=None, name='default', verbose=True, amp=False, reproduce=True):
        '''
        :param model: torch.nn.Module object
        :param dataset: torch.utils.data.Dataset object
            This dataset is used for training.
            Recommended return format from dataset is: {'x': x, 'y': y}
            where 'x' is the input, and 'y' is the target values.

        :param validation: dict of Validation objects

        :param cfg_train: dict-like object which contains:
            lr
            batch_size
            weight_decay (optional)
            patience (optional)

        :param criterion: torch.nn.Module object, used to compute loss function

        Recommended way of making hs.node.Node object is like the following:

            kwargs = {'model': model, 'dataset': train_dataset, 'validation': None, 'cfg_train': cfg.train,
                    'criterion': criterion, 'model_dir': path['model'], 'node_dir': path['node'], 'verbose': True, 'amp': True}
            node = hs.node.Node(**kwargs)
        '''
        # Store configurations
        self.model = model
        self.dataset = dataset
        self.cfg_train = dcopy(dict(cfg_train))
        self.criterion = criterion
        self.model_dir = model_dir
        self.node_dir = node_dir
        self.validation = validation if issubclass(type(validation), dict) or validation is None else V.VDict({'default': validation}) # wrap with VDict if single validation object is given.
        self.earlystopper = earlystopper
        self.name = name
        self.verbose = verbose
        self.amp = amp
        self.reproduce = reproduce

        # Initializations
        if self.model_dir is not None:
            if os.path.exists(self.model_dir): log.warning(f'path: {self.model_dir} exists. Be careful')
            os.makedirs(self.model_dir, exist_ok=True)

        if self.node_dir is not None:
            if os.path.exists(self.node_dir): log.warning(f'path: {self.node_dir} exists. Be careful')
            os.makedirs(self.node_dir, exist_ok=True)

        if self.validation is None and self.earlystopper is not None: log.warning('validation is None but earlystopper is given. earlystopper will be ignored')
        if self.earlystopper is not None:
            assert earlystopper.target_validation in self.validation.keys(), 'earlystopper.target_valiation not provided in validation'

        self.train_meter = tools.modules.AverageMeter() # Tracks loss per epoch
        self.loss_tracker = tools.modules.ValueTracker() # Tracks loos over all training
        self.set_misc()
        self.reset()

        self._targets_type = self.infer_targets_type()

    def reset(self):
        self.iter = 0
        self.n_batch=0

    def print(self, content):
        if self.verbose:
            print(content)
        else:
            log.info(content)

    def set_misc(self):
        '''Set miscellaneous variables'''
        self.misc = tools.TDict()
        if self.dataset is not None:
            if hasattr(self.dataset, 'get_f'): # get_f equal to preprocessing pipeline before deep learning model
                self.print('get_f found in loader.dataset')
                self.misc.get_f = self.dataset.get_f

    def validate(self):
        if self.validation is not None:
            score_summary = {}
            for cv_name, validation in self.validation.items(): # Different types of datasets
                score = validation.step(self)
                score_summary[cv_name] = score
                self.print(f'[cv_name: {cv_name}] Validation Score: {score}')
            if self.earlystopper is not None:
                patience_end = self.earlystopper.step(self, score_summary, os.path.join(self.model_dir, f'model_{self.iter}.pt'))
                if patience_end:
                    self.print('patience met, flushing earlystopper history')
                    self.earlystopper.history.reset()
            else:
                patience_end = False
        return patience_end

    def generate_loader(self):
        if self.dataset is not None:
            reproduce_kwargs = U.reproducible_worker_dict() if self.reproduce else {}
            drop_last = len(self.dataset) % self.cfg_train['batch_size'] == 1 # To avoid batch normalization layers from raising exceptions
            self.loader = D.DataLoader(self.dataset, batch_size=self.cfg_train['batch_size'], shuffle=True, drop_last=drop_last, **reproduce_kwargs)
            # self.loader = D.DataLoader(self.dataset, batch_size=self.cfg_train['batch_size'], shuffle=True, drop_last=True, **U.reproducible_worker_dict()) if len(self.dataset) % self.cfg_train['batch_size'] == 1 \
            #         else D.DataLoader(self.dataset, batch_size=self.cfg_train['batch_size'], shuffle=True, drop_last=False, **U.reproducible_worker_dict())
        else:
            log.warning('No dataset found. Skipping generate_loader()')

    def train(self, epoch=None, new_op=True, no_val=False, step=None, reset_loss_tracker=False):
        '''
        Trains the model with the specified duration.
        '''
        assert epoch is None or step is None, f'only one of epoch or step can be specified. received epoch: {epoch}, step: {step}'
        if step is None:
            horizon = 'epoch'
            if epoch is None: # When neither epoch or step are specified
                assert 'epoch' in self.cfg_train, 'key "epoch" must be provided in cfg_train, or the argument "epoch" must be provided \
                                                when argument "step" is not specified.'
                epoch = self.cfg_train['epoch']
            log.debug(f'[Node: {self.name}] train for {epoch} epochs')
        else:
            assert epoch is None, f'Either epoch or step must be specified. Received epoch: {epoch}, step: {step}'
            horizon = 'step'
            step = step
            log.debug(f'[Node: {self.name}] train for {step} steps')

        self.model.train()
        device = tools.torch.get_device(self.model)
        self.criterion = self.criterion.to(device)
        if reset_loss_tracker: self.loss_tracker.reset()
        self.generate_loader()
        '''
        There may be one or more loaders, but self.loader is the standard of synchronization
        Either return multiple values from dataset, or modify self.forward to use other loaders
        '''

        if self.validation is not None:
            if 'cv_step' not in self.cfg_train:
                self.print('Node.validation given, but "cv_step" not specified in cfg_train. Defaults to 1 epoch')
                self.cfg_train['cv_step'] = len(self.loader)
            self.validation.reset()
            self.validate() # initial testing

        # Make new optimizer
        if new_op or not hasattr(self, 'op'):
            if not hasattr(self, 'op') and not new_op:
                log.warning("new_op=False when there's no pre-existing optimizer. Ignoring new_op...")
            # Weight decay optional
            self.op = optim.Adam(self.model.parameters(), lr=self.cfg_train['lr'], weight_decay=self.cfg_train['weight_decay']) if 'weight_decay' in self.cfg_train \
                        else optim.Adam(self.model.parameters(), lr=self.cfg_train['lr'])
            # self.op = optim.Adam(self.model.parameters(), **self.cfg_train)

        if horizon == 'epoch':
            self._step_epoch(T=epoch, no_val=no_val, device=device)
        elif horizon=='step':
            self._step_step(T=step, no_val=no_val, device=device)

        # TODO: Return criterion back to its original device, meaning we have to store its previous device info
        self.criterion = self.criterion.cpu()
        return self.loss_tracker

    def _step_epoch(self, T, no_val=False, device=None):
        self._device = device if device is not None else tools.torch.get_device(self.model)

        _iter = 0
        for epoch in range(1, T+1):
            self.train_meter.reset()
            self.epoch_f()
            for batch_i, data in enumerate(self.loader, 1):
                self.iter += 1
                _iter += 1
                loss = self._update(data)
                self.print(f'[Node: {self.name}][iter_sum: {self.iter}][Epoch: {epoch}/{T}][Batch: {batch_i}/{len(self.loader)}][Loss: {loss:.7f} (Avg: {self.train_meter.avg:.7f})]')
                self.loss_tracker.step(self.iter, loss)

                # Validation
                if (self.validation is not None) and (not no_val) and (_iter % self.cfg_train['cv_step']==0):
                    patience_end = self.validate()
                    if patience_end: # If patience has reached, stop training
                        self.print('Patience met, stopping training')
                        return None # return None since double break is impossible in python

    def _step_step(self, T, no_val=False, device=None):
        self._device = device if device is not None else tools.torch.get_device(self.model)
        if hasattr(self, '_loader_inst'): del self._loader_inst

        for _iter in range(1, T+1):
            # Get Data
            try:
                if hasattr(self, '_loader_inst'):
                    data = next(self._loader_inst)
                    self.n_batch += 1
                else:
                    raise StopIteration
            except StopIteration as e:
                self.train_meter.reset()
                self.epoch_f()
                self._loader_inst = iter(self.loader)
                data = next(self._loader_inst)
                self.n_batch = 1

            self.iter += 1
            loss = self._update(data)
            self.print(f'[Node: {self.name}][iter_sum: {self.iter}][Iter: {_iter}/{T}][Batch: {self.n_batch}/{len(self.loader)}][Loss: {loss:.7f} (Avg: {self.train_meter.avg:.7f})]')

            self.loss_tracker.step(self.iter, loss)

            # Validation
            if (self.validation is not None) and (not no_val) and (_iter % self.cfg_train['cv_step']==0):
            # if (not no_val) and (self.iter % self.cfg_train.cv_step==0):
                patience_end = self.validate()
                if patience_end: # If patience has reached, stop training
                    self.print('Patience met, stopping training')
                    return None # return None since double break is impossible in python

    def _update(self, data):
        '''
        Pseudo function to support amp (automatic mixed precision)
        '''
        if self.amp:
            # Mixed precision for acceleration
            with torch.autocast(device_type=self._device.type):
                return self.update(data)
        else:
            return self.update(data)

    def update(self, data):
        """
        - Perform single update (forward/backward pass + gradient descent step) with the given data.
        - Store loss in self.train_meter
        - This is where a lot of errors happen, so there's a pdb to save time.
          When there's error, use pdb to figure out the shape, device, tensor dtype, and more.

        Parameters
        ----------
        data : tuple, list, or dict of tensors (Batch of data)
            This is received from a torch.utils.Data.DataLoader
            Depending on the given format, the data is fed to the forwad pass

        Returns
        -------
        loss : float
        """
        try:
            data_pred, N = self._forward(data)
            loss = self._criterion(data_pred)

            self.op.zero_grad()
            loss.backward()
            self.op.step()

            loss = loss.item()
            self.train_meter.step(loss, N)
            return loss

        except Exception as e:
            log.warning(e)
            import pdb; pdb.set_trace()

    def _forward(self, data):
        '''
        Pseudo function to support amp (automatic mixed precision)
        '''
        # When data is given as a tuple/list
        if type(data) is tuple or type(data) is list:
            data = [x.to(self._device) for x in data]
            N = len(data[0]) # number of data in batch
            data_pred = self.forward(*data)

        # When data is given as a dict
        elif type(data) is dict:
            data = {key: value.to(self._device) for key, value in data.items()}
            N = len(next(iter(data))) # number of data in batch
            data_pred = self.forward(**data)

        else:
            raise Exception(f'return type from dataset must be one of [tuple, list, dict], received: {type(data)}')
        return data_pred, N

    def forward(self, x, y):
        """
        Forward pass. Receive data and return the loss function.
        Inherit Node and define new forward() function to build custom forward pass.

        May return tuple or dictionary, whichever will be feeded to criterion.
        """

        y_hat = self.model(x)

        return y_hat, y

    def _criterion(self, data_pred):
        if type(data_pred) is tuple or type(data_pred) is list:
            loss = self.criterion(*data_pred)
        elif type(data_pred)==dict:
            loss = self.criterion(**data_pred)
        else:
            raise Exception(f'return type from forward must be one of [tuple, list, dict], received: {type(data_pred)}')
        return loss

    def epoch_f(self):
        # TODO: rename to forward hook? epoch_hook?
        '''function to call every other epoch. May be used in subclass nodes'''
        pass

    def infer_targets_type(self):
        if self.dataset is not None and hasattr(self.dataset, 'targets_type'):
            return self.dataset.targets_type
        elif self.validation is not None and 'val' in self.validation:
            if type(self.validation['val'].dataset)==list:
                return self.validation['val'].dataset[0].targets_type
            else:
                return self.validation['val'].dataset.targets_type
        else:
            return None

    def post_train(self, val_dataset=None):
        # Deafult to self.validation['val'].dataset
        if val_dataset is None:
            assert 'val' in self.validation, f'if no val_dataset is given, then "val" must exist in self.validation: {self.validation.keys()}'
            val_dataset = self.validation['val'].dataset

        if self._targets_type == 'binary':
            self.print(f'[Node: {self.name}][post_train] binary classfication: choose threshold based on validation set')
            self.threshold = E.binary_threshold(self, val_dataset)
        else:
            self.print(f'[Node: {self.name}][post_train] no post-train procedure for _targets_type: {self._targets_type}')

    '''
    Save/Load functions
    state_dict()
    load_state_dict()

    save()
    save_best()
    load()
    '''
    def state_dict(self):
        state_dict = {
        'loss_tracker': self.loss_tracker,
        } # tools.TDict raises error when called in tools.save_pickle
        if 'get_f' in self.misc:
            state_dict['misc.get_f'] = self.misc.get_f
        if hasattr(self, 'threshold'):
            state_dict['threshold'] = self.threshold
        if self.validation is not None:
            state_dict['validation.history'] = {name: validation.history for name, validation in self.validation.items()}
        return state_dict

    def load_state_dict(self, state_dict):
        state_dict = dcopy(state_dict)

        if 'misc.get_f' in state_dict.keys():
            self.print(f'Updating get_f: {state_dict["misc.get_f"]}')
            self.misc.get_f = state_dict['misc.get_f']
            if self.dataset is not None:
                self.print('updating get_f to loader...')
                self.dataset.get_f = self.misc.get_f
            del state_dict['misc.get_f']

        if 'threshold' in state_dict.keys():
            self.print(f'Updating threshold: {state_dict["threshold"]}')
            self.threshold = state_dict['threshold']
            del state_dict['threshold']

        self.__dict__.update(state_dict) # update attributes

    def save(self, path=None, best=True):
        '''
        Save the following:
        state_dict() -> path/state_dict.p
        model.state_dict() -> path/model.pt
        '''
        path = self.node_dir if path is None else path
        self.print(f'[Node: {self.name}]')

        state_dict_path = os.path.join(path, 'node.p')
        self.print(f'[save] Saving node info to: {state_dict_path}')
        state_dict = self.state_dict()
        self.print(f'[save] state_dict: {list(state_dict.keys())}')
        tools.save_pickle(state_dict, state_dict_path)

        model_path = os.path.join(path, 'model.pt')
        if best:
            if self.earlystopper is None:
                self.print(f'[save][best: {best}] earlystopper not defined. Saving current model -> [{model_path}]')
                torch.save(self.model.state_dict(), model_path)
            else:
                if self.earlystopper.best_model != None:
                    self.print(f'[save][best: {best}] Saving [{self.earlystopper.best_model}] -> [{model_path}]')
                    shutil.copy(self.earlystopper.best_model, model_path)
                else:
                    self.print(f'[save][best: {best}] no best_model in self.earlystopper, Saving current model -> [{model_path}]')
                    torch.save(self.model.state_dict(), model_path)
        else:
            self.print(f'[save][best: {best}] Saving model to: {model_path}')
            torch.save(self.model.state_dict(), model_path)

    def load(self, path=None):
        '''
        load state_dict() and model:
        path/node.p -> state_dict
        path/model.pt -> model.state_dict
        '''
        path = self.node_dir if path is None else path
        self.print(f'[Node: {self.name}]')

        state_dict_path = os.path.join(path, 'node.p')
        self.print(f'[load] Loading from path: {state_dict_path}')
        state_dict = tools.load_pickle(state_dict_path)
        self.print(f'[load] Updating: {list(state_dict.keys())}')
        self.load_state_dict(state_dict)

        model_path = os.path.join(path, 'model.pt')
        self.print(f'[load] Loading model from: {model_path}')
        self.model.load_state_dict(torch.load(model_path))
