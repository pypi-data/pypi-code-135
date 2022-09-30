#
# Copyright (c) 2015-2021 Thierry Florac <tflorac AT ulthar.net>
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#

"""PyAMS_scheduler.task.rest module

This module defines REST caller task.
"""

import codecs
import json
import pprint
import sys
import traceback
from urllib import parse

import chardet
import requests
from requests import ConnectionError
from zope.schema.fieldproperty import FieldProperty

from pyams_scheduler.interfaces.task import TASK_STATUS_ERROR, TASK_STATUS_FAIL, TASK_STATUS_OK
from pyams_scheduler.interfaces.task.rest import IRESTCallerTask
from pyams_scheduler.task import Task
from pyams_security.interfaces.names import UNCHANGED_PASSWORD
from pyams_utils.dict import format_dict
from pyams_utils.factory import factory_config
from pyams_utils.html import html_to_text


__docformat__ = 'restructuredtext'

from pyams_scheduler import _  # pylint: disable=ungrouped-imports


@factory_config(IRESTCallerTask)
class RESTCallerTask(Task):
    """REST API caller task"""

    label = _("HTTP service")
    icon_class = 'fab fa-battle-net'

    base_url = FieldProperty(IRESTCallerTask['base_url'])
    service = FieldProperty(IRESTCallerTask['service'])
    params = FieldProperty(IRESTCallerTask['params'])
    verify_ssl = FieldProperty(IRESTCallerTask['verify_ssl'])
    connection_timeout = FieldProperty(IRESTCallerTask['connection_timeout'])
    allow_redirects = FieldProperty(IRESTCallerTask['allow_redirects'])
    ok_status = FieldProperty(IRESTCallerTask['ok_status'])
    authenticate = FieldProperty(IRESTCallerTask['authenticate'])
    username = FieldProperty(IRESTCallerTask['username'])
    _password = FieldProperty(IRESTCallerTask['password'])
    use_proxy = FieldProperty(IRESTCallerTask['use_proxy'])
    proxy_server = FieldProperty(IRESTCallerTask['proxy_server'])
    proxy_port = FieldProperty(IRESTCallerTask['proxy_port'])
    proxy_username = FieldProperty(IRESTCallerTask['proxy_username'])
    _proxy_password = FieldProperty(IRESTCallerTask['proxy_password'])
    use_jwt_authority = FieldProperty(IRESTCallerTask['use_jwt_authority'])
    jwt_authority_url = FieldProperty(IRESTCallerTask['jwt_authority_url'])
    jwt_token_service = FieldProperty(IRESTCallerTask['jwt_token_service'])
    jwt_login_field = FieldProperty(IRESTCallerTask['jwt_login_field'])
    jwt_password_field = FieldProperty(IRESTCallerTask['jwt_password_field'])
    jwt_token_attribute = FieldProperty(IRESTCallerTask['jwt_token_attribute'])
    jwt_use_proxy = FieldProperty(IRESTCallerTask['jwt_use_proxy'])

    @property
    def password(self):
        """Password getter"""
        return self._password

    @password.setter
    def password(self, value):
        """Password setter"""
        if value == UNCHANGED_PASSWORD:
            return
        self._password = value

    @property
    def proxy_password(self):
        """Proxy password getter"""
        return self._proxy_password

    @proxy_password.setter
    def proxy_password(self, value):
        """Proxy password setter"""
        if value == UNCHANGED_PASSWORD:
            return
        self._proxy_password = value

    @property
    def ok_status_list(self):
        """OK status list getter"""
        return map(int, self.ok_status.split(','))

    def run(self, report, **kwargs):
        # pylint: disable=too-many-locals,too-many-branches,too-many-statements
        # get remote service URL
        method, service = self.service
        rest_service = f'{self.base_url}{service}'
        report.write(f'HTTP service output\n'
                     f'===================\n'
                     f'HTTP service: \n    {method} {rest_service}\n\n')
        # check proxy configuration
        proxies = {}
        if self.use_proxy:
            parsed = parse.urlparse(self.base_url)
            if self.proxy_username:
                proxy_auth = f'{self.proxy_username}:{self.proxy_password}@'
            else:
                proxy_auth = ''
            proxies[parsed.scheme] = f'http://{proxy_auth}{self.proxy_server}:{self.proxy_port}'
        # check JWT authorization
        auth = None
        headers = {}
        if self.use_jwt_authority:
            jwt_method, jwt_service = self.jwt_token_service
            jwt_service = f'{self.jwt_authority_url}{jwt_service}'
            jwt_params = {
                self.jwt_login_field: self.username,
                self.jwt_password_field: self.password
            }
            try:
                jwt_request = requests.request(jwt_method, jwt_service,
                                               headers={
                                                   'Content-Type': 'application/json'
                                               },
                                               params=jwt_params if jwt_method == 'GET' else None,
                                               data=json.dumps(jwt_params)
                                                   if jwt_method != 'GET' else None,
                                               proxies=proxies if self.jwt_use_proxy else None,
                                               timeout=self.connection_timeout,
                                               allow_redirects=False)
            except ConnectionError:
                etype, value, tb = sys.exc_info()  # pylint: disable=invalid-name
                report.write('\n\n'
                             'An HTTP error occurred\n'
                             '======================\n')
                report.write(''.join(traceback.format_exception(etype, value, tb)))
                return TASK_STATUS_FAIL, None
            else:
                status_code = jwt_request.status_code
                report.write(f'JWT token status code: {status_code}\n')
                if status_code != requests.codes.ok:  # pylint: disable=no-member
                    report.write(f'JWT headers: {format_dict(jwt_request.headers)}\n')
                    report.write(f'JWT params: {format_dict(jwt_params)}\n')
                    report.write(f'JWT report: {jwt_request.text}\n\n')
                    return TASK_STATUS_ERROR, None
                headers['Authorization'] = f'Bearer ' \
                                           f'{jwt_request.json().get(self.jwt_token_attribute)}'
        # build authorization headers
        elif self.username:
            auth = self.username, self.password
        # check params
        params = {}
        if self.params:
            params.update(json.loads(self.params))
        params.update(kwargs)
        # build HTTP request
        try:
            rest_request = requests.request(method, rest_service,
                                            auth=auth,
                                            headers=headers,
                                            params=params if method == 'GET' else None,
                                            data=params if method != 'GET' else None,
                                            verify=self.verify_ssl,
                                            proxies=proxies,
                                            timeout=self.connection_timeout,
                                            allow_redirects=self.allow_redirects)
        except ConnectionError:
            etype, value, tb = sys.exc_info()  # pylint: disable=invalid-name
            report.write('\n\n'
                         'An HTTP error occurred\n'
                         '======================\n')
            report.write(''.join(traceback.format_exception(etype, value, tb)))
            return TASK_STATUS_FAIL, None
        else:
            # check request status
            status_code = rest_request.status_code
            report.write(f'Status code: {status_code}\n')
            report.write(f'Headers: {format_dict(rest_request.headers)}\n\n')
            # check request content
            content_type = rest_request.headers.get('Content-Type', 'text/plain')
            if content_type.startswith('application/json'):
                response = rest_request.json()
                message = pprint.pformat(response)
            elif content_type.startswith('text/html'):
                message = html_to_text(rest_request.text)
            elif content_type.startswith('text/'):
                message = rest_request.text
            else:
                content = rest_request.content
                if 'charset=' in content_type.lower():
                    charset = content_type.split('=', 1)[1]
                else:
                    charset = chardet.detect(content).get('encoding') or 'utf-8'
                message = codecs.decode(content, charset)
            report.write(message)
            report.write('\n\n')
            return (
                TASK_STATUS_OK if status_code in self.ok_status_list else status_code,
                rest_request
            )
