import requests
import re
from xgpy.constants_understat import DATA_PATTERN
from xgpy.constants_whoscored import WHOSCORED_DATA_PATTERN
import json
import pandas as pd
from bs4 import BeautifulSoup
from bs4 import Comment
import undetected_chromedriver as uc
uc.install()
from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options




class Utility():

    """
    A class comprising of all the helper functions.

    Methods
    -------
    generate_request_url(base_url, param)
        construct the URL to be queried.

    generate_request_object(url)
        generate a request object for the url specified.

    string_escape(s, encoding='utf-8')
        convert the string from given encoding (default utf-8) to human readable text.

    find_match(request, match_string)
        find a match in the request based on the match string provided.

    build_and_match(base_url, id, **filter)
        build and connect to the url and find desired data

    """


    @staticmethod
    def generate_request_url(base_url: str, *param: str):
        """
        Parameters
        ----------
        base_url: str
            the core understat url for the related endpoint. see constants.py for example.
        param: str
            value to format the string with (team or player id).

        Returns
        --------
        str
            a url string to fetch the data from.
        """
        return base_url.format(*param)


    @staticmethod
    def generate_selenium_object(url: str):

        """
        return the driver object based on the URL.
        """


        # create a headless chrome instance
        opts = uc.ChromeOptions()
        opts.headless=True
        opts.add_argument('--headless')
        opts.add_argument("--log-level=0")
        driver = uc.Chrome(options = opts)

        driver.get(url)

        return driver



    @staticmethod
    def generate_request_object(url: str):
        """
        Parameters
        ---------
        url: str
            the url to which a connection is to be made.

        Raises
        ------
        Exception
            A generic exception when a connection cannot be established.

        """

        try:
            return requests.get(url)
        except Exception:
            # TODO: Add a more detailed explanation
            print("An error occured")

    @staticmethod
    def string_escape(s, encoding='utf-8'):
        """
        Parameters
        ----------
        s: str
            the string to be decoded.
        encoding: str
            the encoding with which the string is to be converted.

        Returns
        -------
        str
            a human readable string

        """

        return (s.encode('latin1')         # To bytes, required by 'unicode-escape'
                # Perform the actual octal-escaping decode
                .decode('unicode-escape')
                .encode('latin1')         # 1:1 mapping back to bytes
                .decode(encoding))        # Decode original encoding

    @staticmethod
    def find_match(request, match_string: str, pattern = DATA_PATTERN, type = 'request'):
        """
        Parameters
        ----------
        request: object
            a request object that sucessfully connected to the desired URL.
        match_string: str
            the string used to find a match. Depends on the type of data being queried for. see constants.

        Returns
        -------
        Match
            returns a regex match object
        """

        match_pattern = re.compile(pattern.format(match_string))
        if type == "selenium":
            match = re.search(match_pattern, request.page_source)
        else:
            match = re.search(match_pattern, request.text)


        return match

    @staticmethod
    def build_and_match(base_url: str, search_keyword: str, *url_params: list):
        """
        Parameters
        ----------
        base_url: str
            the base_url from where information is to be queried.
        id: int
            the understat played_id.
        search_keyword: str
            the keyword search for the data to be fetched.

        Returns
        -------
        str:
            returns JSON data in a human readable format
        """

        base_url = Utility.generate_request_url(base_url, *url_params)
        print(base_url)
        r = Utility.generate_request_object(base_url)
        match = Utility.find_match(r, search_keyword)
        print(match)
        string_data = Utility.string_escape(match.group(1))

        return string_data

    @staticmethod
    def filter_data(json_data, **filter):
        """
        Parameters
        ----------
        base_url: str
            the base_url from where information is to be queried.
        id: int
            the understat played_id.
        search_keyword: str
            the keyword search for the data to be fetched.

        Returns
        -------
        str:
            returns JSON data in a human readable format
        """

        # TODO: need to convert filtering to a function
        season = filter.get('season', '')

        # if a filter exists, do something
        if season:
            json_data = [x for x in json_data if x['season'] == season]

        return json_data

    @staticmethod
    def get_and_clean_data(data):
        """
        get clean data by converting to dataframe

        :param data: a dictionary of raw data to be cleaned.
        :type data: dict

        :return: a dictionary of cleaned data.
        :rtype: dict
        """

        df = pd.DataFrame(data)

        # Make the columns the first row and
        # drop the first row
        df.columns = df.iloc[0]
        df = df.drop(df.index[0])

        # Drop the matches columns if it exists.
        df = df.drop(['matches', 'match_report'], axis='columns', errors='ignore')

        # drop empty columns for season based stats
        if 'date' in df.columns:
            df = df[df['date'] != ""]

        if 'opponent' in df.columns:
            df['opponent'] = df['opponent'].str.encode('utf-8')

        # reset index without new column
        df = df.reset_index(drop = True)

        # correct country values
        if 'country' in df.columns:
            df['country'] = pd.DataFrame(df['country'].str.split(' ').tolist()).iloc[:, -1].fillna('-')

        # TODO: Some columns (like minutes) need to be in numerical format
        df = df.apply(pd.to_numeric, errors='ignore')

        # return as a dictionary
        return df.to_dict()


    @staticmethod
    def find_and_get_soup_element(r, parameter_dict):

        soup = BeautifulSoup(r.text, 'html.parser')

        elem = soup.find_all(
            parameter_dict['find_elem'],
            attrs = {
                parameter_dict['arg_attr'] : parameter_dict['arg_value']
            }
        )

        data = {}

        for item in elem[parameter_dict['row_start']:]:

            a_item = item.find(parameter_dict['row_find'])
            key = a_item.text
            href_link = a_item[parameter_dict['row_find_inner']]

            value = href_link.split('/')[parameter_dict['href_elem']]

            data[key] = value

        return data



    @staticmethod
    def find_and_get_soup_table(r, mapped_type, mapped_competition='', return_header = False):
        """
        get the data based on a the stat and the competition

        :param mapped_type: the stat type converted into fbref format
        :type mapped_type: str
        :param mapped_competition: the competition converted into fbref format
        :type mapped_competition: str
        :param return_header: whether to return player_id's of player or not
        :type return_header: bool

        :return: specified stat data for competition of player
        :rtype: dict

        """

        soup = BeautifulSoup(r.text, 'html.parser')                     # Create bs4 html parser

        # When competition argument is not required
        if mapped_competition:
            attribute_key = '_'.join([mapped_type, mapped_competition])     # create the attribute which will be used to find our data
        else:
            attribute_key = mapped_type


        # if all_comps and not standard, then go through comments
        table = ''
        if mapped_competition == 'ks_expanded' and mapped_type != 'stats_standard':

            # Find all comments
            comments = soup.find_all(string=lambda text: isinstance(text, Comment))
            for c in comments:

                # find the table containing the attribute in comments
                soup = BeautifulSoup(c.extract(), 'html.parser')
                table = soup.find('table', attrs={
                    'id': attribute_key
                })
                if table:
                    break
        else:
            table = soup.find('table', attrs={
                'id': attribute_key
            })


        # in case data not present, raise error to double check arguments
        if not table:
            raise ValueError('Please enter a valid stat type and competition or check if stat exists at {}'.format(r.url))


        # find the header information
        # parse data-stat as they are more detailed
        data = []
        table_head = table.find('thead')

        row = table_head.find_all('tr')[-1]
        cols = row.find_all('th')
        cols = [ele["data-stat"].strip() for ele in cols]
        data.append([ele for ele in cols])

        # get body of table
        # iterate through the rows of the table.
        # append everything in a line to an array.
        # append the line to another array.
        table_body = table.find('tbody')

        rows = table_body.find_all('tr')

        # if you just want header details
        # used to get player names and their
        # corresponding id's

        # just do normal table extract
        if not return_header:
            for row in rows:
                cols = row.find_all([
                        'th',
                        'td'
                ])
                cols = [ele.text.strip() for ele in cols]
                data.append([ele for ele in cols])

        # extract player id's
        else:

            # resetting the data field to store dict
            data = {}
            for row in rows:
                th = row.find([
                        'th'
                ])

                href_link = th.find('a')['href']
                player_param = href_link.split('/')[3]
                data[th['data-append-csv']] = player_param

        return data
