import csv

# Read data from CSV file
csv_file_path = 'main_data.csv'  # Replace 'main_data.csv' with the actual path to your CSV file

with open(csv_file_path, 'r', encoding='utf-8') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')  # Update delimiter as needed
    entries = [row for row in csv_reader]

# Separate entries based on dividers
type1_entries = [entry for entry in entries if len(entry[0]) == 8 and entry[0].isdigit()]
type2_entries = [entry for entry in entries if len(entry[0]) == 9 and entry[0].isdigit()]
type3_entries = [entry for entry in entries if len(entry[0]) == 7 and entry[0].isdigit()]

# Save entries into separate CSV files
type1_file_path = 'digits8_data.csv'
with open(type1_file_path, 'w', newline='', encoding='utf-8') as type1_file:
    csv_writer = csv.writer(type1_file, delimiter=',')  # Update delimiter as needed
    csv_writer.writerows(type1_entries)

type2_file_path = 'digits9_data.csv'
with open(type2_file_path, 'w', newline='', encoding='utf-8') as type2_file:
    csv_writer = csv.writer(type2_file, delimiter=',')  # Update delimiter as needed
    csv_writer.writerows(type2_entries)

type3_file_path = 'digits7.csv'
with open(type3_file_path, 'w', newline='', encoding='utf-8') as type3_file:
    csv_writer = csv.writer(type3_file, delimiter=',')  # Update delimiter as needed
    csv_writer.writerows(type3_entries)

print("Separation and CSV file writing complete.")
