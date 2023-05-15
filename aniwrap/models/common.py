"""Module for common models used through out the project."""

from __future__ import annotations

import attrs
from .base import BaseModel

__all__ = (
    "PictureModel",
    "TitlesModel",
    "CommonModel",
    "OptionalPictureModel",
    "RelatedMaterialModel",
    "RelatedMaterialNodeModel",
    "RecommendationModel",
    "RankingModel",
)


@attrs.define(init=False)
class PictureModel(BaseModel):
    """Represents the picture type fields model."""

    medium: str
    """The url for the medium sized picture."""

    large: str
    """The url for the large sized picture"""


@attrs.define(init=False)
class TitlesModel(BaseModel):
    """Represents the model for alternative title fields."""

    synonyms: list(str)
    """Synonyms of the title of Anime/Manga."""

    en: str
    """The English title of the Anime/Manga"""

    ja: str
    """The Japanese title of the Anime/Manga"""


@attrs.define
class CommonModel(BaseModel):
    """Represents a common model - contains `id` and `name`."""

    id: int
    """The id."""

    name: str
    """The name."""


@attrs.define
class OptionalPictureModel(BaseModel):
    """Represents a model for the picture type fields."""

    medium: str
    """The url for the medium sized picture."""

    large: str
    """The url for the large sized picture"""


@attrs.define
class RelatedMaterialModel(BaseModel):
    """Represents related anime/manga model."""

    node: RelatedMaterialNodeModel | None = attrs.field(default=None)
    """Contains details of the related anime/manga."""

    relation_type: str | None = attrs.field(default=None)
    """Unformatted representation of the way this anime/manga is related to the parent anime/manga."""

    relation_type_formatted: str | None = attrs.field(default=None)
    """Formatted representation of the way this anime/manga is related to the parent anime/manga."""


@attrs.define
class RelatedMaterialNodeModel(BaseModel):
    """Represents individual node of the related material model."""

    id: int | None = attrs.field(default=None)
    """The id of the related anime/manga."""

    title: str | None = attrs.field(default=None)
    """The title of the related anime/manga."""

    main_picture: OptionalPictureModel | None = attrs.field(default=None)
    """The urls for medium and large sized pictures of the posters of the related anime/manga."""


@attrs.define
class RecommendationModel(BaseModel):
    """Represents the recommendation type model."""

    node: dict[str, RelatedMaterialNodeModel] | None = attrs.field(default=None)
    """Contains details of the recommended anime/manga."""

    num_recommendations: int | None = attrs.field(default=None)
    """The number of users that recommended this anime/manga."""


@attrs.define
class RankingModel(BaseModel):
    """Represents the ranking model."""

    rank: int
    """Represents the rank of the anime in the list."""
