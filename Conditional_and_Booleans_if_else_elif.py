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
'''
nums = [1, 2, 3, 4, 5]

for num in nums:
    print(num)


output :
1
2
3
4
5
'''
'''
nums = [1, 2, 3, 4, 5]

for num in nums:
    if num == 3:
        print('Found!')
        break
    print(num)

output:
1
2
Found!
'''
'''
for num in nums:
    if num == 3:
        print('Found!')
        continue
    print(num)

output:
1
2
Found!
4
5
'''

'''
nums = [1, 2, 3, 4]

for num in nums:
    for letter in 'abc':
        print(num, letter)

output:
1 a
1 b
1 c
2 a
2 b
2 c
3 a
3 b
3 c
4 a
4 b
4 c
'''

'''
for i in range(1, 11):
    print(i)

Output:
1
2
3
4
5
6
7
8
9
10
'''
'''
x = 0

while x < 10:
    print(x)
    x += 1

output:
0
1
2
3
4
5
6
7
8
9

'''
x = 0

while True:
    if x == 5:
        break
    print(x)
    x += 1
