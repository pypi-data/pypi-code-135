import datetime
from typing import Optional

import ai.h2o.featurestore.api.v1.CoreService_pb2 as pb
from ai.h2o.featurestore.api.v1.CoreService_pb2_grpc import CoreServiceStub

from ..entities.training_data_set import TrainingDataSet
from ..utils import Utils


class TrainingDataSets:
    def __init__(self, stub: CoreServiceStub, feature_view):
        self._feature_view = feature_view
        self._stub = stub

    def create(
        self,
        name: str,
        description: str = "",
        start_date_time: Optional[datetime.datetime] = None,
        end_date_time: Optional[datetime.datetime] = None,
    ):
        request = pb.CreateTrainingDataSetRequest(
            name=name,
            description=description,
            feature_view_id=self._feature_view.id,
            feature_view_version=self._feature_view.version,
            start_date_time=Utils.date_time_to_proto_timestamp(start_date_time),
            end_date_time=Utils.date_time_to_proto_timestamp(end_date_time),
        )

        response = self._stub.CreateTrainingDataSet(request)
        return TrainingDataSet(self._stub, response.training_data_set)

    def get(self, name: str):
        request = pb.GetTrainingDataSetRequest(
            feature_view_id=self._feature_view.id,
            feature_view_version=self._feature_view.version,
            training_data_set_name=name,
        )

        training_data_set = self._stub.GetTrainingDataSet(request)
        return TrainingDataSet(self._stub, training_data_set)

    def list(self):
        request = pb.ListTrainingDataSetsRequest(
            feature_view_id=self._feature_view.id,
            feature_view_version=self._feature_view.version,
        )

        response = self._stub.ListTrainingDataSets(request)
        return [
            TrainingDataSet(self._stub, training_data_set)
            for training_data_set in response.training_data_sets
        ]
