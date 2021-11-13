from typing import List
from action import Action
from lesson import Lesson
from term import Term
from break1 import Break
from timetable1 import Timetable1
from day import Day

from baseterm import BaseTerm
from teacher import Teacher

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
            end_br = br.getEndTime().split(":")
            end_h_br = end_br[0]
            end_m_br = end_br[1]
  
            start_h_br, start_m_br = br.getUniqueStartingHours()

            start_h_term, start_m_term = term.getUniqueStartingHours()
            end_term = term.getEndTime()

            end_h_term = end_term[0]
            end_m_term = end_term[1]
            
            if (int(end_h_br), int(end_m_br)) > (int(start_h_term), int(start_m_term)):
                return True, br.duration

            if (int(end_h_term), int(end_m_term)) > (int(start_h_br), int(start_m_br)):
                return True, br.duration
        
        return False
            
##########################################################
    # def can_be_transferred_to(self, term: Term, full_time: bool) -> bool:

    #     if term.hour < 8:
    #         return False

    #     endtime = term.getEndTime().split(":")
    #     endtime[0],endtime[1] = int(endtime[0]),int(endtime[1]) #date like 17:00 is split between semicolon - then looks like ["17","00"], then both are converted to int.

    #     if endtime[0] > 20:
    #         return False

    #     if endtime[0] == 20 and endtime[1] > 0:
    #         return False

    #     if not self.busy(term):

    #         if term._Term__day.value < 5:
    #             is_fulltime = True

    #         elif term._Term__day.value > 5:
    #             is_fulltime = False

    #         else:

    #             if term._hour < 17:
    #                 is_fulltime = True

    #             else:

    #                 is_fulltime = False

    #         if is_fulltime == full_time:
    #             return True

    #     return False
    def can_be_transferred_to(self, term: Term, full_time: bool) -> bool:
        if self.busy(term):
            return False
        if full_time and term.day.value in [1,2,3,4]:
            if term.hour >= 8 and term.hour <= 20:
                return True
        elif full_time and term.day.value in [5]:
            if term.hour >= 8 and term.hour <= 17:
                return True
        elif not full_time and term.day.value in [5]:
            if term.hour >= 17 and term.hour <= 20:
                return True
        elif not full_time and term.day.value in [6,7]:
            if term.hour >= 8 and term.hour <= 20:
                return True
        return False

##########################################################

    def busy(self, term: Term) -> bool:
        
        for lesson in self._lesson_list:

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

 ##########################################################
 
    def put(self, lesson: Lesson) -> bool:

        if self.busy(lesson._term):
            return False

        else:

            self._lesson_list.append(lesson)
            return True

##########################################################

    def parse(self, actions: List[str]) -> List[Action]:

        action_list = []

        for singularAction in actions:

            if singularAction in Action._value2member_map_:
                action_list.append(Action(singularAction))

        return action_list

##########################################################

    def perform(self, actions: List[Action]):

        counter = 0
        for action_singular in actions:

            if action_singular == Action.DAY_EARLIER:
                self._lesson_list[counter].earlierDay()

            elif action_singular == Action.DAY_LATER:
                self._lesson_list[counter].laterDay()

            elif action_singular == Action.TIME_EARLIER:
                self._lesson_list[counter].earlierTime()

            elif action_singular == Action.TIME_LATER:
                self._lesson_list[counter].laterTime()

            counter += 1
            counter %= len(self._lesson_list)

##########################################################

    def get(self, term: Term) -> Lesson:

        lessonTerm = None

        for lesson in self._lesson_list:

            if lesson.term == term:
                lessonTerm = lesson

                break

        return lessonTerm

    def getTotalHours(self, teacher):

        m_dur = 0
        h_dur = 0   

        for lesson in self._lesson_list:
            if lesson.teacher == teacher:
                h_dur += lesson.term.duration // 45 
                m_dur += lesson.term.duration % 45

        return h_dur*45 + m_dur

    def updateLessons(self, timetable):
        self._lessons = timetable.lessons

if __name__ == "__main__":
    actions = ["t+", "t-", "t+", "d-", "ERROR","d-"]
    term1 = Term(8, 0, 90, Day.TUE)
    term2 = Term(9, 35, 90, Day.WED)
    term3 = Term(17, 20, 110, Day.FRI)
    term4 = Term(9, 35, 90, Day.FRI)
    term5 = Term(17, 20, 110, Day.SAT)

    t1 = Teacher("Tadeusz", "Wokulski")
    t2 = Teacher("Kamila", "Goste")
    t3 = Teacher("Tadeusz", "Wokulski")

    b1 = Break(BaseTerm(9, 30, 5))
    b2 = Break(BaseTerm(11, 5, 10))
    table = Timetable1()
    #print(table.__class__.__name__,"NAMEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE")
    #print(type(table),"EREREEREREKOASIJISDJJASDASDOSDJDSO")
    lesson1 = Lesson(table, term1, "Algebra", t1, 2)
    lesson2 = Lesson(table, term2, "Sledcza", t1, 3)
            #lesson3 = Lesson(table, term3, "WF", t2, 2, False)
    lesson3 = Lesson(table,term3,"WF",t3,2,full_time=False)
    lesson4 = Lesson(table, term4, "Skryptowe", t2, 2)
    lesson5 = Lesson(table, term4, "Skryptowe", t2, 2)
    lesson6 = Lesson(table, term5, "InnePrzed", t2, 2, False)

    table.put(lesson1)
    table.put(lesson2)
    table.put(lesson3)
    table.put(lesson4)
    table.put(lesson6)

    table.put(lesson6)
    table.put(lesson6)
    table.updateLessons(table)
    for lesson in table.lesson_list:
        print(lesson,"\n")
