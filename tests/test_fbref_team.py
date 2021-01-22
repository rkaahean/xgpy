from xgpy.constants_fbref import *
from xgpy.fbref import fbrefTeam

class TestfbrefPlayer():

    def test_get_team_aggregate_stats(self):

        tp = fbrefTeam(TEST_TEAM_ID)
        for stat in FBREF_TEAM_STATS_TO_URL_MAP.keys():

            # might need to add more competitions
            data = tp.get_team_aggregate_stats(TEST_SEASON, 'all_comps', stat)
            assert (isinstance(data, dict) and len(data) > 0)

    def test_get_team_competition_names(self):

        tp = fbrefTeam(TEST_TEAM_ID)

        data = tp.get_team_competition_names(TEST_SEASON)
        assert (isinstance(data, dict) and len(data) > 0)

    def test_get_team_player_ids(self):

        tp = fbrefTeam(TEST_TEAM_ID)

        data = tp.get_team_player_ids(TEST_SEASON)
        assert (isinstance(data, dict) and len(data) > 0)
