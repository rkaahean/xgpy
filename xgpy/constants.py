# MAIN URL's
PLAYER_URL = "https://understat.com/player/{}"
LEAGUE_URL = "https://understat.com/league/{}/{}/"

# Pattern of the JSON variables
DATA_PATTERN = r"{}\s+=\s+JSON.parse\(\'(.*)\'\)"

# JSON_CONSTANTS: The variable names which prefix the data
PLAYER_MATCHES_DATA = "matchesData"
PLAYER_GROUPED_DATA = "groupsData"
PLAYER_SHOT_DATA = "shotsData"
PLAYER_MIN_MAX_DATA = "minMaxPlayerStats"
PLAYER_POSITIONS = "positionsList"
PLAYER_LIST_DATA = "playersData"
TEAMS_STANDINGS_DATA = "teamsData"

# Filter constants
ARG_SEASON = "season"
ARG_START_DATE = 'start_date'
ARG_END_DATE = 'end_date'
ARG_POSITION = 'position'
PLAYER_DATA_COLUMNS = [  # for get_player_list_by_league
        'id',
        'player_name',
        'team_title'
    ]

# Variables for testing
TEST_FILTER = {
    "season": '2020',
}
TEST_PLAYER_ID = 1228
TEST_PLAYER_URL = "https://understat.com/player/{}".format(TEST_PLAYER_ID)
TEST_SEASON = 2020
TEST_LEAGUE = 'EPL'
TEST_TEAM = 'Manchester_United'
