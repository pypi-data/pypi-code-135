from typing import Dict
from ...client.requests import fetch
from requests import get

from sara_sdk.common.session import Session
from ...utils.rest import retrieve as _retrieve, list as _list, list_paginated as _list_paginated, update as _update, delete as _delete, create as _create

RESOURCE = "telemetry"

def listDiagnostics(robotId: str,session: Session = None, **filters):
    """
    List robot telemetry diagnostics
    Args:
      robotId (str): robotId to return telemetry diagnostics
      session (Session): Used only if want to use a different session instead default
      filters (Any): filters to pass to filter the list of telemetry
    Returns:
      result (json): returns the result of the request as json
    Example:
      >>> list("f8b85a7a-4540-4d46-a2ed-00e6134ee84a", page=1,page_size=10)
    """
    result = _list(resource="{}/{}/diagnostics".format(RESOURCE, robotId), session=session, **filters)
    return result

def isOnline(robotId: str,session: Session = None, **filters):
    """
    Check robot connection status
    Args:
      robotId (str): robotId to return connection status
      session (Session): Used only if want to use a different session instead default
      filters (Any): filters to pass to filter the list of telemetry
    Returns:
      result (json): returns the result of the request as json
    Example:
      >>> list("f8b85a7a-4540-4d46-a2ed-00e6134ee84a")
    """
    result = fetch(path="{}/{}/isonline".format(RESOURCE, robotId), method=get, session=session, **filters)
    return result.content.decode("utf-8")

def connection(robotId: str, middleware: str, session: Session = None, **filters):
    """
    Check middleware status
    Args:
      robotId (str): robotId to check middleware status
      middleware (str): middleware to check ('mission-bridge','mqtt-bridge','webrtc-signaling-proxy')
      session (Session): Used only if want to use a different session instead default
      filters (Any): filters to pass to filter the list of telemetry
    Returns:
      result (json): returns the result of the request as json
    Example:
      >>> list("f8b85a7a-4540-4d46-a2ed-00e6134ee84a")
    """
    filters["middleware"] = middleware
    result = _list(resource="{}/{}/connection".format(RESOURCE, robotId), session=session, **filters)
    return result

def srsFeedback(feedbackId: str,session: Session = None, **filters):
    """
    Retrieve last robot feedback
    Args:
      feedbackId (str): feedbackId to return a telemetry
      session (Session): Used only if want to use a different session instead default
      filters (Any): filters to pass to filter the list of telemetry
    Returns:
      result (json): returns the result of the request as json
    Example:
      >>> list("U_a21685f7-aca5-4ac7-b93f-5ec711478858")
    """
    result = _list(resource="{}/srs-feedback/{}".format(RESOURCE, feedbackId), session=session, **filters)
    return result