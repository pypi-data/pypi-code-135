import re
from typing import Optional, List, Union
from captur_ml.core.exceptions import (
    GoogleCloudVertexAIEndpointCorruptedImageError,
    GoogleCloudVertexAIEndpointDoesNotExistError,
    GoogleCloudVertexAIEndpointImageTooLargeError,
    GoogleCloudVertexAIEndpointNoModelDeployedError,
)
from captur_ml.core.entities import VertexAIEndpoint
from captur_ml.core.dtypes.generics import Image

from google.cloud import aiplatform_v1
from google.api_core.client_options import ClientOptions
from google.api_core import exceptions as google_exceptions
from google.cloud.aiplatform.gapic import PredictionServiceClient, schema


def get_image_classification_prediction_from_deployed_automl(
    images: Union[Image, List[Image]],
    endpoint: VertexAIEndpoint,
    prediction_service_client_options: Optional[ClientOptions] = None,
) -> aiplatform_v1.types.PredictResponse:
    """Gets image classification prediction from deployed automl model.

    Args:
        images (Union[Image, List[Image]]): The Image(s) to predict for.
        endpoint (VertexAIEndpoint): VertexAIEndpoint object instance that will be used to make the prediction.
        prediction_service_client_options (Optional[ClientOptions]): Client options to pass to the prediction service client. Default = None.

    Raises:
        `captur_ml.core.exceptions.GoogleCloudVertexAIEndpointDoesNotExistError`: If the specified endpoint does not exist.
        `captur_ml.core.exceptions.GoogleCloudVertexAIEndpointNoModelDeployedError`: If there is no model deployed at the specified endpoint.
        `captur_ml.core.exceptions.GoogleCloudVertexAIEndpointImageTooLargeError`: If the image exceeds the 1.5MB limit.

    Returns:
        automl_v1beta1.types.PredictResponse: An object containing the prediction results for the image.
    """
    if not endpoint.exists:
        raise GoogleCloudVertexAIEndpointDoesNotExistError(
            code=str(404), endpoint_id=endpoint.id
        )
    if not endpoint.is_active:
        raise GoogleCloudVertexAIEndpointNoModelDeployedError(
            code=str(400), endpoint_id=endpoint.id
        )

    if prediction_service_client_options is None:
        prediction_service_client_options = {
            "api_endpoint": f"{endpoint.location}-aiplatform.googleapis.com"
        }

    client = PredictionServiceClient(client_options=prediction_service_client_options)

    if isinstance(images, Image):
        images = [images]

    instances = [
        schema.predict.instance.ImageClassificationPredictionInstance(
            content=image.bytes,
        ).to_value()
        for image in images
    ]

    parameters = schema.predict.params.ImageClassificationPredictionParams(
        confidence_threshold=0.0,
        max_predictions=10,
    ).to_value()

    endpoint = client.endpoint_path(
        project=endpoint.project,
        location=endpoint.location,
        endpoint=endpoint.id,
    )

    try:
        response = client.predict(
            endpoint=endpoint, instances=instances, parameters=parameters
        )
    except google_exceptions.FailedPrecondition as e:
        match = re.search(r"exceeds (\d*.*) limit", e.message)
        if match:
            size_limit = match.group(1)
            raise GoogleCloudVertexAIEndpointImageTooLargeError(
                code=str(e.code.value), size_limit=size_limit
            )
        else:
            raise e
    except google_exceptions.InvalidArgument as e:
        raise GoogleCloudVertexAIEndpointCorruptedImageError(
            code=(e.code.value), message=e.message
        )

    return response
