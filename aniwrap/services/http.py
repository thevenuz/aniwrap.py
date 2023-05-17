"""Module for the HTTP service."""

from __future__ import annotations
from typing import TypeVar, Any

import aiohttp

from aniwrap.models import HttpErrorResponse, HttpSuccessResponse, GenerateRoute
from aniwrap.enums.http import HttpMethod

T = TypeVar("T")

__all__ = ("HttpService",)


class HttpService:
    """The HTTP service that is used to make requests to MAL API.

    Args:
        client_id: X-MAL-CLIENT-ID.
    """

    __slots__ = ("_headers", "_session", "_method_mapping")

    def __init__(
        self, client_id: str | None = None, access_token: str | None = None
    ) -> None:
        self._set_headers(client_id, access_token)
        self._session = aiohttp.ClientSession()

    def _set_headers(
        self, client_id: str | None = None, access_token: str | None = None
    ) -> None:
        """Set headers - either client_id or bearer token"""

        if not client_id and not access_token:
            raise ValueError("Either Client id or bearer token need to be specified.")

        if client_id:
            self._headers = {"X-MAL-CLIENT-ID": client_id}

        if access_token:
            self._headers = {"Authorization": f"Bearer {access_token}"}

    def _get_session_method(self, method: HttpMethod, session: Any) -> Any:
        """Get the session with method type.

        Returns:
            The session with respective method.
        """

        _method_mapping = {
            HttpMethod.Get: session.get,
            HttpMethod.Post: session.post,
            HttpMethod.Put: session.put,
            HttpMethod.Patch: session.patch,
            HttpMethod.Delete: session.delete,
        }

        return _method_mapping[method]

    async def _request(
        self,
        session: Any,
        uri: str,
        params: dict[str, str | int],
        data: dict[str, str | int],
    ) -> HttpErrorResponse | HttpSuccessResponse:
        """Make the actual request to the MAL API based on given params.

        Returns:
            The response from the API call.
        """
        try:
            async with session(
                uri, headers=self._headers, params=params, data=data
            ) as r:
                response = await r.json()
                if r.status == 200:
                    return HttpSuccessResponse(r.status, "Success.", response)

                return HttpErrorResponse(r.status, response.get("error"))

        except Exception as e:
            return HttpErrorResponse(500, str(e))

    async def fetch(
        self, route: GenerateRoute, method: HttpMethod
    ) -> HttpErrorResponse | HttpSuccessResponse:
        """Makes a request to the given route.

        Returns:
            The HTTP response [`HttpSuccessResponse`] or [`HttpErrorResponse`] of the API call.
        """
        try:
            # async with self._session as session:
            return await self._request(
                self._get_session_method(method, self._session),
                route.uri,
                route.params,
                route.data,
            )
        except Exception as e:
            return HttpErrorResponse(500, str(e))

    async def close(self) -> None:
        """Close the open aiohttp clientsession."""

        if self._session and not self._session.closed:
            await self._session.close()
