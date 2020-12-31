#test output of get_player_match_data. See if all the headers are all right. See if the data received is not empty.
from xgpy.constants import TEST_PLAYER_ID, TEST_FILTER
from xgpy.understat import UnderstatPlayer


class TestUnderstatPlayer():

    def test_get_player_match_data(self):

        tp = UnderstatPlayer(TEST_PLAYER_ID)
        data = tp.get_player_match_data(**TEST_FILTER)

        assert isinstance(data, list) and len(data) > 0

    def test_get_player_shot_data(self):

        tp = UnderstatPlayer(TEST_PLAYER_ID)
        data = tp.get_player_shot_data(**TEST_FILTER)

        assert isinstance(data, list) and len(data) > 0

    def test_get_player_grouped_data_by_type(self):

        tp = UnderstatPlayer(TEST_PLAYER_ID)
        data = tp.get_player_grouped_data_by_type(**TEST_FILTER)

        assert isinstance(data, list) and len(data) > 0

    def test_get_player_min_max_data(self):

        tp = UnderstatPlayer(TEST_PLAYER_ID)
        data = tp.get_player_min_max_data()

        assert isinstance(data, dict) and len(data) > 0
