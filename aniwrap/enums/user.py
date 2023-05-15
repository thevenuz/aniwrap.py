"""Module for enums used in user anime and manga lists."""

from __future__ import annotations

from .base import BaseEnum


__all__ = (
    "AnimeListSortType",
    "AnimeWatchStatus",
    "ListPriority",
    "AnimeRewatchValue",
    "MangaReadStatus",
    "MangaListSortType",
    "MangaRereadValue",
)


class AnimeListSortType(BaseEnum):
    """Represents the different sort types of user anime list."""

    ListScore = "list_score"
    """Sorts the anime list in the descending order of score."""

    ListUpdatedAt = "list_updated_at"
    """Sorts the anime list in the descending order of last updated time."""

    AnimeTitle = "anime_title"
    """Sorts the anime list in the ascending order of anime title."""

    AnimeStartDate = "anime_start_date"
    """Sorts the anime list in the descending order of anime start date."""


class AnimeWatchStatus(BaseEnum):
    """Represents the status of anime in the user's anime list."""

    Watching = "watching"

    Completed = "completed"

    OnHold = "on_hold"

    Dropped = "dropped"

    PlanToWatch = "plan_to_watch"


class ListPriority(BaseEnum):
    """Represents the priority(?) of the anime/manga in the list."""

    Low = 0
    Medium = 1
    High = 2


class AnimeRewatchValue(BaseEnum):
    """Represents the anime rewatch value."""

    Empty = 0
    VeryLow = 1
    Low = 2
    Medium = 3
    High = 4
    VeryHigh = 5


class MangaReadStatus(BaseEnum):
    """Represents the status of the manga in user's list."""

    Reading = "reading"

    Completed = "completed"

    OnHold = "on_hold"

    Dropped = "dropped"

    PlanToRead = "plan_to_read"


class MangaListSortType(BaseEnum):
    """Represents the different sort types of user manga list."""

    ListScore = "list_score"
    """Sorts the manga list in the descending of the score."""

    ListUpdatedAt = "list_updated_at"
    """Sorts the manga list in the descending of the last updated time."""

    MangaTitle = "manga_title"
    """Sorts the manga list in the ascending of the manga title."""

    MangaStartDate = "manga_start_date"
    """Sorts the manga list in the descending of the manga start date."""


class MangaRereadValue(BaseEnum):
    """Represents the manga reread value."""

    Empty = 0
    VeryLow = 1
    Low = 2
    Medium = 3
    High = 4
    VeryHigh = 5
