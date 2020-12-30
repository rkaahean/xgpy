from xgpy.constants import *
from xgpy.Utility import Utility
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
    get_player_match_data(**filter)
        get xG data for the player.

    get_player_grouped_data_by_type(type='season', filter)
        get grouped statistics of desired type.

    get_player_shot_data(**filter)
        get shot data.

    get_player_min_max_data(position, **filter)
        get min, max and average data for player.

    get_player_list_positions()
        get list of positions for the player.

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

        # TODO: filter data
        json_data = Utility.filter_data(json_data, **filter)

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

        # TODO: filter data
        json_data = Utility.filter_data(json_data, **filter)

        return json_data

    def get_player_shot_data(self, **filter):

        """
        get the shot data for the player.
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
        string_data = Utility.build_and_match(PLAYER_URL, self.id, PLAYER_SHOT_DATA)

        # TODO: What if empty?
        json_data = json.loads(string_data)

        # TODO: filter data
        json_data = Utility.filter_data(json_data, **filter)

        return json_data

    def get_player_min_max_data(self, position, **filter):

        """
        get the shot data for the player.
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
        string_data = Utility.build_and_match(PLAYER_URL, self.id, PLAYER_MIN_MAX_DATA)

        # TODO: What if empty?
        json_data = json.loads(string_data)

        # TODO: filter data
        json_data = Utility.filter_data(json_data, **filter)

        return json_data

    def get_player_list_positions(self):

        """
        get the possble player locations
        Parameter
        ---------
        **filter: dict
            a dictionary of possible filters.

        Returns
        -------
        json
            a json object contatining the information.

        """
        # TODO: currently, all possible positions (even GK for an outfield player) are being listed
        # would be better if we return just the positions played so far

        # First generate the URL from which data will be fetched
        # Next, generate a request object based on the URL
        # Finally, using regular expressions, finding the json
        # data using the keyword for the query
        string_data = Utility.build_and_match(PLAYER_URL, self.id, PLAYER_POSITIONS)

        # TODO: What if empty?
        json_data = json.loads(string_data)
        return json_data
