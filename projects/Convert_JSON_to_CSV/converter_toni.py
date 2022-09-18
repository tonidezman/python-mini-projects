import json
import csv


def convert_json_to_csv(json_filename, csv_filename):
    with open("input.json", "r") as f:
        lines = f.readlines()
        people = json.loads("".join(lines))

    with open('output_toni.csv', 'w', newline='') as csvfile:
        fieldnames = people[0].keys()
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for person in people:
            writer.writerow(person)


if __name__ == '__main__':
    json_filename = 'input.json'
    csv_filename = 'output_toni.csv'
    convert_json_to_csv(json_filename, csv_filename)
