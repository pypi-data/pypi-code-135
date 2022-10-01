import os
import sys

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
PYTHONPATH = os.path.join(CURRENT_DIR, os.pardir, os.pardir)
sys.path.insert(0, PYTHONPATH)

if True:
    from alphafed.contractor import TaskMessageContractor
    from alphafed import DEV_TASK_ID, logger


contractor = TaskMessageContractor(task_id=DEV_TASK_ID)
logger.info('begin to clean ...')
for _ in contractor.contract_events():
    print('clean 1 msg')
