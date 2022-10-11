from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    symbol: Union[Unset, None, str] = UNSET,
    count: Union[Unset, None, int] = 10,
) -> Dict[str, Any]:
    url = "{}/cn_futures/daily_history".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["symbol"] = symbol

    params["count"] = count

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, HTTPValidationError]]:
    if response.status_code == 200:
        response_200 = cast(Any, response.json())
        return response_200
    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())

        return response_422
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Any, HTTPValidationError]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    symbol: Union[Unset, None, str] = UNSET,
    count: Union[Unset, None, int] = 10,
) -> Response[Union[Any, HTTPValidationError]]:
    """Get Cn Futures Daily History

    Args:
        symbol (Union[Unset, None, str]):
        count (Union[Unset, None, int]):  Default: 10.

    Returns:
        Response[Union[Any, HTTPValidationError]]
    """

    kwargs = _get_kwargs(
        client=client,
        symbol=symbol,
        count=count,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
    symbol: Union[Unset, None, str] = UNSET,
    count: Union[Unset, None, int] = 10,
) -> Optional[Union[Any, HTTPValidationError]]:
    """Get Cn Futures Daily History

    Args:
        symbol (Union[Unset, None, str]):
        count (Union[Unset, None, int]):  Default: 10.

    Returns:
        Response[Union[Any, HTTPValidationError]]
    """

    return sync_detailed(
        client=client,
        symbol=symbol,
        count=count,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    symbol: Union[Unset, None, str] = UNSET,
    count: Union[Unset, None, int] = 10,
) -> Response[Union[Any, HTTPValidationError]]:
    """Get Cn Futures Daily History

    Args:
        symbol (Union[Unset, None, str]):
        count (Union[Unset, None, int]):  Default: 10.

    Returns:
        Response[Union[Any, HTTPValidationError]]
    """

    kwargs = _get_kwargs(
        client=client,
        symbol=symbol,
        count=count,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    symbol: Union[Unset, None, str] = UNSET,
    count: Union[Unset, None, int] = 10,
) -> Optional[Union[Any, HTTPValidationError]]:
    """Get Cn Futures Daily History

    Args:
        symbol (Union[Unset, None, str]):
        count (Union[Unset, None, int]):  Default: 10.

    Returns:
        Response[Union[Any, HTTPValidationError]]
    """

    return (
        await asyncio_detailed(
            client=client,
            symbol=symbol,
            count=count,
        )
    ).parsed
