import unittest

import markov
#from markov import Markov, get_table
#import markov as mk
# can use ---> mk.Markov()

class TestMarkov(unittest.TestCase):
    def test_markov(self):
        m = markov.Markov('ab')
        #m = Markov('ab')
        res = m.predict('a')
        self.assertEqual(res,'b')

    def test_markov2(self):
        m = markov.Markov('abc', size=2)
        #m = Markov('ab')
        res = m.predict('ab')
        self.assertEqual(res,'c')
        
    def test_get_table(self):
        res = markov.get_table('ab')
        self.assertEqual(res,
                         {'a':{'b':1}})
    def test_get_table2(self):
        res = markov.get_table('abc', size = 2)
        self.assertEqual(res,
                         {'ab':{'c':1}})
if __name__ == '__main__':
    unittest.main()
