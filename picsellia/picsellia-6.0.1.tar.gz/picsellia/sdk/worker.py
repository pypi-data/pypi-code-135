import warnings

from beartype import beartype
from beartype.roar import BeartypeDecorHintPep585DeprecationWarning

from picsellia.bcolors import bcolors
from picsellia.decorators import exception_handler
from picsellia.sdk.connexion import Connexion
from picsellia.sdk.dao import Dao
from picsellia.types.schemas import WorkerSchema

warnings.filterwarnings("ignore", category=BeartypeDecorHintPep585DeprecationWarning)


class Worker(Dao):
    def __init__(self, connexion: Connexion, data: dict):
        Dao.__init__(self, connexion, data)

    @property
    def username(self) -> str:
        return self._username

    def __str__(self):
        return "{}Worker '{}' {}".format(bcolors.UNDERLINE, self.username, bcolors.ENDC)

    @exception_handler
    @beartype
    def sync(self) -> dict:
        r = self.connexion.get("/sdk/worker/{}".format(self.id)).json()
        self.refresh(r)
        return r

    @exception_handler
    @beartype
    def refresh(self, data: dict) -> WorkerSchema:
        object = WorkerSchema(**data)
        self._username = object.collaborator.username
        return object

    @exception_handler
    @beartype
    def get_infos(self) -> dict:
        """Retrieve worker info

        Examples:
            ```python
                worker = my_dataset.list_workers()[0]
                print(worker.get_infos())
            ```

        Returns:
            A dict with data of the worker
        """
        return {"username": self.username}
