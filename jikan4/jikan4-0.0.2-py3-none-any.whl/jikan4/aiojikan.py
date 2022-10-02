from __future__ import annotations

import aiohttp


class AioJikan:
    """ Async Jikan API Wrapper"""

    def __init__(self, base_url: str = "https://api.jikan.moe/v4") -> None:
        """Construct a AioJikan object

        Args:
            base_url (str, optional): Base URL for Jikan API. Defaults to "https://api.jikan.moe/v4".

        Returns:
            AioJikan: AioJikan object
        
        Examples:
            >>> aiojikan = AioJikan()
            >>> aiojikan = AioJikan("https://api.jikan.moe/v4")
        """

        base_url = base_url.rstrip("/")
        self.base_url = base_url
        self.session = aiohttp.ClientSession()


    async def close(self) -> None:
        """Close the aiohttp session"""

        await self.session.close()


    async def __aenter__(self) -> AioJikan:
        return self
    
    async def __aexit__(self, exc_type, exc, tb) -> None:
        await self.close()


    async def _get(self, endpoint: str, params: dict = None) -> dict:
        """Make a GET request to the Jikan API

        Args:
            endpoint (str): Endpoint to request
            params (dict, optional): Parameters to send with request. Defaults to None.

        Returns:
            dict: JSON response from Jikan API
        """

        url = f"{self.base_url}/{endpoint}"
        async with self.session.get(url, params=params) as response:
            response.raise_for_status()
            return await response.json()
    

    async def get_anime(self, anime_id: int) -> dict:
        """Get anime information

        Args:
            anime_id (int): Anime ID

        Returns:
            dict: JSON response from Jikan API

        Examples:
            >>> aiojikan = AioJikan()
            >>> aiojikan.get_anime(1)
        """

        endpoint = f"anime/{anime_id}"
        return await self._get(endpoint)


    async def search_anime(self, search_type: str, query: str, page: int = 1) -> dict:
        """Search for anime, manga, people, characters, or news

        Args:
            search_type (str): Type of search to perform (tv, movie, ova, special, ona, music)
            query (str): Query to search for
            page (int, optional): Page number. Defaults to 1.

        Returns:
            dict: JSON response from Jikan API
        
        Examples:
            >>> aiojikan = AioJikan()
            >>> aiojikan.search_anime("anime", "naruto")
        """

        endpoint = f"anime"
        params = {"q": query, "page": page, "type": search_type}
        return await self._get(endpoint, params)