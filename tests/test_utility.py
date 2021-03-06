from xgpy.utility import Utility
from xgpy.constants_understat import PLAYER_URL, TEST_PLAYER_ID, TEST_PLAYER_URL, TEST_STR

class TestUtility():

    def test_generate_url_player(self):

        # assert that the url generated is as intended
        assert Utility.generate_request_url(PLAYER_URL, TEST_PLAYER_ID) == TEST_PLAYER_URL

    def test_generate_request_object(self):
        url = Utility.generate_request_url(PLAYER_URL, TEST_PLAYER_ID )

        # assert that the request went through well
        assert Utility.generate_request_object(url).status_code == 200

    def test_string_escape(self):

        # assert that the string conversion actually works
        assert Utility.string_escape(TEST_STR) == "{"
