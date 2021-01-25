from xgpy.constants_whoscored import *
from xgpy.utility import Utility
import json


class whoMatch():

    """
    a class to get match related data for whoscored.

    :param match_id: id of the match for which data is required.
    :type match_id: str
    """

    def __init__(self, match_id):

        self.id = match_id

    def get_match_data(self):

        """
        get match related data based on filters
        """

        base_url = Utility.generate_request_url(MATCH_LIVE_URL, self.id)
        s = Utility.generate_selenium_object(base_url)

        # using selenium
        match = Utility.find_match(s, MATCH_EVENT_DATA, WHOSCORED_DATA_PATTERN, "selenium")
        string_data = match.group(1)

        json_data = json.loads(string_data[:-1])

        return json_data
