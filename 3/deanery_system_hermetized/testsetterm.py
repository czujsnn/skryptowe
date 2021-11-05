from typing import ValuesView
import unittest
from day import Day
from term import Term


class Test_set_term(unittest.TestCase):

    def test_term1(self):

        term1 = Term(4,20,121,Day.MON)
        date1 = "27 I 2021 8:00 - 28 X 2021 21:00"
        term1.setTerm(date1)
        values = (term1._hour,term1._minute,term1._duration,term1._Term__day.value)
        self.assertEquals(values,(8, '00', 391020, 3))

    def test_term2(self):

        term1 = Term(8,30,1511,Day.TUE)
        date2 = "1 I 2021 11:00 - 1 I 2021 12:59"
        term1.setTerm(date2)
        values = (term1._hour,term1._minute,term1._duration,term1._Term__day.value)
        self.assertEqual(values,(11, '00', 119, 5))

    def test_term3(self):

        term1 = Term(1,30,90,Day.FRI)
        date3 = "5 V 2021 12:40 - 5 V 2021 12:41"
        term1.setTerm(date3)
        values = (term1._hour,term1._minute,term1._duration,term1._Term__day.value)

        self.assertEqual(values,(12, '40', 1,3))

if __name__ == '__main__':
    unittest.main()