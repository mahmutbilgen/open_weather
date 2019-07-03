'''

import my_module1

courses = ['History','Math','Physics','CompSci']

output:
Imported my_module1 ...


import my_module1 as mm

courses = ['History', 'Math', 'Physics', 'CompSci']

index = mm.find_index(courses, 'Math')
print(index)


output:
Imported my_module1 ...
1
'''

'''
from my_module1 import find_index as f_index, my_test_str

courses = ['History', 'Math', 'Physics', 'CompSci']

index = f_index(courses, 'Math')
print(index)
print(my_test_str)

out:
Imported my_module1 ...
1
My Test string

'''

'''
# importing everything from my_module1
from my_module1 import *

courses = ['History', 'Math', 'Physics', 'CompSci']

index = find_index(courses, 'Math')
print(index)
print(my_test_str)

# output:
# Imported my_module1 ...
# 1
# My Test string
#
# '''
'''
import sys

sys.path.append('/Users/mbilgen/python_ws/My_Modules')
print(f"Python Module Path :  {sys.path}")

import my_module1

# output :
# Python Path :  ['/Users/mbilgen/python_ws', '/Users/mbilgen/python_ws', '/Library/Frameworks/Python.framework/Versions/3.7/lib/python37.zip', '/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7', '/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/lib-dynload', '/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages', '/Users/mbilgen/python_ws/My_Modules']
# Imported my_module1 ...

'''

'''
import random

courses = ['History', 'Math', 'Physics', 'CompSci']

random_course = random.choice(courses)

print(random_course)


Output:
1st run : Math
2nd run : CompSci
3nd run :  History

'''

'''
import datetime
import calendar

today = datetime.date.today()

print(today)
print(calendar.isleap(2020))

output :
2019-07-02
True
'''
'''
import os

print(os.getcwd())
print(os.__file__)

'''

'''
output : 
/Users/mbilgen/python_ws
/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/os.py

'''
##  Funny run below code
import antigravity



