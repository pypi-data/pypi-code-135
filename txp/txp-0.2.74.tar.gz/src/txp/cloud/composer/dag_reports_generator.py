from airflow import DAG
from airflow.operators.dummy import DummyOperator
from airflow.operators.python import PythonOperator

from cronsim import CronSim
import datetime
import os
import pytz

#######################################################################################
# PARAMETERS
#######################################################################################

nameDAG = 'dag_reports_generator'
trigger_time = "0 11 * * *"

default_args = {
    'depends_on_past': True,
    'start_date': datetime.datetime.now(tz=pytz.UTC),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 2,
    'retry_delay': datetime.timedelta(minutes=1),
    'project_id': os.environ.get("GCP_PROJECT_ID", "tranxpert-mvp"),
    'dataset': os.environ.get("DATASET", "telemetry_test"),
}


#######################################################################################

def get_reports_sections(ds, **kwargs):
    it = CronSim("0 11 * * *", default_args["start_date"])
    a = next(it)
    b = next(it)
    delta = b - a
    delta_minutes = int(delta.total_seconds() / 60)
    ds.xcom_push(key='delta_minutes', value=delta_minutes)
    print(f"get reports sections {delta_minutes}")


#######################################################################################

def build_pdf(ds, **kwargs):
    delta_minutes = ds.xcom_pull(key='delta_minutes', task_ids='get_reports_sections')
    print(f"build pdf {delta_minutes}")
    pass


#######################################################################################


with DAG(nameDAG,
         default_args=default_args,
         catchup=False,
         max_active_runs=3,
         schedule_interval=trigger_time) as dag:
    t_begin = DummyOperator(task_id="begin")

    get_reports_sections = PythonOperator(
        task_id='get_reports_sections',
        python_callable=get_reports_sections
    )

    build_pdf = PythonOperator(
        task_id='build_pdf',
        python_callable=build_pdf
    )

    t_end = DummyOperator(task_id="end")

    t_begin >> get_reports_sections >> build_pdf >> t_end
