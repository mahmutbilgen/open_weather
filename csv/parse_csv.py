import csv
'''
DictReader is reading all line with key-value pairs
First line is coming as a key
'''
with open('names.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    with open('new_names.csv', 'w') as new_file:
        # fieldnames = ['first_name', 'last_name', 'email']

        # email value deleted
        fieldnames = ['first_name', 'last_name']

        csv_writer = csv.DictWriter(
            new_file, fieldnames=fieldnames, delimiter='\t')

        # Write headers as we gave
        csv_writer.writeheader()

        for line in csv_reader:
            # email value deleted
            del line['email']
            csv_writer.writerow(line)

    # for line in csv_reader:
    #     # print(line)
    #     # with Below we can print only email coloum
    #     print(line['email'])


'''  Regular Reader Method
     with open('names.csv', 'r') as csv_file:
'''
# csv_reader = csv.reader(csv_file)

# next(csv_reader) # For passing header

# with open('new_names.csv', 'w') as new_file:
#     csv_writer = csv.writer(new_file, delimiter='\t')

#     for line in csv_reader:
#         csv_writer.writerow(line)


# Below code using delimiter as TAB instead of COMMA
# with open('new_names.csv', 'r') as csv_file:
#     csv_reader = csv.reader(csv_file,delimiter='\t')

#     for line in csv_reader:
#         print(line)
