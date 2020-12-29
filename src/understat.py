from Utility import Utility
from constants import *
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
        get xG data for the player in question.

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
        get the match data for the player.

        Returns
        -------
        json
            a json object contatining the information.

        """

        # First generate the URL from which data will be fetched
        # Next, generate a request object based on the URL
        # Finally, using regular expressions, finding the json
        # data using the keyword for the query

        base_url = Utility.generate_request_url(PLAYER_URL, self.id)
        r = Utility.generate_request_object(base_url)
        match = Utility.find_match(r, PLAYER_MATCHES_DATA)
        string_data = Utility.string_escape(match.group(1))

        # TODO: What if empty?
        json_data = json.loads(string_data)

        # TODO: need to add filtering params
        filtered_data = Utility.filter_data(json_data, **filter)

        return filtered_data
