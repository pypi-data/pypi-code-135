from typing import Dict
import json
from sara_sdk.client.requests import fetch
from sara_sdk.common.session import Session
from requests import post

RESOURCE = "metrics"


def retrieve(measurement: str, range: str, filters: Dict = None, options: Dict = None, groups: list[str] = None, session: Session = None, **kwargs):
    """
    Retrieve a metric by measurement, range and body
    Args:
      measurement (string): Measurement name
      range (string): Measurement range
      filters (Dict): A dictionary with the data the will be used on metric (optional) assisted, robot
      options (Dict): A dictionary with the options the will be used on metric (optional) window, function, empty
      groups (list[str]): A list with the groups the will be used on metric (optional)
      session (Session): Used only if want to use a different session instead default
      filters (Any): filters to pass to filter the list of metrics
    Returns:
      result (json): returns the result of the request as json
    Example:
      >>> retrieve("missions_v2_status", "start:-5m", {"locality": "locality_slug"}, {"window": "1m"}, ["group_name"])
    """
    body = {
        "filters": filters,
        "range": range,
        "measurement": measurement,
        "options": options,
        "groups": groups
    }
    result = fetch(method=post, path="{}/{}".format(RESOURCE,
                   measurement), session=session, payload=body, **kwargs)
    return result.json()
