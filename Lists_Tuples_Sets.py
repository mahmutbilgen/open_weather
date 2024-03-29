'''
This is a  sample of List, tuple and ...
'''
# courses = ['History', 'Math', 'Physics', 'CompSci']

'''
course_str = ' - '.join(courses)

new_list = course_str.split(' - ')

print(course_str)
print(new_list)
'''
'''
Output:
History - Math - Physics - CompSci
['History', 'Math', 'Physics', 'CompSci']

'''
'''
course_str = ', '.join(courses)

print(course_str)

'''
'''
Output:
History, Math, Physics, CompSci
'''
'''
course_str = ' - '.join(courses)

print(course_str)

Output:
History - Math - Physics - CompSci
'''
'''
for item in courses:
    print(item)

'''
'''
Output:
History
Math
Physics
CompSci

'''

'''
for index, course in enumerate(courses):
    print(index, course)

Output:
0 History
1 Math
2 Physics
3 CompSci

'''

'''print('Math' in courses)
print('Art' in courses)


output:
True
False'''

'''
print(courses.index('Physics'))

Output :
2

'''

'''
print(courses.index('Art'))

Output :
Traceback (most recent call last):
  File "/Users/mbilgen/python_ws/Lists_Tuples_Sets.py", line 6, in <module>
    print(courses.index('Art'))
ValueError: 'Art' is not in list
'''


# courses_2 = ['Art', 'Education']

'''
courses.remove('Math')

print(courses)
# Output : ['History', 'Physics', 'CompSci']
'''

'''
popped = courses.pop()

print(popped)
print(courses)
# Output :
CompSci
['History', 'Math', 'Physics']

'''
'''
courses_reversed = courses.reverse()
print(courses)
print(courses_reversed)
# Output : ['CompSci', 'Physics', 'Math', 'History']
'''


'''
print(courses)
courses.sort()
print(courses)
# Output :
['History', 'Math', 'Physics', 'CompSci']
['CompSci', 'History', 'Math', 'Physics']
'''

'''
courses = ['History', 'Math', 'Physics', 'CompSci']
nums = [1, 5, 2, 4, 3]

sorted_courses = sorted(courses)

print(sorted(nums))
print(sum(nums))
print(sorted_courses)'''

'''
sorted_courses = sorted(courses)

print(sorted(nums))
print(sum(nums))
print(sorted_courses)

Output :
[1, 2, 3, 4, 5]
15
['CompSci', 'History', 'Math', 'Physics']


'''


'''
courses.sort(reverse=True)
nums.sort(reverse=True)

print(nums)
print(courses)
'''
'''
Output :
[5, 4, 3, 2, 1]
['Physics', 'Math', 'History', 'CompSci']

'''
'''
courses.sort()
nums.sort()

print(nums)
print(courses)

# Output :
['CompSci', 'History', 'Math', 'Physics']
[1, 2, 3, 4, 5]

'''

'''

nums.sort(reverse=True)
print(nums)


courses.insert(0, courses_2)
print(courses)
Output: [['Art', 'Education'], 'History', 'Math', 'Physics', 'CompSci']


courses.extend(courses_2)
print(courses)
#['History', 'Math', 'Physics', 'CompSci', 'Art', 'Education']

courses.append(courses_2)
print(courses)
# Output : ['History', 'Math', 'Physics', 'CompSci', ['Art', 'Education']]

print('----------')
print(courses[0:2])
# Output : ['History', 'Math']

print(courses[:2])
# Output : ['History', 'Math']

print(courses[2])
# Output : Physics

courses.append('Art')
print(courses)
Art goes to end of the list
Output: ['History', 'Math', 'Physics', 'CompSci', 'Art']


courses.insert(0, 'Art')
print(courses)
# Output : ['Art', 'History', 'Math', 'Physics', 'CompSci']
'''
'''

Tuple Samples
Tuple is immutable (degismez)

'''
'''

list_1 = ['History', 'Math', 'Physics', 'CompSci']
list_2 = list_1

print(list_1)
print(list_2)

list_1[0] = 'Art'

print(list_1)
print(list_2)

# Changing list value effecting the other list
Output:
['History', 'Math', 'Physics', 'CompSci']
['History', 'Math', 'Physics', 'CompSci']
['Art', 'Math', 'Physics', 'CompSci']
['Art', 'Math', 'Physics', 'CompSci']

'''

# Tuple immutable, Can't add or change
'''
list_1 = ('History', 'Math', 'Physics', 'CompSci')

print(list_1)


list_1[0] = 'Art'
'''
# Changing Tuple : Can't add or change

'''
Output:
    list_1[0] = 'Art'
TypeError: 'tuple' object does not support item assignment
'''

'''
 #
 # SET
 # Set is not care about sort
 #
cs_courses = {'History', 'Math', 'Physics', 'CompSci', 'Math'}

print(cs_courses)

# Output :
1st Run : {'Math', 'CompSci', 'History', 'Physics'}
2nd Run : {'Physics', 'CompSci', 'Math', 'History'}
... Run : chaning the order


cs_courses = {'History', 'Math', 'Physics', 'CompSci', 'Math', 'Math', 'Math'}

print(cs_courses)

# Output :
{'Math', 'CompSci', 'History', 'Physics'}

'''
'''
cs_courses = {'History', 'Math', 'Physics', 'CompSci', 'Math', 'Math', 'Math'}

print('Math' in cs_courses)

# Output :
True


'''
'''
cs_courses = {'History', 'Math', 'Physics', 'CompSci'}
art_courses = {'History', 'Math', 'Art', 'Design'}

print(cs_courses.intersection(art_courses))

# Output : {'Math', 'History'}
'''

'''
cs_courses = {'History', 'Math', 'Physics', 'CompSci'}
art_courses = {'History', 'Math', 'Art', 'Design'}

print(cs_courses.difference(art_courses))

# Output :{'CompSci', 'Physics'}

'''
'''
cs_courses = {'History', 'Math', 'Physics', 'CompSci'}
art_courses = {'History', 'Math', 'Art', 'Design'}

print(cs_courses.union(art_courses))

# Output :{'History', 'Math', 'Physics', 'Design', 'Art', 'CompSci'}

'''
'''
# Creating List,  Tuple, SET,
empty_list = []
empty_list = list()

# Empty Tuple
empty_tuple = ()
empty_tuple = tuple()

# Empty Set
empty_set = {}  # This isn't right! It's a dictionary
empty_set = set()


'''
