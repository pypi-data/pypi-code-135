from typing import Dict
import json
from sara_sdk.common.session import Session
from ...utils.rest import list as _list, list_paginated as _list_paginated, create as _create, retrieve as _retrieve
from requests import get, post, delete as _delete, patch
from ...client.requests import fetch

RESOURCE = "missions"


def list(robot: str, session: Session = None, **filters):
    """
    List a array of missions

    Args:
      robot (UUID): robot to return a mission
      session (Session): Used only if want to use a different session instead default
      filters (Any): filters to pass to filter the list of missions

    Returns:
      result (json): returns the result of the request as json

    Example:
      >>> list(page=1,page_size=10,name="mission name")
    """
    filters["robot_id"] = robot
    result = _list(resource=RESOURCE, session=session, version="v2", **filters)
    return result


def retrieve(uuid: str, session: Session = None):
    """
    Retrieve a mission by passing uuid

    Args:
      mission (UUID): mission uuid to retrieve
      session (Session): Used only if want to use a different session instead default

    Returns:
      result (json): returns the result of the request as json

    Example:
      >>> retrieve("f8b85a7a-4540-4d46-a2ed-00e6134ee84a")
    """
    result = _retrieve(RESOURCE, id=uuid, session=session, version="v2")
    return result


def list_paginated(robot: str, session: Session = None, **filters):
    """
    List iterator of pages of missions

    Args:
      robot (UUID): robot to return a mission
      session (Session): Used only if want to use a different session instead default
      filters (Any): filters to pass to filter the list of missions

    Returns:
      result (json): returns the result of the request as json by page

    Example:
      >>> next(list(page=1,page_size=10,name="mission name"))
    """
    filters["robot_id"] = robot
    result = _list_paginated(resource=RESOURCE, session=session,
                             version="v2", **filters)
    return result


def last(robot: str, session: Session = None):
    """
    Retrieve the last mission by robot id

    Args:
      robot (UUID): robot to return a mission
      session (Session): Used only if want to use a different session instead default

    Returns:
      result (json): returns the result of the request as json

    Example:
      >>> retrieve("f8b85a7a-4540-4d46-a2ed-00e6134ee84a")
    """
    result = _list(RESOURCE+"/last", session=session,
                   version="v2", robot_id=robot)
    return result


def create(robot: str, stages: Dict, session: Session = None):
    """
    Create a mission by passing an model (Data)

    Args:
      robot (UUID): robot uuid to create mission
      stages (Dict): A dictionary with the data the will be used to create an mission
      session (Session): Used only if want to use a different session instead default

    Returns:
      result (json): returns the result of the request as json
    """
    model = {
        "robot": robot,
        "stages": json.dumps(stages)
    }
    result = _create(RESOURCE, payload=model, session=session, version="v2")
    return result


def retry(mission: str, session: Session = None):
    """
    Retry a mission by passing uuid

    Args:
      mission (UUID): mission uuid to retry
      session (Session): Used only if want to use a different session instead default

    Returns:
      null

    Example:
      >>> retry("f8b85a7a-4540-4d46-a2ed-00e6134ee84a")
    """
    result = fetch(path=RESOURCE+"/"+mission+"/retry",
                   session=session, method=post, version="v2")
    if result and result.status == 202:
        return True
    return False


def cancel(mission: str, session: Session = None):
    """
    Cancel a mission by passing uuid

    Args:
      mission (UUID): mission uuid to cancel
      session (Session): Used only if want to use a different session instead default

    Returns:
      null

    Example:
      >>> cancel("f8b85a7a-4540-4d46-a2ed-00e6134ee84a")
    """
    result = fetch(path=RESOURCE+"/"+mission+"/cancel",
                   session=session, method=post, version="v2")
    if result and result.status == 202:
        return True
    return False


def pause(mission: str, session: Session = None):
    """
    Pause a mission by passing uuid

    Args:
      mission (UUID): mission uuid to pause
      session (Session): Used only if want to use a different session instead default

    Returns:
      null

    Example:
      >>> pause("f8b85a7a-4540-4d46-a2ed-00e6134ee84a")
    """
    result = fetch(path=RESOURCE+"/"+mission+"/pause",
                   session=session, method=post, version="v2")
    if result and result.status == 202:
        return True
    return False


def resume(mission: str, session: Session = None):
    """
    Resume a mission by passing uuid

    Args:
      mission (UUID): mission uuid to resume
      session (Session): Used only if want to use a different session instead default

    Returns:
      null

    Example:
      >>> resume("f8b85a7a-4540-4d46-a2ed-00e6134ee84a")
    """
    result = fetch(path=RESOURCE+"/"+mission+"/resume",
                   session=session, method=post, version="v2")
    if result and result.status == 202:
        return True
    return False


def list_tags(mission: str, session: Session = None):
    """
    List a array of missions tags

    Args:
      mission (UUID): mission to return a mission tags
      session (Session): Used only if want to use a different session instead default

    Returns:
      result (json): returns the result of the request as json

    Example:
      >>> list_tags("f8b85a7a-4540-4d46-a2ed-00e6134ee84a")
    """
    result = _list(resource="{}/{}/tags".format(RESOURCE,
                   mission), session=session, version="v2")
    return result


def retrieve_tags(mission: str, tag: str, session: Session = None):
    """
    Retrieve a mission tag by passing uuid

    Args:
      mission (UUID): mission uuid to retrieve
      tag (UUID): tag uuid to retrieve
      session (Session): Used only if want to use a different session instead default

    Returns:
      result (json): returns the result of the request as json

    Example:
      >>> retrieve_tags("f8b85a7a-4540-4d46-a2ed-00e6134ee84a","f8b85a7a-4540-4d46-a2ed-00e6134ee84a")
    """
    result = _retrieve(resource="{}/{}/tags".format(RESOURCE,
                       mission), id=tag, session=session, version="v2")
    return result


def list_steps(mission: str, session: Session = None):
    """
    List a array of steps from one mission

    Args:
      mission (UUID): mission to return a mission steps
      session (Session): Used only if want to use a different session instead default

    Returns:
      result (json): returns the result of the request as json

    Example:
      >>> list_steps("f8b85a7a-4540-4d46-a2ed-00e6134ee84a")
    """
    result = _list(resource="{}/{}/steps".format(RESOURCE,
                   mission), session=session, version="v2")
    return result


def retrieve_steps(mission: str, step: str, session: Session = None):
    """
    Retrieve a step of a mission by passing uuid

    Args:
      mission (UUID): mission uuid to retrieve
      step (UUID): step uuid to retrieve
      session (Session): Used only if want to use a different session instead default

    Returns:
      result (json): returns the result of the request as json

    Example:
      >>> retrieve_steps("f8b85a7a-4540-4d46-a2ed-00e6134ee84a","f8b85a7a-4540-4d46-a2ed-00e6134ee84a")
    """
    result = _retrieve(resource="{}/{}/steps".format(RESOURCE,
                       mission), id=step, session=session, version="v2")
    return result


def list_stages(mission: str, session: Session = None):
    """
    List a array of stages of one mission

    Args:
      mission (UUID): mission to return its stages
      session (Session): Used only if want to use a different session instead default

    Returns:
      result (json): returns the result of the request as json

    Example:
      >>> list_missions_stages("f8b85a7a-4540-4d46-a2ed-00e6134ee84a")
    """
    result = _list(resource="{}/{}/stages".format(RESOURCE,
                   mission), session=session, version="v2")
    return result


def retrieve_stages(mission: str, stage: str, session: Session = None):
    """
    Retrieve a stage of one mission by passing uuid

    Args:
      mission (UUID): mission uuid to retrieve
      stage (UUID): stage uuid to retrieve
      session (Session): Used only if want to use a different session instead default

    Returns:
      result (json): returns the result of the request as json

    Example:
      >>> retrieve_stage("f8b85a7a-4540-4d46-a2ed-00e6134ee84a","f8b85a7a-4540-4d46-a2ed-00e6134ee84a")
    """
    result = _retrieve(resource="{}/{}/stages".format(RESOURCE,
                       mission), id=stage, session=session, version="v2")
    return result


def list_stages_steps(mission: str, stage: str, session: Session = None):
    """
    List a array of steps of one stage of one mission

    Args:
      mission (UUID): mission to return its stages
      stage (UUID): stage to return its steps
      session (Session): Used only if want to use a different session instead default

    Returns:
      result (json): returns the result of the request as json

    Example:
      >>> list_stages_steps("f8b85a7a-4540-4d46-a2ed-00e6134ee84a","f8b85a7a-4540-4d46-a2ed-00e6134ee84a")
    """
    result = _list(resource="{}/{}/stages/{}/steps".format(RESOURCE,
                   mission, stage), session=session, version="v2")
    return result


def retrieve_stages_steps(mission: str, stage: str, step: str, session: Session = None):
    """
    Retrieve a step of one step of one mission by passing uuid

    Args:
      mission (UUID): mission uuid to retrieve
      stage (UUID): stage uuid to retrieve
      step (UUID): step uuid to retrieve
      session (Session): Used only if want to use a different session instead default

    Returns:
      result (json): returns the result of the request as json

    Example:
      >>> retrieve_missions_stages_step("f8b85a7a-4540-4d46-a2ed-00e6134ee84a","f8b85a7a-4540-4d46-a2ed-00e6134ee84a","f8b85a7a-4540-4d46-a2ed-00e6134ee84a")
    """
    result = _retrieve(resource="{}/{}/stages/{}/steps".format(RESOURCE,
                       mission, stage), id=step, session=session, version="v2")
    return result


def list_stages_params(mission: str, stage: str, session: Session = None):
    """
    List a array of params of one stage of one mission

    Args:
      mission (UUID): mission to return its stages
      stage (UUID): stage to return its params
      session (Session): Used only if want to use a different session instead default

    Returns:
      result (json): returns the result of the request as json

    Example:
      >>> list_stages_params("f8b85a7a-4540-4d46-a2ed-00e6134ee84a","f8b85a7a-4540-4d46-a2ed-00e6134ee84a")
    """
    result = _list(resource="{}/{}/stages/{}/params".format(RESOURCE,
                   mission, stage), session=session, version="v2")
    return result


def retrieve_stage_params(mission: str, stage: str, param: str, session: Session = None):
    """
    Retrieve a param of one stage of one mission by passing uuid

    Args:
      mission (UUID): mission uuid to retrieve
      stage (UUID): stage uuid to retrieve
      param (UUID): param uuid to retrieve
      session (Session): Used only if want to use a different session instead default

    Returns:
      result (json): returns the result of the request as json

    Example:
      >>> retrieve_stage_params("f8b85a7a-4540-4d46-a2ed-00e6134ee84a","f8b85a7a-4540-4d46-a2ed-00e6134ee84a","f8b85a7a-4540-4d46-a2ed-00e6134ee84a")
    """
    result = _retrieve(resource="{}/{}/stages/{}/params".format(RESOURCE,
                       mission, stage), id=param, session=session, version="v2")
    return result
