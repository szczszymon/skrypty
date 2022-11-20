from day import Day
from term import Term
from lesson import Lesson
from Break import Break
from typing import List
from BasicTimetable import BasicTimetable


class TimetableWithBreaks(BasicTimetable):
    def __init__(self, breaks: List[Break], skipBreaks: bool = False):
        super().__init__()
        self.breaks = breaks
        self.skipBreaks = skipBreaks

    def can_be_transferred_to(self, term: Term, fullTime: bool) -> bool:
        if self.busy(term):
            return False

        if fullTime == Lesson.fullTime:
            if term.day.value == 4:
                if fullTime:
                    if 8 <= term.hour < 17 and not self.busy(term) and not (self.skipBreaks and self.breakOverlap(term)):
                        return True
                else:
                    if 17 <= term.hour < 20 and not self.busy(term) and not (self.skipBreaks and self.breakOverlap(term)):
                        return True
            elif term.day.value in (0, 1, 2, 3, 5, 6) and 8 <= term.hour < 20 and not self.busy(term) and not (self.skipBreaks and self.breakOverlap(term)):
                return True

        return False

    def breakOverlap(self, term: Term):
        for _ in self.breaks:
            end_hr, end_min = term.ending_Time()
            br_hr, br_min = _.term.ending_Time()
            if _.term.hour > term.hour and (br_hr < end_hr or (br_hr == end_hr and br_min <= end_min)):
                return True
        return False

    def put(self, lesson: Lesson) -> bool:
        if self.busy(lesson.term):
            raise ValueError("Termin zajęty")
        elif type(lesson) != Lesson:
            raise TypeError("put() musi otrzymać argument typu Lesson")

        if not self.breakOverlap(lesson.term):
            self.dct[lesson.term] = lesson
            self.timetable.append(lesson)
            return True
        return False

    def __str__(self):
        s = f'{"":<14}| '

        for i in range(1, 7):
            s += f'{str(Day(i)):<17}|  '
        s += "\n"
        for i in range(0, 14):
            s += "-"
        s += "|"

        for i in range(1, 7):
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

        while h < 21:
            hd = h + ho
            md = m + mo

            if md >= 60:
                hd += 1
                md -= 60

            s += f'{h:02d}:{m:02d}-{hd:02d}:{md:02d}   | '

            for i in range(1, 8):
                found = False
                for l in list(self.dct.values()):
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

            b = self.get_break_end(h, m)
            if b is not None:
                h = b.hour
                m = b.minute
        return s

    def get_break_end(self, h, m, e=False, re=True) -> Term:
        for b in self.breaks:
            if e:
                b = b.term.end()
            else:
                b = b.term
            if b.hour == h and b.minute == m:
                return b.end() if re else b
        return None

