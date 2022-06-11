import csv
file = open("/Users/fikadu.balcha/Training/near_earth_objects/workspace/data/neos.csv")
csvreader = csv.reader(file)
header = next(csvreader)
print(header)
rows = []
for row in csvreader:
    rows.append(row)
print(rows)
file.close()