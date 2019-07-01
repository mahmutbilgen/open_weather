# if we want to fill later we need to use 'pass'
#

'''
def hello_func():
    pass

print(hello_func())

Output:
None
'''

'''
def hello_func():
    print('Hello Function!')

hello_func()

Output:
Hello Function!

'''

'''
def hello_func():
    return 'Hello Function!'

print(hello_func())

Output:
Hello Function!

'''

'''
def hello_func():
    return 'Hello Function!'


print(len('Test'))

print(hello_func().upper())

Output:
4
HELLO FUNCTION!
'''

'''
def hello_func(greeting):
    return '{} Function!'.format(greeting)


print(hello_func('Hi'))

Output:
Hi Function!

'''

'''
def hello_func(greeting, name='You'):
    return f'{greeting} {name} !'


print(hello_func('Hi'))
print(hello_func('Hi', 'Mahoni'))

Output:
Hi You !
Hi Mahoni !
'''


# def hello_func(greeting, name='You'):
#     return f'{greeting} {name} !'

'''
def student_info(*args, **kwargs):
    print(args)
    print(kwargs)


student_info('Math', 'Art', name='Mahoni', age=22)

Output:
('Math', 'Art')
{'name': 'Mahoni', 'age': 22}

'''

'''
def student_info(*args, **kwargs):
    print(args)
    print(kwargs)


courses = ['Math', 'Art']
info = {'name': 'Mahoni', 'age': 22}

student_info(courses, info)
print('-------')
student_info(*courses, **info)


Output:
(['Math', 'Art'], {'name': 'Mahoni', 'age': 22})
{}
-------
('Math', 'Art')
{'name': 'Mahoni', 'age': 22}
'''
'''
# Number of days per month. First value placeholder for indexing purposes

month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def is_leap(year):
    """ Return True for leap years, False for non-leap years."""
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def days_in_month(year, month):
    """ Return number of the days in that month in that years. """
    if not 1 <= month <= 12:
        return 'Invalid. Month'

    if month == 2 and is_leap(year):
        return 29
    return month_days[month]


print(days_in_month(2017, 2))
print(days_in_month(2020, 2))
'''
'''
Output:
28
29


'''
