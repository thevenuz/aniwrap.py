"""Module for the http related enums."""

from __future__ import annotations
from .base import BaseEnum

__all__ = ("HttpMethod",)

class HttpMethod(BaseEnum):
    """HTTP method enum."""

    Get = "GET"
    Post = "POST"
    Put = "PUT"
    Patch = "PATCH"
    Delete = "DELETE"
