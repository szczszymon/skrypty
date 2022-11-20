from day import Day


class Term:
    def __init__(self, day: Day, hour, minute, duration=90):
        self.hour = hour
        self.minute = minute
        self.duration = duration
        self.__day = day

    def laterThan(self, termin):
        if self.__day.value > termin._Term__day.value:
            return True
        elif self.hour > termin.hour and self.__day.value >= termin._Term__day.value:
            return True
        elif self.minute > termin.minute and self.hour >= termin.hour and self.__day.value >= termin._Term__day.value:
            return True
        return False

    def earlierThan(self, termin):
        if self.__day.value < termin._Term__day.value:
            return True
        elif self.hour < termin.hour and self.__day.value <= termin._Term__day.value:
            return True
        elif self.minute < termin.minute and self.hour <= termin.hour and self.__day.value <= termin._Term__day.value:
            return True
        return False

    def equals(self, termin):
        if termin._Term__day.value == self.__day.value and termin.hour == self.hour and termin.minute == self.minute:
            return True
        return False

    def __str__(self):
        dni = ["Poniedziałek", "Wtorek", "Środa", "Czwartek", "Piątek", "Sobota", "Niedziela"]
        return f"{dni[self.__day.value]} {self.hour}:{self.minute:02d} [{self.duration}]"

    def __eq__(self, other):
        return self.equals(other)

    def __ge__(self, other):
        return self.equals(other) or self.laterThan(other)

    def __le__(self, other):
        return self.equals(other) or self.earlierThan(other)

    def __gt__(self, other):
        return self.laterThan(other)

    def __lt__(self, other):
        return self.earlierThan(other)

    def __sub__(self, other):
        czas_trwania = ((self.__day.value - other._Term__day.value - 1) * 24 + (23 - other.hour) + self.hour) * 60 + (60 - other.minute) + self.minute + self.duration
        return Term(other._Term__day, other.hour, other.minute, czas_trwania)


'''
>>> term1 = Term(Day.MON, 8, 30)
>>> term2 = Term(Day.TUE, 9, 45, 30)
>>> term3 = Term(Day.TUE, 9, 45, 90)
>>> print(term1)
Poniedziałek 8:30 [90]
>>> print(term2)
Wtorek 9:45 [30]
>>> print(term3)
Wtorek 9:45 [90]
>>> print("term1 < term2:", term1 < term2)
term1 < term2: True
>>> print("term1 <= term2:", term1 <= term2)
term1 <= term2: True
>>> print("term1 > term2:", term1 > term2)
term1 > term2: False
>>> print("term1 >= term2:", term1 >= term2)
term1 >= term2: False
>>> print("term2 == term2:", term2 == term2)
term2 == term2: True
>>> print("term2 == term2:", term2 == term3)
term2 == term2: True
>>> term4 = term3 - term1
>>> print(term4)
Poniedziałek 8:30 [1605]
'''