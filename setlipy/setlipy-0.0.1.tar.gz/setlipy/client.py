""" A simple Python wrapper for the setlist.fm API """
from typing import Optional

import requests

from setlipy.string_encoding import check_for_special_chars


class Setlipy(object):
    """
    Example usage:

    from setlipy import client

    sfm = client.Setlipy(auth="YOUR_API_KEY")

    results = sfm.setlists(artist_name="The Rolling Stones", year="2022")

    json_dump = (results.json())

    for idx, setlists in enumerate(json_dump["setlist"]):
        print(idx, setlists)
    """

    def __init__(self, file_format: str = "json", auth: str = None):
        """
        Creates a Setlipy client.

        Args:
            file_format: defines the data interchange format
            auth: Setlist.fm authentication id
        """
        self.base_url: str = "https://api.setlist.fm/rest/1.0/"
        self._auth: Optional[str] = auth
        self.accept_lang: str = f"application/{file_format}"

    def set_auth(self, auth: str):
        """
        Define the authentication id from Setlist.fm
        Args:
            auth: Setlist.fm authentication id
        """
        self._auth: str = auth

    def _internal_call(self, url, params) -> requests.Response:
        args = dict(params=params)

        if not url.startswith("http"):
            url = self.base_url + url

        request_args = ""
        for k, v in args["params"].items():
            if v:
                v = check_for_special_chars(v)
                request_args += f"{k}={v}&"

        request_url = url + request_args

        response: requests.Response = requests.get(
            request_url, headers={"X-API-Key": self._auth, "Accept": self.accept_lang}
        )
        return response

    def _get(self, url, **kwargs):
        return self._internal_call(url, kwargs)

    def artists(
        self,
        artist_mbid: str = "",
        artist_name: str = "",
        artist_tmid: int = None,
        result_page_num: int = 1,
        sort_by: str = "sortName",
    ):
        """
        Search for artists.

        Args:
            artist_mbid: the artist's Musicbrainz Identifier (mbid)
            artist_name: the artist's name
            artist_tmid: the artist's Ticketmaster Identifier (tmid)
            result_page_num: the number of the result page you'd like to have
            sort_by: the sort of the result, either sortName (default) or relevance
        """

        path_url = "search/artists?"

        return self._get(
            url=path_url,
            artistMbid=artist_mbid,
            artistName=artist_name,
            artistTmid=artist_tmid,
            p=result_page_num,
            sort=sort_by,
        )

    def setlists(
        self,
        artist_mbid: str = "",
        artist_name: str = "",
        artist_tmid: int = None,
        city_id: str = "",
        city_name: str = "",
        country_code: str = "",
        date_of_event: str = "",
        last_fm: int = None,
        last_updated: str = "",
        result_page_num: int = 1,
        state: str = "",
        state_code: str = "",
        tour_name: str = "",
        venue_id: str = "",
        venue_name: str = "",
        year: str = "",
    ):
        """
        Search for setlists.

        Args:
            artist_mbid: the artist's Musicbrainz Identifier (mbid)
            artist_name: the artist's name
            artist_tmid: the artist's Ticketmaster Identifier (tmid)
            city_id: the city's geoId
            city_name: the name of the city
            country_code: the country code
            date_of_event: the date of the event (format dd-MM-yyyy)
            last_fm: the event's Last.fm Event ID (deprecated)
            last_updated: the date and time (UTC) when this setlist was last updated (format yyyyMMddHHmmss) - either
            edited or reverted. search will return setlists that were updated on or after this date
            result_page_num: the number of the result page
            state: the state
            state_code: the state code
            tour_name:
            venue_id: the venue id
            venue_name: the name of the venue
            year: the year of the event
        """

        path_url = "search/setlists?"

        return self._get(
            path_url,
            artistMbid=artist_mbid,
            artistName=artist_name,
            artistTmid=artist_tmid,
            cityId=city_id,
            cityName=city_name,
            countryCode=country_code,
            date=date_of_event,
            lastFm=last_fm,
            last_updated=last_updated,
            p=result_page_num,
            state=state,
            stateCode=state_code,
            tourName=tour_name,
            venueId=venue_id,
            venueName=venue_name,
            year=year,
        )

    def cities(
        self,
        country: str = "",
        name: str = "",
        result_page_num: int = 1,
        state: str = "",
        state_code: str = "",
    ):
        """
        Search for a city.

        Args:
            country: the city's country
            name: name of the city
            result_page_num: the number of the result page you'd like to have
            state: state the city lies in
            state_code: state code the city lies in
        """
        path_url: str = "search/cities?"

        return self._get(
            path_url,
            country=country,
            name=name,
            p=result_page_num,
            state=state,
            stateCode=state_code,
        )

    def countries(self):
        """
        Get a complete list of all supported countries.
        """

        path_url: str = "search/countries?"

        return self._get(path_url)

    def venues(
        self,
        city_id: str = "",
        city_name: str = "",
        country: str = "",
        name: str = "",
        result_page_num: int = 1,
        state: str = "",
        state_code: str = "",
    ):
        """
        Search for venues.

        Args:
            city_id: the city's geoId
            city_name: name of the city where the venue is located
            country: the city's country
            name: name of the venue
            result_page_num: the number of the result page you'd like to have
            state: the city's state
            state_code: the city's state code
        """
        path_url: str = "search/venues?"

        return self._get(
            url=path_url,
            cityId=city_id,
            cityName=city_name,
            country=country,
            name=name,
            p=result_page_num,
            state=state,
            stateCode=state_code,
        )

    def setlist_version(self, version_id: str):
        """
        Returns a setlist for the given versionId. The setlist returned isn't necessarily the most recent version.
        E.g. if you pass the versionId of a setlist that got edited since you last accessed it, you'll get the same
        version as last time.

        Args:
            version_id: Setlist version Id.
        """
        path_url: str = f"setlist/version/{version_id}?"

        return self._get(path_url)

    def setlist_by_id(self, setlist_id: str):
        """
        Returns the current version of a setlist. E.g. if you pass the id of a setlist that got edited since you last
        accessed it, you'll get the current version.

        Args:
            setlist_id: Setlist id.
        """
        path_url: str = f"setlist/{setlist_id}?"

        return self._get(path_url)

    def user(self, user_id: str):
        """
        Get a user by userId. (deprecated) Note: This endpoint always returns a result, even if the user doesn't exist

        Args:
            user_id: the user's userId
        """
        path_url: str = f"user/{user_id}?"

        return self._get(path_url)

    def user_attended(self, user_id: str, result_page_num: int = 1):
        """
        Get a list of setlists of concerts attended by a user.

        Args:
            user_id: the user's userId.
            result_page_num: the number of the result page.
        """

        path_url: str = f"user/{user_id}/attended?"

        return self._get(path_url, p=result_page_num)

    def user_edited(self, user_id: str, result_page_num: int = 1):
        """
        Get a list of setlists of concerts edited by a user. The list contains the current version, not the version
        edited.

        Args:
            user_id: the user's userId.
            result_page_num: the number of the result page.
        """
        path_url: str = f"user/{user_id}/edited?"

        return self._get(path_url, p=result_page_num)

    def venue(self, venue_id: str):
        """
        Get a venue by its unique id.

        Args:
            venue_id: the id of the venue
        """

        path_url: str = f"venue/{venue_id}?"

        return self._get(path_url)

    def setlists_for_venue(self, venue_id: str, result_page_num: int = 1):
        """
         Get setlists for a specific venue.

        Args:
            venue_id: the id of the venue
            result_page_num: the number of the result page.
        """
        path_url: str = f"venue/{venue_id}/setlists?"

        return self._get(path_url, p=result_page_num)

    def city(self, geo_id: str):
        """
        Get a city by its unique geoId.

        Args:
            geo_id: the city's geo id.
        """

        path_url: str = f"city/{geo_id}?"

        return self._get(path_url)

    def artist_for_musicbrainz_id(self, mbid: str):
        """
        Returns an artist for a given Musicbrainz MBID

        Args:
            mbid: a Musicbrainz MBID, e.g. 0bfba3d3-6a04-4779-bb0a-df07df5b0558
        """

        path_url: str = f"artist/{mbid}?"

        return self._get(path_url)

    def artist_setlists_for_musicbrainz_id(self, mbid: str, result_page_num: int = 1):
        """
        Get a list of an artist's setlists.

        Args:
            mbid: the Musicbrainz MBID of the artist
            result_page_num: the number of the result page
        """

        path_url: str = f"artist/{mbid}/setlists?"

        return self._get(path_url, p=result_page_num)