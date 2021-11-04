from enum import Enum


class Day(Enum):
    MON = 1
    TUE = 2
    WED = 3
    THU = 4
    FRI = 5
    SAT = 6
    SUN = 7

    def difference(self, day):

        difference_days = day.value - self.value   
        return difference_days + 7 if difference_days <= -4 else (difference_days - 7 if difference_days >= 4 else difference_days)


def nthDayFrom(n, day):

    value = day.value + n
    return Day(value + 7) if value <= 0 else (Day(value - 7) if value >= 8 else Day(value))