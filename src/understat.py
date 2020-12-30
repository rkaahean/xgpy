from src.constants import *
from src.Utility import Utility
import json


class UnderstatPlayer():

    """
    A class that represents an understat football player logically.

    ...

    Attributes
    ----------
    id : int
        the id of the player instance in understat.

    Methods
    --------
    get_player_match_data()
        get xG data for the player.

    """

    id = -1

    def __init__(self, player_id):
        """
        Parameter
        ---------
        id : int
            the id of the player who's data is needed.
        """

        self.id = player_id

    def get_player_match_data(self, **filter):
        """
        get xG data for the player.

        Parameter
        ---------
        **filter: dict
            a dictionary of possible filters.

        Returns
        -------
        json
            a json object contatining the information.

        """
        # First generate the URL from which data will be fetched
        # Next, generate a request object based on the URL
        # Finally, using regular expressions, finding the json
        # data using the keyword for the query
        string_data = Utility.build_and_match(PLAYER_URL, self.id, PLAYER_MATCHES_DATA)

        # TODO: What if empty?
        json_data = json.loads(string_data)

        # TODO: need to convert filtering to a function
        season = filter.get('season', '')

        # if a filter exists, do something
        if season:
            json_data = [x for x in json_data if x['season'] == season]

        return json_data

    def get_player_grouped_data_by_type(self, type = 'season', **filter):

        """
        get the per season data for the player.
        Parameter
        ---------
        type: str
            the type of data to be fetched. see website for more information.

        **filter: dict
            a dictionary of possible filters.

        Returns
        -------
        json
            a json object contatining the information.

        """
        # First generate the URL from which data will be fetched
        # Next, generate a request object based on the URL
        # Finally, using regular expressions, finding the json
        # data using the keyword for the query
        string_data = Utility.build_and_match(PLAYER_URL, self.id, PLAYER_GROUPED_DATA)

        # TODO: What if empty?
        json_data = json.loads(string_data)

        # TODO: Add error handling here
        json_data = json_data[type]

        # TODO: need to convert filtering to a function
        season = filter.get('season', '')

        # if a filter exists, do something
        if season:
            json_data = [x for x in json_data if x['season'] == season]

        return json_data
