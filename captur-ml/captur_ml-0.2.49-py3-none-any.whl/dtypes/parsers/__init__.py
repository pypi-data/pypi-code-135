from typing import Dict


def parse_batch_predict_request(batch_predict_request: Dict) -> Dict:
    """
    Parses the batch predict request sent to the ML Gateway into the form
    necessary to be received by the Batch Predict Cloud Function.
    Note: currently just identity function.

    Args:
        batch_predict_request (Dict): Dictionary version of the batch predict request sent to the MLGateway.

    Returns:
        Dict: Batch Predict request to be sent to the Batch Predict Cloud Function
    """
    return batch_predict_request


def parse_live_predict_request(live_predict_request: Dict) -> Dict:
    """
    Parses the live predict request sent to the ML Gateway into the form
    necessary to be received by the Live Predict Cloud Function.
    Note: currently just identity function.

    Args:
        live_predict_request (Dict): Dictionary version of the Live Predict request sent to the MLGateway.

    Returns:
        Dict: Live Predict request to be sent to the Live Predict Cloud Function
    """
    return live_predict_request


def parse_mongo_model_evaluate_request(model_evaluate_request: Dict) -> Dict:
    """
    Parses the model evaluate request sent to the ML Gateway into the form
    necessary to be received by the model evaluate Cloud Function.

    Args:
        model_evaluate_request (Dict): Dictionary version of the model evaluate request sent to the MLGateway.

    Returns:
        Dict: Model Evaluate request to be sent to the Model Evaluate Cloud Function
    """
    audit_labels = [image["audit_labels"] for image in model_evaluate_request["data"]["images"]]
    if None in audit_labels:
        audit_labels = None
    parsed_request = {
        "labels": [image["label"] for image in model_evaluate_request["data"]["images"]],
        "audit_labels": audit_labels,
        "predictions": [image["predictions"] for image in model_evaluate_request["data"]["images"]],
        "webhooks": model_evaluate_request["meta"]["webhooks"],
        "request_id": model_evaluate_request["meta"]["request_id"],
        "metrics": model_evaluate_request["meta"]["metrics"],
        "is_external": model_evaluate_request["meta"]["is_external"],
    }
    return parsed_request


def parse_model_train_request(model_train_request: Dict) -> Dict:
    """
    Parses the model train request sent to the ML Gateway into the form
    necessary to be received by the Model Train Cloud Function.
    Note: currently just identity function.

    Args:
        model_train_request (Dict): Dictionary version of the model train request sent to the MLGateway.

    Returns:
        Dict: Model Train request to be sent to the Model Train Cloud Function
    """
    return model_train_request


def parse_model_deploy_request(model_deploy_request: Dict) -> Dict:
    """
    Parses the model deploy request sent to the ML Gateway into the form
    necessary to be received by the Model Deploya Cloud Function.
    Note: currently just identity function.

    Args:
        model_deploy_request (Dict): Dictionary version of the model deploy request sent to the MLGateway.

    Returns:
        Dict: Model Deploy request to be sent to the Model Deploy Cloud Function
    """
    return model_deploy_request
