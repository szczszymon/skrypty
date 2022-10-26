import unittest
from term import Term
from day import Day


class Test_Days(unittest.TestCase):
    def test_earlier(self):
        term1 = Term(Day.TUE, 9, 45)
        term2 = Term(Day.WED, 10, 15)
        term3 = Term(Day.SUN, 9, 27)
        term4 = Term(Day.WED, 10, 15)
        self.assertEqual(term1.earlierThan(term2), True)
        self.assertEqual(term3.earlierThan(term3), False)
        self.assertEqual(term3.earlierThan(term4), False)
        self.assertEqual(term4.earlierThan(term2), False)
        self.assertEqual(term2.earlierThan(term3), True)

    def test_later(self):
        term1 = Term(Day.TUE, 9, 45)
        term2 = Term(Day.WED, 10, 15)
        term3 = Term(Day.SUN, 9, 27)
        term4 = Term(Day.WED, 10, 15)
        self.assertEqual(term1.laterThan(term2), False)
        self.assertEqual(term2.laterThan(term2), False)
        self.assertEqual(term3.laterThan(term1), True)
        self.assertEqual(term4.laterThan(term2), False)
        self.assertEqual(term3.laterThan(term2), True)

    def test_equal(self):
        term1 = Term(Day.TUE, 9, 45)
        term2 = Term(Day.WED, 10, 15)
        term3 = Term(Day.SUN, 9, 27)
        term4 = Term(Day.WED, 10, 15)
        self.assertEqual(term1.equals(term2), False)
        self.assertEqual(term1.equals(term1), True)
        self.assertEqual(term2.equals(term2), True)
        self.assertEqual(term1.equals(term3), False)
        self.assertEqual(term2.equals(term4), True)
        self.assertEqual(term4.equals(term3), False)

    def test_nazwa(self):
        term1 = Term(Day.TUE, 9, 45)
        term2 = Term(Day.WED, 10, 15)
        term3 = Term(Day.SUN, 9, 27)
        self.assertEqual(term1.__str__(), "Wtorek 9:45 [90]")
        self.assertEqual(term2.__str__(), "Środa 10:15 [90]")
        self.assertEqual(term3.__str__(), "Niedziela 9:27 [90]")


if __name__ == "__main__":
    unittest.main()
