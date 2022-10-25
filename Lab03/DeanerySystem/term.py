from day import Day


class Term:
    __day = Day

    def __init__(self, day, hour, minute):
        self.hour = hour
        self.minute = minute
        self.duration = 90
        self.__day = day

    def __str__(self):
        day_name = ["Poniedziałek", "Wtorek", "Środa", "Czwartek", "Piątek", "Sobota", "Niedziela"]
        return f"{day_name[self.__day.value]} {self.hour}:{self.minute} [{self.duration}]"

# TODO: Nie działa - 1 > 2
    def earlierThan(self, termin):
        if termin._Term__day.value > self.__day.value:
            return True
        elif termin.hour > self.hour:
            return True
        elif termin.minute > self.minute:
            return True
        else:
            return False

# TODO: Nie działa - 1 > 2 - faza testów
    def laterThan(self, termin):
        if termin._Term__day.value < self.__day.value:
            print(termin._Term__day.value," ",self.__day.value)
            return True
        if termin.hour < self.hour:
            print(termin.hour," ",self.hour)
            return True
        if termin.minute < self.minute:
            print(termin.minute," ",self.minute)
            return True
        return False

# TODO: To w sumie działa, ale lepiej sprawdzić
    def equals(self, termin):
        if termin._Term__day.value == self.__day.value and termin.hour == self.hour and termin.minute == self.minute:
            return True
        else:
            return False
