"""All models, enums, services, etc are exported here."""

from __future__ import annotations
from typing import Final

__all__ = (
    "client",
    "endpoints",
    "enums",
    "models",
    "result",
    "serializer",
    "services",
    "AnimeStatus",
    "AnimeType",
    "AnimeSeason",
    "AnimeRankingType",
    "AnimeSortType",
    "NSFWLevel",
    "MangaRankingType",
    "MangaType",
    "MangaStatus",
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
    "HttpService",
    "BaseService",
    "AnimeService",
    "MangaService",
    "ForumService",
    "Client",
    "Result",
    "Success",
    "Error",
)

from . import client
from . import endpoints
from . import enums
from . import models
from . import services
from . import result
from .client import *
from .endpoints import *
from .enums import *
from .models import *
from .services import *
from .serializer import *
from .result import *
