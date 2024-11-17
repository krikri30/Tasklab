# TODO импортировать необходимые молули
import json
import csv

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def csv_to_json(csv_file_path, delimiter=',', line_terminator='n') -> None:
    data = []
    with open(csv_file_path, mode='r', newline='') as csv_file:
        reader = csv.DictReader(csv_file, delimiter=delimiter)
        for row in reader:
            data.append(row)
    with open(OUTPUT_FILENAME, "w") as file:
        json.dump(data, file, indent=4)
    json_data = json.dumps(data, indent=4)
    return json_data
csv_file_path = 'input.csv'
json_output = csv_to_json(csv_file_path)

if __name__ == '__main__':
    # Нужно для проверки
    csv_to_json(csv_file_path)

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
