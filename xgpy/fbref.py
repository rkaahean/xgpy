from xgpy.constants_fbref import *
from xgpy.Utility import Utility
from bs4 import BeautifulSoup
import json
import pandas as pd

class fbrefPlayer():

    """
    A class dedicated to fetch information about a player
    from fbref.

    """

    def __init__(self, player_id):

        # store the player id
        self.id = player_id

    def get_player_aggregate_stats(self, type, competition='dom_lg'):

        main_url = Utility.generate_request_url(PLAYER_URL, *(self.id, FBREF_COMPETITION_TO_URL_MAP[competition]))
        r = Utility.generate_request_object(main_url)
        print(main_url)
        soup = BeautifulSoup(r.text, 'html.parser')

        data = []
        ky = '_'.join([FBREF_STATS_TO_CLASS_MAP[type], FBREF_COMPETITION_TO_KEY_MAP[competition]])

        print(ky)
        table = soup.find('table', attrs={'id':ky})
        table_body = table.find('tbody')

        rows = table_body.find_all('tr')
        for row in rows:
            cols = row.find_all([
                'th',
                'td'
            ])
            cols = [ele.text.strip() for ele in cols]
            data.append([ele for ele in cols])

        return data
