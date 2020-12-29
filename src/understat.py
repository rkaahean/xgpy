from src.Utility import Utility
from src.constants import *

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
        --------
        id : int
            the id of the player who's data is needed.
        """

        self.id = player_id

    def get_player_match_data(self):
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

        base_url = Utility().generate_request_url(PLAYER_URL, self.id)
        r = Utility().generate_request_object(base_url)
        match = Utility().find_match(r, PLAYER_MATCHES_DATA)

        # TODO: need to add filtering params

        return Utility.string_escape(match.group(1))
