from zad01 import Operacje
import unittest


class test_operacje(unittest.TestCase):
    def test_sumowanie(self):
        oper = Operacje()

        self.assertEqual(oper.suma(1, 2, 3), 6)
        self.assertEqual(oper.suma(1, 2), 7)
        self.assertEqual(oper.suma(1), 10)

        with self.assertRaises(TypeError):
            oper.suma()

        oper['suma'] = [1, 2]

        self.assertEqual(oper.suma(0), 3)

    def test_odejmowanie(self):
        oper = Operacje()
        self.assertEqual(oper.roznica(2, 1), 1)
        self.assertEqual(oper.roznica(2), -2)
        self.assertEqual(oper.roznica(), -1)

        oper['roznica'] = [1, 2, 3]

        self.assertEqual(oper.roznica(), -1)


if __name__ == '__main__':
    unittest.main()
