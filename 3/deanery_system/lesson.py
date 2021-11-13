from day import Day
from term import Term

class Lesson(object):
    def get_fulltime_value(self):

            if self._term._Term__day.value > 5:
                return False
            elif self._term._Term__day.value < 5:
                return True
            
            if self._term.hour < 17:
                return True
            else:
                return False

    def __init__(self, term, name, teacherName, year):
        self._term = term
        self._name = name
        self._teacherName = teacherName
        self._year = year
        self._translate = {"MON":"Poniedziałek","TUE":"Wtorek","WED":"Środa","THU":"Czwartek","FRI":"Piątek","SAT":"Sobota","SUN":"Niedziela"}
        self._full_time = self.get_fulltime_value()

        if term._Term__day.value < 4:
            if term.hour*60+term.minute+term.duration < 20*60:
                self._full_time = True
            
    def earlierDay(self):
        if True:
            self._term._Term__day = Day(self._term._Term__day.value-1)

    def laterDay(self):
        if True:
            self._term._Term__day = Day(self._term._Term__day.value+1)

    def earlierTime(self):
        self._term.hour-=self.term.duration//60
        t = self._term.duration%60
        if self._term.minute >= t:
           self._term.minute -= t
        else:
            self._term.hour -= 1
            self._term.minute -= (t-60)

    def laterTime(self):
        self._term.hour += self.term.duration//60
        t = self._term.hour%60
        self._term.hour += t
        if self._term.hour > 60:
            self._term.hour -= 1
            self._term.minute -= 60

    def __str__(self) -> str:
        if self._full_time == True:
            self._fulltime_print = "Stacjonarnych"
        else:
            self._fulltime_print = "Niestacjonarnych"
        return (f"{self.name} ({self.translate[self.term._Term__day.name]} {self.term.hour}:{self.term.getStartTime()}-{self.term.getEndTime()})\n{self.year} rok studiów {self.fulltime_print}\nProwadzący:{self.teacherName}")


lesson = Lesson(Term(10, 00,90, Day.TUE), "Programowanie skryptowe", "Stanisław Polak", 2)
print(lesson)