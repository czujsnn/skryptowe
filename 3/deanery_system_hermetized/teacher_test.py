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
    def setUp(self):
        global term1, term2, term3, term4, term5, lesson1, lesson2, lesson3, lesson4, lesson5, lesson6
        global b1, b2, b3, b4, t1, t2, t3, act, actions, table
                
        term1 = Term(8, 0, 90, Day.MON)
        

        table = Timetable2([""])

        t1 = Teacher("Teacher", "One")
        t2 = Teacher("Teacher","Two")
        t3 = Teacher("Teacher","Two")

        lesson1 = Lesson(table,term1,"SAMPLE",t1,2,True)
        lesson2 = Lesson(table,term1,"SAMPLE2",t2,2,True)

        table.put(lesson1)
        table.put(lesson2)

    def test_basic_teacher_addition(self):
        self.assertEqual(lesson1 + t2, True)
        self.assertEqual(lesson2 + t1, True)

    def test_basic_teacher_substraction(self):

        self.assertEqual(lesson1 - t1, True)
        self.assertEqual(lesson2 - t2, True)
        self.assertEqual(lesson1._Lesson__teacher.imie,None)

    

if __name__ == '__main__':
    unittest.main()