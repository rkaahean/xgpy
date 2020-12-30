import requests
import re
from xgpy.constants import *
import json


class Utility():

    """
    A class comprising of all the helper functions.

    Methods
    -------
    generate_request_url(base_url, param)
        construct the URL to be queried.

    generate_request_object(url)
        generate a request object for the url specified.

    string_escape(s, encoding='utf-8')
        convert the string from given encoding (default utf-8) to human readable text.

    find_match(request, match_string)
        find a match in the request based on the match string provided.

    build_and_match(base_url, id, **filter)
        build and connect to the url and find desired data

    """


    @staticmethod
    def generate_request_url(base_url: str, param: str):
        """
        Parameters
        ----------
        base_url: str
            the core understat url for the related endpoint. see constants.py for example.
        param: str
            value to format the string with (team or player id).

        Returns
        --------
        str
            a url string to fetch the data from.
        """
        return base_url.format(param)

    @staticmethod
    def generate_request_object(url: str):
        """
        Parameters
        ---------
        url: str
            the url to which a connection is to be made.

        Raises
        ------
        Exception
            A generic exception when a connection cannot be established.

        """

        try:
            return requests.get(url)
        except Exception:
            # TODO: Add a more detailed explanation
            print("An error occured")

    @staticmethod
    def string_escape(s, encoding='utf-8'):
        """
        Parameters
        ----------
        s: str
            the string to be decoded.
        encoding: str
            the encoding with which the string is to be converted.

        Returns
        -------
        str
            a human readable string

        """

        return (s.encode('latin1')         # To bytes, required by 'unicode-escape'
                # Perform the actual octal-escaping decode
                .decode('unicode-escape')
                .encode('latin1')         # 1:1 mapping back to bytes
                .decode(encoding))        # Decode original encoding

    @staticmethod
    def find_match(request, match_string: str):
        """
        Parameters
        ----------
        request: object
            a request object that sucessfully connected to the desired URL.
        match_string: str
            the string used to find a match. Depends on the type of data being queried for. see constants.

        Returns
        -------
        Match
            returns a regex match object
        """

        match_pattern = re.compile(DATA_PATTERN.format(match_string))
        match = re.search(match_pattern, request.text)

        return match

    @staticmethod
    def build_and_match(base_url: str, id: int, search_keyword: str):
        """
        Parameters
        ----------
        base_url: str
            the base_url from where information is to be queried.
        id: int
            the understat played_id.
        search_keyword: str
            the keyword search for the data to be fetched.

        Returns
        -------
        str:
            returns JSON data in a human readable format
        """

        base_url = Utility.generate_request_url(base_url, id)
        r = Utility.generate_request_object(base_url)
        match = Utility.find_match(r, search_keyword)
        string_data = Utility.string_escape(match.group(1))

        return string_data

    @staticmethod
    def filter_data(json_data, **filter):
        """
        Parameters
        ----------
        base_url: str
            the base_url from where information is to be queried.
        id: int
            the understat played_id.
        search_keyword: str
            the keyword search for the data to be fetched.

        Returns
        -------
        str:
            returns JSON data in a human readable format
        """

        # TODO: need to convert filtering to a function
        season = filter.get('season', '')

        # if a filter exists, do something
        if season:
            json_data = [x for x in json_data if x['season'] == season]

        return json_data
