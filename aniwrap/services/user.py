"""Module for all the user anime and manga related services."""

from __future__ import annotations

from typing import TypeVar, Any

from .base import BaseService
from aniwrap import endpoints
from aniwrap.enums.http import HttpMethod
from aniwrap.enums import (
    AnimeListSortType,
    AnimeWatchStatus,
    ListPriority,
    AnimeRewatchValue,
    MangaReadStatus,
    MangaListSortType,
    MangaRereadValue,
)
from aniwrap.models import (
    HttpErrorResponse,
    AnimeList,
    AnimeListUpdate,
    MangaListUpdate,
    MangaList,
)
from aniwrap.result import Result, Success, Error

T = TypeVar("T")
ValueT = TypeVar("ValueT")
ResultT = Result[ValueT, HttpErrorResponse]

__all__ = ("UserService",)


class UserService(BaseService):
    """Hanldes all the methods related to user Anime and Manga."""

    __slots__ = ()
    _anime_fields = "id,title,main_picture,alternative_titles,start_date,end_date,synopsis,mean,rank,popularity,num_list_users,num_scoring_users,nsfw,created_at,updated_at,media_type,status,genres,num_episodes,start_season,broadcast,source,average_episode_duration,rating,pictures,background,related_anime,related_manga,recommendations,studios,statistics,list_status"
    _manga_fields = "id,title,main_picture,alternative_titles,start_date,end_date,synopsis,mean,rank,popularity,num_list_users,num_scoring_users,nsfw,created_at,updated_at,media_type,status,genres,my_list_status,num_volumes,num_chapters,authors{first_name,last_name},pictures,background,related_anime,related_manga,recommendations,serialization,list_status"

    # region anime
    async def get_anime_list(
        self,
        username: str,
        *,
        status: AnimeWatchStatus | None = None,
        sort: AnimeListSortType | None = None,
        limit: int | None = 10,
        offset: int | None = 0,
    ) -> ResultT[list[AnimeList]]:
        """Get anime list of a user by username.

        Args:
            username: The username of the user.

        KeywordArgs:
            status: The optional status based on which the results will be filtered. If not specified, the result will contain anime with all the status.
                Defaults to `None`.

            sort: The optional sort filter based on which the results will be sorted. If not specified, by default the results will be sorted in the descending order of last updated date.
                Defaults to `None`.

            limit: The optional limit to use with requests, which specifies the number of results in the response. Should be between 1 and 100.
                Defaults to `10`

            offset: The optional offset to use with requests, which specifies the offset from the start when fetching response.
                Defaults to `0`

        Returns:
            [`Result`][aniwrap.Result] containing `list[AnimeList]` model on success or [`HttpErrorResponse`] data on error.


        ??? example

            ```py
            import aniwrap

            user_client = aniwrap.UserClient(...)

            result = await user_client.user.get_anime_list("your-user-name")

            if result.is_success:
                anime_list = result.value

            if result.is_error:
                error = result.error

            await user_client.close()
            ```
        """

        params = {
            "fields": self._anime_fields,
            "status": status.value if status else "",
            "sort": sort.value if sort else "",
            "limit": 100 if limit > 100 else limit,
            "offset": 0 if offset < 0 else offset,
        }

        route = endpoints.GET_USER_ANIME_LIST.generate_route(username).with_params(
            params
        )
        result = await self._http.fetch(route, HttpMethod.Get)

        if isinstance(result, HttpErrorResponse):
            return Error(result)

        return Success(
            [
                self._serializer.deserialize_user_anime_list(a)
                for a in result.data.get("data", [])
            ]
        )

    async def update_anime_list(
        self,
        anime_id: int,
        *,
        status: AnimeWatchStatus | None = None,
        is_rewatching: bool | None = None,
        score: int | None = None,
        num_watched_episodes: int | None = None,
        priority: ListPriority | None = None,
        num_times_rewatched: int | None = None,
        rewatch_value: AnimeRewatchValue | None = None,
        tags: str | None = None,
        comments: str | None = None,
    ) -> ResultT[AnimeListUpdate]:
        """Update anime details in user anime list. If the anime doesn't already exists, this will add the anime to the list.
            Only specify the params that need to be updated.

        Args:
            anime_id: The id of the anime.

        Keyword Args:
            status: The watch status of the anime.

            is_rewatching: The rewatching status of the anime.

            score: The score of the anime. Score should be in between 0 and 10.

            num_watched_episodes: The number of episodes watched.

            priority: The priority of the anime in the user list.

            num_times_rewatched: The number of times rewatched.

            rewatch_value: The rewatch value of the anime.

            tags: The tags that need to be added.

            comments: The user comments.

        Returns:
            [`Result`][aniwrap.Result] containing [`AnimeListUpdate`][aniwrap.AnimeListUpdate] model on success or `HttpErrorResponse` data on error.
            `HttpErrorResponse.status` will be `404` if no anime with the provided anime_id contains on MAL.

        ??? example

            ```py
            import aniwrap

            user_client = aniwrap.UserClient(...)

            result = await user_client.user.update_anime_list(5114, score=8)

            if result.is_success:
                anime_list_update = result.value

            if result.is_error:
                error = result.error

            await user_client.close()
            ```
        """

        data = self._generate_data_map(
            status=status,
            is_rewatching=is_rewatching,
            score=None
            if not score
            else 10
            if score > 10
            else 0
            if score < 0
            else score,
            num_watched_episodes=num_watched_episodes,
            priority=priority.value if priority else None,
            num_times_rewatched=num_times_rewatched,
            rewatch_value=rewatch_value.value if rewatch_value else None,
            tags=tags,
            comments=comments,
        )

        route = endpoints.UPDATE_USER_ANIME_LIST.generate_route(anime_id).with_data(
            data
        )
        result = await self._http.fetch(route, HttpMethod.Patch)

        if isinstance(result, HttpErrorResponse):
            return Error(result)

        return Success(self._serializer.deserialize_anime_list_update(result.data))

    async def delete_anime_from_list(self, anime_id: str) -> ResultT[str]:
        """Delete an anime from user's list.

        Args:
            anime_id: The Id of the anime to be deleted from the list.

        Returns:
            [`Result`][aniwrap.Result] containing `str` with success message on success or [`HttpErrorResponse`] data on error. [`HttpErrorResponse.status`] will be `404` if no anime with the provided anime_id contains on MAL.

        ??? example

            ```py
            import aniwrap

            user_client = aniwrap.UserClient(...)

            result = await user_client.user.delete_anime_from_list(52034)

            if result.is_success:
                print("deleted")

            if result.is_error:
                error = result.error

            await user_client.close()
            ```
        """

        route = endpoints.DELETE_ANIME_FROM_LIST.generate_route(anime_id)
        result = await self._http.fetch(route, HttpMethod.Delete)

        if isinstance(result, HttpErrorResponse):
            return Error(result)

        return Success("Succesfully deleted anime from the list.")

    # endregion

    # region manga
    async def get_manga_list(
        self,
        username: str,
        *,
        status: MangaReadStatus | None = None,
        sort: MangaListSortType | None = None,
        limit: int | None = 10,
        offset: int | None = 0,
    ) -> ResultT[list[MangaList]]:
        """Get the manga list of a user by user name.

        Args:
            username: The user name of the user.

        KeywordArgs:
            status: The status with which the list need to be filtered. If specified, the result will only contain manga of this status.
                Defaults to `None` and result contains manga of all status'.

            sort: The type of sorting on the manga list.
                Defaults to `None`.

            limit: The optional limit to use with requests, which specifies the number of results in the response. Should be between 1 and 100.
                Defaults to `10`

            offset: The optional offset to use with requests, which specifies the offset from the start when fetching response.
                Defaults to `0`

        Returns:
            [`Result`][aniwrap.Result] containing `list[MangaList]` model on success or [`HttpErrorResponse`] data on error.

        ??? example

            ```py
            import aniwrap

            user_client = aniwrap.UserClient(...)

            result = await await user_client.user.get_manga_list("your-user-name")

            if result.is_success:
                manga_list = result.value

            if result.is_error:
                error = result.error

            await user_client.close()
            ```
        """

        params = {
            "fields": self._manga_fields,
            "status": status.value if status else "",
            "sort": sort.value if sort else "",
            "limit": 100 if limit > 100 else limit,
            "offset": 0 if offset < 0 else offset,
        }

        route = endpoints.GET_USER_MANGA_LIST.generate_route(username).with_params(
            params
        )
        result = await self._http.fetch(route, HttpMethod.Get)

        if isinstance(result, HttpErrorResponse):
            return Error(result)

        return Success(
            [
                self._serializer.deserialize_user_manga_list(m)
                for m in result.data.get("data", [])
            ]
        )

    async def update_manga_list(
        self,
        manga_id: str,
        *,
        status: MangaReadStatus | None = None,
        is_rereading: bool | None = None,
        score: int | None = None,
        num_volumes_read: int | None = None,
        num_chapters_read: int | None = None,
        priority: ListPriority | None = None,
        num_times_reread: int | None = None,
        reread_value: MangaRereadValue | None = None,
        tags: str | None = None,
        comments: str | None = None,
    ) -> ResultT[MangaListUpdate]:
        """Update manga details in user manga list. If the manga doesn't already exists, this will add the manga to the list.
            Only specify the params that need to be updated/added.

        Args:
            manga_id: The id of the manga.

        Keyword Args:
            status: The Read status of the manga.

            is_rereading: The rereading status of the manga.

            score: The score of the manga. Score should be in between 0 and 10.

            num_volumes_read: The number of volumes read.

            num_chapters_read: The number of chapters read.

            priority: The priority of the manga in the user list.

            num_times_reread: The number of times reread.

            reread_value: The reread value of the manga.

            tags: The tags that need to be added.

            comments: The user comments.

        Returns:
            [`Result`][aniwrap.Result] containing [`MangaListUpdate`][aniwrap.MangaListUpdate] model on success or `HttpErrorResponse` data on error.
            `HttpErrorResponse.status` will be `404` if no manga with the provided manga_id contains on MAL.

        ??? example

            ```py
            import aniwrap

            user_client = aniwrap.UserClient(...)

            result = await user_client.user.update_manga_list(13759, status=MangaReadStatus.PlanToRead)

            if result.is_success:
                manga_list_update = result.value

            if result.is_error:
                error = result.error

            await user_client.close()
            ```
        """

        data = self._generate_data_map(
            status=status,
            is_rereading=is_rereading,
            score=None
            if not score
            else 10
            if score > 10
            else 0
            if score < 0
            else score,
            num_volumes_read=num_volumes_read,
            num_chapters_read=num_chapters_read,
            priority=priority.value if priority else None,
            num_times_reread=num_times_reread,
            reread_value=reread_value.value if reread_value else None,
            tags=tags,
            comments=comments,
        )

        route = endpoints.UPATE_USER_MANGA_LIST.generate_route(manga_id).with_data(data)
        result = await self._http.fetch(route, HttpMethod.Patch)

        if isinstance(result, HttpErrorResponse):
            return Error(result)

        return Success(self._serializer.deserialize_manga_list_update(result.data))

    async def delete_manga_from_list(self, manga_id: str) -> ResultT[str]:
        """Delete an manga from user's list.

        Args:
            manga_id: The Id of the manga to be deleted from the list.

        Returns:
            [`Result`][aniwrap.Result] containing `str` with success message on success or [`HttpErrorResponse`] data on error. [`HttpErrorResponse.status`] will be `404` if no anime with the provided manga_id contains on MAL.

        ??? example

            ```py
            import aniwrap

            user_client = aniwrap.UserClient(...)

            result = await user_client.user.delete_manga_from_list(13759)

            if result.is_success:
                print("deleted")

            if result.is_error:
                error = result.error

            await user_client.close()
            ```
        """

        route = endpoints.DELETE_MANGA_FROM_LIST.generate_route(manga_id)
        result = await self._http.fetch(route, HttpMethod.Delete)

        if isinstance(result, HttpErrorResponse):
            return Error(result)

        return Success("Succesfully deleted manga from the list.")

    # endregion

    def _generate_data_map(self, **kwargs) -> dict[str, Any]:
        """Generarates a dict from input keyword args."""

        data = {}
        for key, value in kwargs.items():
            if value:
                data[key] = value

        return data
