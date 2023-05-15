"""Module for all the models related to user anime and manga list."""

from __future__ import annotations
from datetime import datetime

from .base import BaseModel
from .anime import Anime
from .manga import Manga
from aniwrap.enums import (
    AnimeWatchStatus,
    ListPriority,
    AnimeRewatchValue,
    MangaReadStatus,
    MangaRereadValue,
)

import attrs


__all__ = (
    "AnimeListStatus",
    "AnimeList",
    "AnimeListUpdate",
    "MangaListStatus",
    "MangaList",
    "MangaListUpdate",
)


@attrs.define(init=False)
class AnimeListStatus(BaseModel):
    """Represents the anime list status model."""

    status: AnimeWatchStatus
    """The anime watch status in the anime list."""

    updated_at: datetime
    """The last updated time."""

    score: int = 0
    """The score of the anime in the list. Defaults to `0`"""

    num_episodes_watched: int = 0
    """The number of episodes watched. Defaults to `0`"""

    is_rewatching: bool = False
    """Rewatch status. Defaults to `False`"""

    start_date: datetime | None = attrs.field(default=None)
    """The date on which the user started watching the anime."""

    finish_date: datetime | None = attrs.field(default=None)
    """The date on which the user finished watching the anime."""


@attrs.define
class AnimeList(BaseModel):
    """Represents the user anime list model."""

    anime_data: Anime
    """Represents the anime details."""

    list_status: AnimeListStatus
    """The status details of the anime in the list."""


@attrs.define(init=False)
class AnimeListUpdate(BaseModel):
    """Represents different params present in anime list update."""

    status: AnimeWatchStatus
    """The anime watch status in the anime list."""

    updated_at: datetime
    """The last updated time."""

    score: int = 0
    """The score of the anime in the list. Defaults to `0`"""

    num_episodes_watched: int = 0
    """The number of episodes watched. Defaults to `0`"""

    is_rewatching: bool = False
    """Rewatch status. Defaults to `False`"""

    priority: ListPriority = ListPriority.Low
    """The anime priority."""

    num_times_rewatched: int = 0
    """The number of times anime is rewatched."""

    rewatch_value: AnimeRewatchValue | None = None

    tags: list[str] | None = None

    comments: str | None = None


@attrs.define(init=False)
class MangaListStatus(BaseModel):
    """Represents the Manga list status model."""

    status: MangaReadStatus
    """The manga read status in the user list."""

    updated_at: datetime
    """The last updated time."""

    is_rereading: bool = False
    """The rereading status."""

    num_volumes_read: int = 0
    """The number of volumes read in the manga."""

    num_chapters_read: int = 0
    """The number of chapters read in the manga."""

    score: int = 0
    """The score of the manga."""

    start_date: datetime | None = attrs.field(default=None)
    """The date on which the user started reading the manga."""

    finish_date: datetime | None = attrs.field(default=None)
    """The date on which the user finished reading the manga."""


@attrs.define
class MangaList(BaseModel):
    """Represents the user manga list model."""

    manga: Manga
    """Represents the manga details."""

    list_status: MangaListStatus
    """The status details of the manga in the user list."""


@attrs.define(init=False)
class MangaListUpdate(BaseModel):
    """Represents different params present in manga list update."""

    status: MangaReadStatus
    """The manga read status in the manga list."""

    updated_at: datetime
    """The last updated time."""

    score: int = 0
    """The score of the manga in the list. Defaults to `0`"""

    num_volumes_read: int = 0
    """The number of volumes read in the manga. Defaults to `0`"""

    num_chapters_read: int = 0
    """The number of chapters read in the manga. Defaults to `0`"""

    priority: ListPriority = ListPriority.Low
    """The manga priority in the list."""

    num_times_reread: int = 0
    """The manga reread times."""

    is_rereading: bool = False

    reread_value: MangaRereadValue | None = None

    tags: list[str] | None = None

    comments: str | None = None
