import zad2
import unittest


class Test(unittest.TestCase):
    def test_Polecenie(self):
        self.assertEqual(zad2.Find("Ala"), [[], ["Ala"]])
        self.assertEqual(zad2.Find("ma"), [[], ["ma"]])
        self.assertEqual(zad2.Find("1kota"), [["1"], ["kota"]])
        self.assertEqual(zad2.Find("oraz"), [[], ["oraz"]])
        self.assertEqual(zad2.Find("psów20"), [["20"], ["psów"]])
        self.assertEqual(zad2.Find("ponadto"), [[], ["ponadto"]])
        self.assertEqual(zad2.Find("50"), [["50"], []])
        self.assertEqual(zad2.Find("chomików"), [[], ["chomików"]])

    def test_letter_digit(self):
        self.assertEqual(zad2.Find("aaa1b2c33dd4e555"), [["1", "2", "33", "4", "555"], ["aaa", "b", "c", "dd", "e"]])


if __name__ == '__main__':
    unittest.main()
