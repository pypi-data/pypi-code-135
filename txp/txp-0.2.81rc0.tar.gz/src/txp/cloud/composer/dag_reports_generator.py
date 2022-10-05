import pytz
from airflow import DAG
from airflow.operators.dummy import DummyOperator
from airflow.operators.python import PythonOperator
from google.cloud import firestore
from txp.common.utils import firestore_utils
from cronsim import CronSim
import datetime
import os
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()
logger.setLevel(logging.INFO)
#######################################################################################
# PARAMETERS
#######################################################################################

nameDAG = 'dag_reports_generator'

default_args = {
    'depends_on_past': True,
    'start_date': datetime.datetime(2021, 11, 5),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 2,
    'retry_delay': datetime.timedelta(minutes=1),
    'project_id': os.environ.get("GCP_PROJECT_ID", "tranxpert-mvp"),
    'dataset': os.environ.get("DATASET", "reports"),
    'reports_bucket': os.environ.get("REPORTS_BUCKET", "txp-reports"),
    'trigger_time': "0 11 * * *"
}


#######################################################################################

def run_report_jobs_for_tenants(ti):
    it = CronSim("0 11 * * *", default_args["start_date"])
    a = next(it)
    b = next(it)
    delta = b - a
    delta_minutes = int(delta.total_seconds() / 60)
    firestore_db = firestore.Client()
    end_date = datetime.datetime.now(tz=pytz.UTC)
    start_date = end_date - datetime.timedelta(minutes=delta_minutes)
    all_tenants = firestore_utils.get_all_tenants_from_firestore(firestore_db)
    for tenant in all_tenants:
        logging.info(f"Deploying batch pipeline in interval [{start_date}, {end_date}]"
                     f"tenant_id: {tenant['tenant_id']}")
        yield tenant['tenant_id']
    firestore_db.close()


#######################################################################################

def some_shit(element):
    print("juan por aqui")
    print(element)


with DAG(nameDAG,
         default_args=default_args,
         catchup=False,
         max_active_runs=3,
         schedule_interval=default_args["trigger_time"]) as dag:
    t_begin = DummyOperator(task_id="begin")

    run_report_jobs_for_tenants = PythonOperator(
        task_id='get_reports_sections',
        python_callable=run_report_jobs_for_tenants
    )

    some_shit = PythonOperator(
        task_id='get_reports_sections',
        python_callable=some_shit
    )

    t_end = DummyOperator(task_id="end")

    t_begin >> run_report_jobs_for_tenants >> some_shit >> t_end
