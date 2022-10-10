import re
import datetime as dt
import json
import sys
import traceback
from abc import ABC, abstractmethod
from distutils.util import strtobool
from typing import List, Optional, Dict, Union, Iterable, Any, Type

import pandas as pd
from flask import jsonify, request, Response, Blueprint
from pandas import DataFrame

from lumipy.common.string_utils import indent_str
from lumipy.query.expression.sql_value_type import SqlValType
from .common import table_dict_to_df
from .metadata import (
    ColumnMeta, ParamMeta, TableParam,
    RegistrationType, RegistrationCategory, RegistrationAttributes, LifeCycleStage
)
from enum import Enum


def _cast(name: str, value: Any, data_type: str) -> Union[int, float, str, bool, DataFrame, dt.datetime]:
    data_type = SqlValType[data_type]

    if value is None:
        return value

    if data_type == SqlValType.Int:
        return int(value)
    elif data_type == SqlValType.Double:
        return float(value)
    elif data_type == SqlValType.Text:
        return str(value)
    elif data_type == SqlValType.Boolean:
        return bool(strtobool(str(value)))
    elif data_type == SqlValType.Table:
        return table_dict_to_df(value)
    elif data_type == SqlValType.DateTime:
        return pd.to_datetime(value, utc=True)
    elif data_type == SqlValType.Date:
        return pd.to_datetime(value, utc=True)
    else:
        TypeError(f"Unsupported data type for parameter '{name}': {data_type.name}.")


def _metadata_type_check(name: str, target_type: Type, values: Union[str, Enum, Iterable]):

    if not hasattr(values, '__len__'):
        values = [values]

    if len(values) == 1 and values[0] is None:
        return

    for value in values:
        if value is not None and not isinstance(value, target_type):
            raise TypeError(f"{name} input value must be type {target_type.__name__} but was {type(value).__name__}.")


class BaseProvider(ABC):
    """Abstract base class for local python luminesce providers.

    All local provider classes must inherit from this class, call super().__init__() and implement the _get_data method.

    """

    @abstractmethod
    def __init__(
            self,
            name: str,
            columns: List[ColumnMeta],
            parameters: Optional[List[ParamMeta]] = None,
            table_parameters: Optional[List[TableParam]] = None,
            description: Optional[str] = None,
            documentation_link: Optional[str] = None,
            license_code: Optional[str] = None,
            registration_type: Optional[RegistrationType] = None,
            registration_category: Optional[RegistrationCategory] = None,
            registration_attributes: Optional[RegistrationAttributes] = None,
            lifecycle_stage: Optional[LifeCycleStage] = None,
    ):
        """Constructor of the BaseProvider class.

        Args:
            name (str): name to give the provider (e.g. Example.Local.Provider).
            columns (List[ColumnMeta]): list of columns metadata objects that define the parameter's columns.
            parameters (Optional[List[ParamMeta]]): optional list of parameter metadata objects that define the
            provider's parameters. If no values are supplied then the provider will be parameterless.
            description (Optional[str]): description of the provider.
            documentation_link (Optional[str]): the url linking to the provider documentation.
            license_code (Optional[str]): the license code of this provider.
            registration_type (Optional[RegistrationType]): registration type of the provider.
            registration_category (Optional[RegistrationCategory]): registration category of the provider.
            registration_attributes (Optional[RegistrationAttributes]): registration attributes of the provider.
            lifecycle_stage (Optional[LifeCycleStage])]: stage of the development lifecycle of the provider.

        """

        if (name is None) or re.match('^[a-zA-Z0-9.]+$', name) is None:
            raise ValueError("Provider name must be a non-empty string containing only '.' and alphanumeric chars.")

        if (len(columns) == 0) or any(not isinstance(c, ColumnMeta) for c in columns):
            raise TypeError(f"Provider columns input must be a non-empty list of {ColumnMeta.__name__}.")

        _metadata_type_check('parameters', ParamMeta, parameters)
        _metadata_type_check('table_parameters', TableParam, table_parameters)
        _metadata_type_check('registration_type', RegistrationType, registration_type)
        _metadata_type_check('registration_category', RegistrationCategory, registration_category)
        _metadata_type_check('registration_attributes', RegistrationAttributes, registration_attributes)
        _metadata_type_check('lifecycle_stage', LifeCycleStage, lifecycle_stage)

        self.name = name
        self.description = description
        self.documentation_link = documentation_link
        self.license_code = license_code
        self.registration_type = registration_type
        self.registration_category = registration_category
        self.registration_attributes = registration_attributes
        self.lifecycle_stage = lifecycle_stage

        self.path_name = name.replace('.', '-').lower()

        self.columns = {c.name: c for c in columns}
        self.parameters = {p.name: p for p in parameters} if parameters is not None else {}
        self.table_parameters = {p.name: p for p in table_parameters} if table_parameters is not None else {}

    def shutdown(self) -> None:
        """Method that is called whenever the provider needs to be shut down. By default this is a no-op, but if your
        provider needs to clean up after itself it should do it by overloading this method.

        """
        pass

    @abstractmethod
    def get_data(
            self,
            data_filter: Optional[Dict[str, object]],
            limit: Union[int, None],
            **params
    ) -> Iterable[Dict[str, Union[str, int, float]]]:
        """Abstract method that represents getting and then returning data from the provider given a data filter
        dictionary, an optional limit value, and a set of named parameter values. Overriding this method implements the
        core behaviour of the provider when its associated /api/v1/provider-name/data/ endpoint is called.

        Args:
            data_filter (Optional[Dict[str, object]]): data filter dictionary that represents a nested set of filter
            expressions on the provider data or None (no filter given in query). Inheritors must be able to handle both.
            limit (Optional[int]): integer limit value or None (no limit). Inheritors must be able to handle both.
            **params: parameter name-value pairs corresponding to the parameters given to the provider.

        Returns:
            List[Dict[str, Union[str, int, float]]]: list of dictionaries where the keys are the column names and the
            values are the column values. Each dictionary represents a row of data from the provider.
        """
        raise NotImplementedError("super()._get_data() does not do anything and shouldn't be called.")

    def _cast_row(self, row):
        return {k: _cast(self.columns[k].name, v, self.columns[k].data_type.name) for k, v in row.items()}

    def _fill_defaults(self, pvs):

        pv_dict = {pv['name']: pv for pv in pvs}

        for p_name, p_meta in self.parameters.items():
            if p_name not in pv_dict.keys():
                if p_meta.default_value is None and p_meta.is_required:
                    raise ValueError(f'The parameter {p_name} of {self.name} was not given but is required.')

                pv_dict[p_name] = {'name': p_name, 'value': p_meta.default_value, 'data_type': p_meta.data_type.name}

        for tp_name in self.table_parameters.keys():
            if tp_name not in pv_dict.keys():
                raise ValueError(f'The table parameter {tp_name} of {self.name} was not given but is required.')

        return pv_dict.values()

    def blueprint(self) -> Blueprint:
        """Create a flask blueprint object that implements the API for this local provider instance.

        Returns:
            Blueprint: flask blueprint object representing the API routes for this instance.
        """

        bp = Blueprint(self.path_name, self.path_name)

        @bp.route(f'/api/v1/{self.path_name}/metadata', methods=['GET'])
        def provider_metadata():
            return jsonify({
                "Name": self.name,
                "Description": self.description,
                "DocumentationLink": self.documentation_link,
                'LicenseCode': self.license_code,
                'RegistrationType': self.registration_type.name if self.registration_type else None,
                'RegistrationCategory': self.registration_category.name if self.registration_category else None,
                'RegistrationAttributes': self.registration_attributes.name if self.registration_attributes else None,
                'LifecycleStage': self.lifecycle_stage.name if self.lifecycle_stage else None,
                "Columns": [c.to_dict() for c in self.columns.values()],
                "Params": [p.to_dict() for p in self.parameters.values()],
                "TableParams": [t.to_dict() for t in self.table_parameters.values()],
            })

        @bp.route(f'/api/v1/{self.path_name}/data', methods=['POST'])
        def provider_data():

            def get_content(key, default=None):

                j = request.get_json(silent=True)
                if j is not None:
                    value = j.get(key)
                else:
                    value = None

                return default if value is None else value

            try:
                data_filter = get_content('filter')
                limit = get_content('limit')
                pvs = get_content('params', default=[])

                pvs = self._fill_defaults(pvs)

                param_dict = {pv['name']: _cast(**pv) for pv in pvs}

                response = self.get_data(data_filter, limit, **param_dict)
                return jsonify([self._cast_row(r) for r in response])

            except Exception as e:
                # Package up error and return info as a 400
                err_data = {
                    "Provider": self.name,
                    "ErrorType": type(e).__name__,
                    "ErrorInfo": ''.join(traceback.format_exception(*sys.exc_info()))
                }

                print(f"\nError raised in {self.name}")
                print(indent_str(err_data["ErrorInfo"], n=4), end='\n\n')

                return Response(json.dumps(err_data), status=400, content_type='application/json')

        return bp
