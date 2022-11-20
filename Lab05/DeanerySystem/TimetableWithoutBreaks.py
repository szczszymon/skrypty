from typing import List
from day import Day
from term import Term
from lesson import Lesson
from action import Action
from BasicTimetable import BasicTimetable


class TimetableWithoutBreaks(BasicTimetable):
    def __init__(self):
        super().__init__()

    """ Class containing a set of operations to manage the timetable """

##########################################################
    def can_be_transferred_to(self, term: Term, fullTime: bool) -> bool:
        if self.busy(term):
            return False

        if fullTime == Lesson.fullTime:
            if term.day.value == 4:
                if fullTime:
                    if 8 <= term.hour < 17 and not self.busy(term):
                        return True
                else:
                    if 17 <= term.hour < 20 and not self.busy(term):
                        return True
            elif term.day.value in (0, 1, 2, 3, 5, 6) and 8 <= term.hour < 20 and not self.busy(term):
                return True

        return False

##########################################################

    def put(self, lesson: Lesson) -> bool:
        if self.busy(lesson.term):
            raise ValueError("Termin zajęty")
        elif type(lesson) != Lesson:
            raise TypeError("put() musi otrzymać argument typu Lesson")

        self.timetable[lesson.term] = lesson
        return True

##########################################################
    def __str__(self):
        s = f'{"":<14}| '

        for i in range(1, 8):
            s += f'{str(Day(i)):<17}|  '
        s += "\n"
        for i in range(0, 14):
            s += "-"
        s += "|"

        for i in range(1, 8):
            for j in range(0, 19):
                if i == 1 and j == 0:
                    continue
                s += "-"
            s += "|"
        s += "\n"

        duration = 90

        h = 8
        m = 0
        ho = duration // 60
        mo = duration % 60

        while h < 20:
            hd = h + ho
            md = m + mo

            if md >= 60:
                hd += 1
                md -= 60

            s += f'{h:02d}:{m:02d}-{hd:02d}:{md:02d}   | '

            for i in range(1, 8):
                found = False
                for l in list(self.timetable.values()):
                    if l.term.day.value == i and l.term.hour == h and l.term.minute == m:
                        s += f'{l.name:<17}|  '
                        found = True
                        break

                if not found:
                    s += f'{"":<17}|  '

            if h != 18:
                s += f'\n{"":<14}|{"":<18}|{"":<19}|{"":<19}|{"":<19}|{"":<19}|{"":<19}|{"":<19}|\n'
            else:
                s += "\n\n"

            h = hd
            m = md

        return s
