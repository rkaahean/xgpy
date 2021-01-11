from xgpy.constants_fbref import *
from xgpy.utility import Utility

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
        :return: the aggregate career statistics for the given league and stat type
        :rtype: dict
        """

        # get request object
        main_url = Utility.generate_request_url(PLAYER_MAIN_URL, *(self.id, FBREF_COMPETITION_TO_URL_MAP[competition]))
        r = Utility.generate_request_object(main_url)

        # Check for two things
        # 1. If competition passed is valid
        # 2. If stat passed is valid
        if type not in FBREF_STATS_TO_CLASS_MAP.keys():
            raise ValueError('{} is not a valid stat type. Please refer to documentation for supported stat types.'.format(type))

        if competition not in FBREF_COMPETITION_TO_URL_MAP.keys():
            raise ValueError('{} is not a valid competition. Please refer to documentation for supported competitions.'.format(competition))

        # Get the data as a raw dictionary
        data = Utility.find_and_get_soup_table(r, FBREF_STATS_TO_CLASS_MAP[type], FBREF_COMPETITION_TO_KEY_MAP[competition])

        # clean the data
        cleaned_data = Utility.get_and_clean_data(data)
        return cleaned_data


    def get_player_season_stats(self, type, season):

        """
        get statistics for a particular season of a player.

        :param type: this is the type of statistics that are to be fetched. possible values:
            - summary
            - passing
            - passing_types
            - gca (Goal and Shot Creation)
            - defense (Defensive Actions)
            - possession
            - misc
        :type type: str
        :param season: The season for which data is needed. For the 2020/21 season, enter 2020
        :type season: int

        :return: the given season's and stat type of the player
        :rtype: dict
        """

        # Just ignore competition filter. It should not be hard
        # to filter rows once you have data. It's not a lot given its
        # only a season's worth anyways

        season_param = str(season) + '-' + str(season + 1)
        main_url = Utility.generate_request_url(PLAYER_SEASON_URL, *(self.id, season_param, type))
        r = Utility.generate_request_object(main_url)

        # Check for two things
        # 1. If competition passed is valid
        # 2. If stat passed is valid
        # if type not in FBREF_STATS_TO_CLASS_MAP.keys():
        #     raise ValueError('{} is not a valid stat type. Please refer to documentation for supported stat types.'.format(type))

        # Get the data as a raw dictionary
        data = Utility.find_and_get_soup_table(r, PLAYER_SEASON_TABLE_ID)

        # clean the data
        cleaned_data = Utility.get_and_clean_data(data)
        return cleaned_data
