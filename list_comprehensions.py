nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# my_list = []
#
# for n in nums:
#     my_list.append(n)
#
# print(my_list)

'''
Output :
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

'''

# my_list = [x for x in nums]

# print(my_list)

'''
Output :
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

'''
# my_list = []
# for n in nums:
#     my_list.append(n * n)

# print(my_list)

'''
Output :
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

'''
# my_list = [x * x for x in nums]

# print(my_list)

'''
Output :
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

'''

# my_list = map(lambda x: x * x, nums)

# print(my_list)

'''
Output :
<map object at 0x105f1e4e0>

'''

# my_list = []

# for n in nums:
#     if n % 2 == 0:
#         my_list.append(n)
# print(my_list)

'''
Output :
[2, 4, 6, 8, 10]

'''
# my_list = [n for n in nums if n % 2 == 0]
# print(my_list)
'''
Output :
[2, 4, 6, 8, 10]

'''
# my_list = filter(lamda n: n % 2 == 0, nums)
