# Copyright (c) 2022 Shapelets.io
# 
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT
import json
from types import SimpleNamespace

from blacksheep import FromJSON, Response
from blacksheep.server.controllers import ApiController, get, post
from requests import Session
from typing import List, Optional

from .idataappsservice import IDataAppsService
from ..docs import docs
from ..model.dataapps import DataAppAttributes, DataAppProfile, DataAppId


class DataAppsHttpServer(ApiController):
    def __init__(self, svr: IDataAppsService) -> None:
        self._svr = svr
        super().__init__()

    @classmethod
    def route(cls) -> Optional[str]:
        return '/api/dataapps'

    @get("/")
    async def dataapp_list(self) -> List[DataAppProfile]:
        return self._svr.get_all()

    @post("/")
    async def create(self, attributes: FromJSON[DataAppAttributes]) -> List[DataAppProfile]:
        dataapp_attributes = DataAppAttributes(name=attributes.value.name,
                                               version=attributes.value.version,
                                               description=attributes.value.description,
                                               creationDate=attributes.value.creationDate,
                                               spec=attributes.value.spec)
        return self._svr.create(dataapp_attributes)

    @get("/{id}")
    async def get_dataapp(self, id) -> DataAppProfile:
        return self._svr.get_dataapp(id)

    @get("/remove/{id}")
    async def delete(self, dataapp_id: int) -> bool:
        return self._svr.delete(dataapp_id)

    @get("/removeAll")
    async def delete_all(self) -> bool:
        return self._svr.delete_all()

    @get("/{id}/privileges")
    async def get_dataapp_privileges(self, dataapp_id: int) -> List[DataAppProfile]:
        return self._svr.get_dataapp_privileges(dataapp_id)


class DataAppsHttpProxy(IDataAppsService):
    def __init__(self, session: Session) -> None:
        self.session = session

    def get_all(self) -> List[DataAppProfile]:
        return self.session.get('/api/dataapps/')

    def create(self, dataapp) -> DataAppProfile:
        payload = DataAppAttributes(name=dataapp.name,
                                    version=dataapp.version,
                                    description=dataapp.description,
                                    creationDate=dataapp.creation_date,
                                    spec=dataapp.to_json())
        return self.session.post('/api/dataapps/', json=json.loads(payload.json()))

    def get_dataapp(self, dataapp_id: int) -> DataAppProfile:
        return self.session.get('/api/dataapps/', params=[("dataapp_id", dataapp_id)])

    def delete_dataapp(self, dataapp_id: int):
        self.session.get('/api/dataapps/remove/{id}', params=[("dataapp_id", dataapp_id)])

    def delete_all(self) -> bool:
        self.session.get('/api/dataapps/removeAll')
        return True

    def get_dataapp_privileges(self, dataapp_id: int) -> List[DataAppProfile]:
        pass
