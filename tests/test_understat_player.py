#test output of get_player_match_data. See if all the headers are all right. See if the data received is not empty.

class TestUnderstat():

    def test_get_player_match_data(self):
        from src.constants import TEST_PLAYER_ID, TEST_FILTER
        from src.understat import UnderstatPlayer

        tp = UnderstatPlayer(TEST_PLAYER_ID)
        data = tp.get_player_match_data(**TEST_FILTER)

        assert isinstance(data, list) and len(data) > 0
