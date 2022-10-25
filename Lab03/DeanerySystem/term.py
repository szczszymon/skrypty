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
        if termin._Term__day.value == self.__day.value and termin.hour == self.hour and termin.minute == self.minute:
            return True
        else:
            return False
