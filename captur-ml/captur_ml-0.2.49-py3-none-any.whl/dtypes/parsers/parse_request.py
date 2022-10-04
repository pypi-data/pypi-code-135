from captur_ml_sdk._services.pubsub import publish
from captur_ml_sdk.dtypes import parsers


def parse_request(ml_gateway_request):
    """Responds to any HTTP request to MLGateway.
    Args:
        ml_gateway_request (dict) : the request made to the ML Gateway parsed using pydantic's parse_obj_as.
    Returns:
        Errors or Result (dict)
    """
    pubsub_topics = {
        "batch_predict": "ml-batch-prediction-pre-run",
        "live_predict": "ml-live-prediction",
        "model_train": "ml-train-pre-run",
        "model_evaluate": "ml-evaluation",
        "model_deploy": "ml-model-registration"
    }

    request_results = {
        "predict": [],
        "live_predict": [],
        "train": [],
        "evaluate": [],
        "register_model": []
    }

    parser_mapping = {
        "batch_predict": parsers.parse_batch_predict_request,
        "live_predict": parsers.parse_live_predict_request,
        "model_train": parsers.parse_model_train_request,
        "model_evaluate": parsers.parse_mongo_model_evaluate_request,
        "deploy_model": parsers.parse_model_deploy_request
    }

    for ml_operation, parser in parser_mapping.items():
        field = ml_gateway_request.dict()[ml_operation]
        if field:
            ml_operation_requests = parser(field)
            print(ml_operation_requests)
            for ml_operation_request in ml_operation_requests:
                publish(pubsub_topics[ml_operation], ml_operation_request)
                request_results[ml_operation].append(ml_operation_request)

    return {
        "result": request_results
    }
