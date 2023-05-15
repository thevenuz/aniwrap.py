"""Module for the base service."""

from __future__ import annotations

import abc

from . import HttpService
from aniwrap import serializer


__all__ = ("BaseService",)


class BaseService(abc.ABC):
    """The base service from which all the other services inherit.

    Args:
        http_service: The http service to use for requests.
    """

    __slots__ = ("_http", "_serializer")

    def __init__(
        self, http_service: HttpService, serializer: serializer.Serializer
    ) -> None:
        self._http = http_service
        self._serializer = serializer
