import unittest
from lesson_jurbanska import Lesson
from term_jurbanska import Term
from day import Day


class Test_Lesson(unittest.TestCase):
    def test_later_day(self):
        lesson1 = Lesson(Term(Day.WED, 9, 30), "Programowanie Skryptowe", "Stanisław Polak", 2)
        lesson2 = Lesson(Term(Day.FRI, 16, 30), "WDSI", "Robert Wójcik", 1)
        lesson3 = Lesson(Term(Day.THU, 16, 45, 15), "Język angielski", "Magdalena Potręć", 3)

        self.assertEqual(lesson1.laterDay(), True)
        self.assertEqual(lesson2.laterDay(), False)
        self.assertEqual(lesson3.laterDay(), True)

    def test_earlier_day(self):
        lesson1 = Lesson(Term(Day.WED, 9, 30), "Programowanie Skryptowe", "Stanisław Polak", 2)
        lesson2 = Lesson(Term(Day.MON, 16, 30), "WDSI", "Robert Wójcik", 1)
        lesson3 = Lesson(Term(Day.SAT, 17, 0), "Język angielski", "Magdalena Potręć", 3)

        self.assertEqual(lesson1.earlierDay(), True)
        self.assertEqual(lesson2.earlierDay(), False)
        self.assertEqual(lesson3.earlierDay(), True)

    def test_later_time(self):
        lesson1 = Lesson(Term(Day.WED, 19, 30), "Programowanie Skryptowe", "Stanisław Polak", 2)
        lesson2 = Lesson(Term(Day.FRI, 16, 30, 15), "WDSI", "Robert Wójcik", 1)
        lesson3 = Lesson(Term(Day.THU, 19, 45, 15), "Język angielski", "Magdalena Potręć", 3)

        self.assertEqual(lesson1.laterTime(), False)
        self.assertEqual(lesson2.laterTime(), True)
        self.assertEqual(lesson3.laterTime(), False)

    def test_earlier_time(self):
        lesson1 = Lesson(Term(Day.WED, 9, 30, 135), "Programowanie Skryptowe", "Stanisław Polak", 2)
        lesson2 = Lesson(Term(Day.FRI, 16, 30), "WDSI", "Robert Wójcik", 1)
        lesson3 = Lesson(Term(Day.FRI, 17, 45, 60), "Język angielski", "Magdalena Potręć", 3)

        self.assertEqual(lesson1.earlierTime(), False)
        self.assertEqual(lesson2.earlierTime(), True)
        self.assertEqual(lesson3.earlierTime(), False)


if __name__ == "__main__":
    unittest.main()
