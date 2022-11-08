from term import Term
from day import Day


def prev_start(hr: int, mins: int, dur: int):
    while dur >= 60:
        hr -= 1
        dur -= 60

    if mins - dur >= 0:
        mins -= dur
    else:
        hr -= 1
        dur -= mins
        mins = 60 - dur

    return hr, mins


def ending_Time(hr: int, mins: int, dur: int):
    while dur >= 60:
        hr += 1
        dur -= 60

    if mins + dur < 60:
        mins += dur
    elif mins + dur == 60:
        hr += 1
        mins = 00
    else:
        hr += 1
        mins += dur - 60

    return hr, mins


class Lesson:
    term = Term
    name = str
    teacherName = str
    year = int
    fullTime = bool

    def __init__(self, term: Term, name: str, teacher: str, year: int):
        self.term = term
        self.name = name
        self.teacherName = teacher
        self.year = year

        if term._Term__day.value in range(0, 5):
            self.fullTime = True
        elif term._Term__day.value in range(5, 7):
            self.fullTime = False

    def __str__(self):
        day_name = ["Poniedziałek", "Wtorek", "Środa", "Czwartek", "Piątek", "Sobota", "Niedziela"]
        match self.year:
            case 1:
                year_name = "Pierwszy rok"
            case 2:
                year_name = "Drugi rok"
            case 3:
                year_name = "Trzeci rok"
            case 4:
                year_name = "Czwarty rok"
            case 5:
                year_name = "Piąty rok"

        if self.fullTime:
            studies_type = "studiów stacjonarnych"
        else:
            studies_type = "studiów niestacjonarnych"

        end_hr, end_min = ending_Time(self.term.hour, self.term.minute, self.term.duration)

        return f'''{self.name} ({day_name[self.term._Term__day.value]} {self.term.hour}:{self.term.minute}-{end_hr}:{end_min})
{year_name} {studies_type}
Prowadzący: {self.teacherName}'''

    def earlierDay(self):
        match self.term._Term__day.value:
            case 0:
                return False
            case 1:
                self.term._Term__day = Day.MON
                return True
            case 2:
                self.term._Term__day = Day.TUE
                return True
            case 3:
                self.term._Term__day = Day.WED
                return True
            case 4:
                if self.fullTime:
                    self.term._Term__day = Day.THU
                    return True
                return False
            case 5:
                if self.term.hour >= 17:
                    self.term._Term__day = Day.FRI
                    return True
                return False
            case 6:
                self.term._Term__day = Day.SAT
                return True

    def laterDay(self):
        match self.term._Term__day.value:
            case 0:
                self.term._Term__day = Day.TUE
                return True
            case 1:
                self.term._Term__day = Day.WED
                return True
            case 2:
                self.term._Term__day = Day.THU
                return True
            case 3:
                hr, mins = ending_Time(self.term.hour, self.term.minute, self.term.duration)

                if hr < 17 or (hr == 17 and mins == 00):
                    self.term._Term__day = Day.FRI
                    return True
                return False
            case 4:
                if not self.fullTime:
                    self.term._Term__day = Day.SAT
                    return True
                return False
            case 5:
                self.term._Term__day = Day.SUN
                return True
            case 6:
                return False

    def earlierTime(self):
        hr, mins = prev_start(self.term.hour, self.term.minute, self.term.duration)

        if not self.fullTime and self.term._Term__day.value == 4:
            if hr < 17:
                return False
            self.term.hour = hr
            self.term.minute = mins
            return True
        else:
            if hr < 8:
                return False
            self.term.hour = hr
            self.term.minute = mins
            return True

    def laterTime(self):
        hr, mins = ending_Time(self.term.hour, self.term.minute, self.term.duration)

        if self.fullTime and self.term._Term__day.value == 4:
            max_hr = 17
        else:
            max_hr = 20

        max_hr, max_mins = prev_start(max_hr, 00, self.term.duration)

        if hr < max_hr or (hr == max_hr and mins <= max_mins):
            self.term.hour = hr
            self.term.minute = mins
            return True
        return False


if __name__ == "__main__":
    lesson = Lesson(Term(Day.WED, 12, 15), "Programowanie Skryptowe", "Stanisław Polak", 5)

    print(lesson)
    print("---------------------------------------------")

    lesson.earlierDay()
    lesson.earlierTime()
    print(lesson)
    print("---------------------------------------------")

    lesson.laterDay()
    lesson.laterTime()
    print(lesson)
