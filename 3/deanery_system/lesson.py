from day import Day
from term import Term

class Lesson(object):
    def get_fulltime_value(self):
            if self.term._Term__day.value > 5:
                return False
            elif self.term._Term__day.value < 5:
                return True
            
            if self.term.hour < 17:
                return True
            else:
                return False

    def __init__(self, term, name, teacherName, year):
        self.term = term
        self.name = name
        self.teacherName = teacherName
        self.year = year
        self.translate = {"MON":"Poniedziałek","TUE":"Wtorek","WED":"Środa","THU":"Czwartek","FRI":"Piątek","SAT":"Sobota","SUN":"Niedziela"}
        self.full_time = self.get_fulltime_value()

        

        if term._Term__day.value < 4:
            if term.hour*60+term.minute+term.duration < 20*60:
                self.full_time = True
            
    def earlierDay(self):
        if True:
            self.term._Term__day = Day(self.term._Term__day.value-1)

    def laterDay(self):
        if True:
            self.term._Term__day = Day(self.term._Term__day.value+1)

    def earlierTime(self):
        self.term.hour-=self.term.duration//60
        t = self.term.duration%60
        if self.term.minute >= t:
           self.term.minute -= t
        else:
            self.term.hour -= 1
            self.term.minute -= (t-60)

    def laterTime(self):
        self.term.hour += self.term.duration//60
        t = self.term.hour%60
        self.term.hour += t
        if self.term.hour > 60:
            self.term.hour -= 1
            self.term.minute -= 60

    def __str__(self) -> str:
        if self.full_time == True:
            fulltime_print = "Stacjonarnych"
        else:
            fulltime_print = "Niestacjonarnych"
        return (f"{self.name} ({self.translate[self.term._Term__day.value]}")
term1 = Term(9,35,90,Day.TUE)
print(term1)
lesson = Lesson(Term(9, 35,90, Day.TUE), "Programowanie skryptowe", "Stanisław Polak", 2)
print(lesson)