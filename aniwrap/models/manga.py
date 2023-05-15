"""Module for all Manga related models."""

from __future__ import annotations
from datetime import datetime

import attrs

from .base import BaseModel
from .common import (
    CommonModel,
    PictureModel,
    OptionalPictureModel,
    TitlesModel,
    RelatedMaterialModel,
    RecommendationModel,
    RankingModel,
)
from aniwrap.enums import NSFWLevel, MangaType, MangaStatus

__all__ = ("AuthorName", "Author", "Serialization", "Manga", "MangaRanking")


@attrs.define
class AuthorName(BaseModel):
    """Represents the author name model."""

    id: int
    """The id related to the author."""

    first_name: str
    """The first name of the author."""

    last_name: str
    """The last name of the author."""


@attrs.define
class Author(BaseModel):
    """Represents the author model."""

    node: AuthorName
    """Represents author details."""

    role: str | None = attrs.field(default=None)
    """The role of the author (Story, art etc.)."""


@attrs.define
class Serialization(BaseModel):
    """Represents the model for serialization."""

    node: CommonModel
    """Contains the id and name of the serialization."""


@attrs.define(init=False)
class Manga(BaseModel):
    """Represents model for all the fields a manga can contain."""

    id: int
    """The id of the Manga."""

    title: str
    """The title of the Manga."""

    main_picture: PictureModel
    """The urls for medium and large sized images of the posters."""

    alternative_titles: TitlesModel
    """The Alternative titles for the Manga. Contains synonyms, Japanese title and any other English title."""

    start_date: datetime
    """The start date of the Manga publication."""

    popularity: int
    """The popularity of the Manga."""

    nsfw: NSFWLevel
    """The NSFW level."""

    created_at: datetime
    """The date on which the manga was created on MAL."""

    updated_at: datetime
    """The date on which the manga was last updated on MAL."""

    media_type: MangaType
    """The type of the Manga."""

    status: MangaStatus
    """The status of the Manga."""

    genres: list[CommonModel]
    """The list of genres to which the manga belongs to."""

    num_volumes: int
    """The number of volumes of the manga that are currently published."""

    num_chapters: int
    """The total number of the chapters present in the Manga."""

    authors: list[Author]
    """The details of the manga authors."""

    end_date: datetime | None = attrs.field(default=None)
    """The Manga end date."""

    synopsis: str | None = attrs.field(default=None)
    """The synopsis of the Manga."""

    mean: float | None = attrs.field(default=None)
    """The score of the manga on MAL. Defaults to `None` for manga that are not published yet."""

    rank: int | None = attrs.field(default=None)
    """The rank of the Manga."""

    num_list_users: int | None = attrs.field(default=None)
    """The number of users that added the manga to their lists."""

    num_scoring_users: int | None = attrs.field(default=None)
    """The number of users that scored the manga."""

    background: str | None = attrs.field(default=None)
    """Some extra information related to the manga."""

    # related_anime: list[RelatedAnimeType] | None = attrs.field(default=None)
    # """The other anime that are related to the current anime."""

    pictures: list[OptionalPictureModel] | None = attrs.field(default=None)
    """The list of urls for medium and large sized images related to the anime. Defaults to `None` if information is not available."""

    related_manga: list[RelatedMaterialModel] | None = attrs.field(default=None)
    """The other manga that are related to the current manga."""

    recommendations: list[RecommendationModel] | None = attrs.field(default=None)
    """The recommended manga by other users."""

    serialization: Serialization | None = attrs.field(default=None)


@attrs.define
class MangaRanking(BaseModel):
    """Represents all the fields that contain in Manga Ranking result."""

    manga_data: Manga
    """Represents all the manga details."""

    ranking: RankingModel
    """Represents the ranking of the manga in the list."""
