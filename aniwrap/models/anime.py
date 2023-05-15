"""Module for Anime related models."""

from __future__ import annotations
from datetime import datetime
import time
from .base import BaseModel
from aniwrap.enums import AnimeSeason, AnimeType, AnimeStatus, NSFWLevel
from .common import (
    PictureModel,
    TitlesModel,
    CommonModel,
    OptionalPictureModel,
    RecommendationModel,
    RelatedMaterialModel,
    RankingModel,
)

import attrs

__all__ = (
    "Season",
    "Broadcast",
    "AnimeStatisticsStatus",
    "AnimeStatistics",
    "Anime",
    "AnimeRanking",
)


@attrs.define
class Season(BaseModel):
    """Represents the model for anime season details."""

    year: str
    """The year."""

    season: AnimeSeason
    """The season."""


@attrs.define
class Broadcast(BaseModel):
    """Represents the model for broadcast details."""

    day_of_the_week: str
    """The day on which the anime airs."""

    start_time: time.struct_time
    """The time at which the anime airs."""


@attrs.define
class AnimeStatisticsStatus(BaseModel):
    """Represents the model for anime statistics."""

    watching: str | None = attrs.field(default=None)
    """The number of users that are currently watching the anime."""

    completed: str | None = attrs.field(default=None)
    """The number of users that completed the anime."""

    on_hold: str | None = attrs.field(default=None)
    """The number of users that put the anime on hold."""

    dropped: str | None = attrs.field(default=None)
    """The number of users that dropped the anime."""

    plan_to_watch: str | None = attrs.field(default=None)
    """The number of users that are planning to watch the anime."""


@attrs.define
class AnimeStatistics(BaseModel):
    """Represents the model for statistics of the anime."""

    status: AnimeStatisticsStatus | None = attrs.field(default=None)
    """Represnts different statistics of the anime."""

    num_list_users: int | None = attrs.field(default=None)
    """The total number of users that added this anime to their lists."""


@attrs.define(init=False)
class Anime(BaseModel):
    """Represents a model for all the fields that an anime can contain."""

    id: int
    """The id of the anime."""

    title: str
    """The title of the anime."""

    main_picture: PictureModel
    """The urls for medium and large sized pictures of the posters."""

    alternative_titles: TitlesModel
    """The Alternative titles for the anime."""

    start_date: datetime
    """The anime's airing start date. For anime that are not aired, the date might be defaulted to first of the month."""

    synopsis: str
    """The synopsis of the anime."""

    popularity: int
    """The popularity ranking of the anime."""

    nsfw: NSFWLevel
    """The nsfw level of the anime."""

    created_at: datetime
    """The date on which the anime is added on MAL."""

    updated_at: datetime
    """The last updated date of the anime."""

    media_type: AnimeType
    """The type of the anime."""

    status: AnimeStatus
    """The status of the anime."""

    genres: list[CommonModel]
    """The list of genres."""

    source: str
    """The source of the anime."""

    rating: str
    """The rating of the anime (R-rated, PG etc.)."""

    studios: list[CommonModel] | None = attrs.field(default=None)
    """The studios that produced the anime. Defaults to `None` if information is not available."""

    end_date: datetime | None = attrs.field(default=None)
    """The anime's airing end date. Defaults to `None` if the anime is not aired yet."""

    mean: float | None = attrs.field(default=None)
    """The score of the anime on MAL. Defaults to `None` for anime that are not aired yet."""

    rank: int | None = attrs.field(default=None)
    """The rank of the anime on MAL. Defaults to `None` if information is not available."""

    num_list_users: int | None = attrs.field(default=None)
    """The number of users that added the anime to their lists. Defaults to `None` if information is not available."""

    num_scoring_users: int | None = attrs.field(default=None)
    """The number of users that scored the anime. Defaults to `None` if information is not available."""

    num_episodes: int = attrs.field(default=0)
    """The number of episodes in the anime. Defaults to `0` if not aired or no information is available."""

    start_season: Season | None = attrs.field(default=None)
    """The season in which the anime started airing. Defaults to `None` if not aired or information is not available."""

    broadcast: Broadcast | None = attrs.field(default=None)
    """The broadcast day and time details. Defaults to `None` if not aired or information is not available."""

    average_episode_duration: int = attrs.field(default=0)
    """The average episode duration of the anime represented in seconds. Defaults to `0` if not aired or information is not available."""

    pictures: list[OptionalPictureModel] | None = attrs.field(default=None)
    """The list of urls for medium and large sized images related to the anime. Defaults to `None` if information is not available."""

    background: str | None = attrs.field(default=None)
    """Some extra information related to the anime. Defaults to `None` if information is not available."""

    related_anime: list[RelatedMaterialModel] | None = attrs.field(default=None)
    """The other anime that are related to the current anime. Defaults to `None` if information is not available."""

    # related_manga - not implemented

    recommendations: list[RecommendationModel] | None = attrs.field(default=None)
    """The recommended anime by other users.  Defaults to `None` if information is not available."""

    statistics: AnimeStatistics | None = attrs.field(default=None)
    """Represents different statistics related to the anime.  Defaults to `None` if information is not available."""


@attrs.define
class AnimeRanking:
    """Represents all the fields that contain in Anime Ranking result."""

    anime_data: Anime
    """Represents all the anime details."""

    ranking: RankingModel
    """Represents the ranking of the anime in the list."""
