import csv


class DataSource:
    def read(self, fileName):
        with open(fileName, newline="") as csvfile:
            reader = csv.DictReader(csvfile)
            return list(reader)

    def write(self, fileName, fields, values):
        with open(fileName, "w", newline="") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fields)
            writer.writeheader()
            for row in values:
                writer.writerow(row)
