# Main URL's to fetch data
PLAYER_MAIN_URL = 'https://fbref.com/en/players/{}/{}/'
PLAYER_SEASON_URL = 'https://fbref.com/en/players/{}/matchlogs/{}/{}/'


# statistics class mapping
FBREF_STATS_TO_CLASS_MAP = {
    'standard': 'stats_standard',
    'shooting': 'stats_shooting',
    'passing':  'stats_passing',
    'passing_types': 'stats_passing_types',
    'goal_shot_creation': 'stats_gca',
    'defensive_actions': 'stats_defense',
    'possession': 'stats_possession',
    'playing_time': 'stats_playing_time',
    'miscellaneous': 'stats_misc'
}

# This is used to generate the competition
# part of the class id from which data is to be identified
FBREF_COMPETITION_TO_KEY_MAP = {
    'all_competitions': 'ks_expanded',
    'all_competitions_collapsed': 'ks_collapsed',
    'domestic_league': 'dom_lg',
    'domestic_cup': 'dom_cup',
    'internationl_cup': 'intl_cup',
    'national_team': 'nat_tm'
}

# This is used to convert the competition
# argument into a parameter for the URL
FBREF_COMPETITION_TO_URL_MAP = {
    'all_competitions': 'all_comps',
    'all_competitions_collapsed': 'all_comps',
    'domestic_league': 'dom_lg',
    'domestic_cup': 'dom_cup',
    'internationl_cup': 'intl_cup',
    'national_team': 'nat_tm'
}

# Main Class ID's
PLAYER_SEASON_TABLE_ID = "matchlogs_all"

# Testing constants
TEST_PLAYER_ID = '507c7bdf'
