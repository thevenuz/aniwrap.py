"""Module for HTTP response model."""

from __future__ import annotations

from typing import Any
import attrs

from .base import BaseModel

__all__ = ("HttpErrorResponse", "HttpSuccessResponse")


@attrs.define
class HttpSuccessResponse(BaseModel):
    """Represents HTTP success response."""

    status: int
    """The HTTP status code."""

    message: str
    """The success message."""

    data: Any
    """The API json response."""


@attrs.define
class HttpErrorResponse(BaseModel):
    """Represents HTTP success response."""

    status: int
    """The HTTP status code."""

    message: str
    """The error message."""
