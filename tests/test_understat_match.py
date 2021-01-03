from xgpy.constants import TEST_MATCH, TEST_FILTER, TEST_SEASON, TEST_LEAGUE
from xgpy.understat import UnderstatMatch

class TestUnderstatMatch():

    def test_get_match_shot_data(self):

        tp = UnderstatMatch(TEST_MATCH)
        data = tp.get_match_shot_data()

        assert isinstance(data, dict) and len(data) > 0
