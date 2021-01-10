from xgpy.constants_understat import TEST_MATCH, TEST_FILTER, TEST_SEASON, TEST_LEAGUE
from xgpy.understat import UnderstatMatch

class TestUnderstatMatch():

    def test_get_match_shot_data(self):

        tp = UnderstatMatch(TEST_MATCH)
        data = tp.get_match_shot_data()

        assert isinstance(data, dict) and len(data) > 0

    def test_get_match_stats(self):

        tp = UnderstatMatch(TEST_MATCH)
        data = tp.get_match_stats()

        assert isinstance(data, dict) and len(data) > 0

    def test_get_match_roster(self):

        tp = UnderstatMatch(TEST_MATCH)
        data = tp.get_match_roster()

        assert isinstance(data, dict) and len(data) > 0
