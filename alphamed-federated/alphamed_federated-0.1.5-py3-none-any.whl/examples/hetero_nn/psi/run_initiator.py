import os
import sys

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
PYTHONPATH = os.path.join(CURRENT_DIR, os.pardir, os.pardir, os.pardir, os.pardir)
sys.path.insert(0, PYTHONPATH)


if True:
    from alphafed import logger
    from alphafed.examples.hetero_nn.psi.demos import (AGGREGATOR_ID,
                                                       DATA_OWNER_3_ID,
                                                       DATA_OWNER_4_ID,
                                                       DATA_OWNER_5_ID,
                                                       get_ids, get_task_id)
    from alphafed.hetero_nn.psi import RSAPSIInitiatorScheduler


ids = get_ids()
logger.info(f'local ids: {ids}')
initiator_scheduler = RSAPSIInitiatorScheduler(
    task_id=get_task_id(),
    initiator_id=AGGREGATOR_ID,
    ids=ids,
    collaborator_ids=[DATA_OWNER_3_ID, DATA_OWNER_4_ID, DATA_OWNER_5_ID]
)
initiator_scheduler._data_channel._ports = [i for i in range(21000, 21010)]
intersection = initiator_scheduler.make_intersection()
logger.info(f'intersection ids: {intersection}')
