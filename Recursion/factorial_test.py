from factorial_recursion import *
import unittest


# unittesting
class TestFactorial(unittest.TestCase):
    def test_factorial(self):
        self.assertEqual(factorial(2),2)
        self.assertEqual(factorial(5),120)

    def test_indexerror(self):
        self.assertRaises(IndexError, factorial, -1)

if __name__ == '__main__':
    unittest.main(exit=False)