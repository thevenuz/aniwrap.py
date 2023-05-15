"""Module for all models used in the project."""

from __future__ import annotations


__all__ = (
    "BaseModel",
    "Route",
    "GenerateRoute",
    "HttpErrorResponse",
    "HttpSuccessResponse",
    "Season",
    "Broadcast",
    "AnimeStatisticsStatus",
    "AnimeStatistics",
    "Anime",
    "AnimeRanking",
    "PictureModel",
    "TitlesModel",
    "CommonModel",
    "OptionalPictureModel",
    "RelatedMaterialModel",
    "RelatedMaterialNodeModel",
    "RecommendationModel",
    "RankingModel",
    "ForumSubBoard",
    "ForumBoard",
    "Forum",
    "ForumTopic",
    "PostCreator",
    "ForumPost",
    "ForumTopicDetails",
    "AuthorName",
    "Author",
    "Serialization",
    "Manga",
    "MangaRanking",
    "AnimeListStatus",
    "AnimeList",
    "AnimeListUpdate",
    "MangaListStatus",
    "MangaList",
    "MangaListUpdate",
)

from .base import *
from .anime import *
from .route import *
from .http import *
from .manga import *
from .common import *
from .forum import *
from .user import *
