from xgpy.constants_fbref import *
from xgpy.utility import Utility
from bs4 import BeautifulSoup

class fbrefPlayer():

    """
    A class dedicated to fetch information about a player
    from fbref.

    :param player_id: the id of the player the class is based on
    :type player_id: str
    """

    def __init__(self, player_id):

        # store the player id
        self.id = player_id

    def get_player_aggregate_stats(self, type, competition='dom_lg'):

        """
        get aggregate career statistics of player.

        :param type: this is the type of statistics that are to be fetched.
            Possible values:
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
        :param competition: the competition for which stats are to be fetched.
            Possible values:
                - all_competitions
                - domestic_league
                - domestic_cup
                - internationl_cup
                - national_team
        :type competition: str
        :return: the aggregate career statistics for the given league and stat type
        :rtype: dict
        """

        # get request object
        main_url = Utility.generate_request_url(PLAYER_MAIN_URL, *(self.id, FBREF_COMPETITION_TO_URL_MAP[competition]))
        r = Utility.generate_request_object(main_url)

        # Check for two things
        # 1. If competition passed is valid
        # 2. If stat passed is valid
        if type not in FBREF_PLAYER_STATS_TO_CLASS_MAP.keys():
            raise ValueError('{} is not a valid stat type. Please refer to documentation for supported stat types.'.format(type))

        if competition not in FBREF_COMPETITION_TO_URL_MAP.keys():
            raise ValueError('{} is not a valid competition. Please refer to documentation for supported competitions.'.format(competition))

        # Get the data as a raw dictionary
        data = Utility.find_and_get_soup_table(r, FBREF_PLAYER_STATS_TO_CLASS_MAP[type], FBREF_COMPETITION_TO_KEY_MAP[competition])

        # clean the data
        cleaned_data = Utility.get_and_clean_data(data)
        return cleaned_data


    def get_player_season_stats(self, type, season):

        """
        get statistics for a particular season of a player.

        :param type: this is the type of statistics that are to be fetched.
            Possible values:
                - summary
                - passing
                - passing_types
                - gca (Goal and Shot Creation)
                - defense (Defensive Actions)
                - possession
                - misc
        :type type: str
        :param season: the season for which data is needed. For the 2020/21 season, enter 2020.
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

class fbrefTeam():

    """
    A class dedicated to fetch information about a team
    from fbref.

    :param team_id: the id of the team the class is based on
    :type team_id: str
    """

    def __init__(self, team_id):
        self.id = team_id

    def get_team_competition_names(self, season):
        """
        get the competitions which team is involved in for a given season

        :param season: the season for which data is needed. For the 2020/21 season, enter 2020.
        :type season: int

        :return: the competition name and corresponding ID's
        :rtype: dict
        """

        # Build and connect to the URL for teams
        season_param = str(season) + '-' + str(season + 1)
        main_url = Utility.generate_request_url(TEAM_MAIN_URL, *(self.id, season_param))
        r = Utility.generate_request_object(main_url)

        # Get the list element that has information about competitions
        soup = BeautifulSoup(r.text, 'html.parser')
        ul_elem = soup.find('ul', attrs = {
            'class': ""
        })

        # iterate through all rows in a list
        # get the competition id from the href in list and
        # corresponding competition name
        li_elem = ul_elem.find_all("li")
        link_to_name = {}
        for link in li_elem:
            href_link = link.find('a')['href']
            comp_param = href_link.split('/')[5]
            link_to_name[link.text.strip()] = comp_param

        return link_to_name

    def get_team_aggregate_stats(self, season, comp_id, type='scores_and_fixtures'):

        """
        get the statistics of team in a given season and competition.

        :param season: the season for which data is needed. For the 2020/21 season, enter 2020.
        :type season: int
        :param comp_id: the id of the competition for which data is required. to get appropriate competition_id's
        use the get_team_competition_names for a given season.
        :type comp_id: str

        :return: the competition name and corresponding ID's
        :rtype: dict
        """

        # TODO: What if competition does not exist?
        # TODO: error handling for stat type

        # Connect to the appropriate team, competition, season and stat type
        season_param = str(season) + '-' + str(season + 1)
        main_url = Utility.generate_request_url(TEAM_COMP_STAT_URL,
                                                *(self.id, season_param, comp_id, FBREF_TEAM_STATS_TO_URL_MAP[type]))
        r = Utility.generate_request_object(main_url)

        # Stupid fbref. The id for the class depends on the competition.
        # so if it is all comps, then it is the standard constant.
        # if not, the numerical part of the competition id is appended.
        class_param = 'matchlogs_'
        if comp_id != 'all_comps':
            class_param += comp_id[1:]
        else:
            class_param = TEAM_SEASON_TABLE_ID

        data = Utility.find_and_get_soup_table(r, class_param)
        cleaned_data = Utility.get_and_clean_data(data)
        
        return cleaned_data
