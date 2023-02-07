from pathlib import Path
import csv
import json
from json_builder import main



CSV_PATH = Path(__file__).parent / "NLP with Disaster Tweets.csv"
ROOT_PATH = "C:/Users/smarotta/Desktop/silvanus4.4 ann"
jsonFilePath = Path(__file__).parent / "NLP with Disaster Tweets.json"


def make_json(csvFilePath, jsonFilePath, primary_key: str):
    # create a dictionary
    data = {}

    # Open a csv reader called DictReader
    with open(csvFilePath, encoding='utf-8') as csvf:
        csvReader = csv.DictReader(csvf)

        # Convert each row into a dictionary
        # and add it to data
        for rows in csvReader:
            # Assuming a column named 'No' to
            # be the primary key
            key = rows[primary_key]
            data[key] = rows

    # Open a json writer, and use the json.dumps()
    # function to dump data
    with open(jsonFilePath, 'w', encoding='utf-8') as jsonf:
        jsonf.write(json.dumps(data, indent=4))


if __name__ == "__main__":
    # Call the make_json function
    make_json(CSV_PATH, jsonFilePath, "id")
    main(jsonFilePath, text_key="text")