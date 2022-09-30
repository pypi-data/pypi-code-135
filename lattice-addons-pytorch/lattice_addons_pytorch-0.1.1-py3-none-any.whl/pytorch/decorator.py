from typing import Callable, Optional

from lattice_addons.pytorch.state import BreezeState

from lattice_addons.pytorch.wrappers.sampler import BreezeDistributedSampler
from lattice_addons.pytorch.wrappers.dataloader import BreezeDataLoader
from lattice_addons.pytorch.wrappers.optimizer import BreezeOptimizer
from lattice_addons.pytorch.wrappers.scheduler import BreezeScheduler
from lattice_addons.pytorch.wrappers.module import BreezeDistributedDataParallel

import logging


def run(func: Callable):
    """Decorator used to wrap all classes and allow model to have reference to each object
    """

    def wrapper(model, sampler, loader, optimizer, lr_scheduler: Optional = None, *args, **kwargs):
        breeze_state = BreezeState()
        breeze_sampler = BreezeDistributedSampler(breeze_state, sampler)
        breeze_loader = BreezeDataLoader(breeze_state, loader, breeze_sampler)
        breeze_model = model
        # BreezeDistributedDataParallel(breeze_state, model)
        breeze_optimizer = BreezeOptimizer(breeze_state, optimizer)
        breeze_scheduler = BreezeScheduler(breeze_state, lr_scheduler)
        breeze_state.load_ref(breeze_sampler, breeze_loader, breeze_model, breeze_optimizer, breeze_scheduler)
        breeze_state.find_and_load_state()

        logging.info("lte.run wrapped")
        return func(model=breeze_model, sampler=breeze_sampler, loader=breeze_loader, optimizer=breeze_optimizer,
                    lr_scheduler=breeze_scheduler, *args, **kwargs)

    return wrapper
