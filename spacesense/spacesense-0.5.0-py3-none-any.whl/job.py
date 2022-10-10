"""
Job.py
====================================
All classes necessary to use SpaceSense library for large datasets.
"""
import json
import logging
import os
from pathlib import Path

import grpc
import pandas as pd
from tqdm import tqdm

from spacesense import config
from spacesense.common.proto.backend import backend_pb2, backend_pb2_grpc
from spacesense.grpc_auth import GrpcAuth

logger = logging.getLogger(__name__)


class JobList:
    def __init__(
        self,
        items: list = None,
        ok: bool = True,
        reason: str = None,
    ):
        """
        Create an instance of the Job list Result class :py:class:`JobList`

        Attributes:
            ok (bool): :py:attr:`JobList.ok` is True when :py:meth:`Client.compute_ard` returns usable data, False otherwise.
            reason (str, None): Provides additional information when :py:attr:`JobList.ok` is false and result is not accessible. if :py:attr:`JobList.ok` is True, :py:attr:`JobList.reason` will be None.
            items (list): List of jobs descriptor dictionary
        """
        self.ok = ok
        self.reason = reason
        self._items = items
        if self._items:
            columns = [
                "job_id",
                "job_name",
                "experiment_id",
                "workflow_id",
                "status",
            ]
            dataframe = pd.DataFrame(data=items, columns=columns)
            self._dataframe = dataframe

    def has_results(self):
        return self.dataframe is not None and len(self.dataframe) > 0

    @property
    def dataframe(self):
        return self._dataframe

    @dataframe.setter
    def dataframe(self, dataframe: pd.DataFrame):
        if type(dataframe) != pd.DataFrame:
            raise ValueError("dataframe should be a pandas.DataFrame")
        self._dataframe = dataframe
        self._items = [scene for scene in self._items if scene["title"] in self._dataframe["title"].values]

    @property
    def to_dict(self):
        dataframe = self.dataframe.copy()
        return dataframe.to_dict(orient="records")


class Job:
    """Class that allows you to interact with SpaceSense Job backend.

    Args:
            name (str, optional): User defined name for this specific job run.
            workflow_id (str): ID corresponding to a specified workflow constructed on the SpaceSense backend.
            experiment_id (str): ID describing the experiment and workspace. This ID corresponds to the cloud workspace where any downloaded data is stored from previous runs. To reduce your download costs and usage, if running an experiment multiple times, please keep this ID identical between runs.
            id (str, optional): Automatically generated unique ID of your instance.
    """

    def __init__(
        self,
        id,
        experiment_id,
        name=None,
        workflow_id=None,
        status=None,
        backend_url=None,
        local_output_path=None,
        reason=None,
    ):
        """Create an instance of the :py:class:`Job`"""
        self.backend_url = backend_url or config.BACKEND_URL

        self.api_key = os.environ.get("SS_API_KEY")

        if not self.api_key:
            raise ValueError("Could not find SpaceSense API in SS_API_KEY environment variable.")
        self.id = id
        self.name = name or ""
        self.workflow_id = workflow_id
        self.experiment_id = experiment_id
        self.status = status
        self.local_output_path = local_output_path
        self.reason = reason
        self._execution_report = None
        if self.experiment_id and not self.local_output_path:
            self.local_output_path = os.path.join("./generated", self.experiment_id)

    @classmethod
    def load_from_id(cls, experiment_id, id, backend_url=None):
        job = cls(experiment_id=experiment_id, id=id, backend_url=backend_url)
        job.refresh()
        return job

    def refresh(
        self,
    ):
        """Refresh the status of the current job and all the issued tasks"""

        channel_opt = [
            ("grpc.max_send_message_length", config.GRPC_MAX_SEND_MESSAGE_LENGTH),
            ("grpc.max_receive_message_length", config.GRPC_MAX_RECEIVE_MESSAGE_LENGTH),
        ]
        with grpc.secure_channel(
            self.backend_url,
            grpc.composite_channel_credentials(
                grpc.ssl_channel_credentials(config.CERT), grpc.metadata_call_credentials(GrpcAuth(self.api_key))
            ),
            options=channel_opt,
        ) as channel:
            stub = backend_pb2_grpc.JobStub(channel)
            request = backend_pb2.GetJobReportRequest(job_id=self.id, experiment_id=self.experiment_id)
            try:
                response = stub.GetJobReport(request)
                self.name = response.job_name
                self.workflow_id = response.workflow_id
                if response.status != backend_pb2.Status.Value("COMPLETED"):
                    self.status = "RUNNING"
                    logger.error(
                        "Could not find job status, if you just started this job, you should wait for some time for the job to start"
                    )
                    return
                self._execution_report = json.loads(response.execution_report)
                statuses = [status.get("status", "") for status in self._execution_report.values()]
                if "RUNNING" in statuses:
                    self.status = "RUNNING"
                elif "COMPLETED" not in statuses and "ERROR" in statuses:
                    self.status = "ERROR"
                elif "COMPLETED" in statuses:
                    self.status = "COMPLETED"
            except grpc.RpcError as e:
                logger.error(f"Could not refresh, try again .. detail : {e.details()}")

    def execution_report(self):
        """A simple report, in the form of a dataframe, detailing the current steps and status of the job tasks"""
        return pd.DataFrame.from_dict(self._execution_report, orient="index")

    def download_result(self, output_dir=None):
        """Download the completed results of the job task"""

        channel_opt = [
            ("grpc.max_send_message_length", config.GRPC_MAX_SEND_MESSAGE_LENGTH),
            ("grpc.max_receive_message_length", config.GRPC_MAX_RECEIVE_MESSAGE_LENGTH),
        ]
        with grpc.secure_channel(
            self.backend_url,
            grpc.composite_channel_credentials(
                grpc.ssl_channel_credentials(config.CERT), grpc.metadata_call_credentials(GrpcAuth(self.api_key))
            ),
            options=channel_opt,
        ) as channel:
            stub = backend_pb2_grpc.JobStub(channel)
            request = backend_pb2.StreamJobResultsRequest(job_id=self.id, experiment_id=self.experiment_id)
            try:
                self.local_output_path = output_dir or self.local_output_path
                self.local_output_path = os.path.join(self.local_output_path, self.experiment_id)
                Path(self.local_output_path).mkdir(parents=True, exist_ok=True)
                print(f"Starting to download Job results to path {self.local_output_path}")
                downloaded_list = []
                total_tasks = 0
                for response in tqdm(stub.StreamJobResults(request)):
                    total_tasks = response.total_tasks
                    if response.total_tasks == 0:
                        logger.info("No results found")
                    if response.current_task == 1:
                        logger.info("Downloading results")
                    with open(os.path.join(self.local_output_path, f"{response.task_id}.nc"), "wb") as f:
                        f.write(response.task_data)
                        downloaded_list.append(response.task_id)
                print(f"Downloaded {len(downloaded_list)} files out of {total_tasks}")
            except grpc.RpcError as e:
                logger.error(e.details())

    def retry(self):
        """Retries the execution of the job ONLY for the individual tasks that failed in error"""

        # Allow to transfer up to 500mo as grpc message
        channel_opt = [
            ("grpc.max_send_message_length", config.GRPC_MAX_SEND_MESSAGE_LENGTH),
            ("grpc.max_receive_message_length", config.GRPC_MAX_RECEIVE_MESSAGE_LENGTH),
        ]
        with grpc.secure_channel(
            self.backend_url,
            grpc.composite_channel_credentials(
                grpc.ssl_channel_credentials(config.CERT), grpc.metadata_call_credentials(GrpcAuth(self.api_key))
            ),
            options=channel_opt,
        ) as channel:
            stub = backend_pb2_grpc.JobStub(channel)
            request = backend_pb2.RetryJobRequest(
                job_id=self.id,
                experiment_id=self.experiment_id,
                workflow_id=self.workflow_id,
            )
            try:
                response = stub.RetryJob(request)
                if response.status == backend_pb2.Status.Value("ERROR"):
                    self.status = "ERROR"
                    self.reason = response.reason
                    logger.error(f"Could not start to process this Job. reason: {self.reason}")
                elif response.status == backend_pb2.Status.Value("RUNNING"):
                    self.status = "RUNNING"
                    logger.info(f"Experiment (id:{response.experiment_id}) Started for Job(id:{response.job_id})")
            except grpc.RpcError as e:
                logger.error(e.details())
