import json
import os

# Paths for JSON files
CONFIG_PATH = os.path.join(os.path.dirname(__file__), "config.json")
TESTDATA_PATH = os.path.join(os.path.dirname(__file__), "testdata.json")

# Load Configuration
with open(CONFIG_PATH, "r") as config_file:
    config = json.load(config_file)

# Load Test Data
with open(TESTDATA_PATH, "r") as testdata_file:
    testdata = json.load(testdata_file)
