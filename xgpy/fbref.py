from xgpy.constants_fbref import *
from xgpy.utility import Utility
import json
import pandas as pd

class fbrefPlayer():

    """
    A class dedicated to fetch information about a player
    from fbref.

    """

    def __init__(self, player_id):

        # store the player id
        self.id = player_id

    def get_player_aggregate_stats(self, type, competition='dom_lg'):

        """
        get aggregate career statistics of player.

        :param type: this is the type of statistics that are to be fetched. possible values:
            - standard
            - shooting
            - passing
            - passing_types
            - goal_shot_creation
            - defensive_actions
            - possession
            - playing_time
            - miscellaneous
        :type type: str
        :param competition: the competition for which stats are to be fetched. possible values:
            - all_competitions
            - domestic_league
            - domestic_cup
            - internationl_cup
            - national_team
        """


        # TODO: add option for collapsed in all_comps

        # get request object
        main_url = Utility.generate_request_url(PLAYER_URL, *(self.id, FBREF_COMPETITION_TO_URL_MAP[competition]))
        r = Utility.generate_request_object(main_url)

        # Check for two things
        # 1. If competition passed is valid
        # 2. If stat passed is valid
        if type not in FBREF_STATS_TO_CLASS_MAP.keys():
            raise ValueError('{} is not a valid stat type. Please refer to documentation for supported stat types.'.format(type))

        if competition not in FBREF_COMPETITION_TO_URL_MAP.keys():
            raise ValueError('{} is not a valid competition. Please refer to documentation for supported competitions.'.format(type))

        # Get the data as a raw dictionary
        data = Utility.find_and_get_soup_table(r, FBREF_STATS_TO_CLASS_MAP[type], FBREF_COMPETITION_TO_KEY_MAP[competition])

        # clean the data
        cleaned_data = Utility.get_and_clean_data(data)
        return cleaned_data
