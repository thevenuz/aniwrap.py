"""Module for all Forum related services."""

from __future__ import annotations

from typing import TypeVar

from . import BaseService
from aniwrap.models import HttpErrorResponse, Forum, ForumTopicDetails, ForumTopic
from aniwrap import endpoints
from aniwrap.enums.http import HttpMethod
from aniwrap.result import Result, Success, Error

T = TypeVar("T")
ValueT = TypeVar("ValueT")
ResultT = Result[ValueT, HttpErrorResponse]

__all__ = ("ForumService",)


class ForumService(BaseService):
    """Handles all forum related methods."""

    __slots__ = ()

    async def get_forum_boards(self) -> ResultT[list[Forum]]:
        """Get list of all the fourm boards filtered by category.

        Returns:
            [`Result`][aniwrap.Result] containing `list[Forum]` on success or error data on error.

        ??? example

            ```py
            import aniwrap

            client = aniwrap.Client(...)

            result = await client.forum.get_forum_boards()

            if result.is_success:
                boards = result.value

            if result.is_error:
                error = result.error

            await client.close()
            ```
        """

        route = endpoints.GET_FORUM_BOARDS.generate_route()
        result = await self._http.fetch(route, HttpMethod.Get)

        if isinstance(result, HttpErrorResponse):
            return Error(result)

        return Success(
            [
                self._serializer.deserialize_forum_board(c)
                for c in result.data.get("categories", [])
            ]
        )

    async def get_forum_topics(
        self,
        *,
        query: str | None = None,
        board_id: int | None = None,
        subboard_id: int | None = None,
        limit: int | None = 10,
        offset: int | None = 0,
        topic_user_name: str | None = None,
        username: str | None = None,
    ) -> ResultT[list[ForumTopic]]:
        """Get topics by different parameters. At least one of the arguments must be specified.

        Keyword Args:
            query: The query parameter to search - usually matches the title of the topic
                Defaults to `None`

            board_id: The Id of specific board
                Defaults to `None`

            subboard_id: The Id of any specific sub board
                Defaults to `None`

            limit: The optional limit to use with requests, which specifies the number of results in the response. Should be between 1 and 100.
                Defaults to `10`

            offset: The optional offset to use with requests, which specifies the offset from the start when fetching response.
                Defaults to `0`

            topic_user_name: The username of the user that started the topic
                Defaults to `None`

            username: The username of the users that participated in the topic
                Defaults to `None`

        Returns:
            [`Result`][aniwrap.Result] containing `ForumTopic` on success or error data on error.

        Raises:
            ValueError: When no arguments are given

        ??? example

            ```py
            import aniwrap

            client = aniwrap.Client(...)

            result = await client.forum.get_forum_topics(query="new anime")

            if result.is_success:
                topics = result.value

            if result.is_error:
                error = result.error

            await client.close()
            ```
        """

        if query or board_id or subboard_id or topic_user_name or username:
            params = {
                "q": query if query else "",
                "board_id": board_id if board_id else "",
                "subboard_id": subboard_id if subboard_id else "",
                "topic_user_name": topic_user_name if topic_user_name else "",
                "username": username if username else "",
                "limit": limit,
                "offset": offset,
            }

            route = endpoints.GET_FORUM_TOPICS.generate_route().with_params(params)
            result = await self._http.fetch(route, HttpMethod.Get)

            if isinstance(result, HttpErrorResponse):
                return Error(result)

            return Success(
                [
                    self._serializer.deserialize_forum_topic(t)
                    for t in result.data.get("data", [])
                ]
            )

        else:
            raise ValueError("Atleast one parameter must be specified.")

    async def get_forum_topic_details(
        self, topic_id: int, *, limit: int | None = 10, offset: int | None = 0
    ) -> ResultT[ForumTopicDetails]:
        """Get topic details by topic id.

        Args:
            topic_id: The Id of the topic

        Keyword Args:
            limit: The optional limit to use with requests, which specifies the number of results in the response. Should be between 1 and 100.
                Defaults to `10`

            offset: The optional offset to use with requests, which specifies the offset from the start when fetching response.
                Defaults to `0`

        Returns:
            [`Result`][aniwrap.Result] containing `ForumTopicDetails` on success or error data on error.

        ??? example

            ```py
            import aniwrap

            client = aniwrap.Client(...)

            result = await client.forum.get_forum_topic_details(2070198)

            if result.is_success:
                topic_details = result.value

            if result.is_error:
                error = result.error

            await client.close()
            ```
        """

        params = {"limit": limit, "offset": offset}

        route = endpoints.GET_FORUM_TOPIC_DETAILS.generate_route(topic_id).with_params(
            params
        )
        result = await self._http.fetch(route, HttpMethod.Get)

        if isinstance(result, HttpErrorResponse):
            return Error(result)

        return Success(
            self._serializer.deserialize_forum_topic_details(
                result.data.get("data", {})
            )
        )
