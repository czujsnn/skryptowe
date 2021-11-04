from typing import List
from day import Day
from action import Action
from lesson import Lesson
from term import Term

class Timetable1:
    """ Class containing a set of operations to manage the timetable """

##########################################################
    def can_be_transferred_to(self, term: Term, full_time: bool) -> bool:

        if term.hour < 8:
            return False

        endTime = term.getEndTime()
        print(endTime)
        


        pass
        """
Informs whether a lesson can be transferred to the given term

Parameters
----------
term : Term
    The term checked for the transferability
full_time : bool
    Full-time or part-time studies

Returns
-------
bool
    **True** if the lesson can be transferred to this term
"""

        pass

##########################################################

    def busy(self, term: Term) -> bool:

        for lesson in self.lesson_list:
            if lesson.term == term:
                return True

            lesson_start = (lesson.term.hour, lesson.term.minute)
            lesson_end = lesson.term.getEndTime()
            term_lesson_start = (term.hour, term.minute)
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


        """
Informs whether the given term is busy.  Should not be confused with ``can_be_transfered_to()``
since there might be free term where the lesson cannot be transferred.

Parameters
----------
term : Term
    Checked term

Returns
-------
bool
    **True** if the term is busy
        """

        pass

 ##########################################################

    def put(self, lesson: Lesson) -> bool:
        """
Add the given lesson to the timetable.

Parameters
----------
lesson : Lesson
    The added  lesson

Returns
-------
bool
    **True**  if the lesson was added.  The lesson cannot be placed if the timetable slot is already occupied.
        """

        pass

##########################################################

    def parse(self, actions: List[str]) -> List[Action]:
        """
Converts an array of strings to an array of 'Action' objects.

Parameters
----------
actions:  List[str]
    A list containing the strings: "d-", "d+", "t-" or "t+"

Returns
-------
    List[Action]
        A list containing the values:  DAY_EARLIER, DAY_LATER, TIME_EARLIER or TIME_LATER
        """

        action_list = []

        for singularAction in actions:

            if singularAction in Action._value2member_map_:
                action_list.append(Action(singularAction))

        return action_list


##########################################################

    def perform(self, actions: List[Action]):
        """
Transfer the lessons included in the timetable as described in the list of actions. N-th action should be sent the n-th lesson in the timetable.

Parameters
----------
actions : List[Action]
    Actions to be performed
        """

        pass
##########################################################

    def get(self, term: Term) -> Lesson:
        """
Get object (lesson) indicated by the given term.

Parameters
----------
term: Term
    Lesson date

Returns
-------
lesson: Lesson
    The lesson object or None if the term is free
        """

        pass

t1 = Timetable1()
z=t1.parse(["d-","d+","AAA","--"])
print(z)
term2 = Term(10,00,90,Day.MON)
t1.can_be_transferred_to(term2,True)