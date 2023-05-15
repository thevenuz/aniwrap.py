"""Module for all the manga related enums."""

from __future__ import annotations
from .base import BaseEnum

__all__ = ("MangaRankingType", "MangaType", "MangaStatus")


class MangaRankingType(BaseEnum):
    """Represents the manga ranking type."""

    All = "all"
    """Represents top series - includes Manga, Novels, Manhwa etc."""

    Manga = "manga"
    """Represents top manga series."""

    Novels = "novels"
    """Represents top novels."""

    Oneshots = "oneshots"
    """Represents top one-shots."""

    Doujin = "doujin"
    """Represents top Doujinshi."""

    Manhwa = "manhwa"
    """Represents top Manhwa."""

    Manhua = "manhua"
    """Represents top Manhua."""

    ByPopularity = "bypopularity"
    """Represents top series by popularity."""

    Favorite = "favorite"
    """Represents top favourited series."""


class MangaType(BaseEnum):
    """Represents Manga type enum."""

    Doujinshi = "doujinshi"
    LightNovel = "light_novel"
    Manga = "manga"
    Manhua = "manhua"
    Manhwa = "manhwa"
    Novel = "novel"
    Oel = "oel"
    OneShot = "one_shot"
    Unknown = "unknown"


class MangaStatus(BaseEnum):
    """Represents Manga status enum."""

    Finished = "finished"
    NotPublished = "not_yet_published"
    Publishing = "currently_publishing"
    OnHiatus = "on_hiatus"
    Discontinued = "discontinued"
