# MAIN URL's
PLAYER_URL = "https://understat.com/player/{}"

# Pattern of the JSON variables
DATA_PATTERN = "{}\s+=\s+JSON.parse\(\'(.*)\'\)"

# JSON_CONSTANTS: The variable names which prefix the data
PLAYER_MATCHES_DATA = "matchesData"

# Variables for testing
TEST_PLAYER_ID = 1228
TEST_PLAYER_URL = "https://understat.com/player/{}".format(TEST_PLAYER_ID)
