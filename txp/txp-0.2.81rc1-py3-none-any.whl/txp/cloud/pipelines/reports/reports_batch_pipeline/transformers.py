import logging
from txp.common.config import settings
import datetime
import pytz
import os
from txp.common.utils import firestore_utils
from google.cloud import storage, firestore
import apache_beam as beam
import io


class BuildPdf(beam.DoFn):
    def to_runner_api_parameter(self, unused_context):
        return "beam:transforms:custom_parsing:custom_v0", None

    def build_report_pdf(self, tenant_doc, report_id, sections):
        from fpdf import FPDF
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font('Arial', 'B', 11)
        pdf.cell(40, 10, "this is a report :D")
        return pdf

    def get_pdf_name(self, tenant_doc, report_id):
        datetime_format = settings.time.datetime_zoned_format.replace(" ", "_")
        return f'{tenant_doc["tenant_id"]}_{report_id}_' \
               f'{datetime.datetime.now(tz=pytz.UTC).strftime(datetime_format)}.pdf'

    def process(self, element, timestamp=beam.DoFn.TimestampParam,
                window=beam.DoFn.WindowParam):
        tenant_id, report_id, sections = element
        firestore_db = firestore.Client()
        tenant_doc = firestore_utils.pull_tenant_doc(firestore_db, tenant_id).to_dict()
        logging.info(f'Building pdf for report: {report_id} of tenant: {tenant_doc["tenant_id"]} which contains '
                     f'{len(sections)} sections')
        pdf_path = f"{tenant_doc['tenant_id']}/{report_id}/{self.get_pdf_name(tenant_doc, report_id)}"
 
        pdf = self.build_report_pdf(tenant_doc, report_id, sections)

        logging.info(f'Built pdf for report: {report_id} of tenant: {tenant_doc["tenant_id"]} which contains '
                     f'{len(sections)} sections')

        yield pdf_path, pdf
        firestore_db.close()


class StorePdf(beam.DoFn):
    def to_runner_api_parameter(self, unused_context):
        return "beam:transforms:custom_parsing:custom_v0", None

    def process(self, element, reports_bucket, timestamp=beam.DoFn.TimestampParam,
                window=beam.DoFn.WindowParam):
        pdf_path, pdf = element
        logging.info(f"Storing {pdf_path} at gcs")
        storage_client = storage.Client()
        bucket = storage_client.bucket(reports_bucket, user_project=os.environ.get("GCP_PROJECT_ID", "tranxpert-mvp"))
        blob = bucket.blob(pdf_path)
        pdf_byte = io.BytesIO(bytes(pdf.output(dest='S'), encoding='latin1'))
        blob.upload_from_file(pdf_byte)
        storage_client.close()
        logging.info(f"{pdf_path} Stored at gcs")

