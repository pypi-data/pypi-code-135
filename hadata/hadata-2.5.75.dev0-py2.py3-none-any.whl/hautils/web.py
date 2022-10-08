import datetime
import os
import traceback
import humps
import bson
from fastapi.responses import Response
from hautils.logger import logger
import json
from mongoengine import Document, QuerySet, DateTimeField, ObjectIdField, ReferenceField
from mongoengine.base import TopLevelDocumentMetaclass
from pydantic import BaseModel
from fastapi import status

from hautils.slack import slack_notify

def to_camel_case(snake_str: dict):
    for k,v in list(snake_str.items()):
        if type(v) is dict:
            snake_str[humps.camelize(k)] = to_camel_case(v)
        else:
            snake_str[humps.camelize(k)] = v
        if humps.camelize(k) != k:
            snake_str.pop(k)

    return snake_str


def mongo_to_dict(content):
    if not issubclass(type(content), Document) and not issubclass(type(content), dict) and not issubclass(type(content),
                                                                                                          BaseModel):
        logger.warn("unsupported object type %s " % (type(content)))
        raise Exception
    if issubclass(type(content), Document):
        response_object = json.loads(content.to_json())
        # response_object["id"] = str(content.id)
        response_object.pop("_id")
        for field in content._fields.values():
            logger.debug("handling field %s of type %s" % (field.name, type(content[field.name])))
            try:
                if hasattr(field, 'sensitive') and field.sensitive:
                    if field.name in response_object:
                        response_object.pop(field.name)
                    continue
            except Exception as e:
                logger.error("error handling sensitive field %s" % (field.name,))
            if isinstance(content[field.name], DateTimeField) and content[field.name] is not None:
                response_object[field.name] = int(content[field.name].timestamp())
            elif isinstance(content[field.name], datetime.datetime) and content[field.name] is not None:
                response_object[field.name] = int(content[field.name].timestamp())
            elif isinstance(content[field.name], bson.objectid.ObjectId) and content[field.name] is not None:
                response_object[field.name] = str(content[field.name])
            elif isinstance(content[field.name], ObjectIdField) and content[field.name] is not None:
                response_object[field.name] = str(content[field.name])
            elif isinstance(field, ReferenceField) and content[field.name] is not None:
                response_object[field.name] = mongo_to_dict(content[field.name])
    elif issubclass(type(content), BaseModel):
        response_object = content.dict()
    else:
        logger.debug("format type %s" % (type(content)))
        response_object = content

    response_object = to_camel_case(response_object)

    return response_object


def json_response(content=None, dict_content: dict = None, http_status=200, pop_fields={}):
    try:
        if issubclass(type(content), QuerySet) or issubclass(type(content), list):
            response = []
            for doc in content:
                response.append(doc_cleanup(doc, pop_fields))
        else:
            response = doc_cleanup(content if content is not None else dict_content, pop_fields)
        logger.debug("json dumping type %s" % (type(response)))
        response = json.dumps(response)
        logger.info("json encode %s" % (response,))
        return Response(content=response, status_code=http_status, media_type="application/json")
    except Exception as e:
        exception_log(e)


def doc_cleanup(doc, pop_fields):
    response = mongo_to_dict(doc)
    for field in pop_fields:
        try:
            response.pop(field)
        except Exception as e:
            logger.error("field %s not in dictionary" % (field,))
    return response


def mongo_to_log(content):
    try:
        return json.dumps(mongo_to_dict(content))
    except Exception as e:
        return ""


def exception_log(e):
    logger.error(e)
    traceback_log = traceback.format_exception(type(e), e, e.__traceback__)
    logger.debug(traceback_log)
    formatted_message = """# Exception 
```
{}
```
""".format(traceback_log, os.getenv("APP_PREFIX"))
    slack_notify(message=formatted_message)
    raise ProcessException(http_status=status.HTTP_500_INTERNAL_SERVER_ERROR, errors={"error": str(type(e))})


class ProcessException(Exception):
    def __init__(self, errors=None, data=None, http_status=status.HTTP_500_INTERNAL_SERVER_ERROR):
        if data is None:
            data = {}
        self.errors = errors
        self.data = data
        self.status = http_status
