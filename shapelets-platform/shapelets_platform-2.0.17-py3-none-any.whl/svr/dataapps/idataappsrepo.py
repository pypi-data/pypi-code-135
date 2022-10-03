# Copyright (c) 2022 Shapelets.io
#
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

from abc import ABC, abstractmethod
from typing import List, Optional, Set, Tuple

from ..model import DataAppAttributes, DataAppField, DataAppProfile, PrincipalId


class IDataAppsRepo(ABC):
    @abstractmethod
    def create(self, details: DataAppAttributes) -> Optional[DataAppProfile]:
        pass


    @abstractmethod
    def load_by_id(self, dataapp_id: int) -> Optional[DataAppProfile]:
        pass

    @abstractmethod
    def load_by_name(self, dataapp_name: str) -> Optional[DataAppProfile]:
        pass

    @abstractmethod
    def load_by_principal(self, principal: PrincipalId) -> Optional[DataAppProfile]:
        pass

    @abstractmethod
    def delete_by_name(self, dataapp_name: str):
        pass

    @abstractmethod
    def delete_by_id(self, dataapp_id: int):
        pass

    @abstractmethod
    def load_all(self,
                 attributes: Set[DataAppField],
                 skip: Optional[int],
                 sort_by: Optional[List[Tuple[DataAppField, bool]]],
                 limit: Optional[int]) -> List[DataAppProfile]:
        pass
