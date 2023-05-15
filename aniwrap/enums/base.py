"""Module for base enum."""

from __future__ import annotations

from typing import TypeVar, Type
from enum import Enum

T = TypeVar("T", bound="BaseEnum")


class BaseEnum(Enum):
    """BaseEnum from which all the other enums inherit from."""

    def __str__(self) -> str:
        return self.value

    @classmethod
    def from_str(cls: Type[T], value: str) -> T:
        """Generate the enum from the given string value.

        Args:
            value: The string value to generate from.

        Returns:
            The generated enum.
        """
        return cls(value)

    @classmethod
    def try_from_str(cls: Type[T], value: str) -> T | None:
        """Try to generate the enum from the given value.

        Args:
            value: the string value to generate the enum from.

        Returns:
            The generated enum or `None` if the value is not valid.
        """
        try:
            return cls(value)
        except ValueError:
            return None
