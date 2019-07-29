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


class Markov:
    def __init__(self, text):
        self.table = None

    def predict(self, data):
        return 'b'
