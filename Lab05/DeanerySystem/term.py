from day import Day
from BasicTerm import BasicTerm


class Term(BasicTerm):
    __day = Day

    def __init__(self, day, hour, minute, duration=90):
        super().__init__(hour, minute, duration)
        self.__day = day

    @property
    def day(self):
        return self.__day

    @day.setter
    def day(self, value):
        self.__day = value

    def __str__(self):
        day_name = ["Poniedziałek", "Wtorek", "Środa", "Czwartek", "Piątek", "Sobota", "Niedziela"]
        return f"{day_name[self.day.value]} {self.hour}:{self.minute:02d} [{self.duration}]"

    def earlierThan(self, termin):
        if self.day.value < termin.day.value:
            return True
        elif self.hour < termin.hour and self.day.value <= termin.day.value:
            return True
        elif self.minute < termin.minute and self.hour <= termin.hour and self.day.value <= termin.day.value:
            return True
        else:
            return False

    def laterThan(self, termin):
        if self.day.value > termin.day.value:
            return True
        elif self.hour > termin.hour and self.day.value >= termin.day.value:
            return True
        elif self.minute > termin.minute and self.hour >= termin.hour and self.day.value >= termin.day.value:
            return True
        else:
            return False

    def equals(self, termin):
        if termin.day.value == self.day.value and termin.hour == self.hour and termin.minute == self.minute and self.duration == termin.duration:
            return True
        else:
            return False

    def __gt__(self, termin):
        if self.laterThan(termin):
            return True
        return False

    def __ge__(self, termin):
        if self.laterThan(termin) or self.equals(termin):
            return True
        return False

    def __eq__(self, termin):
        if self.equals(termin):
            return True
        return False

    def __le__(self, termin):
        if self.earlierThan(termin) or self.equals(termin):
            return True
        return False

    def __lt__(self, termin):
        if self.earlierThan(termin):
            return True
        return False

    def __sub__(self, termin):
        if self.earlierThan(termin):
            begin, end = self, termin
        else:
            begin, end = termin, self

        days = end.day.value - begin.day.value - 1
        hrs = 23 - begin.hour + end.hour
        mins = 60 - begin.minute + end.minute + end.duration
        tmp_dur = (days * 24 + hrs) * 60 + mins
        return Term(termin.day, termin.hour, termin.minute, tmp_dur)


