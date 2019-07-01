#
# Conditionals and Booleans - If, Else, and Elif Statements

'''
language = 'Python'

if language == 'Python':
    print('Condition was True')

Output:
Condition was True

'''
'''
language = 'Java'

if language == 'Python':
    print('Condition was True')
else:
    print('No match')

Output:
No match

'''
'''
language = 'Java'

if language == 'Python':
    print('Language is Python')
elif language == 'Java':
    print('Language is Java')
else:
    print('No Match')

Output:
Language is Java
'''

# AND
# OR
# NOT
'''
user = 'Admin'

logged_in = True

if user == 'Admin' and logged_in:
    print('Admin Page')
else:
    print('Bad Creds')

Output:
Admin Page
'''
'''
user = 'Admin'

logged_in = False

if user == 'Admin' or logged_in:
    print('Admin Page')
else:
    print('Bad Creds')

Output:
Admin Page

'''
'''
user = 'Admin'

logged_in = False

if not logged_in:
    print('Please Log in')
else:
    print('Welcome')

Output:
Please Log in

'''
'''
a = [1, 2, 3]
b = [1, 2, 3]

print(a == b)
print(id(a))
print(id(b))
print(a is b)

Output:
True
4408131464
4408131528
False
'''
'''

a = [1, 2, 3]
b = a

print(a == b)
print(id(a))
print(id(b))
print(a is b)
print(id(a) is id(b))


Output:
True
4551167880
4551167880
True
False
'''
# Below Values evaluated False :
#   False
#   None
#   Zero of any numeric type
#   Any empty sequence. For example, '', (), []
#   Any empyt mapping. For example, {}
'''
condition = ()

if condition:
    print('Evaluated to True')
else:
    print('Evaluated to False')

output :
Evaluated to False

'''
