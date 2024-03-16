import csv

csv_file_path = 'main_data.csv'

with open(csv_file_path, 'r', encoding='utf-8') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    entries = [row for row in csv_reader]

five_digit_id_entries = [entry for entry in entries if len(entry[0]) == 5]
other_entries = [entry for entry in entries if len(entry[0]) != 5]

five_digit_id_file_path = 'teachers_data.csv'
with open(five_digit_id_file_path, 'w', newline='', encoding='utf-8') as five_digit_id_file:
    csv_writer = csv.writer(five_digit_id_file, delimiter=',')
    csv_writer.writerows(five_digit_id_entries)

other_entries_file_path = 'students_data.csv'
with open(other_entries_file_path, 'w', newline='', encoding='utf-8') as other_entries_file:
    csv_writer = csv.writer(other_entries_file, delimiter=',')
    csv_writer.writerows(other_entries)

print("Separation and CSV file writing complete.")
