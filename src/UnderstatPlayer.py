from bs4 import BeautifulSoup
import requests
import re
from constants import *
import json
from Utility import Utility

class UnderstatPlayer():

    id = -1

    def __init__(self, player_id):
        self.id = player_id

    def get_player_match_data(self):

        base_url = Utility().generate_request_url(PLAYER_URL, self.id)
        r = Utility().generate_request_object(base_url)
        match = Utility().find_match(r, PLAYER_MATCHES_DATA)

        return Utility.string_escape(match.group(1))
