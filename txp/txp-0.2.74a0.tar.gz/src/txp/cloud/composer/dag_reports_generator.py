import pytz
from airflow import DAG
from airflow.operators.dummy import DummyOperator
from airflow.operators.python import PythonOperator
from google.cloud import firestore, bigquery, storage
from txp.common.utils import firestore_utils, reports_utils
from cronsim import CronSim
import datetime
import os
import logging
from txp.common.config import settings
from fpdf import FPDF
from airflow import configuration

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()
logger.setLevel(logging.INFO)
#######################################################################################
# PARAMETERS
#######################################################################################

nameDAG = 'dag_reports_generator'
trigger_time = "0 11 * * *"
TEMP_FOLDER = configuration.get('core', 'dags_folder')

default_args = {
    'depends_on_past': True,
    'start_date': datetime.datetime(2021, 11, 5),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 2,
    'retry_delay': datetime.timedelta(minutes=1),
    'project_id': os.environ.get("GCP_PROJECT_ID", "tranxpert-mvp"),
    'dataset': os.environ.get("DATASET", "reports"),
    'reports_bucket': os.environ.get("REPORTS_BUCKET", "txp-reports")
}


# TODO: this 2 functions are going to be moved to a dataflow job.
#######################################################################################

def get_pdf_name(tenant_doc, report_id):
    datetime_format = settings.time.datetime_zoned_format.replace(" ", "_")
    return f'{tenant_doc["tenant_id"]}_{report_id}_{datetime.datetime.now(tz=pytz.UTC).strftime(datetime_format)}.pdf'


def build_pdf(tenant_doc, report_id, sections):
    logging.info(f'Building pdf for report: {report_id} of tenant: {tenant_doc["tenant_id"]} which contains ' \
                 f'{len(sections)} sections')
    pdf_name = get_pdf_name(tenant_doc, report_id)
    pdf_path = os.path.join(TEMP_FOLDER, pdf_name)

    pdf = reports_utils.build_report_pdf(tenant_doc, report_id, sections)
    pdf.output(pdf_path, 'F')

    logging.info(f'Built pdf for report: {report_id} of tenant: {tenant_doc["tenant_id"]} which contains '
                 f'{len(sections)} sections')

    storage_client = storage.Client()
    bucket = storage_client.bucket(default_args["reports_bucket"], user_project=default_args["project_id"])
    blob = bucket.blob(f"{tenant_doc['tenant_id']}/{report_id}/{pdf_name}")
    with open(pdf_path, 'rb') as pdf:
        blob.upload_from_file(pdf)
    if os.path.exists(pdf_path):
        os.remove(pdf_path)
    storage_client.close()


def get_sections_for_tenant(ti, tenant_doc, start_datetime, end_datetime):
    firestore_db = firestore.Client()
    bigquery_db = bigquery.Client()
    if "reports" in tenant_doc:
        for report_id in tenant_doc["reports"]:
            sections = reports_utils.get_report_sections(firestore_db, bigquery_db,
                                                         f"{default_args['dataset']}.sections",
                                                         tenant_doc["tenant_id"], report_id, start_datetime,
                                                         end_datetime)
            if sections is None:
                sections = []
            logging.info(f'On start date: {start_datetime} and end date: {end_datetime} '
                         f'for {tenant_doc["tenant_id"]} on report {report_id} there are {len(sections)} sections')
            build_pdf(tenant_doc, report_id, sections)
    firestore_db.close()
    bigquery_db.close()


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
        get_sections_for_tenant(ti, tenant, start_date, end_date)
    firestore_db.close()


#######################################################################################


with DAG(nameDAG,
         default_args=default_args,
         catchup=False,
         max_active_runs=3,
         schedule_interval=trigger_time) as dag:
    t_begin = DummyOperator(task_id="begin")

    run_report_jobs_for_tenants = PythonOperator(
        task_id='get_reports_sections',
        python_callable=run_report_jobs_for_tenants
    )

    t_end = DummyOperator(task_id="end")

    t_begin >> run_report_jobs_for_tenants >> t_end
