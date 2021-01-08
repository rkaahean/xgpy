from xgpy.constants_fbref import *
from xgpy.Utility import Utility
from bs4 import BeautifulSoup
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

        # TODO: there seems to be something wrong with /all_comps/ endpoint
        # TODO: in all_comps endpoint, not able to fetch other than standard stats. commented out.
        # TODO: need to add error appropriate error handling when accessing dictionaries.
        # TODO: format the output data with column names and remove unncessary columns (matches)

        main_url = Utility.generate_request_url(PLAYER_URL, *(self.id, FBREF_COMPETITION_TO_URL_MAP[competition]))
        r = Utility.generate_request_object(main_url)
        print(main_url)

        if type not in FBREF_STATS_TO_CLASS_MAP.keys():
            raise ValueError('{} is not a valid stat type. Please refer to documentation for stat types.'.format(type))

        if competition not in FBREF_COMPETITION_TO_URL_MAP.keys():
            raise ValueError('{} is not a valid competition. Please refer to documentation for supported competitions.'.format(type))

        data = Utility.find_and_get_soup_table(r, FBREF_STATS_TO_CLASS_MAP[type], FBREF_COMPETITION_TO_URL_MAP[competition])
        df = pd.DataFrame(data)
        df.columns = df.iloc[0]
        df = df.drop(df.index[0])

        return df
