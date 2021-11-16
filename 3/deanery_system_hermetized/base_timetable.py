from term import Term
from lesson import Lesson
from action import Action
from typing import List

class BaseTimetable():
    """ Class containing a set of operations to manage the timetable """
    def __init__(self):
        self._lesson_list = []

    @property
    def lessons(self):
        return self._lesson_list

    @lessons.setter
    def setLessons(self, value):
        self._lesson_list = value


    def busy(self, term: Term) -> bool:
            
            for lesson in self._lesson_list:

                if lesson._term == term:

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
            raise ValueError("This lesson term is busy")

        return True if self._lesson_list.append(lesson) else False

    def parse(self, actions: List[str]) -> List[Action]:

            action_list = []

            for singularAction in actions:

                if singularAction in Action._value2member_map_:
                    action_list.append(Action(singularAction))
                else:
                    raise ValueError(f"Translation `{singularAction}` is incorrect.")

            return action_list

    def perform(self, actions: List[Action]):

        counter = 0
        for action_singular in actions:

            if action_singular == Action.DAY_EARLIER:
                self.lesson_list[counter].earlierDay()

            elif action_singular == Action.DAY_LATER:
                self.lesson_list[counter].laterDay()

            elif action_singular == Action.TIME_EARLIER:
                self.lesson_list[counter].earlierTime()

            elif action_singular == Action.TIME_LATER:
                self.lesson_list[counter].laterTime()

            counter += 1
            counter %= len(self.lesson_list)

    def get(self, term: Term) -> Lesson:

        lessonTerm = None

        for lesson in self.lesson_list:

            if lesson.term == term:
                lessonTerm = lesson

                break

        return lessonTerm

    def getTotalHours(self, teacher):

        m_dur = 0
        h_dur = 0   

        for lesson in self.lesson_list:
            if lesson.teacher == teacher:
                h_dur += lesson.term.duration // 45 
                m_dur += lesson.term.duration % 45

        return h_dur*45 + m_dur

    def test(self):
        raise ValueError

