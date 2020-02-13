import csv

with open('test_csv.csv', 'r') as f:
    csv_reader = csv.reader(f)

    with open('new_test_csv.csv', 'w') as wf:
        csv_writer = csv.writer(wf, delimiter='-')
        for line in csv_reader:
            csv_writer.writerow(line)

# DictReader , will return each line as a OrderedDict

with open('test_csv.csv', 'r') as f:
    csv_reader = csv.DictReader(f, delimiter=",")

    for line in csv_reader:
        print(line['email'])

# DictWriter

with open('test_csv.csv', 'r') as f:
    csv_reader = csv.DictReader(f, delimiter=',')
    fieldnames = ['first_name', 'last_name']
    with open('new_test_csv2.csv', 'w') as wf:
        csv_writer = csv.DictWriter(wf, fieldnames=fieldnames, delimiter='\t')
        csv_writer.writeheader()
        for line in csv_reader:
            del line['email']
            csv_writer.writerow(line)
