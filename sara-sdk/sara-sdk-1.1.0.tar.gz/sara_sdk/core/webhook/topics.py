from typing import Dict
from sara_sdk.common.session import Session
from ...utils.rest import list as _list, create as _create
from ...client.requests import fetch
from requests import delete as _delete

RESOURCE = "webhook/topics"


def list(service: str, session: Session = None, **filters):
    """
    List a array of topics

    Args:
      service (string): service of the topic
      session (Session): Used only if want to use a different session instead default
      filters (Any): filters to pass to filter the list of topics

    Returns:
      result (json): returns the result of the request as json

    Example:
      >>> list(service="service_name")
    """
    filters["service"] = service
    result = _list(resource=RESOURCE, session=session, **filters)
    return result


def create(name: str, action: str, service: str, session: Session = None):
    """
    Create a new topic

    Args:
      name (string): name of the topic
      action (string): name of the action
      service (string): service of the topic
      session (Session): Used only if want to use a different session instead default

    Returns:
      result (json): returns the result of request as json

    Example:
      >>> create("topic.action, topic.name, topic.service")
    """
    data = {"action": action, "name": name, "service": service}
    result = _create(resource=RESOURCE, payload=data, session=session)
    return result


def delete(service: str, action: str, session: Session = None):
    """
    Delete a topic

    Args:
      uuid (string): uuid of the topic
      session (Session): Used only if want to use a different session instead default

    Returns:
      result (json): returns the result of request as json

    Example:
      >>> delete("service_name", "action_name")
    """
    result = fetch(method=_delete, path="{}/{}/{}".format(RESOURCE, service, action),
                   session=session)
    return result.json()
