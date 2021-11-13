from day import Day
from term import Term
from teacher import Teacher

class Lesson(object):

    def __init__(self,timetable, term, name, teacher, year = None,full_time: bool = True):
        #from timetable2 import Timetable2
        #if not timetable.__class__.__name__ == "Timetable1": raise Exception("Timetable must be type of `Timetable2`.")

        self._timetable = timetable
        self._term = term
        self._name = name
        self._year = year
        self._translate = {"MON":"Poniedziałek","TUE":"Wtorek","WED":"Środa","THU":"Czwartek","FRI":"Piątek","SAT":"Sobota","SUN":"Niedziela"}
        self._full_time = full_time
        self.__teacher = teacher

        if self._term._Term__day.value < 4:
            if self._term._hour*60+term._minute+term._duration < 20*60:
                self._full_time = True

    def get_fulltime_value(self):

            if self._term._Term__day.value > 5:
                return False
            elif self._term._Term__day.value < 5:
                return True
            elif self._term._Term__day.value == 5:
                if self._term.hour > 17:
                    return False
                else:
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
    def teacher(self):
        return self.__teacher

    @teacher.setter
    def setTeacher(self, value):
        self.__teacher = value

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

    def earlierTime(self):
        hour_d = self._term._duration // 60
        min_d = self._term._duration % 60

        new_hour = self._term._hour - hour_d
        new_min = self._term._minute - min_d
        if new_min < 0:
            new_hour -= 1
            new_min = 60 + new_min
        
        new_term = Term(new_hour, new_min, self._term._duration, self._term._Term__day)

        isOnBreak = self._timetable.onBreak(new_term)

        if isOnBreak:
            new_min -=  isOnBreak[1]
            if new_min < 0:
                new_hour -= 1
                new_min = 60 + new_min
            new_term = Term(new_hour, new_min, self._term._duration, self._term._Term__day)

        if self._timetable.can_be_transferred_to(new_term, self._full_time):
            self._term._hour = new_hour
            self._term._minute = new_min
            return True
        else:
            return False        

    def laterTime(self):
        hour_d = self._term._duration // 60
        min_d = self._term._duration % 60

        new_hour = self._term._hour + hour_d
        new_min = self._term._minute + min_d
        if new_min >= 60:
            new_hour += 1
            new_min = new_min - 60

        new_term = Term(new_hour, new_min, self._term._duration, self._term._Term__day)

        isOnBreak = self._timetable.onBreak(new_term)
        if isOnBreak and not self._timetable.skipBreaks:
            print("self.skipBreaks is set to False. Can't move lesson")
            return False

        if isOnBreak:
            new_min += isOnBreak[1]
            if new_min >= 60:
                new_hour += 1
                new_min = new_min - 60
            new_term = Term(new_hour, new_min, self._term._duration, self._term._Term__day)

        if self._timetable.can_be_transferred_to(new_term, self._full_time):
            self._term._hour = new_hour
            self._term._minute = new_min
            return True
        else:
            return False

    def __add__(self, teacher):

        if type(teacher) == Teacher:

            total_time = self._timetable.getTotalHours(teacher) + (self.term.duration // 45)*45 + (self.term.duration % 45)
            if total_time <= 6*45:

                self.__teacher = teacher
                return True

        return False

    def __sub__(self, teacher):

        if type(teacher) == Teacher and teacher.id == self.teacher.id:
            self.__teacher = Teacher(None, None)

            return True

        return False


    def __str__(self) -> str:

        if self._full_time == True:
            self._fulltime_print = "Stacjonarnych"
        else:
            self._fulltime_print = "Niestacjonarnych"
        return (f"{self._name} ({self._translate[self._term._Term__day.name]} {self._term._hour}:{self._term.getStartTime()}-{self._term.getEndTime()})\n{self._year} rok studiów {self._fulltime_print}\nProwadzący:{self.teacher}")

