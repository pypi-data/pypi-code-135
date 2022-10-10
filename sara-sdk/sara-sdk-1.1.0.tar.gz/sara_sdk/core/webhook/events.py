from typing import Dict
import json
from sara_sdk.common.session import Session
from ...utils.rest import retrieve as _retrieve, list as _list, update as _update, delete as _delete, create as _create

RESOURCE = "webhook/events"


def retrieve(uuid: str, session: Session = None):
    """
    Retrieve a event

    Args:
      uuid (string): uuid of the event
      session (Session): Used only if want to use a different session instead default

    Returns:
      result (json): returns the result of request as json

    Example:
      >>> retrieve("f8b85a7a-4540-4d46-a2ed-00e6134ee84a")
    """
    result = _retrieve(resource=RESOURCE, id=uuid, session=session)
    return result
