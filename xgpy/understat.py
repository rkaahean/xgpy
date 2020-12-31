from xgpy.constants import *
from xgpy.Utility import Utility
import json


class UnderstatPlayer():

    """
    A class that represents an understat football player logically.

    Attributes
    ----------
    id : int
        the id of the player instance in understat.

    """

    def __init__(self, player_id):

        """
        intializer for the UnderstatPlayer class.

        :param id: the id of the player who's data is needed.
        :type id: int
        """

        self.id = player_id

    def get_player_match_data(self, **filter):

        """
        get xG data for the player.

        :param \*\*filter: a dictionary of possible filters.
        :type \*\*filter: dict
        :return: match data of the player
        :rtype: list
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

        :param type: the type of data to be fetched.
        :type type: str
        :param \*\*filter: a dictionary of possible filters.
        :type \*\*filter: dict
        :return: match data of the player
        :rtype: list
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

        :param \*\*filter: a dictionary of possible filters.
        :type \*\*filter: dict
        :return: shot data of the player
        :rtype: list
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
        get the min, max and average data for the player.

        :param position: the type of data to be fetched.
        :type position: str
        :param \*\*filter: a dictionary of possible filters.
        :type \*\*filter: dict
        :return: min max data of the player
        :rtype: list
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

        :return: list of positions of the player
        :rtype: list
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


class UnderstatTeam():
    """

    """
    def __init__(self):
        print("hello team")
