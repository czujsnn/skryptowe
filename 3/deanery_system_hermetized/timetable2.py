from typing import List
from action import Action
from lesson import Lesson
from term import Term
from break1 import Break
from timetable1 import Timetable1

class Timetable2(Timetable1):

    skipBreaks: bool = True
    def __init__(self, breaks: List[Break]):
        super().__init__()
        self._breaks = breaks

    @property
    def breaks(self):
        return self._breaks
    
    @breaks.setter
    def setBreaks(self, value):
        self._breaks.append(value)

    @property
    def lesson_list(self):
        return self._lesson_list

    @lesson_list.setter
    def setLesson_list(self, value):
        self._lesson_list = value

    def onBreak(self, term):

        for br in self._breaks:

            end_break = br.getEndTime().split(":")

            end_hour_break = end_break[0]
            end_minute_break = end_break[1]
  
            start_hour_break, start_minute_break = br.getUniqueStartingHours()
            start_hour_term, start_minute_term = term.getUniqueStartingHours()
            
            end_term = term.getEndTime()

            end_hour_term = end_term[0]
            end_minute_term = end_term[1]
            
            if (int(end_hour_break), int(end_minute_break)) > (int(start_hour_term), int(start_minute_term)):
                return True, br.duration

            if (int(end_hour_term), int(end_minute_term)) > (int(start_hour_break), int(start_minute_break)):
                return True, br.duration
        
        return False

    def put(self, lesson: Lesson) -> bool:
        if self.busy(lesson._term):
            return False
        else:
            self._lesson_list[lesson.term.__str__()] = lesson
            return True

    def busy(self, term: Term) -> bool:
        
        for lesson in self._lesson_list.values():

            if lesson.term == term:

                return True

            lesson_start = f"{lesson._term._hour}:{lesson._term._minute}"
            lesson_end = lesson.term.getEndTime()
            term_lesson_start = f"{term._hour}:{term._minute}"
            term_lesson_end = term.getEndTime()

            if lesson_end > term_lesson_start and lesson_end < term_lesson_end:
                return True

            if term_lesson_end > lesson_start and term_lesson_end < lesson_end:
                return True

            if lesson_start > term_lesson_start and lesson_start < term_lesson_end:
                return True

            if term_lesson_start > lesson_start and term_lesson_start < lesson_end:
                return True

        return False

 