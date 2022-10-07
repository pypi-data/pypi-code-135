from abc import ABC, abstractmethod

from spt_datascience.credentials import Credentials
from spt_datascience.datascience.model_manager import SPTModelManager
from spt_datascience.datascience.model_util import MongoModelUtil
from spt_datascience.datascience.models_storage import  S3ModelStorage
from spt_datascience.datascience.pipeline_manager import SPTPipelineManager


class Resource(ABC):

    def __init__(self, c: Credentials):
        self.c = c

    @abstractmethod
    def get_object(self):
        pass

    @staticmethod
    @abstractmethod
    def get_name():
        pass


class Any:
    __slots__ = "creds"

    def __init__(self, creds):
        self.creds = creds

    def get_creds(self):
        return self.creds


class AnyCreds(Resource):

    def get_object(self):
        return Any(self.c.get_credentials())

    @staticmethod
    def get_name():
        return 'any_creds'


class ModelManagerResource(Resource):

    def get_object(self):
        credential = self.c.get_credentials()
        return SPTModelManager(
            spt_resource_factory=credential['spt_resource_factory'],
            spt_ds_factory=credential['spt_ds_factory']
        )

    @staticmethod
    def get_name():
        return 'model_manager'


class PipelineManagerResource(Resource):

    def get_object(self):
        credential = self.c.get_credentials()
        return SPTPipelineManager(
            spt_resource_factory=credential['spt_resource_factory'],
            model_manager=credential['spt_ds_factory'].get_model_manager()
        )

    @staticmethod
    def get_name():
        return 'pipeline_manager'
