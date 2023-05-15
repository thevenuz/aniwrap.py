"""Module for all the anime related enums."""

from __future__ import annotations
from .base import BaseEnum

__all__ = (
    "AnimeStatus",
    "AnimeType",
    "AnimeSeason",
    "AnimeRankingType",
    "AnimeSortType",
)


class AnimeStatus(BaseEnum):
    """Represents all available Anime status."""

    Airing = "currently_airing"
    """Represents currently airing anime"""

    Finished = "finished_airing"
    """Represents anime that are finished airing."""

    NotAired = "not_yet_aired"
    """Represents anime that are yet to be aired."""


class AnimeType(BaseEnum):
    """Represents type of the Anime."""

    Movie = "movie"
    Ona = "ona"
    Ova = "ova"
    Special = "special"
    Tv = "tv"
    Unknown = "unknown"


class AnimeSeason(BaseEnum):
    """Represents anime Season."""

    Winter = "winter"
    """Represents winter - January, February, March months."""

    Spring = "spring"
    """Represents spring - April, May, June."""

    Summer = "summer"
    """Represents summer - July, August, September."""

    Fall = "fall"
    """Represents fall - October, November, December."""


class AnimeRankingType(BaseEnum):
    """Represents the anime ranking type."""

    All = "all"
    """Represents top anime series."""

    Airing = "airing"
    """Represents top airing anime."""

    Upcoming = "upcoming"
    """Represents top upcoming anime."""

    Tv = "tv"
    """Represents top TV anime series."""

    Ova = "ova"
    """Represents top anime OVA series."""

    Movie = "movie"
    """Represents top anime movies."""

    Special = "special"
    """Represents top anime specials."""

    ByPopularity = "bypopularity"
    """Represents top anime by popularity."""

    Favorite = "favorite"
    """Represents top favourited anime."""


class AnimeSortType(BaseEnum):
    """Represents the type of ways anime result can be sorted."""

    AnimeScore = "anime_score"
    """Sorts the anime result based on score of the anime on mal in descending order."""

    NumberOfUsers = "anime_num_list_users"
    """Sorts the anime result based on the number of users added the anime to their list on mal in descending order."""
