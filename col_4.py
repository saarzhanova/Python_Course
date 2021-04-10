from collections import OrderedDict
import csv

d = {}
with open('new_1.csv', 'w', encoding="utf8") as new_file_1:
    with open('new_2.csv', 'w', encoding="utf8") as new_file_2:
        with open('stage3_test.csv', encoding="utf8") as csv_file:
            file_reader = csv.reader(csv_file)
            file_writer_1 = csv.writer(new_file_1)
            file_writer_2 = csv.writer(new_file_2)
            for row in file_reader:
                d[row[-1]] = row[-2]
            new_d = OrderedDict(sorted(d.items()))
            for key in new_d:
                keys = (key, new_d[key])
                file_writer_1.writerow(keys)
            for key in reversed(new_d):
                keys = (key, new_d[key])
                file_writer_2.writerow(keys)
