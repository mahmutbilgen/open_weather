'''
This is a  sample of List, tuple and ...
'''
courses = ['History', 'Math', 'Physics', 'CompSci']
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


'''''''''
print(courses)
courses.sort()
print(courses)
# Output :
['History', 'Math', 'Physics', 'CompSci']
['CompSci', 'History', 'Math', 'Physics']
'''''''''

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
