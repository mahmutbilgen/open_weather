'''
Text read and write samples

1. Method
'''
#
# f=open('./sample_text.txt')
# text = f.read()
# f.close()
#
# print("Read Text file content is below:")
# print(text)
#
# exit

'''
Output:

Read Text file content is below:
Reading and writing text files is an essential programming skill.
Python gives you a simple and powerful tool for working with text files: the open function.
This lets you open a wide variety of files - both text or binary - in many different modes (read, write and append).
In this tutorial we will show you how to read and write text files, and show you several ways to accomplish each task.

'''

'''
2nd Method : open with

'''

# with open("./sample_text.txt") as fobj:
#     text = fobj.read()
#
# alist = text.split('\n')  ## text : {Str} -> list
# print(alist[0:2])

'''
Output:

['Reading and writing text files is an essential programming skill.', 'Python gives you a simple and powerful tool for working with text files: the open function.']

'''

'''
File Not Found Exception
if the file not found try-except statement will catch the error
'''

try:
    with open("not_exist_file.txt") as afile:
        text = afile.read()
except FileNotFoundError:
    text=None

print(text)


'''
Output :

None

'''












