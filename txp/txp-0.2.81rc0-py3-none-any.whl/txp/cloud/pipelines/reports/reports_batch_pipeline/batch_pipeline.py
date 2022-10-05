import argparse
import logging
import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions
from google.cloud import firestore, bigquery
from txp.common.utils import firestore_utils, reports_utils
from txp.common.config import settings
from txp.cloud.pipelines.reports.reports_batch_pipeline import transformers as ts
import datetime
import os

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()
logger.setLevel(logging.INFO)

BIGQUERY_TABLE = "PROJECT_ID:DATASET_NAME.TABLE_NAME"
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "../../../../common/credentials/pub_sub_to_bigquery_credentials.json"


def get_all_sections(dataset, tenant_id, start_time, end_time):
    dataset = dataset.replace(":", ".")
    start_datetime = datetime.datetime.strptime(start_time, settings.time.datetime_zoned_format)
    end_datetime = datetime.datetime.strptime(end_time, settings.time.datetime_zoned_format)
    firestore_db = firestore.Client()
    bigquery_db = bigquery.Client()
    tenant_doc = firestore_utils.pull_tenant_doc(firestore_db, tenant_id).to_dict()
    if "reports" in tenant_doc:
        for report_id in tenant_doc["reports"]:
            sections = reports_utils.get_report_sections(firestore_db, bigquery_db,
                                                         f"{dataset}.sections",
                                                         tenant_doc["tenant_id"], report_id, start_datetime,
                                                         end_datetime)
            if sections is None:
                continue
            logging.info(f'On start date: {start_datetime} and end date: {end_datetime} '
                         f'for {tenant_doc["tenant_id"]} on report {report_id} there are {len(sections)} sections')
            yield report_id, sections
    firestore_db.close()
    bigquery_db.close()


def run():
    parser = argparse.ArgumentParser()
    parser.add_argument("--reports_dataset", help="Bigquery sections dataset name")
    parser.add_argument("--tenant_id", help="Tenant for which the pipeline is going to run")
    parser.add_argument("--start_datetime",
                        help="Start for report time interval, reports are going to be generated from "
                             "[start_time, end_time]")
    parser.add_argument("--end_datetime", help="End for report time interval, reports are going to be generated from "
                                               "[start_time, end_time]")
    parser.add_argument("--reports_bucket_name", help="Google cloud storage final destination for report pdf files")

    known_args, pipeline_args = parser.parse_known_args()

    pipeline_options = PipelineOptions(pipeline_args)

    with beam.Pipeline(options=pipeline_options) as p:
        (
                p
                | "GetAllSections" >> beam.Create(get_all_sections(known_args.reports_dataset,
                                                                   known_args.tenant_id,
                                                                   known_args.start_datetime,
                                                                   known_args.end_datetime))
                | "BuildPdf" >> beam.ParDo(ts.BuildPdf(), known_args.tenant_id)
                | "StorePdf" >> beam.ParDo(ts.StorePdf(), known_args.reports_bucket_name)
        )


if __name__ == "__main__":
    run()
