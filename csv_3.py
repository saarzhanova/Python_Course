import csv
with open('1.csv', 'w', encoding="utf8") as new_csvfile:
    with open('stage3_test.csv', encoding="utf8") as csvfile:
        reader = csv.DictReader(csvfile)
        writer = csv.DictWriter(new_csvfile, fieldnames=reader.fieldnames)
        writer.writeheader()
        for row in reader:
            if row['Images'].count(',') > 2:
                writer.writerow(row)