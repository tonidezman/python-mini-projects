import json
import csv

with open("input.json", "r") as f:
    lines = f.readlines()
    people = json.loads("".join(lines))

with open('output_toni.csv', 'w', newline='') as csvfile:
    fieldnames = people[0].keys()
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for person in people:
        writer.writerow(person)
