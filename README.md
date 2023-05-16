# aniwrap

An asynchronous wrapper for the [MyAnimeList V2 API](https://myanimelist.net/apiconfig/references/api/v2).

Aniwrap aims to make it easier to interact with MAL API.

## Disclaimer

The library is still in Alpha, and the features may change at any time.

## Installation

Python version 3.10 or greater is required to use aniwrap.

```sh
pip install aniwrap
```

## Features

- Search anime and manga by name
- Fetch anime and manga details by ID
- Fetch seasonal anime
- Fetch anime and manga rankings
- Fetch forum boards and discussions
- Fetch and manipulate user's anime and manga list using user's access token

## Usage

- Example of using anime and manga related actions

```Python
from  aniwrap  import  Client

client = Client("your MAL client Id")

anime_search_result = await client.anime.search_anime("attack on titan")
manga_search_result = await client.manga.search_manga("attack on titan")

if anime_search_result.is_success:
    anime_results = anime_search_result.value

if anime_search_result.is_error:
    error = anime_search_result.error

if manga_search_result.is_success:
    manga_results = manga_search_result.value

if manga_search_result.is_error:
    error = manga_search_result.error

await  client.close()
```

- Example of using user related actions

```python
from aniwrap import UserClient

user_client = UserClient("user's access token")

anime_list_result = await user_client.user.get_anime_list("user's username")
manga_list_result = await user_client.user.get_manga_list("user's username")

if anime_list_result.is_success:
    anime_list = anime_list_result.value

if anime_list_result.is_error:
    error = anime_list_result.error

if manga_list_result.is_success:
    manga_list = manga_list_result.value

if manga_list_result.is_error:
    error = manga_list_result.error

await  user_client.close()
```

You can find information on generating Client Id and user's access token used in the above examples on [MAL documentation](https://myanimelist.net/apiconfig/references/authorization).

## Issues

If you're facing any problems with the library, please open an issue [here](https://github.com/thevenuz/aniwrap.py/issues).

## Credits

- Credits to [Jonxslays](https://github.com/Jonxslays)'s [wom.py](https://github.com/Jonxslays/wom.py). Lot of stuff is ~~copied~~ inspired from wom.py.

## License

aniwrap is licensed under [MIT License](https://github.com/thevenuz/aniwrap.py/blob/master/LICENSE).
