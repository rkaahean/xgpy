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

# Filter constants
ARG_SEASON = "season"
ARG_START_DATE = 'start_date'
ARG_END_DATE = 'end_date'
ARG_POSITION = 'position'

# Variables for testing
TEST_FILTER = {
    "season": '2020',
}
TEST_PLAYER_ID = 1228
TEST_PLAYER_URL = "https://understat.com/player/{}".format(TEST_PLAYER_ID)
