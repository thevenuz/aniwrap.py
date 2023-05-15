"""Module for result which every method in the module returns."""

from __future__ import annotations

import abc
from typing import Any, TypeVar, Generic

S = TypeVar("S")
E = TypeVar("E")

__all__ = ("Result", "Success", "Error")


class Result(Generic[S, E], abc.ABC):
    """Represents Result."""

    __slots__ = ("_error", "_value")

    def __init__(self, value, error) -> None:
        self._value = value
        self._error = error

    @property
    def is_success(self) -> bool:
        """Returns `True` for success result and `False` for error result."""

    @property
    def is_error(self) -> bool:
        """Returns `True` for error result and `False` for success result."""

    @property
    def value(self) -> S:
        """Returns data for a success result and `None` for an error result."""

    @property
    def error(self) -> E:
        """Returns error for an error result and `None` for a success result."""


class Success(Result[S, E]):
    """Reprsents Success result class."""

    __slots__ = ()

    def __init__(self, value) -> None:
        self._value = value

    @property
    def is_success(self) -> bool:
        """Returns `True` for success result."""

        return True

    @property
    def is_error(self) -> bool:
        """Returns `False` for success result."""

        return False

    @property
    def value(self) -> S:
        return self._value

    @property
    def error(self) -> E:
        return None


class Error(Result[S, E]):
    """Represents Error result class."""

    __slots__ = ()

    def __init__(self, error) -> None:
        self._error = error

    @property
    def is_success(self) -> bool:
        """Returns `False` for success result."""

        return False

    @property
    def is_error(self) -> bool:
        """Returns `True` for success result."""

        return True

    @property
    def value(self) -> S:
        return None

    @property
    def error(self) -> E:
        return self._error
