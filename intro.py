greeting = 'Hello'
name = 'Michael'

message = '{}, {}. Welcome!'.format(greeting, name)


# print(dir(name))
# print(
# f'this is {greeting.lower()} sample. Say to {name.upper()} {greeting.upper() }')

# print(dir(name))

# sample_url = 'http://mahmutbilgen.com'
# print(sample_url[7:-4])


# student = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}

# student.update({'name': 'Jane', 'age': 26, 'phone': '555-5555'})
# print(student)


student = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}


print(len(student))
print(student.keys())
print(student.values())
print(student.items())

print(help(dict))

print(student.pop('name'))
print(student.items())
