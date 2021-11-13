from typing import List
from day import Day
from action import Action
from lesson import Lesson
from term import Term

class Timetable1:
    """ Class containing a set of operations to manage the timetable """

    def __init__(self):
        self.lesson_list = []

    def __str__(self):

        self.translate = {"MON":"Poniedziałek","TUE":"Wtorek","WED":"Środa","THU":"Czwartek","FRI":"Piątek","SAT":"Sobota","SUN":"Niedziela"}
        termList = []

        for lesson in self.lesson_list:
            termList.append(lesson.term)

        termList = sorted(termList)
        displayTimetable = []

        for iter8Times in range(8):
            displayTimetable.append([])

            for _ in range(len(termList) + 1):
                displayTimetable[iter8Times].append('')
        
        for day in Day:
            displayTimetable[day.value][0] = self.translate[day.name]  #translate MON,TUE etc. to Poniedziałek, wtorek etc.

        counter =0
        for term in termList:
            
            displayTimetable[0][counter + 1] = f'{term.getStartTime_pr()}-{term.getEndTime()}'
            counter += 1

        for lesson in self.lesson_list:
            displayTimetable[lesson.term.day.value][termList.index(lesson.term) + 1] = lesson.name

        #concatenate padding and make printable timetable.

        paddingStarBlock = f'\n{"": ^12}{"*"*92}\n'
        timeTablePrintable = ""

        for line in range(len(termList) + 1):
            for row in range(8):

                timeTablePrintable += f'{displayTimetable[row][line]: ^12}*'
            timeTablePrintable += paddingStarBlock

        return timeTablePrintable

##########################################################
    def can_be_transferred_to(self, term: Term, full_time: bool) -> bool:

        if term.hour < 8:
            return False

        endtime = term.getEndTime().split(":")
        endtime[0],endtime[1] = int(endtime[0]),int(endtime[1]) #date like 17:00 is split between semicolon - then looks like ["17","00"], then both are converted to int.

        if endtime[0] > 20:
            return False

        if endtime[0] == 20 and endtime[1] > 0:
            return False

        if not self.busy(term):

            if term._Term__day.value < 5:
                is_fulltime = True

            elif term._Term__day.value > 5:
                is_fulltime = False

            else:

                if term._hour < 17:
                    is_fulltime = True

                else:

                    is_fulltime = False

            if is_fulltime == full_time:
                return True

        return False


##########################################################

    def busy(self, term: Term) -> bool:
        
        for lesson in self.lesson_list:

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

        if self.busy(lesson._term):
            return False

        else:

            self.lesson_list.append(lesson)
            return True

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

        lessonTerm = None

        for lesson in self.lesson_list:

            if lesson.term == term:
                lessonTerm = lesson

                break

        return lessonTerm


if __name__ == "__main__":

    timetable = Timetable1()
    lesson = Lesson(timetable,Term(15,30,90, Day.FRI), "Prog. skr.", "Stanisław Polak", 2)
    timetable.put(lesson)
    lesson2 = Lesson(timetable,Term(8,30,90, Day.MON), "WF", "wfman", 2)
    timetable.put(lesson2)
    lesson3 = Lesson(timetable,Term(12,30,90, Day.MON), "Krypto", "Paweł Topa", 2)
    lesson4 = Lesson(timetable,Term(10,30,90, Day.TUE), "Fizyka ĆW", "Gabriela Lewińska", 2)
    lesson5 = Lesson(timetable,Term(12,30,90, Day.TUE), "Fizyka LAB", "Gabriela Lewińska", 2)
    lesson6 = Lesson(timetable,Term(14,30,60, Day.WED), "Fizyka LAB", "Gabriela Lewińska", 2)
    timetable.put(lesson3)
    timetable.put(lesson4)
    timetable.put(lesson5)
    timetable.put(lesson6)
    print(timetable)
