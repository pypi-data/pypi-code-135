import pydantic

from pydantic import root_validator

from captur_ml_sdk.dtypes.interfaces import LivePredictionRequest
from captur_ml_sdk.dtypes.interfaces.MLGateway import (
    MLBatchPredict,
    MongoModelTrainRequest,
    MongoModelEvaluateRequest,
    MLModelDeploy,
)

class GatewayRequest(pydantic.BaseModel):
    live_predict: LivePredictionRequest = pydantic.Field(
        None,
        description="The live predict request body",
    )
    batch_predict: MLBatchPredict.BatchPredictionRequest = pydantic.Field(
        None,
        description="The batch predict request body.",
    )
    model_train: MongoModelTrainRequest = pydantic.Field(
        None,
        description="The model train request body."
    )
    model_evaluate: MongoModelEvaluateRequest = pydantic.Field(
        None,
        description="The model evaluate request body."
    )
    model_deploy: MLModelDeploy.ModelDeployRequest = pydantic.Field(
        None,
        description="The model deploy request body."
    )

    @root_validator
    def request_must_have_predict_live_predict_train_or_evaluate(cls, values):
        if not values.get("batch_predict") \
                and not values.get("live_predict") \
                and not values.get("model_train") \
                and not values.get("model_evaluate") \
                and not values.get("model_deploy"):
            raise ValueError(
                "Request must include either 'batch_predict', 'live_predict', 'model_train', 'model_evaluate' or 'model_deploy'")

        return values
