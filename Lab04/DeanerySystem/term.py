from day import Day


class Term:
    __day = Day

    def __init__(self, day, hour, minute, duration=90):
        self.hour = hour
        self.minute = minute
        self.duration = duration
        self.__day = day

    def __str__(self):
        day_name = ["Poniedziałek", "Wtorek", "Środa", "Czwartek", "Piątek", "Sobota", "Niedziela"]
        return f"{day_name[self.__day.value]} {self.hour}:{self.minute:02d} [{self.duration}]"

    def earlierThan(self, termin):
        if self.__day.value < termin._Term__day.value:
            return True
        elif self.hour < termin.hour and self.__day.value <= termin._Term__day.value:
            return True
        elif self.minute < termin.minute and self.hour <= termin.hour and self.__day.value <= termin._Term__day.value:
            return True
        else:
            return False

    def laterThan(self, termin):
        if self.__day.value > termin._Term__day.value:
            return True
        elif self.hour > termin.hour and self.__day.value >= termin._Term__day.value:
            return True
        elif self.minute > termin.minute and self.hour >= termin.hour and self.__day.value >= termin._Term__day.value:
            return True
        else:
            return False

    def equals(self, termin):
        if termin._Term__day.value == self.__day.value and termin.hour == self.hour and termin.minute == self.minute and self.duration == termin.duration:
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

        days = end._Term__day.value - begin._Term__day.value - 1
        hrs = 23 - begin.hour + end.hour
        mins = 60 - begin.minute + end.minute + end.duration
        tmp_dur = (days * 24 + hrs) * 60 + mins
        return Term(termin._Term__day, termin.hour, termin.minute, tmp_dur)
