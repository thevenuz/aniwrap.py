"""This module has the client to connect to MAL API."""

from __future__ import annotations
from aniwrap import services, serializer


__all__ = ("Client", "UserClient")


class Client:
    """An asynchronous client used to interact with the MAL API.

    Args:
        client_id: The MAL Client Id to be used with the requests.
    """

    __slots__ = ("_http", "_serializer", "_anime", "_manga", "_forum")

    def __init__(self, client_id: str) -> None:
        self._http = services.HttpService(client_id=client_id)
        self._serializer = serializer.Serializer()
        self._anime = services.AnimeService(self._http, self._serializer)
        self._manga = services.MangaService(self._http, self._serializer)
        self._forum = services.ForumService(self._http, self._serializer)

    @property
    def anime(self) -> services.AnimeService:
        """The [`AnimeService`][aniwrap.AnimeService] used to make anime related requests."""
        return self._anime

    @property
    def manga(self) -> services.MangaService:
        """The [`MangaService`][aniwrap.MangaService] used to make manga related requests."""
        return self._manga

    @property
    def forum(self) -> services.ForumService:
        """The [`ForumService`][aniwrap.ForumService] used to make forum related requests."""
        return self._forum

    async def close(self) -> None:
        """Close the existing client session.

        !!! warning

            You will receive an error in your console if this is not called before the program terminates.
        """
        await self._http.close()


class UserClient:
    """
    An asynchronous client used to interact with the user methods of MAL API.

    Args:
        access_token: The access token that is generated using the MAL oauth flow. 

    !!! Note    
        The `access_token` will be unique for each MAL user.
    """

    __slots__ = ("_http", "_serializer", "_user")

    def __init__(self, access_token: str) -> None:
        self._http = services.HttpService(access_token=access_token)
        self._serializer = serializer.Serializer()
        self._user = services.UserService(self._http, self._serializer)

    @property
    def user(self) -> services.UserService:
        """"""
        return self._user

    async def close(self) -> None:
        """Close the existing client session.

        !!! warning

            You will receive an error in your console if this is not called before the program terminates.
        """
        await self._http.close()
