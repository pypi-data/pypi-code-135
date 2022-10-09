from __future__ import annotations

import logging
import httpx
import os.path
import hashlib

from pydantic import BaseModel as PydanticBaseModel
from pydantic import ValidationError

from enum import Flag, auto


logger = logging.getLogger(__name__)


class ModelCheckFlag(Flag):
  """checks to perform during the model.fetch operation
     none: no check
     exists: assert the response is not none
     single: assert a single object was returned, if a list, take the first object
     many: assert a list was returned with more than one object
  """
  none = 0
  exists = auto()
  single = auto()
  many = auto()


class BaseModel(PydanticBaseModel):
  """extension of the pydantic basemodel

     supports hashing to string
     post to endpoint
     get from endpoint

     NB: endpoints returning a list will attempt to convert to a list of objects,
         this happens when the validation (BaseModel.parse_obj(response.json())) fails
         with a ValidationError. Models with no required fields (None defaults, etc)
         will NOT throw a validation error when presented with a list and will
         simply produce an object with all defaults or all Nones.

         **Models which use fetch must have at least one required attribute.**
  """
  @classmethod
  def __uri(cls, uri):
    if not (isinstance(uri, (list, tuple)) or isinstance(uri, str)):
      raise ValueError("unsupported uri type: '%s' [%s]", str(uri), str(type(uri)))

    return uri if not isinstance(uri, (list,tuple)) else os.path.join(*uri)

  @classmethod
  def __parse_response(cls, x, container_key):
    """parse a json response into this class"""
    def parse_single(x: dict) -> cls:
      return cls.parse_obj(x)

    def parse_list(x: list[dict]) -> [cls]:
      return [cls.parse_obj(_x) for _x in x]

    def parse_list_with_key(x: list[dict]) -> [cls]:
      if container_key is None:
        raise ValueError("container_key cannot be None")

      return [cls.parse_obj(_x) for _x in x[container_key]]

    parsers = (parse_single, parse_list, parse_list_with_key)

    for parser in parsers:
      try:
        return parser(x)
      except ValidationError as e:
        continue
      except ValueError as e:
        logger.warning(str(e))
        continue
      except KeyError as e:
        logger.error("'%s' not found in '%s'", str(container_key), str(x.keys()))
        raise e

    raise ValueError("could not parse '%s'" % str(x))

  async def submit(self, uri, httpx_client=None, return_type=None) -> dict:
    """post this model somewhere
       FIXME: use httpx.response.raise_for_status() and return the response json
    """
    uri = self.__uri(uri)

    if httpx_client is None:
      try:
        async with httpx.AsyncClient() as hx:
          resp = await hx.post(uri, json=self.dict(by_alias=True))
      except httpx.ConnectError as e:
        logger.error("'%s' connection error", uri)
        return False
    else:
      resp = await httpx_client.post(uri, json=self.dict(by_alias=True))

    if resp.status_code != 200:
      logger.error("'%s': [%03i] %s", uri, resp.status_code, resp.text)
      raise ValueError

    if return_type is None:
      return resp.status_code == 200
    elif return_type == dict:
      return resp.json()
    elif callable(return_type):
      return return_type(resp.json())

  @classmethod
  async def fetch(
      cls,
      uri: str,
      httpx_client=None,
      headers: dict=None,
      container_key: str="items",
      ensure: ModelCheckFlag=ModelCheckFlag.none
    ):
    """get this model from a url

       uri: httpx endpoint, str or iterable of string (if iterable, os.path.join'd)
       httpx_client: httpx client session to use, if None a new is created
       headers: dict of HTTP headers to pass through to the call (will be added to httpx_client if present)
       container_key: if response is a list of dict, check in this key at the root for items
       ensure: qualities to ensure about the return value

       returns instantiation of the class with data from the endpoint

       raises:
         pydantic.ValidationError if the endpoint json cannot be mapped onto the class
    """
    uri = cls.__uri(uri)

    try:
      if httpx_client is None:
        async with httpx.AsyncClient() as hx:
          resp = await hx.get(uri, headers=headers)
      else:
        resp = await httpx_client.get(uri, headers=headers)
      resp.raise_for_status()
    except httpx.RequestError as e:
      logger.error("connection failed: '%s' [%s]", uri, str(e))
      return None
    except httpx.HTTPStatusError as e:
      logger.error("[%04i] '%s': '%s'", e.response.status_code, uri, e.response.text)
      return None

    data = cls.__parse_response(resp.json(), container_key)

    if ensure == ModelCheckFlag.none:
      return data

    if ensure & ModelCheckFlag.exists:
      assert data is not None

    if ensure & ModelCheckFlag.single:
      if isinstance(data, (list, tuple)):
        if len(data) > 1:
          logger.warning("recieved %i items with single constraint, retaining first", len(data))
          data = data[0]
        elif len(data) == 1:
          data = data[0]
        elif len(data) == 0:
          logger.warning("zero items recieved with single constraint, returning None")
          data = None

    if ensure & ModelCheckFlag.many:
      if not isinstance(data, (list, tuple)):
        data = [data]

    return data

  def hash(self) -> str:
    j = self.json(by_alias=True, sort_keys=True)
    return hashlib.md5(j.encode()).hexdigest()

  def __hash__(self) -> int:
    return int(self.hash(), base=16)

#  class Config:
#    arbitrary_types_allowed = True
