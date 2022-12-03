from day import Day


class BasicTerm:
    def __init__(self, hour, minute, duration=90):
        if hour < 0 or 23 < hour or minute < 0 or 59 < minute:
            raise ValueError("Nieprawidłowy czas rozpoczęcia.")
        if duration < 0:
            raise ValueError("Długość zajęć musi być dodatnia.")

        self.__hour = hour
        self.__minute = minute
        self.__duration = duration

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
        if value < 0:
            raise ValueError("Długość zajęć musi być dodatnia.")
        self.__duration = value

    def ending_Time(self):
        hr = self.hour
        mins = self.minute
        dur = self.duration

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

    def end(self):
        hoursDelta = self.duration // 60
        minutesDelta = self.duration % 60
        h = self.hour + hoursDelta
        m = self.minute + minutesDelta

        if m > 59:
            h += 1
            m -= 60

        return BasicTerm(h, m, self.duration)

