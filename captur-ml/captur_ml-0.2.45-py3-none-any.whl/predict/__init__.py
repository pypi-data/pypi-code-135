from typing import Union, List

from captur_ml.core.dtypes.generics import Image
from captur_ml.core.entities import VertexAIEndpoint
from captur_ml.core.dtypes.results import ImageClassificationResult
from captur_ml.core.services.aiplatform.live_predict import (
    get_image_classification_prediction_from_deployed_automl,
)


def get_live_automl_image_classification(
    images: Union[Image, List[Image]],
    endpoint: VertexAIEndpoint,
    return_raw_automl_response: bool = False,
):
    """Perform image classification on an image or list of images using AutoML.

    Args:
        images (Union[Image, List[Image]]): The image(s) to classify.
        endpoint (VertexAIEndpoint): The Vertex AI endpoint to use for prediction.
        return_raw_automl_response (bool, optional): If True, AutoML response will not be cast to
            captur_ml_sdk.dtypes.ImageClassificationResult. Defaults to False.

    Returns:
        ImageClassificationResult: Result of the model prediction
    """
    if isinstance(images, Image):
        images = [images]

    image_classification_predictions = (
        get_image_classification_prediction_from_deployed_automl(
            images=images,
            endpoint=endpoint,
        )
    )

    image_classification_raw_results = list(
        zip(images, image_classification_predictions)
    )

    if return_raw_automl_response:
        return image_classification_raw_results

    image_classification_results = [
        ImageClassificationResult.from_automl_response(
            image, image_classification_raw_result
        )
        for image, image_classification_raw_result in image_classification_raw_results
    ]

    return image_classification_results
