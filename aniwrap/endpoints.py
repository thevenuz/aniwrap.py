"""Module for all the different MAL API enpoints used in the library."""

from __future__ import annotations

from typing import Final

from aniwrap.models import Route

__all__ = ()

BASEURL: Final[str] = "https://api.myanimelist.net/v2"

ANIMEURL: Final[str] = f"{BASEURL}/anime"
MANGAURL: Final[str] = f"{BASEURL}/manga"
FORUMURL: Final[str] = f"{BASEURL}/forum"
USERURL: Final[str] = f"{BASEURL}/users"

SEARCH_ANIME: Final[Route] = Route("GET", f"{ANIMEURL}")
GET_ANIME: Final[Route] = Route("GET", f"{ANIMEURL}/()")
GET_ANIME_RANKING: Final[Route] = Route("GET", f"{ANIMEURL}/ranking")
GET_SEASONAL_ANIME: Final[Route] = Route("GET", f"{ANIMEURL}/season/()/()")

SEARCH_MANGA: Final[Route] = Route("GET", f"{MANGAURL}")
GET_MANGA: Final[Route] = Route("GET", f"{MANGAURL}/()")
GET_MANGA_RANKING: Final[Route] = Route("Get", f"{MANGAURL}/ranking")

GET_FORUM_BOARDS: Final[Route] = Route("Get", f"{FORUMURL}/boards")
GET_FORUM_TOPICS: Final[Route] = Route("Get", f"{FORUMURL}/topics")
GET_FORUM_TOPIC_DETAILS: Final[Route] = Route("Get", f"{FORUMURL}/topic/()")

GET_USER_ANIME_LIST: Final[Route] = Route("Get", f"{USERURL}/()/animelist")
UPDATE_USER_ANIME_LIST: Final[Route] = Route("Patch", f"{ANIMEURL}/()/my_list_status")
DELETE_ANIME_FROM_LIST: Final[Route] = Route("Delete", f"{ANIMEURL}/()/my_list_status")

GET_USER_MANGA_LIST: Final[Route] = Route("Get", f"{USERURL}/()/mangalist")
UPATE_USER_MANGA_LIST: Final[Route] = Route("Patch", f"{MANGAURL}/()/my_list_status")
DELETE_MANGA_FROM_LIST: Final[Route] = Route("Delete", f"{MANGAURL}/()/my_list_status")
