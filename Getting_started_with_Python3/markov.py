#!/usr/bin/env python
'''
Getting started with Python 3
Wednesday, July 17⋅5:00 – 8:00am
##
 Launch IDLE editor from iMac

 $ python3 -m idlelib.idle
'''


"""
This  is a docstring fro the markov module

>>> m = Markov('ab')
>>> m.predict('a')
'b'

"""
import random
import urllib.request as req
import sys
import argparse

class Markov:
    def __init__(self, text, size=1):
        #self.table = get_table(text)
        self.tables = []
        for i in range(size):
            self.tables.append(
                get_table(text, size=i+1))
        
    def predict(self, data):
        table = self.tables[len(data)-1]
        options = table.get(data, {})
        #options = self.table.get(data, {})
        if not options:
            raise KeyError(f'{data} not in training')
        possibles = []
        for letter, count  in options.items():
            for i in range(count):
                possibles.append(letter)
        return random.choice(possibles)

def get_table(text, size=1):
    '''This is the function docstring
    >>> get_table('ab')
    {'a' :{'b': 1}}
    '''
    results = {}  # dictionary literal
    for i in range(len(text)):
        chars = text[i:i+size]
        try:
            out = text[i+size]
        except IndexError:
            break
        char_dict = results.get(chars, {})
        char_dict.setdefault(out, 0)
        char_dict[out] += 1
        results[chars] = char_dict
    return results

def fetch_url(url, fname):
    fin = req.urlopen(url)
    data = fin.read()
##    fout = open (fname, mode='w',
##                 encoding='utf8')
##    fout.write(data.decode('utf8'))
##    fout.close()
    with open (fname, mode='w',
                 encoding='utf8') as fout:
            fout.write(data.decode('utf8'))


def from_file(fname, size=1):
    with open(fname, encoding='utf8') as fin:
       m = Markov(fin.read(), size=size)
    return m

if __name__ == '__main__':
    print(f"executing: {__name__}")
    m = from_file('pp.txt', size=4)
else:
    print(f"Loading: {__name__}")

