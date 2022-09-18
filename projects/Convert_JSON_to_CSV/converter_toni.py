import json
import csv


def convert_json_to_csv(json_filename, csv_filename):
    with open(json_filename, "r") as f:
        json_file = f.read()
        people = json.loads(json_file)

    with open(csv_filename, "w") as f:
        fieldnames = people[0].keys()
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for person in people:
            writer.writerow(person)


if __name__ == "__main__":
    json_filename = "input.json"
    csv_filename = "output_toni.csv"
    convert_json_to_csv(json_filename, csv_filename)
