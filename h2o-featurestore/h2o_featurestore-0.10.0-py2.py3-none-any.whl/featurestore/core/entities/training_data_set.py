import datetime

from google.protobuf.timestamp_pb2 import Timestamp

import ai.h2o.featurestore.api.v1.CoreService_pb2 as pb
from ai.h2o.featurestore.api.v1.CoreService_pb2_grpc import CoreServiceStub

from ..utils import Utils
from .training_data_feature import TrainingDataSetFeature


class TrainingDataSet:
    def __init__(self, stub: CoreServiceStub, training_data_set_proto):
        tds = pb.TrainingDataSet()
        tds.CopyFrom(training_data_set_proto)
        self._training_data_set = tds
        self._stub = stub

    @property
    def id(self):
        return self._training_data_set.id

    @property
    def name(self):
        return self._training_data_set.name

    @property
    def description(self):
        return self._training_data_set.description

    @description.setter
    def description(self, value):
        update_request = pb.UpdateTrainingDataSetRequest(
            training_data_set_id=self.id,
            description=value,
        )
        training_data_set_proto = self._stub.UpdateTrainingDataSet(update_request)
        tds = pb.TrainingDataSet()
        tds.CopyFrom(training_data_set_proto)
        self._training_data_set = tds

    @property
    def start_date_time(self):
        timestamp: Timestamp = self._training_data_set.start_date_time
        if timestamp:
            return datetime.datetime.fromtimestamp(
                timestamp.ToMilliseconds() / 1000, tz=datetime.timezone.utc
            )
        else:
            return None

    @property
    def end_date_time(self):
        timestamp: Timestamp = self._training_data_set.end_date_time
        if timestamp:
            return datetime.datetime.fromtimestamp(
                timestamp.ToMilliseconds() / 1000, tz=datetime.timezone.utc
            )
        else:
            return None

    @property
    def features(self):
        return [
            TrainingDataSetFeature(feature)
            for feature in self._training_data_set.features
        ]

    def delete(self):
        request = pb.DeleteTrainingDataSetRequest(training_data_set_id=self.id)
        self._stub.DeleteTrainingDataSet(request)

    def download(self, output_dir=None):
        request = pb.RetrieveTrainingDataSetAsAsLinksRequest(
            training_data_set_id=self.id
        )
        response: pb.RetrieveTrainingDataSetAsSparkResponse = (
            self._stub.RetrieveTrainingDataSetAsLinks(request)
        )

        return Utils.download_files(output_dir, response.download_links)

    def as_spark_frame(self, spark_session):
        from ..commons.spark_utils import SparkUtils

        session_id = spark_session.conf.get("ai.h2o.featurestore.sessionId", "")
        request = pb.RetrieveTrainingDataSetAsSparkRequest(
            training_data_set_id=self.id, session_id=session_id
        )

        response = self._stub.RetrieveTrainingDataSetAsSpark(request)
        spark_session.conf.set("ai.h2o.featurestore.sessionId", response.session_id)

        SparkUtils.configure_user_spark(spark_session)
        for k, v in response.options.items():
            spark_session.conf.set(k, v)

        return spark_session.read.format("parquet").load(response.path)
