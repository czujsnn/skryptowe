from logging import logProcesses
from typing import List
from term import Term
from base_timetable import BaseTimetable

class Timetable1(BaseTimetable):
    def __init__(self):
        super().__init__()

    @property
    def lessons(self):
        return self._lesson_list

    @lessons.setter
    def setLessons(self, value):
        self._lesson_list = value

    def can_be_transferred_to(self, term: Term, full_time: bool) -> bool:

        days_daily = [1,2,3,4]
        friday = [5]
        weekend = [6,7]

        if self.busy(term):
            return False

        if full_time and term.day.value in days_daily:
            if term.hour >= 8 and term.hour <= 20:
                return True

        elif full_time and term.day.value in friday:
            if term.hour >= 8 and term.hour <= 17:
                return True

        elif not full_time and term.day.value in friday:
            if term.hour >= 17 and term.hour <= 20:
                return True

        elif not full_time and term.day.value in weekend:
            if term.hour >= 8 and term.hour <= 20:
                return True

        return False

