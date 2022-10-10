from typing import Dict
from sara_sdk.common.session import Session
from ...utils.rest import list as _list, list_paginated as _list_paginated, create as _create, retrieve as _retrieve, delete as _delete

RESOURCE = "missions/tags"

def list(session: Session = None, **filters):
    """
    List a array of tags
    Args:
      session (Session): Used only if want to use a different session instead default
      filters (Any): filters to pass to filter the list of tags
    Returns:
      result (json): returns the result of the request as json
    Example:
      >>> list(page=1,page_size=10,name="tag name")
    """
    result = _list(resource=RESOURCE, session=session,version="v2", **filters)
    return result

def list_paginated(session: Session = None, **filters):
    """
    List iterator of pages of tags
    Args:
      session (Session): Used only if want to use a different session instead default
      filters (Any): filters to pass to filter the list of tags
    Returns:
      result (json): returns the result of the request as json by page
    Example:
      >>> next(list(page=1,page_size=10,name="tag name"))
    """
    result = _list_paginated(resource=RESOURCE, session=session,
                             version="v2", **filters)
    return result

def retrieve(uuid: str, session: Session = None):
    """
    Retrieve a tag by passing id
    Args:
      id (UUID): tag id to retrieve
      session (Session): Used only if want to use a different session instead default
    Returns:
      result (json): returns the result of the request as json
    Example:
      >>> retrieve("f8b85a7a-4540-4d46-a2ed-00e6134ee84a")
    """
    result = _retrieve(RESOURCE, id=uuid, session=session, version="v2")
    return result

def create(model: Dict, session: Session = None):
    """
    Create a tag
    Args:
      name (str): name of the tag
      session (Session): Used only if want to use a different session instead default
    Returns:
      result (json): returns the result of the request as json
    Example:
      >>> create("tag name")
    """
    result = _create(RESOURCE, payload=model, session=session,version="v2")
    return result

def delete(uuid: str, session: Session = None):
    """
    Delete a tag
    Args:
      uuid (str): id of the tag
      session (Session): Used only if want to use a different session instead default
    Returns:
      result (json): returns the result of the request as json
    Example:
      >>> delete("f8b85a7a-4540-4d46-a2ed-00e6134ee84a")
    """
    print('delete')
    result = _delete(RESOURCE, id=uuid, session=session, version="v2")
    return result