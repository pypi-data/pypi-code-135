# Copyright (c) 2022 Shapelets.io
# 
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT


from typing import List, Optional, Set, Tuple

from .idataappsrepo import IDataAppsRepo
from .idataappsservice import IDataAppsService
from ..db import transaction
from ..model import (
    DataAppAttributes,
    DataAppField,
    DataAppAllFields,
    DataAppId,
    DataAppProfile
)


class DataAppsService(IDataAppsService):
    __slots__ = ('_dataapps_repo',)

    def __init__(self, dataapp_repo: IDataAppsRepo) -> None:
        self._dataapp_repo = dataapp_repo

    def get_all(self,
                attributes: Optional[Set[DataAppField]] = DataAppAllFields,
                sort_by: Optional[List[Tuple[DataAppField, bool]]] = None,
                skip: Optional[int] = None,
                limit: Optional[int] = None) -> List[DataAppProfile]:
        return self._dataapp_repo.load_all(attributes, sort_by, skip, limit)

    def create(self, attributes: DataAppAttributes) -> DataAppProfile:
        # TODO: some checks
        # if attributes.version is None:
        #     raise ValueError("Invalid version")
        with transaction():
            return self._dataapp_repo.create(attributes)

    def get_dataapp(self, dataapp_id: DataAppId):
        if isinstance(dataapp_id, str):
            return self._dataapp_repo.load_by_id(dataapp_id)
        return self._dataapp_repo.load_by_id(str(dataapp_id))

    def delete_dataapp(self, dataapp_id: DataAppId) -> DataAppProfile:
        if isinstance(dataapp_id, str):
            return self._dataapp_repo.delete_by_name(dataapp_id)
        return self._dataapp_repo.delete_by_id(str(dataapp_id))

    def delete_all(self) -> bool:
        self._dataapp_repo.delete_all()

    def get_dataapp_privileges(self, dataapp_id: DataAppId) -> List[DataAppProfile]:
        pass
