import logging
import subprocess
import warnings
from functools import partial
from typing import Dict, List
from uuid import UUID

import orjson
from beartype import beartype
from beartype.roar import BeartypeDecorHintPep585DeprecationWarning

from picsellia.bcolors import bcolors
from picsellia.decorators import exception_handler
from picsellia.exceptions import BadConfigurationScan
from picsellia.sdk.connexion import Connexion
from picsellia.sdk.dao import Dao
from picsellia.sdk.experiment import Experiment
from picsellia.sdk.scan_file import ScanFile
from picsellia.types.enums import RunStatus
from picsellia.types.schemas import RunSchema
from picsellia.utils import filter_payload

logger = logging.getLogger("picsellia")
warnings.filterwarnings("ignore", category=BeartypeDecorHintPep585DeprecationWarning)


class Run(Dao):
    def __init__(self, connexion: Connexion, data: dict) -> None:
        Dao.__init__(self, connexion, data)

    @property
    def scan_id(self) -> UUID:
        return self._scan_id

    @property
    def experiment_id(self) -> UUID:
        return self._experiment_id

    @property
    def order(self) -> int:
        return self._order

    @property
    def parameters(self) -> Dict:
        return self._parameters

    @property
    def status(self) -> RunStatus:
        return self._status

    def __str__(self):
        return "{}Run {}{} of scan {} (id: {})".format(
            bcolors.BLUE, self.order, bcolors.ENDC, self.scan_id, self.id
        )

    @exception_handler
    @beartype
    def sync(self) -> dict:
        r = self.connexion.get("/sdk/run/{}".format(self.id)).json()
        self.refresh(r)
        return r

    @exception_handler
    @beartype
    def refresh(self, data: dict) -> RunSchema:
        object = RunSchema(**data)
        self._order = object.order
        self._parameters = object.parameters
        self._status = object.status
        self._scan_id = object.scan_id
        self._experiment_id = object.experiment_id
        return object

    @exception_handler
    @beartype
    def update(self, status: RunStatus = None) -> None:
        """Update this run.

        Examples:
            ```python
                run.update(status=RunStatus.TERMINATED)
            ```
        """
        payload = {"status": status}
        filtered_payload = filter_payload(payload)
        r = self.connexion.patch(
            "/sdk/run/{}".format(self.id), data=orjson.dumps(filtered_payload)
        ).json()
        self.refresh(r)
        logger.info("{} updated".format(self))

    @exception_handler
    @beartype
    def end(self) -> None:
        """End a run

        Examples:
            ```python
                run.end()
            ```
        """
        r = self.connexion.post("/sdk/run/{}/end".format(self.id)).json()
        self.refresh(r["run"])
        logger.info("{} ended: {}".format(self, r["message"]))

    @exception_handler
    @beartype
    def get_script(
        self,
    ) -> ScanFile:
        """Retrieve the script of this run.

        Returns:
            A (ScanFile) object
        """
        r = self.connexion.get("/sdk/scan/{}".format(self.scan_id)).json()

        if "script_id" not in r or r["script_id"] is None:
            raise BadConfigurationScan("This scan has no script.")

        r = self.connexion.get("/sdk/scan/file/{}".format(r["script_id"])).json()
        return ScanFile(self.connexion, r)

    @exception_handler
    @beartype
    def list_data_files(
        self,
    ) -> List[ScanFile]:
        """List all data files of this run

        Examples:
            ```python
                files = run.list_data_files()
            ```

        Returns:
            List of (ScanFile) object
        """
        r = self.connexion.get("/sdk/scan/{}/scanfiles".format(self.scan_id)).json()
        return list(map(partial(ScanFile, self.connexion), r["items"]))

    @exception_handler
    @beartype
    def install_requirements(self) -> None:
        """Install requirements from the run requirements dictionnary.

        Examples:
            ```python
                run.install_requirements()
            ```
        """
        r = self.connexion.get("/sdk/scan/{}".format(self.scan_id)).json()
        requirements = r["requirements"]

        for module in requirements:
            name = (
                "{}=={}".format(module["package"], module["version"])
                if module["version"] != ""
                else module["package"]
            )
            subprocess.call(["pip", "install", name])

    @exception_handler
    @beartype
    def get_experiment(self) -> Experiment:
        """Retrieve linked experiment

        Examples:
            ```python
                my_experiment = run.get_experiment()
            ```

        Returns:
            An (Experiment) object linked to this run
        """
        r = self.connexion.get("/sdk/experiment/{}".format(self.experiment_id)).json()
        return Experiment(self.connexion, r)

    @exception_handler
    @beartype
    def delete(self) -> None:
        """Delete this run from the platform.

        :warning: **DANGER ZONE**: Be very careful here!

        Examples:
            ```python
                run.delete()
            ```
        """
        self.connexion.delete("/sdk/run/{}".format(self.id))
        logger.info("{} deleted.".format(self))
