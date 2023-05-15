"""Module for all manga related services."""

from __future__ import annotations

from typing import TypeVar

from . import BaseService
from aniwrap.result import Result, Success, Error
from aniwrap.models import HttpErrorResponse, Manga, MangaRanking
from aniwrap import endpoints
from aniwrap.enums.http import HttpMethod
from aniwrap.enums import MangaRankingType

T = TypeVar("T")
ValueT = TypeVar("ValueT")
ResultT = Result[ValueT, HttpErrorResponse]

__all__ = ("MangaService",)


class MangaService(BaseService):
    """Handles all methods related to Manga."""

    _fields = "id,title,main_picture,alternative_titles,start_date,end_date,synopsis,mean,rank,popularity,num_list_users,num_scoring_users,nsfw,created_at,updated_at,media_type,status,genres,my_list_status,num_volumes,num_chapters,authors{first_name,last_name},pictures,background,related_anime,related_manga,recommendations,serialization"
    __slots__ = ()

    async def search_manga(
        self, manga_name: str, *, limit: int | None = 10, offset: int | None = 0
    ) -> ResultT[list[Manga]]:
        """Search for Manga by title.

        Args:
            manga_name: Title or name of the manga.

        Keyword Args:
            limit: The optional limit to use with requests, which specifies the number of results in the response. Should be between 1 and 100.
                Defaults to `10`

            offset: The optional offset to use with requests, which specifies the offset from the start when fetching response.
                Defaults to `0`

        Returns:
            [`Result`][aniwrap.Result] containing `list[Manga]` on success or error data on error.

        ??? example

            ```py
            import aniwrap

            client = aniwrap.Client(...)

            result = await client.manga.search_manga("shingeki no kyojin", limit=5, offset=0)

            if result.is_success:
                manga_list = result.value

            if result.is_error:
                error = result.error

            await client.close()
            ```
        """

        params = {
            "fields": self._fields,
            "limit": 100 if limit > 100 else limit,
            "offset": 0 if offset < 0 else offset,
            "q": manga_name,
        }

        route = endpoints.SEARCH_MANGA.generate_route().with_params(params)
        result = await self._http.fetch(route, HttpMethod.Get)

        if isinstance(result, HttpErrorResponse):
            return Error(result)

        return Success(self._serializer.deserialize_manga_results(result.data))

    async def get_manga(self, id: int | str) -> ResultT[Manga]:
        """Get details of manga by the manga id.

        Args:
            id: The Id of the manga.

        Returns:
            [`Result`][aniwrap.Result] containing `Manga` on success or error data on error.

        ??? example

            ```py
            import aniwrap

            client = aniwrap.Client(...)

            result = await client.manga.get_manga(23390)

            if result.is_success:
                manga_details = result.value

            if result.is_error:
                error = result.error

            await client.close()
            ```
        """

        params = {"fields": self._fields}

        route = endpoints.GET_MANGA.generate_route(id).with_params(params)
        result = await self._http.fetch(route, HttpMethod.Get)

        if isinstance(result, HttpErrorResponse):
            return Error(result)

        return Success(self._serializer.deserialize_manga(result.data))

    async def get_manga_ranking(
        self,
        ranking_type: MangaRankingType,
        *,
        limit: int | None = 10,
        offset: int | None = 0,
    ) -> Result[list[MangaRanking]]:
        """Get different types of manga rankings.

        Args:
            ranking_type: The type of ranking. Check enum `MangaRankingType` for all the possible types.

        Keyword Args:
            limit: The optional limit to use with requests, which specifies the number of results in the response. Should be between 1 and 100.
                Defaults to `10`

            offset: The optional offset to use with requests, which specifies the offset from the start when fetching response.
                Defaults to `0`

        Returns:
            [`Result`][aniwrap.Result] containing `list[MangaRanking]` model on success or error data on error.

        ??? example

            ```py
            import aniwrap

            client = aniwrap.Client(...)

            result = await client.manga.get_manga_ranking(MangaRankingType.ByPopularity, limit=5, offset=0)

            if result.is_success:
                manga_list = result.value

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

        route = endpoints.GET_MANGA_RANKING.generate_route().with_params(params)
        result = await self._http.fetch(route, HttpMethod.Get)

        if isinstance(result, HttpErrorResponse):
            return Error(result)

        return Success(self._serializer.deserialize_manga_ranking(result.data))
