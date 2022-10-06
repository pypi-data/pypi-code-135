from typing import List, Literal, Optional

from humanloop.api.models.project import FeedbackSchema, ProjectResponse
from humanloop.sdk.init import _get_client


def create_project(project: str) -> ProjectResponse:
    """Create a project with the specified name.

    Returns None if successful.
    """
    client = _get_client()
    return client.create_project(project)


def set_active_model_config(project: str, model_config_id: str) -> ProjectResponse:
    """Set the active model config for the project.

    This will unset the active experiment if one is set.
    """
    client = _get_client()
    return client.update_project(
        project=project, update={"active_model_config_id": model_config_id}
    )


def set_active_experiment(project: str, experiment_id: str) -> ProjectResponse:
    """Set the active experiment for the project.

    This will unset the active model config if one is set.
    """
    client = _get_client()
    return client.update_project(
        project=project, update={"active_experiment_id": experiment_id}
    )


def remove_active_model_config(project: str) -> ProjectResponse:
    """Remove the project's active model config, if set."""
    client = _get_client()
    return client.remove_project_active_model_config(project=project)


def remove_active_experiment(project: str) -> ProjectResponse:
    """Remove the project's active experiment, if set."""
    client = _get_client()
    return client.remove_project_active_experiment(project=project)


def add_feedback_group(
    project: str,
    feedback_group: str,
    type: Literal["text", "categorical"],
    labels: Optional[List[str]] = None,
) -> FeedbackSchema:
    """Add a new feedback group to your project.

    Feedback groups of type "text" and "categorical" are currently supported.
    When creating a feedback group of type "categorical", you can specify a
    list of labels to create.
    If creating a feedback group of type "text", "labels" should not be
    provided.
    """
    if type == "text" and labels is not None:
        raise ValueError(
            "Cannot create a feedback group of type text while specifying a list of labels."
        )

    if type == "text":
        schema = {"groups": [{"name": feedback_group, "type": type}]}
    elif type == "categorical":
        schema = {"groups": [{"name": feedback_group, "type": type, "labels": labels}]}
    else:
        raise ValueError(
            f"Unknown feedback group type. Should be one of 'text' or 'categorical'. Found: {type}"
        )

    client = _get_client()
    return client.add_feedback_labels_and_groups(
        project=project,
        schema=schema,
    )


def add_feedback_labels(
    project: str, feedback_group: str, labels: List[str]
) -> FeedbackSchema:
    """Add feedback labels to a categorical feedback group"""
    client = _get_client()
    return client.add_feedback_labels_and_groups(
        project=project,
        schema={"groups": [{"name": feedback_group, "type": type, "labels": labels}]},
    )
