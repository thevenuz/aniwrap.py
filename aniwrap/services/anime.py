"""Module for anime related services."""

from __future__ import annotations
from typing import TypeVar

from . import BaseService
from aniwrap.models import Anime, HttpErrorResponse, AnimeRanking
from aniwrap import endpoints
from aniwrap.enums.http import HttpMethod
from aniwrap.enums import AnimeSeason, AnimeRankingType, AnimeSortType
from aniwrap.result import Result, Success, Error

T = TypeVar("T")
ValueT = TypeVar("ValueT")
ResultT = Result[ValueT, HttpErrorResponse]

__all__ = ("AnimeService",)


class AnimeService(BaseService):
    """Hanldes all the methods related to Anime."""

    _fields = "id,title,main_picture,alternative_titles,start_date,end_date,synopsis,mean,rank,popularity,num_list_users,num_scoring_users,nsfw,created_at,updated_at,media_type,status,genres,num_episodes,start_season,broadcast,source,average_episode_duration,rating,pictures,background,related_anime,related_manga,recommendations,studios,statistics"
    __slots__ = ()

    async def search_anime(
        self, anime_name: str, *, limit: int | None = 10, offset: int | None = 0
    ) -> ResultT[list[Anime]]:
        """Search for anime by title.

        Args:
            anime_name: Title or name of the anime.

        Keyword Args:
            limit: The optional limit to use with requests, which specifies the number of results in the response. Should be between 1 and 100.
                Defaults to `10`

            offset: The optional offset to use with requests, which specifies the offset from the start when fetching response.
                Defaults to `0`

        Returns:
            [`Result`][aniwrap.Result] containing `list[Anime]` on success or error data on error.

        ??? example

            ```py
            import aniwrap

            client = aniwrap.Client(...)

            result = await client.anime.search_anime("blue lock", limit=5, offset=0)

            if result.is_success:
                anime_list = result.value

            if result.is_error:
                error = result.error

            await client.close()
            ```
        """

        params = {
            "fields": self._fields,
            "limit": 100 if limit > 100 else limit,
            "offset": 0 if offset < 0 else offset,
            "q": anime_name,
        }

        route = endpoints.SEARCH_ANIME.generate_route().with_params(params)
        result = await self._http.fetch(route, HttpMethod.Get)

        if isinstance(result, HttpErrorResponse):
            return Error(result)

        return Success(self._serializer.deserialize_anime_results(result.data))

    async def get_anime(self, id: int | str) -> ResultT[Anime]:
        """Get details of anime by the anime id.

        Args:
            id: The Id of the anime.

        Returns:
            [`Result`][aniwrap.Result] containing `Anime` on success or error data on error.

        ??? example

            ```py
            import aniwrap

            client = aniwrap.Client(...)

            result = await client.anime.get_anime(16498)

            if result.is_success:
                anime_details = result.value

            if result.is_error:
                error = result.error

            await client.close()
            ```
        """

        params = {"fields": self._fields}
        route = endpoints.GET_ANIME.generate_route(id).with_params(params)
        result = await self._http.fetch(route, HttpMethod.Get)

        if isinstance(result, HttpErrorResponse):
            return Error(result)

        return Success(self._serializer.deserialize_anime(result.data))

    async def get_anime_ranking(
        self,
        ranking_type: AnimeRankingType,
        *,
        limit: int | None = 10,
        offset: int | None = 0,
    ) -> ResultT[list[AnimeRanking]]:
        """Get different types of anime rankings.

        Args:
            ranking_type: The type of ranking. Check enum `AnimeRankingType` for all the possible types.

        Keyword Args:
            limit: The optional limit to use with requests, which specifies the number of results in the response. Should be between 1 and 100.
                Defaults to `10`

            offset: The optional offset to use with requests, which specifies the offset from the start when fetching response.
                Defaults to `0`

        Returns:
            [`Result`][aniwrap.Result] containing `list[AnimeRanking]` model on success or error data on error.

        ??? example

            ```py
            import aniwrap

            client = aniwrap.Client(...)

            result = await client.anime.get_anime_ranking(AnimeRankingType.All, limit=5, offset=0)

            if result.is_success:
                anime_list = result.value

            if result.is_error:
                error = result.error

            await client.close()
            ```
        """

        params = {
            "fields": self._fields,
            "limit": 100 if limit > 100 else limit,
            "offset": 0 if offset < 0 else offset,
            "ranking_type": ranking_type.value,
        }

        route = endpoints.GET_ANIME_RANKING.generate_route().with_params(params)
        result = await self._http.fetch(route, HttpMethod.Get)

        if isinstance(result, HttpErrorResponse):
            return Error(result)

        return Success(self._serializer.deserialize_anime_ranking(result.data))

    async def get_seasonal_anime(
        self,
        year: int,
        season: AnimeSeason,
        *,
        sort_type: AnimeSortType = AnimeSortType.AnimeScore,
        limit: int | None = 10,
        offset: int | None = 0,
    ) -> ResultT[list[Anime]]:
        """Get anime by season and year.

        Args:
            year: The year.
            season: The anime season in the year.

        Keyword Args:
            sort_type: The optional sort_type based on which the anime results will be sorted.
                Defaults to `AnimeSortType.AnimeScore`.

            limit: The optional limit to use with requests, which specifies the number of results in the response. Should be between 1 and 100.
                Defaults to `10`

            offset: The optional offset to use with requests, which specifies the offset from the start when fetching response.
                Defaults to `0`

        Returns:
            [`Result`][aniwrap.Result] containing `list[Anime]` model on success or error data on error.

        ??? example

            ```py
            import aniwrap

            client = aniwrap.Client(...)

            result = await client.anime.get_seasonal_anime(
                2020, AnimeSeason.Fall, sort_type=AnimeSortType.NumberOfUsers
            )

            if result.is_success:
                anime_list = result.value

            if result.is_error:
                error = result.error
            ```
        """

        params = {
            "fields": self._fields,
            "limit": 100 if limit > 100 else limit,
            "offset": 0 if offset < 0 else offset,
            "sort": sort_type.value,
        }

        route = endpoints.GET_SEASONAL_ANIME.generate_route(
            year, season.value
        ).with_params(params)
        result = await self._http.fetch(route, HttpMethod.Get)

        if isinstance(result, HttpErrorResponse):
            return Error(result)

        return Success(self._serializer.deserialize_anime_results(result.data))

    # Used when requesting specific fields is implemented
    def _generate_fields_map(self, fields: list[Anime]) -> dict[str, str]:
        """Generate a dict of field params."""

        return {"fields": ",".join([f.value for f in fields])}
