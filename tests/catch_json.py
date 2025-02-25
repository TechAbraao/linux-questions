from pprint import pprint
import json

data_json = "../db_files/data.json"

with open(data_json, 'r') as archive:
    data = json.load(archive)

pprint(data, width=40)