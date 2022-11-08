import unittest
from lesson import Lesson
from term import Term
from day import Day


class Test_Lesson(unittest.TestCase):
    def test_earlier(self):
        lesson1 = Lesson(Term(Day.MON, 8, 40), "Programowanie Skryptowe", "Stanisław Polak", 5)
        lesson2 = Lesson(Term(Day.SAT, 8, 15, 30), "BSST", "Marcin Niemiec", 3)

        lesson3 = Lesson(Term(Day.THU, 16, 40), "Programowanie Skryptowe", "Stanisław Polak", 5)
        lesson4 = Lesson(Term(Day.SAT, 19, 30, 30), "BSST", "Marcin Niemiec", 3)

        self.assertEqual(lesson1.earlierDay(), False)
        self.assertEqual(lesson1.earlierTime(), False)

        self.assertEqual(lesson2.earlierDay(), False)
        self.assertEqual(lesson2.earlierTime(), False)

        self.assertEqual(lesson3.earlierDay(), True)
        self.assertEqual(lesson3.earlierTime(), True)

        self.assertEqual(lesson4.earlierDay(), True)
        self.assertEqual(lesson4.earlierTime(), True)

    def test_later(self):
        lesson1 = Lesson(Term(Day.FRI, 16, 50), "Programowanie Skryptowe", "Stanisław Polak", 5)
        lesson2 = Lesson(Term(Day.SUN, 19, 30, 30), "BSST", "Marcin Niemiec", 3)

        lesson3 = Lesson(Term(Day.THU, 11, 40), "Programowanie Skryptowe", "Stanisław Polak", 5)
        lesson4 = Lesson(Term(Day.SAT, 19, 30, 15), "BSST", "Marcin Niemiec", 3)

        lesson5 = Lesson(Term(Day.THU, 16, 50), "Programowanie Skryptowe", "Stanisław Polak", 5)

        self.assertEqual(lesson1.laterDay(), False)
        self.assertEqual(lesson1.laterTime(), False)

        self.assertEqual(lesson2.laterDay(), False)
        self.assertEqual(lesson2.laterTime(), False)

        self.assertEqual(lesson3.laterDay(), True)
        self.assertEqual(lesson3.laterTime(), True)

        self.assertEqual(lesson4.laterDay(), True)
        self.assertEqual(lesson4.laterTime(), True)

        self.assertEqual(lesson5.laterDay(), False)


if __name__ == "__main__":
    unittest.main()
