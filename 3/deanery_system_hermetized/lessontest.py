import unittest
from timetable1 import Timetable1
from lesson import Lesson
from day import Day
from term import Term
from action import Action

class Test_lesson_methods(unittest.TestCase):

    def test_earlierDay_full_time_true(self):
        
        blankTimeTable = Timetable1()
        lesson0 = Lesson(blankTimeTable, Term(9, 35,90, Day.TUE), "BLANK", "BLANK", 2)
        self.assertEqual(lesson0.earlierDay(), True)

    def test_earlierDay_full_time_false(self):

        blankTimeTable = Timetable1()
        lesson1 = Lesson(blankTimeTable, Term(9, 35,90, Day.MON), "BLANK", "BLANK", 2)
        self.assertEqual(lesson1.earlierDay(), False)

    def test_earlierDay_non_full_time_true(self):

        blankTimeTable = Timetable1()
        lesson2 = Lesson(blankTimeTable, Term(17, 35,90, Day.SAT), "BLANK", "BLANK", 2)
        self.assertEqual(lesson2.earlierDay(), True)

    def test_earlierDay_non_full_time_false(self):

        blankTimeTable = Timetable1()
        lesson3 = Lesson(blankTimeTable, Term(9, 35,90, Day.SAT), "BLANK", "BLANK", 2)
        self.assertEqual(lesson3.earlierDay(), False)
    
    def test_laterDay_full_time_true(self):

        blankTimeTable = Timetable1()
        lesson0 = Lesson(blankTimeTable, Term(9, 35,90, Day.TUE), "BLANK", "BLANK", 2)
        self.assertEqual(lesson0.laterDay(), True)

    def test_laterDay_full_time_false(self):

        blankTimeTable = Timetable1()
        lesson1 = Lesson(blankTimeTable, Term(17, 35,90, Day.THU), "BLANK", "BLANK", 2)
        self.assertEqual(lesson1.laterDay(), False)

    def test_laterDay_non_full_time_true(self):

        blankTimeTable = Timetable1()
        lesson2 = Lesson(blankTimeTable, Term(14, 35,90, Day.SAT), "BLANK", "BLANK", 2)
        self.assertEqual(lesson2.laterDay(), True)

    def test_laterDay_non_full_time_false(self):

        blankTimeTable = Timetable1()
        lesson3 = Lesson(blankTimeTable, Term(9, 35,90, Day.SUN), "BLANK", "BLANK", 2)
        self.assertEqual(lesson3.laterDay(), False)

    def test_earlierTime_full_time_true(self):

        blankTimeTable = Timetable1()
        lesson0 = Lesson(blankTimeTable, Term(9, 35,90, Day.TUE), "BLANK", "BLANK", 2)
        self.assertEqual(lesson0.earlierTime(), True)

    def test_earlierTime_full_time_false(self):

        blankTimeTable = Timetable1()
        lesson1 = Lesson(blankTimeTable, Term(8, 5,90, Day.MON), "BLANK", "BLANK", 2)
        self.assertEqual(lesson1.earlierTime(), False)

    def test_earlierTime_non_full_time_true(self):

        blankTimeTable = Timetable1()
        lesson2 = Lesson(blankTimeTable, Term(17, 35,90, Day.SAT), "BLANK", "BLANK", 2)
        self.assertEqual(lesson2.earlierTime(), True)

    def test_earlierTime_non_full_time_false(self):

        blankTimeTable = Timetable1()
        lesson3 = Lesson(blankTimeTable, Term(17, 35,90, Day.FRI), "BLANK", "BLANK", 2)
        self.assertEqual(lesson3.earlierTime(), False)
    

    def test_laterTime_non_full_time_false(self):

        blankTimeTable = Timetable1()
        lesson3 = Lesson(blankTimeTable, Term(17, 35,90, Day.SUN), "BLANK", "BLANK", 2)
        self.assertEqual(lesson3.laterTime(), False)



if __name__ == '__main__':
    unittest.main()