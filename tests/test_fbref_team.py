from xgpy.constants_fbref import *
from xgpy.fbref import fbrefTeam

class TestfbrefPlayer():

    def test_get_player_aggregate_stats(self):

        tp = fbrefTeam(TEST_TEAM_ID)
        for stat in FBREF_TEAM_STATS_TO_URL_MAP.keys():

            # might need to add more competitions
            data = tp.get_team_aggregate_stats(TEST_SEASON, 'all_comps', stat)
            assert (isinstance(data, dict) and len(data) > 0)
