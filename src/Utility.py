from bs4 import BeautifulSoup
import requests
import re
from .constants import *
import json

class Utility():

    @staticmethod
    def generate_request_url(base_url: str, param: str):
        return base_url.format(param)

    @staticmethod
    def generate_request_object(url: str):
        try:
            return requests.get(url)
        except Exception:
            print("An error occured")

    @staticmethod
    def string_escape(s, encoding='utf-8'):
        return (s.encode('latin1')         # To bytes, required by 'unicode-escape'
                 .decode('unicode-escape') # Perform the actual octal-escaping decode
                 .encode('latin1')         # 1:1 mapping back to bytes
                 .decode(encoding))        # Decode original encoding

    @staticmethod
    def find_match(request, DATA_CONSTANT:str):

        soup = BeautifulSoup(request.text, "html.parser")
        scripts = soup.find_all("script")

        match_pattern = re.compile(DATA_PATTERN.format(DATA_CONSTANT))

        for script in scripts:
            match = re.search(match_pattern, str(script))
            if match:
                break

        return match
