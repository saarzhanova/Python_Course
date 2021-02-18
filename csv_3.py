import csv


with open('1.csv', 'w', encoding="utf8") as new_csvfile:
    with open('stage3_test.csv', encoding="utf8") as csvfile:
        reader = csv.DictReader(csvfile)
        titles = ['Id', 'Title', 'Price']
        writer = csv.DictWriter(new_csvfile, fieldnames=titles)
        writer.writeheader()
        for row in reader:
            a = {'Id': row['Id'], 'Title': row['Title'], 'Price': row['Price']}
            writer.writerow(a)