import csv
import json

# Open the CSV file
with open("data.csv", "r") as file:
    reader = csv.DictReader(file)
    rows = list(reader)

# Write the JSON file
with open("data.json", "w") as file:
    file.write(json.dumps(rows, indent=4))
