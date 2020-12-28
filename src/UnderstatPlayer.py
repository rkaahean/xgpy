from bs4 import BeautifulSoup
import requests
import re
from constants import *
import json

class UnderstatPlayer():

    id = -1

    def __init__(self, player_id):
        self.id = player_id

    def get_player_match_data(self):
        r = requests.get(PLAYER_URL.format(self.id))

        soup = BeautifulSoup(r.text, 'html.parser')
        scripts = soup.find_all("script")

        def string_escape(s, encoding='utf-8'):
            return (s.encode('latin1')         # To bytes, required by 'unicode-escape'
                     .decode('unicode-escape') # Perform the actual octal-escaping decode
                     .encode('latin1')         # 1:1 mapping back to bytes
                     .decode(encoding))        # Decode original encoding

        data_pattern = re.compile(DATA_PATTERN.format(PLAYER_MATCHES_DATA))

        for script in scripts:
            match = re.search(data_pattern, str(script))
            if match:
                break

        return string_escape(match.group(1))
