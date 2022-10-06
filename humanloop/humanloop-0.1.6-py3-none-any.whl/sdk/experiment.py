from typing import List, Optional

from humanloop.api.models.experiment import TrialResponse
from humanloop.sdk.init import _get_client
from humanloop.sdk.utils import deprecated


@deprecated
def trial(experiment_id: str) -> TrialResponse:
    """Generates a model config according to your experiment to use to execute
     your model.

    The returned TrialResponse contains a `.id` attribute that can be used in a
    subsequent log to such that the log contributes to the experiment.
    """
    client = _get_client()
    return client.trial(experiment_id)


def create_experiment(project: str, name: str, model_config_ids: Optional[List[str]]):
    client = _get_client()
    project = client.get_project(project=project)
    return client.create_experiment(project_id=project.internal_id, experiment={
        "name": name,
        "model_config_ids": model_config_ids,
        "positive_labels": positive_label_ids,
    })
