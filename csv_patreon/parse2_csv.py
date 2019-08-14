import csv

html_output = ''
names = []

with open('patrons.csv', 'r') as data_file:
    # csv_data = csv.reader(data_file)
    csv_data = csv.DictReader(data_file)

    # we don't want the first line headers or first lines

    next(csv_data)

    for line in csv_data:
        if line['FirstName'] == 'No Reward':
            break
        names.append(f" {line['FirstName']} {line['LastName']}")

html_output += f'<p> There are currently {len(names)} public contributors. Than You!</p>'

html_output += '\n<ul>'

for name in names:
    html_output += f'\n\t<li> {name} </li>'

print(html_output)


# html_output += '\n</ul>'
# print(html_output)

# for name in names:
#     print(name)

# we dont want headers or first lines
#     next(csv_data)

#     for line in csv_data:
#         if line["FirstName"] == 'No Reward':
#             break
#         names.append(f"{line['FirstName']}  {line['LastName']}")

# html_output += f'<p> There are currently {len(names)} public contributors. Than You!</p>'

# html_output += '\n<lu>'

# for name in names:
#     html_output += f'\n\t<li>{name}</li>'

# html_output += '\n</lu>'

# print(html_output)
