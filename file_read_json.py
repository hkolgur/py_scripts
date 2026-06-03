"""Read contents of JSON file and write them to console"""

import json

# Read contents of existing Json file. load takes file pointer. loads takes string
with open("file_input.json", "r") as fp:
    data = json.load(fp)
for k, v in data.items():
    print(k, v)

json_string = '{"name": "Alice", "is_active": true}'

# Pass the string directly to json.loads()
data = json.loads(json_string)
print(data["name"])  # Output: Alice
