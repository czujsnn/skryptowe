import unittest
from timetable1 import Timetable1
from lesson import Lesson
from day import Day
from term import Term
from action import Action

class Test_timetable1(unittest.TestCase):

    def test_put_true(self):
        timetable = Timetable1()
        lesson = Lesson(timetable,Term(15,30,90, Day.FRI), "Programowanie skryptowe", "Stanisław Polak", 2)
        self.assertEqual(timetable.put(lesson), True)

    def test_put_false(self):

        timetable = Timetable1()
        lesson = Lesson(timetable,Term(15,30,90, Day.FRI), "Programowanie skryptowe", "Stanisław Polak", 2)
        lesson2 = Lesson(timetable,Term(16,30,90, Day.FRI), "Programowanie skryptowe", "Stanisław Polak", 2)
        timetable.put(lesson)
        self.assertEqual(timetable.put(lesson2), False)

    def test_get_lesson(self):

        timetable = Timetable1()
        term = Term(15, 30,90, Day.FRI)
        lesson = Lesson(timetable,Term(15,30,90, Day.FRI), "Programowanie skryptowe", "Stanisław Polak", 2)
        timetable.put(lesson)
        self.assertEqual(timetable.get(term), lesson)

    def test_get_None(self):

        timetable = Timetable1()
        term = Term(9, 30,90, Day.TUE)
        lesson = Lesson(timetable, term, "-", "-", 2)
        self.assertEqual(timetable.get(lesson), None)

    def test_busy_match(self):

        timetable = Timetable1()
        lesson = Lesson(timetable,Term(15,30,90, Day.FRI), "Programowanie skryptowe", "Stanisław Polak", 2)
        timetable.put(lesson)
        self.assertEqual(timetable.busy(lesson.term), True)

    def test_busy_after_beginning_hour(self):

        timetable = Timetable1()
        lesson = Lesson(timetable,Term(9,30,90, Day.FRI), "Programowanie skryptowe", "Stanisław Polak", 2)
        timetable.put(lesson)
        term = Term(10, 30, 90, Day.FRI)
        self.assertEqual(timetable.busy(term), True)

    def test_busy_false(self):

        timetable = Timetable1()
        lesson = Lesson(timetable,Term(9,30,90, Day.FRI), "Programowanie skryptowe", "Stanisław Polak", 2)
        lesson2 = Lesson(timetable,Term(9,30,90, Day.THU), "Programowanie skryptowe", "Stanisław Polak", 2)
        self.assertEqual(timetable.busy(lesson2.term), False)

    def test_can_be_transfered_to_true(self):

        timetable = Timetable1()
        term = Term(9, 30,90, Day.TUE)
        term2 = Term(12, 00,90, Day.TUE)
        lesson = Lesson(timetable, term, "-", "-", 2)
        timetable.put(lesson)
        self.assertEqual(timetable.can_be_transferred_to(term2, True), True)

    def test_can_be_transfered_to_false(self):
        
        timetable = Timetable1()
        term = Term(9, 30, 90, Day.TUE)
        term2 = Term(11, 00, 90, Day.SAT)
        lesson = Lesson(timetable, term, "-", "-", 2)
        timetable.put(lesson)
        self.assertEqual(timetable.can_be_transferred_to(term2, True), False)

    def test_parase(self):

        timetable = Timetable1()
        strl = ['d-', 'd+', 't-', 't+']
        action = [Action.DAY_EARLIER, Action.DAY_LATER, Action.TIME_EARLIER, Action.TIME_LATER]
        self.assertEqual(timetable.parse(strl), action)
    
    def test_peform(self):

        timetable = Timetable1()
        timetable2 = Timetable1()

        term = Term(8,00,90, Day.WED)
        lesson = Lesson(timetable2, term, 'less1', 'less1', 2)
        action = [Action.DAY_EARLIER, Action.DAY_LATER, Action.TIME_EARLIER, Action.TIME_LATER]

        timetable.put(lesson)
        timetable2.put(lesson)
        
        timetable2.perform(action)

        self.assertEqual(timetable2.lesson_list, timetable.lesson_list)


if __name__ == '__main__':
    unittest.main()