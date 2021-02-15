import csv


with open('1.csv', 'w', encoding="utf8") as new_csvfile:
    with open('stage3_test.csv', encoding="utf8") as csvfile:
        file_reader = csv.reader(csvfile)
        file_writer = csv.writer(new_csvfile)
        for row in file_reader:
            try:
                if 10000 < int(row[-1].replace('.0', '')) < 50000:
                    file_writer.writerow(row)
            except ValueError:
                print('wrong')


