from typing import List

from PySDNSim.Job import Job


class NetworkService:
    """
    Represents a network service.
    """
    _name: str
    _flows: int
    _jobs: List[Job]

    def __init__(self, name: str, flows: int):
        """
        Create a new network service with the given name and flows.

        :param name: name of the network service.
        :param flows: number of flows of the network service.
        """
        self._name = name
        self._flows = flows
        self._jobs = list()

    @property
    def name(self):
        return self._name

    @property
    def flows(self):
        return self._flows

    @flows.setter
    def flows(self, flows: int):
        self._flows = flows

    @property
    def jobs(self):
        return self._jobs

    def add_job(self, job: Job):
        self._jobs.append(job)
