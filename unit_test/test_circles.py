import unittest
from circles import circle_area
# import circles
from math import pi

class TestCircleArea(unittest.TestCase):
    def test_area(self):
        # Test areas when radius >=0
        self.assertAlmostEqual(circle_area(1),pi)
        self.assertAlmostEqual(circle_area(0),0)
        self.assertAlmostEqual(circle_area(2.1), pi * 2.1**2)

    def test_value(self):
        # Make sure values errors are raised when necessary
        self.assertRaises(ValueError, circle_area, -2)

    def test_types(self):
        # Make sure type errors are raised when neccessary
        self.assertRaises(TypeError, circle_area, 3+5j)
        self.assertRaises(TypeError, circle_area, True)
        self.assertRaises(TypeError, circle_area, "string radius")

'''
Mahmuts-iMac:unit_test mbilgen$ python -m unittest 
.F.
======================================================================
FAIL: test_types (test_circles.TestCircleArea)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/mbilgen/python_ws/unit_test/test_circles.py", line 20, in test_types
    self.assertRaises(TypeError, circle_area, True)
AssertionError: TypeError not raised by circle_area

----------------------------------------------------------------------
Ran 3 tests in 0.001s

FAILED (failures=1)

----------------------------------------------------------------------

Mahmuts-iMac:unit_test mbilgen$ python -m unittest 
...
----------------------------------------------------------------------
Ran 3 tests in 0.000s

OK
Mahmuts-iMac:unit_test mbilgen$ 
Mahmuts-iMac:unit_test mbilgen$ 
Mahmuts-iMac:unit_test mbilgen$ 
Mahmuts-iMac:unit_test mbilgen$ python -m unittest 
...
----------------------------------------------------------------------
Ran 3 tests in 0.000s

OK

'''