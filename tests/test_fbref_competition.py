from xgpy.constants_fbref import *
from xgpy.fbref import fbrefCompetition

class TestfbrefCompetition():

    def test_get_competition_names(self):

        data = fbrefCompetition.get_competition_names()
        assert (isinstance(data, dict) and len(data) > 0)
