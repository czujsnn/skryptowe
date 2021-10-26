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

        if difference_days <= -4:
            return difference_days +7

        elif difference_days >= 4:
            return difference_days -7

        else:
            return difference_days

def nthDayFrom(n, day):

    value = day.value + n

    if value <= 0:

        return Day(value + 7)

    elif value >=8:

        return Day(value - 7)

    else:

        return Day(value)


