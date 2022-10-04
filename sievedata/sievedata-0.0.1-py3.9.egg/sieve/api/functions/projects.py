"""
Project related helper methods for Sieve API
"""

from typing import Dict, List
from ...types.api import SieveLayer, SieveModel, SieveProject, SieveWorkflow
from ..constants import API_URL, API_BASE, MODEL_ID, MODEL_NAME, PROJECT_CREATE_CONFIG, PROJECT_LAYER_ITERATION_TYPE, PROJECT_LAYER_MODELS, PROJECT_NAME, PROJECT_LAYERS, PROJECT_USER, PROJECT_STORE_DATA, PROJECT_FPS
from ..utils import get as sieve_get
from ..utils import post as sieve_post

def _model_from_json(models_json) -> SieveModel:
    return SieveModel(
        id=models_json[MODEL_ID],
        name=models_json[MODEL_NAME],
        version='dummy',
        status='dummy'
    )

def _model_to_json(model: SieveModel) -> Dict:
    return {
        MODEL_ID: model.id,
        MODEL_NAME: model.name
    }

def _layer_from_json(layer_json) -> SieveLayer:
    iteration_type = layer_json[PROJECT_LAYER_ITERATION_TYPE]
    models = [_model_from_json(model_json) for model_json in layer_json[PROJECT_LAYER_MODELS]]
    return SieveLayer(
        iteration_type=iteration_type,
        models=models
    )

def _layer_to_json(layer: SieveLayer) -> Dict:
    return {
        PROJECT_LAYER_ITERATION_TYPE: layer.iteration_type.value,
        PROJECT_LAYER_MODELS: [_model_to_json(model) for model in layer.models]
    }

def _project_from_json(project_json) -> SieveProject:
    name = project_json[PROJECT_NAME]
    layers = SieveWorkflow([_layer_from_json(layer_json) for layer_json in project_json[PROJECT_LAYERS]])
    store_data = project_json[PROJECT_STORE_DATA]
    fps = project_json[PROJECT_FPS]
    return SieveProject(
        name=name,
        workflow=layers,
        store_data=store_data,
        fps=fps
    )

def _project_to_json(project: SieveProject) -> Dict:
    return {
        PROJECT_NAME: project.name,
        PROJECT_LAYERS: [_layer_to_json(layer) for layer in project.workflow.layers],
        PROJECT_STORE_DATA: project.store_data,
        PROJECT_FPS: project.fps
    }

def list() -> List[SieveProject]:
    """
    List all projects
    """
    res = sieve_get(f'{API_URL}/{API_BASE}/projects')
    if res.status_code == 200:
        res_json = res.json()
        project_list = res_json['data']
        return [_project_from_json(project_json) for project_json in project_list]
    else:
        try:
            res_json = res.json()
            raise Exception(res_json['description'])
        except:
            raise Exception(f'Error: {res.status_code} {res.text}')

def get(project_name: str) -> SieveProject:
    """
    Gets a single project from Sieve by name

    Args:
        project_name (str): Name of project

    Returns:
        SieveProject: SieveProject object
    """
    res = sieve_get(f'{API_URL}/{API_BASE}/projects/{project_name}')
    if res.status_code == 200:
        res_json = res.json()
        project_json = res_json['data']
        return _project_from_json(project_json)
    else:
        try:
            res_json = res.json()
            raise Exception(res_json['description'])
        except:
            raise Exception(f'Error: {res.status_code} {res.text}')

def create(project: SieveProject) -> SieveProject:
    """
    Creates a project on Sieve

    Args:
        project (SieveProject): SieveProject object

    Returns:
        SieveProject: SieveProject object
    """
    res = sieve_post(
        f'{API_URL}/{API_BASE}/projects',
        data={
            PROJECT_CREATE_CONFIG: _project_to_json(project),
            PROJECT_NAME: project.name
        }
    )
    if res.status_code == 200:
        res_json = res.json()
        project_json = res_json
        return _project_from_json(project_json)
    else:
        try:
            res_json = res.json()
            raise Exception(res_json['description'])
        except:
            raise Exception(f'Error: {res.status_code} {res.text}')
