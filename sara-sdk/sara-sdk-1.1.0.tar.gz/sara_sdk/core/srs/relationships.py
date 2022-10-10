from typing import Dict
from ...client.requests import fetch

from sara_sdk.common.session import Session
from ...utils.rest import retrieve as _retrieve, list as _list, list_paginated as _list_paginated, update as _update, delete as _delete, create as _create

RESOURCE = "srs/relationships"


def list(session: Session = None, **filters):
    """
    List relationships

    Args:
      session (Session): Used only if want to use a different session instead default
      filters (Any): filters to pass to filter the list of relationships

    Returns:
      result (json): returns the result of the request as json

    Example:
      >>> list(page=1,page_size=10,name="relationship name")
    """
    result = _list(resource=RESOURCE, session=session, **filters)
    return result

def list_paginated(session: Session = None, **filters):
    """
    List iterator of relationships pages

    Args:
      session (Session): Used only if want to use a different session instead default
      filters (Any): filters to pass to filter the list of relationships

    Returns:
      result (json): returns the result of the request as json by page

    Example:
      >>> next(list(page=1,page_size=10,name="relationship name"))
    """
    result = _list_paginated(resource=RESOURCE, session=session,
                             version="v2", **filters)
    return result

def retrieve(uuid: str, session: Session = None):
    """
    Retrieve a relationship by uuid

    Args:
      uuid (UUID): uuid to return a relationship
      session (Session): Used only if want to use a different session instead default

    Returns:
      result (json): returns the result of the request as json

    Example:
      >>> retrieve("3daa992b-ccca-4920-bcfd-24015d8f2f10")
    """
    result = _retrieve(RESOURCE, uuid, session=session)
    return result

def create(bucket: str, session: Session = None):
    """
    Create a relationship

    Args:
      bucket (str): bucket to create a relationship
      data (Dict): data to create a relationship
      session (Session): Used only if want to use a different session instead default

    Returns:
      result (json): returns the result of the request as json

    Example:
      >>> create({"bucket": "515488d3-0262-4879-ab2f-7da8d107e447"})
    """
    result = _create(RESOURCE, bucket=bucket, session=session)
    return result

def update(uuid: str, bucket: str, model: Dict, session: Session = None):
    """
    Update a relationship

    Args:
      uuid (UUID): uuid to update a relationship
      data (Dict): data to update a relationship
      session (Session): Used only if want to use a different session instead default

    Returns:
      result (json): returns the result of the request as json

    Example:
      >>> update("515488d3-0262-4879-ab2f-7da8d107e447", {"bucket": "3daa992b-ccca-4920-bcfd-24015d8f2f10"})
    """
    model = {
      "uuid": uuid,
      "bucket": bucket
    }
    result = _update(RESOURCE, uuid, payload=model, session=session)
    return result

def delete(uuid: str, session: Session = None):
    """
    Delete a relationship

    Args:
      uuid (UUID): uuid to delete a relationship
      session (Session): Used only if want to use a different session instead default

    Returns:
      result (json): returns the result of the request as json

    Example:
      >>> delete("515488d3-0262-4879-ab2f-7da8d107e447")
    """
    result = _delete(RESOURCE, uuid, session=session)
    return result