import sys
import json
from csv import DictReader
from itertools import groupby


observable = {}
raw_notebook = sys.argv[1]
observable['notebook'] = raw_notebook.replace('@', '')
observable['history_id'] = sys.argv[2]
output_filename = sys.argv[3]
observable['payload_id'] = sys.argv[4]
full_base_url = sys.argv[5]
observable['base_url'] = full_base_url.replace('https://', '')

with open('individual.csv') as individual_file:
    individual_reader = DictReader(individual_file)
    for row in individual_reader:
        observable[row['key']] = {
            'dataset_id': row['dataset_id'],
            'extension': row['extension']
        }

key_function = lambda row: row['key']
with open('collection.csv') as collection_file:
    collection_reader = DictReader(collection_file)
    groups = groupby(collection_reader, key_function)
    for key, group in groups:
        observable[key] = []
        for element in group:
            element = dict(element)
            del element['key']
            observable[key].append(element)

with open(output_filename, 'w') as outfile:
    json.dump(observable, outfile, indent=2)
