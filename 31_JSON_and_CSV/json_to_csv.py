import json
import csv

# File paths
json_path = r"E:\Jyotsna\Python_Learning\31_JSON_and_CSV\JSON\data.json"
csv_path = r"E:\Jyotsna\Python_Learning\31_JSON_and_CSV\data.csv"

# Load JSON
with open(json_path, "r") as jf:
    data = json.load(jf)

# Write to CSV
with open(csv_path, "w", newline="", encoding="utf-8") as cf:
    writer = csv.writer(cf)

    # Flatten the 'skills' list into a semicolon-separated string
    row = {
        "name": data.get("name"),
        "age": data.get("age"),
        "skills": ";".join(data.get("skills", []))
    }

    # Write header and row
    writer.writerow(row.keys())
    writer.writerow(row.values())

print("JSON converted to CSV successfully!")
