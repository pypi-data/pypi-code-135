import requests

from .models import Anime, AnimeSearch


class Jikan:
    """Jikan wrapper for the jikan.moe API"""

    def __init__(self, base_url: str = "https://api.jikan.moe/v4") -> None:
        """Construct a Jikan object

        Args:
            base_url (str, optional): Base URL for Jikan API. Defaults to "https://api.jikan.moe/v4".

        Returns:
            Jikan: Jikan object

        Examples:
            >>> jikan = Jikan()
            >>> jikan = Jikan("https://api.jikan.moe/v4")
        """

        base_url = base_url.rstrip("/")
        self.base_url = base_url
        self.session = requests.Session()

    def _get(self, endpoint: str, params: dict = None) -> dict:
        """Make a GET request to the Jikan API

        Args:
            endpoint (str): Endpoint to request
            params (dict, optional): Parameters to send with request. Defaults to None.

        Returns:
            dict: JSON response from Jikan API
        """

        url = f"{self.base_url}/{endpoint}"
        response = self.session.get(url, params=params)
        response.raise_for_status()
        return response.json()

    def get_anime(self, anime_id: int) -> Anime:
        """Get anime information

        Args:
            anime_id (int): Anime ID

        Returns:
            Anime: Anime object

        Examples:
            >>> jikan = Jikan()
            >>> anime = jikan.get_anime(1)
        """

        endpoint = f"anime/{anime_id}"
        response = self._get(endpoint)
        return Anime(**response["data"])

    def search_anime(self, search_type: str, query: str, page: int = 1) -> AnimeSearch:
        """Search for anime

        Args:
            search_type (str): Type of search to perform (tv, movie, ova, special, ona, music)
            query (str): Query to search for
            page (int, optional): Page number. Defaults to 1.

        Returns:
            AnimeSearch: AnimeSearch object

        Examples:
            >>> jikan = Jikan()
            >>> result = jikan.search_anime("tv", "naruto")
        """

        endpoint = f"anime"
        params = {"q": query, "page": page, "type": search_type}
        response = self._get(endpoint, params)

        return AnimeSearch(**response)
