import ai.h2o.featurestore.api.v1.CoreService_pb2 as pb
import ai.h2o.featurestore.api.v1.FeatureSetProtoApi_pb2 as FeatureSetApi


class TrainingDataSetFeature:
    def __init__(self, internal_feature: pb.TrainingDataSetFeature):
        self._internal_feature = internal_feature

    @property
    def name(self):
        return self._internal_feature.name

    @property
    def feature_type(self):
        return FeatureSetApi.FeatureTypeInternal.FeatureType.Name(
            self._internal_feature.feature_type
        )

    @property
    def data_type(self):
        return self._internal_feature.data_type
