from UnderstatPlayer import UnderstatPlayer
from bs4 import BeautifulSoup
import requests
import re
from constants import *
import json
# from Utility import Utility

a = UnderstatPlayer(1228)

# def string_escape(s, encoding='utf-8'):
#     return (s.encode('latin1')         # To bytes, required by 'unicode-escape'
#              .decode('unicode-escape') # Perform the actual octal-escaping decode
#              .encode('latin1')         # 1:1 mapping back to bytes
#              .decode(encoding))        # Decode original encoding
#
#
# r = requests.get('https://understat.com/player/1228')
# soup = BeautifulSoup(r.text, 'html.parser')
# scripts = soup.find_all("script")
#
# data_pattern = re.compile(DATA_PATTERN.format(PLAYER_MATCHES_DATA))
#
# for script in scripts:
#     match = re.search(data_pattern, str(script))
#     if match:
#         break
#
# print(string_escape(match.group(1)))
print(a.get_player_match_data())
# Utility.generate_request_object(Utility.generate_request_url(PLAYER_URL, 1228))
