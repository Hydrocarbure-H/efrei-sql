import json
import csv
import pprint


def extract_data():
    """Extract data from a csv file and convert it to a json file."""

    # read the json file
    with open('files/test.json', 'r') as json_file:
        data = json.load(json_file)
        pprint.pprint(data)

    return data
