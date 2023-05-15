"""Contains services that makes the actual requests to MAL api."""

from __future__ import annotations

__all__ = (
    "HttpService",
    "BaseService",
    "AnimeService",
    "MangaService",
    "ForumService",
    "UserService",
)

from .http import *
from .base import *
from .anime import *
from .manga import *
from .forum import *
from .user import *
