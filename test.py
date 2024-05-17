import csv

# Path to the CSV file
file_path = 'GAO Decisions (8).csv'

# Read and analyze the CSV file
with open(file_path, 'r', encoding='utf-8') as file:
    reader = csv.reader(file)
    header = next(reader)  # Read the header
    header_length = len(header)
    row_number = 1  # Start counting rows after the header

    for row in reader:
        row_number += 1
        if len(row) != header_length:
            print(f"Row {row_number} has a different number of columns than the header.")
            print(f"Row content: {row}")

# If no output, all rows have the same number of columns as the header
print("CSV analysis complete.")
