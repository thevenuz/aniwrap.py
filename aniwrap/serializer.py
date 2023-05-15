"""Module to serialize and deserialize JSON data and models."""


from __future__ import annotations

from typing import TypeVar, Any
from datetime import datetime
import time

from aniwrap.models import (
    Anime,
    PictureModel,
    TitlesModel,
    CommonModel,
    Season,
    Broadcast,
    RelatedMaterialModel,
    RelatedMaterialNodeModel,
    RecommendationModel,
    AnimeStatistics,
    AnimeStatisticsStatus,
    OptionalPictureModel,
    AnimeRanking,
    RankingModel,
    Manga,
    Author,
    AuthorName,
    Serialization,
    MangaRanking,
    Forum,
    ForumBoard,
    ForumSubBoard,
    ForumTopic,
    ForumTopicDetails,
    ForumPost,
    PostCreator,
    AnimeList,
    AnimeListStatus,
    AnimeListUpdate,
    MangaListStatus,
    MangaList,
    MangaListUpdate,
)

from aniwrap.enums import (
    AnimeSeason,
    AnimeType,
    AnimeStatus,
    NSFWLevel,
    MangaType,
    MangaStatus,
    AnimeWatchStatus,
    ListPriority,
    AnimeRewatchValue,
    MangaReadStatus,
    MangaRereadValue,
)


T = TypeVar("T")

__all__ = ("Serializer",)


class Serializer:
    """Deserializes JSON data to models."""

    __slots__ = ()

    def _date_from_str(self, date_str: str | None) -> datetime | None:
        """Converts string of `yyyy-mm-dd` or `yyyy-mm` or `yyyy` format to datetime. Returns `None` if input string is empty."""

        format = "%Y-%m-%d"
        if date_str:
            if date_str.count("-") == 0:
                format = "%Y"
            elif date_str.count("-") == 1:
                format = "%Y-%m"

        return datetime.strptime(date_str, format) if date_str else None

    def _datetime_from_str(self, datetime_str: str | None) -> datetime | None:
        """Converts string of `yyyy-mm-ddTH:M:S` to datetime. Returns `None` if input string is empty."""

        return (
            datetime.strptime(datetime_str, "%Y-%m-%dT%H:%M:%S")
            if datetime_str
            else None
        )

    def _datetime_from_iso(self, datetime_str: str | None) -> datetime | None:
        return datetime.fromisoformat(datetime_str) if datetime_str else None

    def _time_from_str(self, time_str: str) -> time.struct_time | None:
        """Converts string of `H:M` format to time."""

        return time.strptime(time_str, "%H:%M") if time_str else None

    def _set_attrs(self, model: Any, data: dict[str, Any], *attrs: str) -> None:
        """Generate model from JSON payload."""

        if data:
            for attr in attrs:
                if data.get(attr) is not None:
                    setattr(model, attr, data[attr])
                else:
                    setattr(model, attr, None)

    def _deserialize_genres(self, data: dict[str, Any]) -> list[CommonModel]:
        """Deserializes genres JSON data into model."""

        return [CommonModel(genre.get("id"), genre.get("name")) for genre in data]

    def _deserialize_studios(self, data: dict[str, Any]) -> list[CommonModel]:
        """Deserializes studios JSON data into model."""

        return [CommonModel(genre.get("id"), genre.get("name")) for genre in data]

    def _deserialize_pictures(self, data: dict[str, Any]) -> list[OptionalPictureModel]:
        """Desrializes picture JSON data to model."""

        return [
            OptionalPictureModel(picture.get("medium"), picture.get("large"))
            for picture in data
        ]

    def _deserialize_related_material(
        self, data: dict[str, Any]
    ) -> list[RelatedMaterialModel]:
        """Deserializes related anime/manga JSON data to model."""

        return [
            RelatedMaterialModel(
                RelatedMaterialNodeModel(
                    rel_material.get("node", {}).get("id"),
                    rel_material.get("node", {}).get("title"),
                    OptionalPictureModel(
                        rel_material.get("node", {})
                        .get("main_picture", {})
                        .get("medium"),
                        rel_material.get("node", {})
                        .get("main_picture", {})
                        .get("large"),
                    ),
                ),
                rel_material.get("relation_type"),
                rel_material.get("relation_type_formatted"),
            )
            for rel_material in data
        ]

    def _deserialize_recommendations(
        self, data: dict[str, Any]
    ) -> list[RecommendationModel]:
        """Deserializes anime/manga recommendations JSON data to model."""

        return [
            RecommendationModel(
                RelatedMaterialNodeModel(
                    recommendation.get("node", {}).get("id"),
                    recommendation.get("node", {}).get("title"),
                    OptionalPictureModel(
                        recommendation.get("node", {})
                        .get("main_picture", {})
                        .get("medium"),
                        recommendation.get("node", {})
                        .get("main_picture", {})
                        .get("large"),
                    ),
                ),
                recommendation.get("num_recommendations"),
            )
            for recommendation in data
        ]

    def _deserialize_alternative_titles(self, data: dict[str, Any]) -> TitlesModel:
        """Deserializes alternative titles json data into model."""

        alternative_titles = TitlesModel()
        self._set_attrs(alternative_titles, data, "synonyms", "en", "ja")

        return alternative_titles

    def _deserialize_main_picture(self, data: dict[str, Any]) -> PictureModel:
        """Deserializes anime/manga main picture JSON data into model."""

        main_picture = PictureModel()
        self._set_attrs(main_picture, data, "medium", "large")
        return main_picture

    def _deserialize_authors(self, data: dict[str, Any]) -> list[Author]:
        """Deserializes Manga authors JSON data into model."""

        return [
            Author(
                AuthorName(
                    author.get("node", {}).get("id"),
                    author.get("node", {}).get("first_name"),
                    author.get("node", {}).get("last_name"),
                ),
                author.get("role"),
            )
            for author in data
        ]

    def _deserialize_manga_serialization(
        self, data: dict[str, Any]
    ) -> list[Serialization]:
        """Deserializes Manga manga serialization JSON data into model"""

        return [
            CommonModel(ser.get("node", {}).get("id"), ser.get("node", {}).get("name"))
            for ser in data
        ]

    def _deserialize_board(self, data: dict[str, Any]) -> ForumBoard:
        """"""

        board = ForumBoard()

        self._set_attrs(board, data, "id", "title", "description")

        subboards = [
            ForumSubBoard(subboard.get("id"), subboard.get("title"))
            for subboard in data.get("subboards", [])
        ]

        board.subboards = subboards
        return board

    def _deserialize_forum_post(self, data: dict[str, Any]) -> ForumPost:
        """"""

        forum_post = ForumPost()
        forum_post_creator = PostCreator()

        forum_post.created_at = self._datetime_from_iso(data.get("created_at"))

        self._set_attrs(
            forum_post_creator, data.get("created_by", {}), "id", "name", "forum_avator"
        )
        forum_post.created_by = forum_post_creator

        self._set_attrs(forum_post, data, "id", "number", "body", "signature")

        return forum_post

    def deserialize_anime_results(
        self, data: list[dict[str, Any]]
    ) -> list[Anime] | None:
        """Deserializes JSON payload into list of Anime model.

        Args:
            data: The JSON payload.

        Returns:
            List of Anime [`list[Anime]`]. Defaults to `None` if no data is found.
        """

        return [
            self.deserialize_anime(element.get("node"))
            for element in data.get("data", {})
        ]

    def deserialize_anime(self, data: dict[str, Any]) -> Anime:
        """Deserialize individual Anime JSON payload into Anime model.

        Args:
            data: The JSON payload.

        Returns:
            `Anime` model.
        """

        anime_fields = Anime()

        anime_fields.main_picture = self._deserialize_main_picture(
            data.get("main_picture", {})
        )

        anime_fields.alternative_titles = self._deserialize_alternative_titles(
            data.get("alternative_titles", {})
        )

        anime_fields.genres = self._deserialize_genres(data.get("genres", []))

        anime_fields.status = AnimeStatus.try_from_str(data.get("status"))
        anime_fields.nsfw = NSFWLevel.try_from_str(data.get("nsfw", "white"))

        anime_fields.start_season = Season(
            data.get("start_season", {}).get("year"),
            AnimeSeason.try_from_str(data.get("start_season", {}).get("season")),
        )

        anime_fields.broadcast = Broadcast(
            data.get("broadcast", {}).get("day_of_the_week"),
            self._time_from_str(data.get("broadcast", {}).get("start_time")),
        )

        anime_fields.studios = self._deserialize_studios(data.get("studios", []))

        anime_fields.media_type = (
            AnimeType.try_from_str(data.get("media_type")) or AnimeType.Unknown
        )

        anime_fields.start_date = self._date_from_str(data.get("start_date"))
        anime_fields.end_date = self._date_from_str(data.get("end_date"))
        anime_fields.created_at = self._datetime_from_iso(data.get("created_at"))
        anime_fields.updated_at = self._datetime_from_iso(data.get("updated_at"))

        anime_fields.pictures = self._deserialize_pictures(data.get("pictures", []))

        anime_fields.related_anime = self._deserialize_related_material(
            data.get("related_anime", [])
        )

        anime_fields.recommendations = self._deserialize_recommendations(
            data.get("recommendations", [])
        )

        anime_fields.statistics = AnimeStatistics(
            AnimeStatisticsStatus(
                data.get("statistics", {}).get("status", {}).get("watching"),
                data.get("statistics", {}).get("status", {}).get("completed"),
                data.get("statistics", {}).get("status", {}).get("on_hold"),
                data.get("statistics", {}).get("status", {}).get("dropped"),
                data.get("statistics", {}).get("status", {}).get("plan_to_watch"),
            ),
            data.get("statistics", {}).get("num_list_users"),
        )

        self._set_attrs(
            anime_fields,
            data,
            "id",
            "title",
            "synopsis",
            "mean",
            "rank",
            "popularity",
            "num_list_users",
            "num_scoring_users",
            "num_episodes",
            "source",
            "average_episode_duration",
            "rating",
            "background",
        )
        return anime_fields

    def deserialize_anime_ranking(self, data: dict[str, Any]) -> list[AnimeRanking]:
        """Deserializes JSON payload into list of AnimeRanking model.

        Args:
            data: The JSON payload.

        Returns:
            List of AnimeRanking [`list[AnimeRanking]`]. Defaults to `None` if no data is found.
        """

        return [
            AnimeRanking(
                self.deserialize_anime(element.get("node", {})),
                RankingModel(element.get("ranking", {}).get("rank")),
            )
            for element in data.get("data", [])
        ]

    def deserialize_manga_results(self, data: list[dict[str, Any]]) -> list[Manga]:
        """Deserializes JSON payload into list of Manga model.

        Args:
            data: The JSON payload.

        Returns:
            List of Manga [`list[Manga]`]. Defaults to `None` if no data is found.
        """

        return [
            self.deserialize_manga(element.get("node"))
            for element in data.get("data", {})
        ]

    def deserialize_manga(self, data: dict[str, Any]) -> Manga:
        """Deserialize individual Manga JSON payload into Manga model.

        Args:
            data: The JSON payload.

        Returns:
            `Manga` model."""

        manga_fields = Manga()

        manga_fields.nsfw = NSFWLevel.try_from_str(data.get("nsfw", "white"))
        manga_fields.media_type = (
            MangaType.try_from_str(data.get("media_type", "unknown"))
            or MangaType.Unknown
        )
        manga_fields.status = MangaStatus.try_from_str(data.get("status"))

        manga_fields.main_picture = self._deserialize_main_picture(
            data.get("main_picture", {})
        )

        manga_fields.pictures = self._deserialize_pictures(data.get("pictures", []))

        manga_fields.alternative_titles = self._deserialize_alternative_titles(
            data.get("alternative_titles", {})
        )

        manga_fields.genres = self._deserialize_genres(data.get("genres", []))
        manga_fields.authors = self._deserialize_authors(data.get("authors", []))
        manga_fields.related_manga = self._deserialize_related_material(
            data.get("related_manga", [])
        )

        manga_fields.recommendations = self._deserialize_recommendations(
            data.get("recommendations", [])
        )

        manga_fields.serialization = self._deserialize_manga_serialization(
            data.get("serialization", {})
        )

        manga_fields.start_date = self._date_from_str(data.get("start_date"))
        manga_fields.end_date = self._date_from_str(data.get("end_date"))
        manga_fields.created_at = self._datetime_from_iso(data.get("created_at"))
        manga_fields.updated_at = self._datetime_from_iso(data.get("updated_at"))

        self._set_attrs(
            manga_fields,
            data,
            "id",
            "title",
            "synopsis",
            "mean",
            "rank",
            "popularity",
            "num_list_users",
            "num_scoring_users",
            "num_volumes",
            "num_chapters",
            "background",
        )

        return manga_fields

    def deserialize_manga_ranking(self, data: dict[str, Any]) -> list[MangaRanking]:
        """Deserializes JSON payload into list of MangaRanking model.

        Args:
            data: The JSON payload.

        Returns:
            List of MangaRanking [`list[MangaRanking]`]. Defaults to `None` if no data is found.
        """

        return [
            MangaRanking(
                self.deserialize_manga(element.get("node", {})),
                RankingModel(element.get("ranking", {}).get("rank")),
            )
            for element in data.get("data", [])
        ]

    def deserialize_forum_board(self, data: dict[str, Any]) -> Forum:
        """"""

        forum_fields = Forum()

        forum_fields.title = data.get("title")
        forum_fields.boards = [
            self._deserialize_board(board) for board in data.get("boards", [])
        ]
        return forum_fields

    def deserialize_forum_topic(self, data: dict[str, Any]) -> ForumTopic:
        """"""

        forum_topic = ForumTopic()

        forum_topic.created_by = CommonModel(
            data.get("created_by", {}).get("id"), data.get("created_by", {}).get("name")
        )

        forum_topic.last_post_created_by = CommonModel(
            data.get("last_post_created_by", {}).get("id"),
            data.get("last_post_created_by", {}).get("name"),
        )

        forum_topic.created_at = self._datetime_from_iso(data.get("created_at"))
        forum_topic.last_post_created_at = self._datetime_from_iso(
            data.get("last_post_created_at")
        )

        self._set_attrs(
            forum_topic, data, "id", "title", "number_of_posts", "is_locked"
        )

        return forum_topic

    def deserialize_forum_topic_details(
        self, data: dict[str, Any]
    ) -> ForumTopicDetails:
        """"""

        forum_topic_details = ForumTopicDetails()

        forum_topic_details.posts = [
            self._deserialize_forum_post(p) for p in data.get("posts", [])
        ]

        self._set_attrs(forum_topic_details, data, "title")

        return forum_topic_details

    def deserialize_user_anime_list(self, data: dict[str, Any]) -> AnimeList:
        """Deserialize JSON payload into AnimeList model."""

        return AnimeList(
            self.deserialize_anime(data.get("node", {})),
            self._deserialize_user_anime_list_status(data.get("list_status", {})),
        )

    def _deserialize_user_anime_list_status(
        self, data: dict[str, Any]
    ) -> AnimeListStatus:
        """Deserialize JSON payload into AnimeListStatus model."""

        anime_list_status = AnimeListStatus()

        anime_list_status.status = AnimeWatchStatus.from_str(
            data.get("status", "watching")
        )
        anime_list_status.updated_at = self._datetime_from_iso(data.get("updated_at"))
        anime_list_status.start_date = self._date_from_str(data.get("start_date"))
        anime_list_status.finish_date = self._date_from_str(data.get("finish_date"))

        self._set_attrs(
            anime_list_status, data, "score", "num_episodes_watched", "is_rewatching"
        )

        return anime_list_status

    def deserialize_anime_list_update(self, data: dict[str, Any]) -> AnimeListUpdate:
        """Deserialize JSON payload into AnimeListUpdate model."""

        anime_list_update = AnimeListUpdate()

        anime_list_update.priority = ListPriority.from_str(data.get("priority"))
        anime_list_update.rewatch_value = AnimeRewatchValue.try_from_str(
            data.get("rewatch_value")
        )
        anime_list_update.updated_at = self._datetime_from_iso(data.get("updated_at"))

        self._set_attrs(
            anime_list_update,
            data,
            "status",
            "score",
            "num_episodes_watched",
            "is_rewatching",
            "num_times_rewatched",
            "tags",
            "comments",
        )

        return anime_list_update

    def deserialize_user_manga_list(self, data: dict[str, Any]) -> MangaList:
        """Deserializes JSON payload into MangaList model."""

        return MangaList(
            self.deserialize_manga(data.get("node", {})),
            self._deserialize_user_manga_list_status(data.get("list_status", {})),
        )

    def _deserialize_user_manga_list_status(
        self, data: dict[str, Any]
    ) -> MangaListStatus:
        """Deserializes JSON payload into MangaListStatus model."""

        manga_list_status = MangaListStatus()

        manga_list_status.status = MangaReadStatus.from_str(
            data.get("status", "reading")
        )
        manga_list_status.updated_at = self._datetime_from_iso(data.get("updated_at"))
        manga_list_status.start_date = self._date_from_str(data.get("start_date"))
        manga_list_status.finish_date = self._date_from_str(data.get("finish_date"))

        self._set_attrs(
            manga_list_status,
            data,
            "score",
            "num_volumes_read",
            "num_chapters_read",
            "is_rereading",
        )

        return manga_list_status

    def deserialize_manga_list_update(self, data: dict[str, Any]) -> MangaListUpdate:
        """Deserializes JSON payload into MangaListUpdate model."""

        manga_list_update = MangaListUpdate()

        manga_list_update.priority = ListPriority.from_str(data.get("priority"))
        manga_list_update.reread_value = MangaRereadValue.try_from_str(
            data.get("reread_value")
        )
        manga_list_update.updated_at = self._datetime_from_iso(data.get("updated_at"))

        self._set_attrs(
            manga_list_update,
            data,
            "status",
            "score",
            "num_volumes_read",
            "num_chapters_read",
            "is_rereading",
            "num_times_reread",
            "tags",
            "comments",
        )

        return manga_list_update
