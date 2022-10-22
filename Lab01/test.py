import main
from fractions import Fraction
import unittest


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

    def test_zespo(self):
        self.assertEqual(main.sum(complex(1, 4), complex(3, 5)), complex(4, 9))

    def test_wymierne(self):
        self.assertEqual(main.sum(Fraction(1, 4), Fraction(3, 5)), Fraction(17, 20))

    def test_nan_nor_str(self):
        # self.assertEqual(main.sum(1, [2, 3]), 1)

        with self.assertRaises(TypeError):
            self.assertEqual(main.sum(1, [2, 3]), 1)


if __name__ == "__main__":
    unittest.main()
