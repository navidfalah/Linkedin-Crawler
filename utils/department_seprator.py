import csv
from collections import defaultdict

csv_file_path_digi8 = 'digits8_data.csv'
csv_file_path_digi7 = 'digits7_data.csv'

def digit_seprator(path, digits):
    with open(path, 'r', encoding='utf-8') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        entries = [row for row in csv_reader]

    data_by_middle_digits = defaultdict(list)

    for entry in entries:
        middle_digits = entry[0][2:5]
        data_by_middle_digits[middle_digits].append(entry)

    for middle_digits, data in data_by_middle_digits.items():
        file_path = f'departments_{digits}/{middle_digits}_data.csv'
        with open(file_path, 'w', newline='', encoding='utf-8') as csv_file:
            csv_writer = csv.writer(csv_file, delimiter=',')
            csv_writer.writerows(data)

    print("Separation and CSV 8 digits file writing complete.")

digit_seprator(csv_file_path_digi8, 8)
digit_seprator(csv_file_path_digi7, 7)
