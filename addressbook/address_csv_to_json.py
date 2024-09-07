import csv
import json

def csv_to_json(csv_file_path, json_file_path):
    # Read the CSV and add data to a dictionary
    data = []
    with open(csv_file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data.append(row)

    # Write the data to a JSON file
    with open(json_file_path, 'w') as jsonfile:
        json.dump(data, jsonfile)

# Specify file paths
csv_file_path = 'addresses.csv'
json_file_path = 'addresses.json'

# Convert CSV to JSON
csv_to_json(csv_file_path, json_file_path)
