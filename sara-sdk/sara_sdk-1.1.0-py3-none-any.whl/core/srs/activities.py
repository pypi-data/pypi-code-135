from typing import Dict
from ...client.requests import fetch

from sara_sdk.common.session import Session
from ...utils.rest import list as _list, list_paginated as _list_paginated, create as _create

RESOURCE = "srs/activities"


def list(session: Session = None, **filters):
    """
    List activities

    Args:
      session (Session): Used only if want to use a different session instead default
      filters (Any): filters to pass to filter the list of activities

    Returns:
      result (json): returns the result of the request as json

    Example:
      >>> list(page=1,page_size=10,name="bucket name")
    """
    result = _list(resource=RESOURCE, session=session, **filters)
    return result

def list_paginated(session: Session = None, **filters):
    """
    List iterator of activities pages

    Args:
      session (Session): Used only if want to use a different session instead default
      filters (Any): filters to pass to filter the list of activities

    Returns:
      result (json): returns the result of the request as json by page

    Example:
      >>> next(list(page=1,page_size=10,name="bucket name"))
    """
    result = _list_paginated(resource=RESOURCE, session=session,
                             version="v2", **filters)
    return result

def create(robot: str, operation: str, payload: str, model: Dict, session: Session = None, **data):
    """
    Create an activity

    Args:
      robot (str): robot uuid
      operation (str): operation to create an activity ('DownloadFile', 'UploadFile', 'ExecuteFile')
      payload (str): filename, including path
      session (Session): Used only if want to use a different session instead default
      data (Any): data to create a activity

    Returns:
      result (json): returns the result of the request as json

    Example:
      >>> create({ "robot": "f8b85a7a-4540-4d46-a2ed-00e6134ee84a", "operation": "DownloadFile", "payload": "test.txt" })
    """
    model = {
      "robot": robot,
      "operation": operation,
      "payload": payload
    }
    result = _create(RESOURCE, payload=model, session=session)
    return result