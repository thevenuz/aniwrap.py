"""Module for all enums related to the project."""

from __future__ import annotations

__all__ = (
    "BaseEnum",
    "AnimeStatus",
    "AnimeType",
    "AnimeSeason",
    "AnimeRankingType",
    "AnimeSortType",
    "NSFWLevel",
    "MangaRankingType",
    "MangaType",
    "MangaStatus",
    "AnimeListSortType",
    "AnimeWatchStatus",
    "ListPriority",
    "AnimeRewatchValue",
    "MangaReadStatus",
    "MangaListSortType",
)

from .base import *
from .anime import *
from .manga import *
from .user import *
from .common import *