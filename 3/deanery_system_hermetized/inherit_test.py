import unittest
from term import Term
from baseterm import BaseTerm
from day import Day
from lesson import Lesson
from teacher import Teacher
from break1 import Break
from timetable2 import Timetable2
from timetable1 import Timetable1

class Test_DSystem(unittest.TestCase):
    #setUp method is called initially, before tests.
    def setUp(self):
        global term1, term2, term3, term4, term5, lesson1, lesson2, lesson3, lesson4, lesson5, lesson6
        global b1, b2, b3, b4, t1, t2, t3, act, actions, table
                
        term1 = Term(8, 0, 90, Day.TUE)
        term2 = Term(9, 35, 90, Day.WED)
        term3 = Term(17, 20, 110, Day.FRI)
        term4 = Term(9, 35, 90, Day.FRI)
        term5 = Term(17, 20, 110, Day.SAT)

        b1 = Break(BaseTerm(9, 30, 5))
        b2 = Break(BaseTerm(11, 5, 10))

        table = Timetable2([b1,b2])

        t1 = Teacher("Teacher", "One")
        t2 = Teacher("Teacher", "Two")


        actions = ["t+", "t-", "t+", "d-"]
        act = table.parse(actions)

        lesson1 = Lesson(table, term1, "Kryptografia", t1, 2)
        lesson2 = Lesson(table, term2, "Spoleczna", t1, 3)
        lesson3 = Lesson(table,term3,"WF",t2,2,full_time=False)
        lesson4 = Lesson(table, term4, "Prog Skrypt", t2, 2)
        lesson5 = Lesson(table, term4, "Skryptowe", t2, 2)
        lesson6 = Lesson(table, term5, "Fizyka", t2, 2, False)

        table.put(lesson1)
        table.put(lesson2)
        table.put(lesson3)
        table.put(lesson4)
        table.put(lesson5)
        table.put(lesson6)

    def test_later_in_total(self):
        #all of those can be put in +term.duration forward in time

        self.assertTrue(lesson1.laterTime())        
        self.assertTrue(lesson2.laterTime())
        self.assertTrue(lesson3.laterTime())
        self.assertTrue(lesson4.laterTime())

    def test_earlier_in_total(self):
        #some can be put in time before -term.duration, some cant be put -term.duration eg. lesson1 cant, be because it would be earlier than 8.

        self.assertFalse(lesson1.earlierTime())
        self.assertTrue(lesson2.earlierTime())
        self.assertFalse(lesson3.earlierTime())
        self.assertTrue(lesson4.earlierTime())

    def test_later_day(self):
        #full_time cant be moved from Friday to saturday.

        self.assertFalse(lesson3.laterDay())

    def test_before_8am(self):
        # can be moved from 9:35 -> 8:00. cant be moved from 8:00 earlier.

        self.assertTrue(lesson2.earlierTime())
        self.assertFalse(lesson2.earlierTime())

    def test_non_full_time_movable(self):
        #False if Non full time tries to move before 17 hour mark, false when tries to move to thursday, True when tried to move to Saturday.

        lesson3 = Lesson(table, Term(19, 20, 120, Day.FRI), "WF", t2, 2,full_time=False)
        self.assertFalse(lesson3.earlierTime())   
        self.assertFalse(lesson3.earlierDay())
        self.assertTrue(lesson3.laterDay())

    def test_raise_value_error_when_parse(self):
        #Raise error when parsing wrong value in actions list.
        table=Timetable1()
        actions = ["t+", "t-", "t+", "d-", "ERROR"]
        
        with self.assertRaises(ValueError):
            table.parse(actions)

    def test_put_same_lesson_twice_value_error(self):
        #lesson 5 cant be put twice in same table.

        table=Timetable1()
        table.put(lesson5)
        with self.assertRaises(ValueError):
            table.put(lesson5)

    def test_skipBreaks(self):
        term1 = Term(8, 0, 90, Day.TUE)
        lesson1 = Lesson(table, term1, "Kryptografia", t1, 2)
        lesson1.laterTime()
        hour,minute = lesson1.term._hour,lesson1.term._minute

        self.assertEqual((hour,minute),(9,35))

    def test_skipBreaks_false(self):
        table.skipBreaks = False
        term1 = Term(8, 0, 90, Day.TUE)
        lesson1 = Lesson(table, term1, "Kryptografia", t1, 2)

        self.assertEqual(lesson1.laterTime(),False)

if __name__ == '__main__':
    unittest.main()