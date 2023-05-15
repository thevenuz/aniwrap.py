"""Module for common enums used in the project."""

from __future__ import annotations
from .base import BaseEnum

__all__ = ("NSFWLevel",)


class NSFWLevel(BaseEnum):
    """Represents different NSFW levels."""

    Black = "black"
    Gray = "gray"
    White = "white"
