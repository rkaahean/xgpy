from xgpy.constants_fbref import *
from xgpy.fbref import fbrefPlayer

class TestfbrefPlayer():

    def test_get_player_aggregate_stats(self):

        tp = fbrefPlayer(TEST_PLAYER_ID)
        for stat in FBREF_PLAYER_STATS_TO_CLASS_MAP.keys():

            data = tp.get_player_aggregate_stats(stat, 'all_competitions')
            assert (isinstance(data, dict) and len(data) > 0)
