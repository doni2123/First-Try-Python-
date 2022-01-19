import csv
with open('20200521054035-.csv') as csvfile:
    my_csv_file = csv.reader(csvfile, delimiter=';')
    for row in my_csv_file:
        print(row)