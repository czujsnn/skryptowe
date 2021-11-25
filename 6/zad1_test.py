import unittest
from zad1 import Operacje


class Test_Zad1(unittest.TestCase):

        
    def test_sum(self):
        op = Operacje()
        self.assertEqual(op.sum(1, 1, 1), 4) #4 to pierwszy wolny element z tablicy
        self.assertEqual(op.sum(1,1),5)
        self.assertEqual(op.sum(1),None)

    def test_error_msg(self):
        op=Operacje()
        with self.assertRaises(TypeError):
            op.sum()

    def test_operator_substraction(self):
        op=Operacje()
        self.assertEqual(op.substraction(1,1), 4)
        self.assertEqual(op.substraction(1), 5)
        self.assertEqual(op.substraction(), 6)

    def test_change_val_of_sum(self):
        op=Operacje()
        op['suma']=[8,9]
        self.assertEqual(op.sum(1), None)
        self.assertEqual(op.sum(1, 1), 9)
        self.assertEqual(op.sum(1, 1, 1), 8)

    def test_change_val_of_substraction(self):
        op=Operacje()
        op['roznica']=[10,11,12]
        self.assertEqual(op.substraction(), 12)
        self.assertEqual(op.substraction(1), 11)
        self.assertEqual(op.substraction(1, 1), 10)
    
if __name__ == "__main__":
    unittest.main()