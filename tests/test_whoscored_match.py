from xgpy.constants_whoscored import *
from xgpy.whoscored import whoMatch

class TestwhoMatch():

    def test_get_match_data(self):

        data = whoMatch(TEST_MATCH).get_match_data()
        assert isinstance(data, dict) and len(data) > 0
