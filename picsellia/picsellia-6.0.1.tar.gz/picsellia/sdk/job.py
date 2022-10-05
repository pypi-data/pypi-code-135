import logging
import warnings
from time import sleep
from typing import List, Union

from beartype import beartype
from beartype.roar import BeartypeDecorHintPep585DeprecationWarning

from picsellia.decorators import exception_handler
from picsellia.exceptions import WaitingAttemptsTimeout
from picsellia.sdk.connexion import Connexion
from picsellia.sdk.dao import Dao
from picsellia.types.enums import JobStatus
from picsellia.types.schemas import JobSchema

logger = logging.getLogger("picsellia")
warnings.filterwarnings("ignore", category=BeartypeDecorHintPep585DeprecationWarning)


class Job(Dao):
    def __init__(self, connexion: Connexion, data: dict) -> None:
        Dao.__init__(self, connexion, data)

    @property
    def status(self) -> JobStatus:
        return self._status

    def __str__(self):
        return "Job {} is currently in state {}"

    @exception_handler
    @beartype
    def sync(self) -> dict:
        r = self.connexion.get("/sdk/job/{}".format(self.id)).json()
        self.refresh(r)
        return r

    @exception_handler
    @beartype
    def refresh(self, data: dict) -> JobSchema:
        object = JobSchema(**data)
        self._status = object.status
        return object

    @exception_handler
    @beartype
    def wait_for_status(
        self,
        statuses: Union[JobStatus, List[JobStatus]] = [
            JobStatus.SUCCESS,
            JobStatus.FAILED,
            JobStatus.TERMINATED,
        ],
        blocking_time_increment: float = 1.0,
        attempts: int = 20,
    ) -> JobStatus:
        if isinstance(statuses, JobStatus):
            statuses = [statuses]

        attempt = 0
        while attempt < attempts:
            self.sync()
            if self.status in statuses:
                break

            sleep(blocking_time_increment)
            attempt += 1

        if attempt >= attempts:
            raise WaitingAttemptsTimeout(
                "Job is still not in the status you've been waiting for, after {} attempts. Please wait a few more moment, or check"
            )

        return self.status
