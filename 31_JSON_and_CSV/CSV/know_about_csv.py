# CSV (Comma-Separated Values) --->

# Stores data in rows and columns, like a spreadsheet.
# Ideal for flat tabular data.
# Widely used in data analysis and Excel.

import csv

with open("data.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

with open("output.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["name", "age", "skills"])
    writer.writerow(["Jyotsna", 24, "Python;Testing;Git"])