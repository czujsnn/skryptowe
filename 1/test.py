import main
import unittest
from fractions import Fraction
import cmath


class Test_TestSum(unittest.TestCase):
    def test_sum_integer_integer(self):
        self.assertEqual(main.sum(2, 2), 4)

    def test_sum_integer_float(self):
        self.assertEqual(main.sum(2, 1.5), 3.5)

    def test_sum_integer_string(self):
        self.assertEqual(main.sum(2, '2'), 4)

    def test_sum_string_string(self):
        self.assertEqual(main.sum('2.1', '2.0'), 4.1)

    def test_sum_integer_wrong_number_in_string(self):
        with self.assertRaises(ValueError):
            self.assertEqual(main.sum(2, 'Ala ma kota123'), 2)
    
    def test_sum_complex_number(self):
        self.assertEqual(main.sum(2 + 1j, 3 + 7j),5+8j)

    def test_sum_rational_numbers(self):
        self.assertEqual(main.sum(1/3, 11/3), 4)

    def test_sum_with_not_number_not_str(self):
        with self.assertRaises(TypeError):
            self.assertEqual(main.sum(1,[2,3]),1)

if __name__ == '__main__':
    unittest.main()