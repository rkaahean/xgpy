from xgpy.constants import *
from xgpy.Utility import Utility
import json
import pandas as pd


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
        string_data = Utility.build_and_match(PLAYER_URL, PLAYER_MATCHES_DATA, self.id)

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
        string_data = Utility.build_and_match(PLAYER_URL, PLAYER_GROUPED_DATA, self.id)

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
        string_data = Utility.build_and_match(PLAYER_URL, PLAYER_SHOT_DATA, self.id)

        # TODO: What if empty?
        json_data = json.loads(string_data)

        # TODO: filter data
        json_data = Utility.filter_data(json_data, **filter)

        return json_data

    def get_player_min_max_data(self, **filter):

        """
        get the min, max and average data for the player.

        :param \*\*filter: a dictionary of possible filters.
        :type \*\*filter: dict
        :return: min max data of the player
        :rtype: list
        """

        # First generate the URL from which data will be fetched
        # Next, generate a request object based on the URL
        # Finally, using regular expressions, finding the json
        # data using the keyword for the query
        string_data = Utility.build_and_match(PLAYER_URL, PLAYER_MIN_MAX_DATA, self.id)

        # TODO: What if empty?
        json_data = json.loads(string_data)

        # TODO: filter data
        json_data = Utility.filter_data(json_data, **filter)

        return json_data

    def get_player_positions(self, **filter):

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
        string_data = Utility.build_and_match(PLAYER_URL, PLAYER_POSITIONS, self.id)

        # TODO: What if empty?
        json_data = json.loads(string_data)

        json_data = Utility.filter_data(json_data, **filter)
        return json_data

    @staticmethod
    def get_player_list_by_league(league, season):

        """
        get all possible players in a league.

        :param league: the league for which the data is to be fetched. multiple values can be passed seperated by a ',' .
            possible values:
                - EPL
                - La_Liga
                - Bundesliga
                - Serie_A
                - Ligue_1
                - RFPL
        :type league: str
        :param season: season for which data is needed. For 2020/21 season, enter 2020.
        :type season int:
        :return: players in the league listed.
        :rtype: dict
        """

        # TODO: there seems to be an issue with certain player names
        # special characters mess up

        # get all parameters seperately. clean any dangling whitespaces.
        all_leagues = [x.strip() for x in league.split(',')]

        # get data for every league. get only select parameters.
        # append league name. concat all leagues and return as dict
        data = []
        for league in all_leagues:
            json_data = Utility.build_and_match(LEAGUE_URL, PLAYER_LIST_DATA, *(league, season))
            clean_data = pd.DataFrame(eval(json_data)).loc[:, PLAYER_DATA_COLUMNS]
            clean_data['league'] = league

            data += [clean_data]

        return pd.concat(data).to_dict()


class UnderstatTeam():
    """
    A class to get data based on a team.

    """
    def __init__(self, team_name, league):
        self.team_name = team_name
        self.league = league

    def get_team_league_history(self, season, **filter):

        """
        get the league history for a given team

        :param season: season for which history is needed. For 2020/2021 season, input 2020.
        :type season: str
        :return: dictionary containing the data for matches played in given season
        :rtype: dict
        """

        string_data = Utility.build_and_match(LEAGUE_URL, TEAMS_STANDINGS_DATA, *(self.league, season))
        json_data = json.loads(string_data)

        json_data = Utility.filter_data(json_data, **filter)

        # get data only for the team instance
        for key in json_data.keys():
            if json_data[key]["title"] == ' '.join(self.team_name.split('_')):
                return json_data[key]

    def get_team_player_summary(self, season, **filter):

        """
        get the summary statistics for each player of the team for a given season.

        :param season: season for which history is needed. For 2020/2021 season, input 2020.
        :type season: str
        :return: list containing summary statistics of players
        :rtype: list
        """

        string_data = Utility.build_and_match(TEAM_URL, PLAYER_LIST_DATA, *(self.team_name, season))
        json_data = json.loads(string_data)

        json_data = Utility.filter_data(json_data, **filter)
        return json_data

    def get_team_fixtures(self, season, **filter):

        """
        get the team fixtures for given season. for the fixtures that have been played, basic stats
        are included.

        :param season: season for which fixtures are needed. For 2020/2021 season, input 2020.
        :type season: str
        :return: list containing fixtures
        :rtype: list

        """

        string_data = Utility.build_and_match(TEAM_URL, TEAMS_FIXTURES_DATA, *(self.team_name, season))
        json_data = json.loads(string_data)

        json_data = Utility.filter_data(json_data, **filter)
        return json_data

    def get_team_grouped_date_by_type(self, season, type='situation', **filter):

        """
        get the per season data for the team.

        :param season: season for which fixtures are needed. For 2020/2021 season, input 2020.
        :type season: str
        :param type: the type of data to be fetched. This can be one of the following:
            - situation
            - formation
            - gameState
            - timing
            - shotZone
            - attackSpeed
        :type type: str
        :return: dictionary containing fixtures
        :rtype: dict
        """

        string_data = Utility.build_and_match(TEAM_URL, TEAMS_GROUPED_DATA, *(self.team_name, season))
        json_data = json.loads(string_data)

        json_data = Utility.filter_data(json_data, **filter)
        return json_data

class UnderstatMatch():

    """
    A class to model a match between two teams and obatin information.
    """

    def __init__(self, match_id):
        self.id = match_id

    def get_match_shot_data(self):

        """
        get the shot data for the match.

        :return: list containing shot data for the match
        :rtype: list
        """

        string_data = Utility.build_and_match(MATCH_URL, MATCH_SHOT_DATA, self.id)
        json_data = json.loads(string_data)

        return json_data
