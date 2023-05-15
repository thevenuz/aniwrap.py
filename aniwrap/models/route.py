"""Module for Route model."""

from __future__ import annotations

from typing import Any

import attrs


__all__ = ("Route", "GenerateRoute")


@attrs.define
class Route:
    """Represents route details."""

    method: str
    """The type of request."""

    uri: str
    """The request uri."""

    def generate_route(self, *args: str | int) -> GenerateRoute:
        """Generate route.

        Args:
            *args: the arguments to insert.

        Returns:

        """
        generated_route = GenerateRoute(self)

        for arg in args:
            generated_route.uri = generated_route.uri.replace(r"()", str(arg), 1)

        return generated_route


class GenerateRoute:
    __slots__ = ("_route", "_params", "_data")

    def __init__(self, route: Route) -> None:
        self._route = route
        self._params: dict[str, str | int] = {}
        self._data: dict[str, str | int] = {}

    @property
    def route(self) -> Route:
        """The route itself."""
        return self._route

    @property
    def uri(self) -> str:
        """The routes uri endpoint."""
        return self.route.uri

    @uri.setter
    def uri(self, val: str) -> str:
        """Set the uri."""
        self.route.uri = val

    @property
    def method(self) -> str:
        """The routes method, i.e. GET, POST..."""
        return self.route.method

    @property
    def params(self) -> dict[str, str | int]:
        """The query params for the route."""
        return self._params

    @property
    def data(self) -> dict[str, str | int]:
        """The input data that needs to be passed."""
        return self._data

    def with_params(self, params: dict[str, Any]) -> GenerateRoute:
        """Adds additional query params to this generated route."""

        if params:
            self.params.update(params)

        return self

    def with_data(self, data: dict[str, Any]) -> GenerateRoute:
        """Adds input data to the generated route."""

        if data:
            self._data.update(data)

        return self
