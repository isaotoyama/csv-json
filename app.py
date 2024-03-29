import csv
import json

# The path to the CSV file you want to convert
csv_file_path = 'data/gao.csv'

# The path where the JSON file will be saved
json_file_path = 'data/gao.json'

# Reading the CSV and adding the data to a dictionary
data = []
with open(csv_file_path, encoding='utf-8') as csvf:
    csv_reader = csv.DictReader(csvf)
    for row in csv_reader:
        data.append(row)

# Writing the dictionary to a JSON file
with open(json_file_path, 'w', encoding='utf-8') as jsonf:
    jsonf.write(json.dumps(data, indent=4))
