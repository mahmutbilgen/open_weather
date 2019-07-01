'''

import my_module1

courses = ['History','Math','Physics','CompSci']

output:
Imported my_module1 ...

'''
'''
import my_module1 as mm

courses = ['History', 'Math', 'Physics', 'CompSci']

index = mm.find_index(courses, 'Math')
print(index)


output:
Imported my_module1 ...
1
'''

from my_module1 import find_index as f_index, my_test_str

courses = ['History', 'Math', 'Physics', 'CompSci']

index = f_index(courses, 'Math')
print(index)
print(my_test_str)
