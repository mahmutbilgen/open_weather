"""
This is a docstring for the markov module.

>>> m = Markov('ab')
>>> m.predict('a')
'b'

"""
import random


class Markov:
    def __init__(self, text):
        self.table = get_table(text)

    def predict(self, data):
        options = self.table.get(data, {})
        if not options:
            #raise KeyError(f'{data} not in training')
            raise KeyError(
                '{} not in training'.format(data))
        possibles = []
        for item in options.items():
            letter = item[0]
            count = item[1]
            for i in range(count):
                possibles.append(letter)
        return random.choice(possibles)
    
    
def get_table(text):
    '''This is the function docstring
    >>> get_table('ab')
    {'a' :{'b': 1}}
    '''
    results = {}  # dictionary literal
    for i in range(len(text)):
        char = text[i]
        try:
            out = text[i+1]
        except IndexError:
            break
        char_dict = results.get(char, {})
        char_dict.setdefault(out, 0)
        char_dict[out] += 1
        results[char] = char_dict
    return results




        
