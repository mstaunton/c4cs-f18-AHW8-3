import unittest

import rpn

class TestBasics(unittest.TestCase):
    def test_add(self):
        result = rpn.calculate(("1 1 +"),0)
        self.assertEqual(2, result)
    def test_subtract(self):
        result = rpn.calculate(("5 3 -"),0)
        self.assertEqual(2, result)
    def test_multiply(self):
        result = rpn.calculate(("5 3 *"),0)
        self.assertEqual(15, result)
    def test_divide(self):
        result = rpn.calculate(("6 3 /"),0)
        self.assertEqual(2, result)
    def test_exponent(self):
        result = rpn.calculate(("5 2 ^"),0)
        self.assertEqual(25,result)
    def test_modulo(self):
        result = rpn.calculate(("6 5 %"),0)
        self.assertEqual(1,result)
    def test_parameter_error(self):
        with self.assertRaises(TypeError) as cm:
            rpn.calculate(("4 2 1 -"),0)
        err = cm.exception
        self.assertEqual(str(err), 'Too many parameters')
    def test_chacracter_error(self):
        with self.assertRaises(KeyError) as cm:
            rpn.calculate(("4 d +"),0)
