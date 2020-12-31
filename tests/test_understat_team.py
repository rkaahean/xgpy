from xgpy.constants import TEST_TEAM, TEST_LEAGUE, TEST_SEASON
from xgpy.understat import UnderstatTeam

class TestUnderstatTeam():

    def test_get_team_league_history(self):
        tp = UnderstatTeam(TEST_TEAM, TEST_LEAGUE)
        data = tp.get_team_league_history(TEST_SEASON)

        assert isinstance(data, dict) and len(data) > 0
