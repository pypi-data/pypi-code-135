import re
from json import JSONDecodeError
from typing import TYPE_CHECKING, Tuple, List

import pandas as pd
import requests

from ._custom_instrument_types import CustomInstrumentTypes
from .._content_provider import (
    HistoricalResponseFactory,
    HistoricalContentValidator,
    HistoricalDataProvider,
    axis_by_day_interval_type,
)
from .._content_type import ContentType
from .._intervals import DayIntervalType, get_day_interval_type, Intervals
from .._join_responses import join_historical_responses
from .._types import Strings
from ..historical_pricing._hp_data_provider import check_count
from ..._errors import RDError
from ..._tools import (
    get_response_reason,
    make_enum_arg_parser,
    custom_insts_datetime_adapter,
    ParamItem,
    ValueParamItem,
)
from ..._tools._dataframe import convert_df_columns_to_datetime
from ...delivery._data._data_provider import (
    RequestFactory,
    ResponseFactory,
    Parser,
    success_http_codes,
    ContentValidator,
    DataProvider,
    DataProviderLayer,
    ContentTypeValidator,
    ValidatorContainer,
    ParsedData,
    Response,
)
from ...delivery._data._data_provider import _check_response as default_check_response
from ...delivery._data._endpoint_data import RequestMethod

if TYPE_CHECKING:
    import httpx

content_type_by_day_interval_type = {
    DayIntervalType.INTER: ContentType.CUSTOM_INSTRUMENTS_INTERDAY_SUMMARIES,
    DayIntervalType.INTRA: ContentType.CUSTOM_INSTRUMENTS_INTRADAY_SUMMARIES,
}

# a20140be-3648-4892-9d1b-ce78ee8617fd
is_instrument_id = re.compile(r"[a-z0-9]{8}(-[a-z0-9]{4}){3}-[a-z0-9]{12}")

# S)INST.GESG1-0000
symbol_with_user_id = re.compile(r".*\.[A-Z0-9]+-[0-9]+")

wrong_uuid_regexp = re.compile(
    r"(Validation Error: .UUID suffix ).*( not matched with userID)"
)
wrong_symbol = "S)Instrument.UUID-0000"


def provide_session(func):
    def _func(value, session, *args, **kwargs):
        return func(value, session)

    return _func


def get_content_type_by_interval(interval) -> ContentType:
    day_interval_type = get_day_interval_type(interval)
    return content_type_by_day_interval_type.get(day_interval_type)


def check_data(data):
    return not all(i is pd.NA for j in data for i in j)


# --------------------------------------------------------------------------------------
#   Response factory
# --------------------------------------------------------------------------------------


def custom_instruments_build_df(content_data: dict, **kwargs) -> pd.DataFrame:
    if isinstance(content_data, dict):
        content_data = [content_data]
    dataframe = pd.DataFrame(content_data)
    dataframe.fillna(pd.NA, inplace=True)
    return dataframe


def custom_instruments_intervals_build_df(content_data: dict, **kwargs) -> pd.DataFrame:
    data = content_data.get("data")
    headers = content_data.get("headers", [])
    columns = [header.get("name") for header in headers]
    dataframe = pd.DataFrame(data, columns=columns)
    convert_df_columns_to_datetime(dataframe, pattern="DATE", utc=True, delete_tz=True)
    dataframe.fillna(pd.NA, inplace=True)
    return dataframe


# --------------------------------------------------------------------------------------
#   Request factory
# --------------------------------------------------------------------------------------
def has_all_error_user_id(response):
    return all(wrong_uuid_regexp.match(error.message) for error in response.errors)


def get_user_id(session=None) -> str:
    provider = DataProviderLayer(
        data_type=ContentType.CUSTOM_INSTRUMENTS_INSTRUMENTS,
        universe=wrong_symbol,
    )
    provider._check_response = (
        lambda response, config: None
        if has_all_error_user_id(response)
        else default_check_response(response, config)
    )
    response = provider.get_data(session=session)
    errors = response.errors
    messages = [error.message for error in errors]
    user_id = ""
    for message in messages:
        if wrong_uuid_regexp.match(message):
            _, user_id = message.rsplit(" ", 1)
            break

    return user_id


def convert_to_symbol(symbol, session=None, uuid=""):
    # "MyNewInstrument"
    retval = symbol
    if not retval.startswith("S)"):
        retval = f"S){retval}"
    # "S)MyNewInstrument"
    if not symbol_with_user_id.match(retval):
        if not uuid:
            uuid = get_user_id(session)
        retval = f"{retval}.{uuid}"
    # "S)MyNewInstrument.GE-1234"
    return retval


def get_valid_symbol(symbol, uuid):
    return convert_to_symbol(symbol, uuid=uuid)


def get_valid_symbol_request(symbol, session):
    return convert_to_symbol(symbol, session)


class BaseRequestFactory(RequestFactory):
    def get_url(self, *args, **kwargs):
        url = super().get_url(*args, **kwargs)
        if self.get_request_method(**kwargs) != RequestMethod.POST:
            url += "/{universe}"
        return url

    def get_path_parameters(self, session, *, universe=None, **kwargs):
        if self.get_request_method(**kwargs) == RequestMethod.POST:
            return {}

        if universe is None:
            raise RDError(-1, "universe can't be None")

        if not is_instrument_id.match(universe):
            universe = get_valid_symbol_request(universe, session)

        return {"universe": universe}

    def extend_query_parameters(self, query_parameters, extended_params=None):
        if extended_params:
            query_parameters = dict(query_parameters)
            query_parameters.update(extended_params)
            query_parameters = list(query_parameters.items())
        return query_parameters

    def extend_body_parameters(self, body_parameters, **kwargs):
        return body_parameters


stat_types_ownership_arg_parser = make_enum_arg_parser(CustomInstrumentTypes)


def default_converter(arg, session):
    return arg


class CustomInstsRequestFactory(BaseRequestFactory):
    @property
    def body_params_config(self):
        return custom_insts_body_params

    def get_body_parameters(self, session, *args, **kwargs):
        body_parameters = {}
        if self.get_request_method(**kwargs) not in {
            RequestMethod.POST,
            RequestMethod.PUT,
        }:
            return body_parameters

        return super().get_body_parameters(session, *args, **kwargs)

    def extend_body_parameters(self, body_parameters, extended_params=None, **kwargs):
        if extended_params:
            result = dict(body_parameters)
            result.update(extended_params)
            return result
        return body_parameters


# --------------------------------------------------------------------------------------
#   Raw data parser
# --------------------------------------------------------------------------------------


class CustomInstsParser(Parser):
    def parse_raw_response(
        self, raw_response: "httpx.Response"
    ) -> Tuple[bool, ParsedData]:
        is_success = False

        if raw_response is None:
            return is_success, ParsedData({}, {})

        is_success = raw_response.status_code in success_http_codes + [
            requests.codes.no_content
        ]

        if is_success:
            parsed_data = self.process_successful_response(raw_response)

        else:
            parsed_data = self.process_failed_response(raw_response)

        return is_success, parsed_data

    def process_failed_response(self, raw_response: "httpx.Response") -> ParsedData:
        status = {
            "http_status_code": raw_response.status_code,
            "http_reason": get_response_reason(raw_response),
        }

        try:
            content_data = raw_response.json()
            if isinstance(content_data, list):
                content_data = content_data[0]
            content_error = content_data.get("error")

            if content_error:
                status["error"] = content_error
                error_code = content_error.get("code")
                if isinstance(error_code, str) and not error_code.isdigit():
                    error_code = raw_response.status_code
                error_message = content_error.get("message")
                errors = content_error.get("errors", {})
                errors = [error.get("reason") for error in errors if error]
                if errors:
                    errors = "\n".join(errors)
                    error_message = f"{error_message}: {errors}"
            elif "state" in content_data:
                state = content_data.get("state", {})
                error_code = state.get("code")
                data = content_data.get("data", [])
                reasons = [_data.get("reason", "") for _data in data]
                reason = "\n".join(reasons)
                error_message = f"{state.get('message')}: {reason}"
            else:
                error_code = raw_response.status_code
                error_message = raw_response.text

        except (TypeError, JSONDecodeError):
            error_code = raw_response.status_code
            error_message = raw_response.text

        if error_code == 403:
            if not error_message.endswith("."):
                error_message += ". "
            error_message += "Contact Refinitiv to check your permissions."

        return ParsedData(
            status, raw_response, error_codes=error_code, error_messages=error_message
        )


# --------------------------------------------------------------------------------------
#   Content data validator
# --------------------------------------------------------------------------------------


class CustomInstsContentValidator(ContentValidator):
    def validate(self, data: "ParsedData") -> bool:
        is_valid = True
        content_data = data.content_data
        status = data.status
        status_code = status.get("http_status_code")

        if content_data is None and status_code != 204:
            is_valid = False
            data.error_codes = 1
            data.error_messages = "Content data is None"

        return is_valid


# --------------------------------------------------------------------------------------
#   Request factory
# --------------------------------------------------------------------------------------

interval_arg_parser = make_enum_arg_parser(Intervals, can_be_lower=True)


class CustomInstsSearchRequestFactory(RequestFactory):
    def get_query_parameters(self, *args, **kwargs):
        access = kwargs.get("access")
        return [
            ("access", access),
        ]

    def extend_query_parameters(self, query_parameters, extended_params=None):
        if extended_params:
            query_parameters = dict(query_parameters)
            query_parameters.update(extended_params)
            query_parameters = list(query_parameters.items())

        return query_parameters

    def extend_body_parameters(self, body_parameters, **kwargs):
        return body_parameters


custom_insts_events_query_params = [
    ValueParamItem("start", "start", custom_insts_datetime_adapter.get_str),
    ValueParamItem("end", "end", custom_insts_datetime_adapter.get_str),
    ValueParamItem("count", "count", check_count),
]
custom_insts_summaries_query_params = [
    ValueParamItem("interval", "interval", interval_arg_parser.get_str),
    ValueParamItem("start", "start", custom_insts_datetime_adapter.get_str),
    ValueParamItem("end", "end", custom_insts_datetime_adapter.get_str),
    ValueParamItem("count", "count", check_count),
]

custom_insts_body_params = [
    ParamItem("symbol", "symbol", provide_session(convert_to_symbol)),
    ParamItem("currency", "currency"),
    ParamItem("description", "description"),
    ParamItem("exchange_name", "exchangeName"),
    ParamItem("formula", "formula"),
    ParamItem("holidays", "holidays"),
    ParamItem("instrument_name", "instrumentName"),
    ParamItem("time_zone", "timeZone"),
    ValueParamItem("type_", "type", stat_types_ownership_arg_parser.get_str),
    ParamItem("basket", "basket"),
    ParamItem("udc", "udc"),
]


class CustomInstsEventsRequestFactory(BaseRequestFactory):
    @property
    def query_params_config(self):
        return custom_insts_events_query_params


class CustomInstsSummariesRequestFactory(BaseRequestFactory):
    @property
    def query_params_config(self):
        return custom_insts_summaries_query_params


class CustomInstsSummariesDataProvider(HistoricalDataProvider):
    @staticmethod
    def _join_responses(
        responses: List["Response"],
        universe: Strings,
        fields: Strings,
        kwargs,
    ) -> "Response":
        interval = kwargs.get("interval")
        axis_name = axis_by_day_interval_type.get(
            get_day_interval_type(interval or DayIntervalType.INTER)
        )
        return join_historical_responses(
            responses, universe, fields, axis_name, check_data=check_data
        )


class CustomInstsEventsDataProvider(HistoricalDataProvider):
    @staticmethod
    def _join_responses(
        responses: List["Response"], universe: Strings, fields: Strings, kwargs
    ) -> "Response":
        axis_name = "Timestamp"
        return join_historical_responses(
            responses, universe, fields, axis_name, check_data=check_data
        )


# --------------------------------------------------------------------------------------
#   Data provider
# --------------------------------------------------------------------------------------

custom_instrument_data_provider = DataProvider(
    response=ResponseFactory(),
    request=CustomInstsRequestFactory(),
    parser=CustomInstsParser(),
    validator=ValidatorContainer(
        content_validator=CustomInstsContentValidator(),
        content_type_validator=ContentTypeValidator({"application/json", ""}),
    ),
)

custom_instrument_search_data_provider = DataProvider(
    request=CustomInstsSearchRequestFactory(),
    parser=CustomInstsParser(),
    validator=ValidatorContainer(
        content_validator=CustomInstsContentValidator(),
        content_type_validator=ContentTypeValidator({"application/json", ""}),
    ),
)

custom_instruments_events_data_provider = CustomInstsEventsDataProvider(
    request=CustomInstsEventsRequestFactory(),
    parser=CustomInstsParser(),
    response=HistoricalResponseFactory(),
    validator=HistoricalContentValidator(),
)

custom_instruments_intraday_summaries_data_provider = CustomInstsSummariesDataProvider(
    request=CustomInstsSummariesRequestFactory(),
    parser=CustomInstsParser(),
    response=HistoricalResponseFactory(),
    validator=HistoricalContentValidator(),
)

custom_instruments_interday_summaries_data_provider = CustomInstsSummariesDataProvider(
    request=CustomInstsSummariesRequestFactory(),
    parser=CustomInstsParser(),
    response=HistoricalResponseFactory(),
    validator=HistoricalContentValidator(),
)
