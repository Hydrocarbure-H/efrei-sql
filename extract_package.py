import json


def extract_data():
    """Extract data from a csv file and convert it to a json file."""

    # read the json file and check if the file exists
    try:
        with open('files/test.json', 'r') as json_file:
            data = json.load(json_file)
    except FileNotFoundError:
        print("File not found")

    return data
