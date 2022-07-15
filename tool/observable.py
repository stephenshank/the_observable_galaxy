import sys
import json


observable = {}
observable['notebook'] = sys.argv[1]
observable['history_id'] = sys.argv[2]
output_filename = sys.argv[3]
observable['payload_id'] = sys.argv[4]

keys = sys.argv[5::2]
vals = sys.argv[6::2]
for key, val in zip(keys, vals):
    observable[key] = val

print(', '.join(sys.argv))
with open(output_filename, 'w') as outfile:
    json.dump(observable, outfile, indent=2)
