# JSON (JavaScript Object Notation) ---->

# Stores data as key-value pairs, similar to Python dictionaries.
# Great for nested and hierarchical data.
# Commonly used in APIs and web applications.

import json

with open("data.json", "r") as file:
    data = json.load(file)
print(data["name"])

with open("output.json", "w") as file:
    json.dump(data, file, indent=4)

