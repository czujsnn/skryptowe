from day import Day
from term import Term

class Lesson(object):

    def __init__(self,timetable, term, name, teacherName, year):

        self._timetable = timetable
        self._term = term
        self._name = name
        self._teacherName = teacherName
        self._year = year
        self._translate = {"MON":"Poniedziałek","TUE":"Wtorek","WED":"Środa","THU":"Czwartek","FRI":"Piątek","SAT":"Sobota","SUN":"Niedziela"}
        self._full_time = self.get_fulltime_value()

        if self._term._Term__day.value < 4:
            if self._term._hour*60+term._minute+term._duration < 20*60:
                self._full_time = True

    def get_fulltime_value(self):

            if self._term._Term__day.value > 5:
                return False
            elif self._term._Term__day.value < 5:
                return True
            
            if self._term.hour < 17:
                return True
            else:
                return False

    @property
    def term(self):
        return self._term

    @term.setter
    def setTerm(self, term):
        self._term = term

    @property
    def name(self):
        return self._name

    @name.setter
    def setName(self, name):
        self._name = name

    @property
    def teacherName(self):
        return self._teacher_name

    @teacherName.setter
    def setTeacherName(self, name):
        self._teacher_name = name

    @property
    def year(self):
        return self._year

    @year.setter
    def setYear(self, year):
        self._year = year

    @property
    def fullTime(self):
        return self._full_time

    @fullTime.setter
    def setFullTime(self, full_time):
        self._full_time = full_time
            
    def earlierDay(self):

       newDayValue = self._term._Term__day.value - 1

       if newDayValue < 1:
           return False

       newDay = Day(newDayValue)

       newTerm = Term(self._term._hour, self._term._minute,90, newDay)

       if not self._timetable.can_be_transferred_to(newTerm, self._full_time):
           return False

       self._term._Term__day = newDay 

       return True

    def laterDay(self):
        newDayValue = self._term._Term__day.value + 1

        if newDayValue > 7:
            return False

        newDay = Day(newDayValue)
        newTerm = Term(self._term._hour, self._term._minute,90, newDay)

        if not self._timetable.can_be_transferred_to(newTerm, self._full_time):
            return False

        self._term._day = newDay
        return True

    def laterTime(self):

        hourDifference = self._term.duration // 60
        minuteDifference = self._term.duration % 60

        if self._term.minute + minuteDifference >= 60:
            minuteDifference -= 60
            hourDifference += 1

        newTerm = Term(self._term._hour + hourDifference,self._term._minute + minuteDifference,90,self._term._Term__day)

        if not self._timetable.can_be_transferred_to(newTerm, self._full_time):
            return False

        self._term._hour += hourDifference
        self._term._minute += minuteDifference

    def earlierTime(self):

        hourDifference = self._term.duration // 60
        minuteDifference = self._term.duration % 60

        if self._term.minute + minuteDifference < 0:
            minuteDifference -= 60
            hourDifference += 1

        newTerm = Term(self._term._hour - hourDifference,self._term._minute - minuteDifference,90,self._term._Term__day)

        if not self._timetable.can_be_transferred_to(newTerm, self._full_time):
            return False

        self._term._hour -= hourDifference
        self._term._minute -= minuteDifference

        return True

    def __str__(self) -> str:

        if self._full_time == True:
            self._fulltime_print = "Stacjonarnych"
        else:
            self._fulltime_print = "Niestacjonarnych"
        return (f"{self._name} ({self._translate[self._term._Term__day.name]} {self._term._hour}:{self._term.getStartTime()}-{self._term.getEndTime()})\n{self._year} rok studiów {self._fulltime_print}\nProwadzący:{self._teacherName}")
