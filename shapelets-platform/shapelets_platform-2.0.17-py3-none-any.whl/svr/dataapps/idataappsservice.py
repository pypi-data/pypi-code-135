# Copyright (c) 2022 Shapelets.io
#
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

from abc import ABC, abstractmethod
from typing import List

from ..model import DataAppAttributes, DataAppProfile, DataAppId


class IDataAppsService(ABC):
    @abstractmethod
    def get_all(self) -> List[DataAppProfile]:
        pass

    @abstractmethod
    def create(self, attributes: DataAppAttributes) -> DataAppProfile:
        pass

    @abstractmethod
    def get_dataapp(self, dataapp_id: DataAppId) -> DataAppProfile:
        pass

    @abstractmethod
    def delete_dataapp(self, dataapp_id: DataAppId):
        pass

    @abstractmethod
    def delete_all(self) -> bool:
        pass

    @abstractmethod
    def get_dataapp_privileges(self, dataapp_id: DataAppId) -> List[DataAppProfile]:
        pass


