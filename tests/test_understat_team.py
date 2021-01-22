from xgpy.constants_understat import TEST_TEAM, TEST_LEAGUE, TEST_SEASON
from xgpy.understat import UnderstatTeam

class TestUnderstatTeam():

    def test_get_team_league_history(self):

        # test that the data received is of type dictionary and not empty

        tp = UnderstatTeam(TEST_TEAM, TEST_LEAGUE)
        data = tp.get_team_league_history(TEST_SEASON)

        assert isinstance(data, dict) and len(data) > 0

    def test_get_team_player_summary(self):

        # test that the data received is of type dictionary and not empty

        tp = UnderstatTeam(TEST_TEAM, TEST_LEAGUE)
        data = tp.get_team_player_summary(TEST_SEASON)

        assert isinstance(data, list) and len(data) > 0

    def test_get_team_player_summary(self):

        # test that the data received is of type dictionary and not empty

        tp = UnderstatTeam(TEST_TEAM, TEST_LEAGUE)
        data = tp.get_team_fixtures(TEST_SEASON)

        assert isinstance(data, list) and len(data) > 0

    def test_get_team_player_summary(self):

        # test that the data received is of type dictionary and not empty

        tp = UnderstatTeam(TEST_TEAM, TEST_LEAGUE)
        data = tp.get_team_grouped_date_by_type(TEST_SEASON)

        assert isinstance(data, dict) and len(data) > 0


    def test_get_team_league_table(self):

        # test that the data received is of type dictionary and not empty

        tp = UnderstatTeam(TEST_TEAM, TEST_LEAGUE)
        data = tp.get_team_league_table(TEST_SEASON)

        assert isinstance(data, dict) and len(data) > 0
