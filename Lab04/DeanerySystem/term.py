from day import Day


class Term:
    __day = Day

    def __init__(self, day, hour, minute, duration=90):
        self.__hour = hour
        self.__minute = minute
        self.__duration = duration
        self.__day = day

    @property
    def day(self):
        return self.__day

    @day.setter
    def day(self, value):
        self.__day = value

    @property
    def hour(self):
        return self.__hour

    @hour.setter
    def hour(self, value):
        self.__hour = value

    @property
    def minute(self):
        return self.__minute

    @minute.setter
    def minute(self, value):
        self.__minute = value

    @property
    def duration(self):
        return self.__duration

    @duration.setter
    def duration(self, value):
        self.__duration = value

    def __str__(self):
        day_name = ["Poniedziałek", "Wtorek", "Środa", "Czwartek", "Piątek", "Sobota", "Niedziela"]
        return f"{day_name[self.__day.value]} {self.__hour}:{self.__minute:02d} [{self.__duration}]"

    def earlierThan(self, termin):
        if self.__day.value < termin._Term__day.value:
            return True
        elif self.__hour < termin._Term__hour and self.__day.value <= termin._Term__day.value:
            return True
        elif self.__minute < termin._Term__minute and self.__hour <= termin._Term__hour and self.__day.value <= termin._Term__day.value:
            return True
        else:
            return False

    def laterThan(self, termin):
        if self.__day.value > termin._Term__day.value:
            return True
        elif self.__hour > termin._Term__hour and self.__day.value >= termin._Term__day.value:
            return True
        elif self.__minute > termin._Term__minute and self.__hour >= termin._Term__hour and self.__day.value >= termin._Term__day.value:
            return True
        else:
            return False

    def equals(self, termin):
        if termin._Term__day.value == self.__day.value and termin._Term__hour == self.__hour and termin._Term__minute == self.__minute and self.__duration == termin._Term__duration:
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
        hrs = 23 - begin._Term__hour + end._Term__hour
        mins = 60 - begin._Term__minute + end._Term__minute + end._Term__duration
        tmp_dur = (days * 24 + hrs) * 60 + mins
        return Term(termin._Term__day, termin._Term__hour, termin._Term__minute, tmp_dur)
