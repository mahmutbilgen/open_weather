#
# Disctionary Key Value Pairs
#
'''
student = {'name': 'John','age':25, 'courses':['Math','CompSci'] }


print(student['name'])
print(student['courses'])

# Output :John
John
['Math', 'CompSci']
'''
'''
# dictionary element can be call directly with key

student = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}

print(student['phone'])



# Output :

File "/Users/mbilgen/python_ws/Disctionary_Key_Value_Pairs.py", line 18, in <module>
            print(student['phone'])
        KeyError: 'phone' '''

# Using a 'get'  method for accesing value
'''
student = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}

print(student.get('courses'))
print(student.get('Phone'))

# Output :
['Math', 'CompSci']
None
'''
'''
student = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}

# we can specify a return value instead of None
print(student.get('phone','Not Found'))


# Output : Not Found
'''
'''

student = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}


student['phone'] = '555-5555'
student['name'] = 'Jane'

print(student)


# Output :
# {'name': 'Jane', 'age': 25, 'courses': ['Math', 'CompSci'], 'phone': '555-5555'}
'''

'''# Update dict variable all-in-one
student = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}


student.update({'name': 'Jane', 'age': 26, 'phone': '555-5555'})
print(student)


# Output :
# {'name': 'Jane', 'age': 26, 'courses': ['Math', 'CompSci'], 'phone': '555-5555'}
'''
'''
# Delete dict variable  with key value
student = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}

del student['age']

print(student)


# Output :
{'name': 'John', 'courses': ['Math', 'CompSci']}
'''
'''
# remove "age" value and popped up from dict value
student = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}

age = student.pop('age')

print(age)

print(student)

# Output :
25
{'name': 'John', 'courses': ['Math', 'CompSci']}

'''
'''
student = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}


print(len(student))
print(student.keys())
print(student.values())
print(student.items())


Output :
3
dict_keys(['name', 'age', 'courses'])
dict_values(['John', 25, ['Math', 'CompSci']])
dict_items([('name', 'John'), ('age', 25), ('courses', ['Math', 'CompSci'])])

'''
'''
student = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}

for key in student:
    print(key)
'''
'''
Output :
name
age
courses

'''

student = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}

for key, value in student.items():
    print(key, value)

'''
Output :
name John
age 25
courses ['Math', 'CompSci']

'''
