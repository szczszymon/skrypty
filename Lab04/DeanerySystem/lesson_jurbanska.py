from term import Term
from day import Day


class Lesson:
    term = Term
    name = str
    teacherName = str
    year = int
    fullTime = bool

    def __init__(self, term: Term, name: str, teacherName: str, year: int):
        self.term = term
        self.name = name
        self.teacherName = teacherName
        self.year = year

        if self.term._Term__day.value in (0, 1, 2, 3):
            self.fullTime = True

        elif self.term._Term__day.value in (5, 6):
            self.fullTime = False

        else:
            if self.term.hour >= 17:
                self.fullTime = False

            else:
                self.fullTime = True

    def earlierDay(self):
        if self.term._Term__day == Day.TUE:
            self.term._Term__day = Day.MON
            return True

        elif self.term._Term__day == Day.WED:
            self.term._Term__day = Day.TUE
            return True

        elif self.term._Term__day == Day.THU:
            self.term._Term__day = Day.WED
            return True

        elif self.term._Term__day == Day.FRI:
            if self.fullTime:
                self.term._Term__day = Day.THU
                return True

            else:
                return False

        elif self.term._Term__day == Day.SAT:
            if self.term.hour >= 17:
                self.term._Term__day = Day.FRI
                return True

            else:
                return False

        elif self.term._Term__day == Day.SUN:
            self.term._Term__day = Day.SAT
            return True

        else:
            return False

    def laterDay(self):
        if self.term._Term__day == Day.MON:
            self.term._Term__day = Day.TUE
            return True

        elif self.term._Term__day == Day.TUE:
            self.term._Term__day = Day.WED
            return True

        elif self.term._Term__day == Day.WED:
            self.term._Term__day = Day.THU
            return True

        elif self.term._Term__day == Day.THU:
            godzina = self.term.hour
            minuty = self.term.minute

            godzina += self.term.duration // 60
            minuty += self.term.duration % 60

            if minuty > 59:
                godzina += 1
                minuty -= 60

            if godzina < 17 or (godzina == 17 and minuty == 00):
                self.term._Term__day = Day.FRI
                return True

            else:
                return False

        elif self.term._Term__day == Day.FRI:
            if not self.fullTime:
                self.term._Term__day = Day.SAT
                return True

            else:
                return False

        elif self.term._Term__day == Day.SAT:
            self.term._Term__day = Day.SUN
            return True

        elif self.term._Term__day == Day.SUN:
            return False

    def earlierTime(self):
        godzina = self.term.hour
        minuty = self.term.minute

        godzina -= self.term.duration // 60
        minuty -= self.term.duration % 60

        if minuty < 0:
            godzina -= 1
            minuty += 60

        if self.fullTime:
            if godzina < 8:
                return False

            else:
                self.term.hour = godzina
                self.term.minute = minuty
                return True

        else:
            if self.term._Term__day == Day.FRI:
                if godzina < 17:
                    return False

            else:
                if godzina < 8:
                    return False

            self.term.hour = godzina
            self.term.minute = minuty
            return True

    def laterTime(self):
        godzina = self.term.hour
        minuty = self.term.minute

        godzina += self.term.duration // 60
        minuty += self.term.duration % 60

        if minuty > 59:
            godzina += 1
            minuty -= 60

        if self.fullTime and self.term._Term__day == Day.FRI:
            godzina_zakonczenia = 17
        else:
            godzina_zakonczenia = 20

        godzina_zakonczenia -= self.term.duration // 60
        godzina_zakonczenia -= 1

        minuty_zakonczenia = (self.term.duration % 60 * -1) + 60

        if godzina_zakonczenia > godzina or (minuty_zakonczenia >= minuty and godzina_zakonczenia == godzina):
            self.term.hour = godzina
            self.term.minute = minuty
            return True

        else:
            return False

    def __str__(self):
        if self.fullTime:
            studia = "studiów stacjonarnych"
        else:
            studia = "studiów niestacjonarnych"

        if self.year == 1:
            rok = "Pierwszy rok"
        elif self.year == 2:
            rok = "Drugi rok"
        elif self.year == 3:
            rok = "Trzeci rok"
        elif self.year == 4:
            rok = "Czwarty rok"
        elif self.year == 5:
            rok = "Piąty rok"

        tekst = f"{self.name} ({self.term})\n{rok} {studia}\nProwadzący: {self.teacherName}"

        return tekst


if __name__ == "__main__":
    lesson = Lesson(Term(Day.WED, 9, 40), "Programowanie Skryptowe", "Stanisław Polak", 2)
    print(lesson, "\n")

    lesson.earlierTime()
    print(lesson, "\n")

    lesson.laterTime()
    print(lesson, "\n")

    lesson.earlierDay()
    print(lesson, "\n")

    lesson.laterDay()
    print(lesson, "\n")
