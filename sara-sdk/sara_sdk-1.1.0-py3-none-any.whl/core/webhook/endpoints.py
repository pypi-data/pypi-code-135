from array import array
from typing import Dict
import json
from sara_sdk.client.requests import fetch
from sara_sdk.common.session import Session
from ...utils.rest import retrieve as _retrieve, list as _list, update as _update, delete as _delete, create as _create
from requests import post


RESOURCE = "webhook/endpoints"


def list(session: Session = None, **filters):
    """
    List a array of endpoints

    Args:
      session (Session): Used only if want to use a different session instead default
      filters (Any): filters to pass to filter the list of endpoints

    Returns:
      result (json): returns the result of the request as json

    Example:
      >>> list()
    """
    result = _list(resource=RESOURCE, session=session, **filters)
    return result


def create(url: Dict, session: Session = None):
    """
    Create a new endpoint

    Args:
      name (string): name of the endpoint
      url (string): url of the endpoint
      session (Session): Used only if want to use a different session instead default

    Returns:
      result (json): returns the result of request as json

    Example:
      >>> create("https://endpoint.url")
    """
    result = _create(resource=RESOURCE, payload=url, session=session)
    return result


def retrieve(uuid: str, session: Session = None):
    """
    Retrieve a endpoint

    Args:
      uuid (string): uuid of the endpoint
      session (Session): Used only if want to use a different session instead default

    Returns:
      result (json): returns the result of request as json

    Example:
      >>> retrieve("f8b85a7a-4540-4d46-a2ed-00e6134ee84a")
    """
    result = _retrieve(resource=RESOURCE, id=uuid, session=session)
    return result


def update(uuid: str, url: Dict, session: Session = None):
    """
    Update a endpoint

    Args:
      uuid (string): uuid of the endpoint
      url (string): url of the endpoint
      session (Session): Used only if want to use a different session instead default

    Returns:
      result (json): returns the result of request as json

    Example:
      >>> update("f8b85a7a-4540-4d46-a2ed-00e6134ee84a", { "url": "https://endpoint.url" })
    """
    data = {"url": url}
    result = _update(resource=RESOURCE, id=uuid, payload=url, session=session)
    return result


def delete(uuid: str, session: Session = None):
    """
    Delete a endpoint

    Args:
      uuid (string): uuid of the endpoint
      session (Session): Used only if want to use a different session instead default

    Returns:
      result (json): returns the result of request as json

    Example:
      >>> delete("f8b85a7a-4540-4d46-a2ed-00e6134ee84a")
    """
    result = _delete(resource=RESOURCE, id=uuid, session=session)
    return result


def list_relations(endpoint: str, session: Session = None, **filters):
    """
    List a array of relations

    Args:
      endpoint (string): uuid of the endpoint
      session (Session): Used only if want to use a different session instead default
      filters (Any): filters to pass to filter the list of relations

    Returns:
      result (json): returns the result of the request as json

    Example:
      >>> list_realations()
    """
    result = _list(resource="{}/{}/relations".format(RESOURCE,
                   endpoint), session=session, **filters)
    return result


def create_relations(endpoint: str, robot: array, topic: array, session: Session = None):
    """
    Create a new relation

    Args:
      endpoint (string): uuid of the endpoint
      topic (string): name of the topics
      robot (string): uuid of the robots
      session (Session): Used only if want to use a different session instead default

    Returns:
      result (string): returns the result of the request as string

    Example:
      >>> create_relations("endpoint_uuid", [robots], [topics])
    """
    data = {"robots": robot, "topics": topic}
    result = fetch(method=post, path="{}/{}/relations".format(RESOURCE,
                                                              endpoint), payload=data, session=session)
    return result.content.decode("utf-8")


def delete_relations(endpoint: str, uuid: str, session: Session = None):
    """
    Delete a relation

    Args:
      endpoint (string): uuid of the endpoint
      uuid (string): uuid of the relation
      session (Session): Used only if want to use a different session instead default

    Returns:
      result (json): returns the result of request as json

    Example:
      >>> delete_relations("endpoint_uuid", "relation_uuid")
    """
    result = _delete(
        resource="{}/{}/relations".format(RESOURCE, endpoint), id=uuid, session=session)
    return result
