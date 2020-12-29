import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')

from Utility import Utility
from constants import PLAYER_URL, TEST_PLAYER_ID, TEST_PLAYER_URL

class TestUtility:

    def test_generate_url_player(self):

        # assert that the url generated is as intended
        assert Utility.generate_request_url(PLAYER_URL, TEST_PLAYER_ID) == TEST_PLAYER_URL

    def test_generate_request_object(self):
        url = Utility.generate_request_url(PLAYER_URL, TEST_PLAYER_ID)

        # assert that the request went through well
        assert Utility.generate_request_object(url).status_code == 200
