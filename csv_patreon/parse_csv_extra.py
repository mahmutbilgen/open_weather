import csv

html_output = ''
names = []

with open('patrons.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    with open('new_names2.cvs', 'w') as new_file:
        csv_writer = csv.writer(new_file, delimiter='-')

        for line in csv_reader:
            csv_writer.writerow(line)


# Copy CSV file into other "new_file2.csv"
# changing  delimiter  from " ," to '-' dash
#
# with open('patrons.csv', 'r') as csv_file:
#     csv_reader = csv.reader(csv_file)

#     with open('new_names2.cvs', 'w') as new_file:
#         csv_writer = csv.writer(new_file, delimiter='-')

#         for line in csv_reader:
#             csv_writer.writerow(line)


#     # csv_data = csv.reader(data_file)
#         csv_data = csv.DictReader(data_file)

#         # we dont want headers or first lines
#         next(csv_data)

#         for line in csv_data:
#             if line["FirstName"] == 'No Reward':
#                 break
#             names.append(f"{line['FirstName']}  {line['LastName']}")

# html_output += f'<p> There are currently {len(names)} public contributors. Than You!</p>'

# html_output += '\n<lu>'

# for name in names:
#     html_output += f'\n\t<li>{name}</li>'

# html_output += '\n</lu>'

# print(html_output)
