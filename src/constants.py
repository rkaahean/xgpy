# MAIN URL's
PLAYER_URL = "https://understat.com/player/{}"

# Pattern of the JSON variables
DATA_PATTERN = "{}\s+=\s+JSON.parse\(\'(.*)\'\)"

# JSON_CONSTANTS: The variable names which prefix the data
PLAYER_MATCHES_DATA = "matchesData"

# Filter constants
ARG_SEASON = "season"
ARG_START_DATE = 'start_date'
ARG_END_DATE = 'end_date'
ARG_POSITION = 'position'

# Variables for testing
TEST_PLAYER_ID = 1228
TEST_PLAYER_URL = "https://understat.com/player/{}".format(TEST_PLAYER_ID)
