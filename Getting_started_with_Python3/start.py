#import markov
from markov import Markov

## from my_module1 import find_index as f_index, my_test_str

m = Markov('ab')
m
m.predict('a')

'''
help(words.get)
Help on built-in function get:
get(key, default=None, /) method of builtins.dict instance
    Return the value for key if key is in the dictionary, else default.


words = {}

words['cat'] = 'furry feline'
words['apple'] = 'crunchy fruit'

print(words['cat'])
'''
