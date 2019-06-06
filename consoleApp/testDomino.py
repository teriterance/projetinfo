import unittest
import math
from domino import Domino

class TestDomino(unittest.TestCase):
    def test_init(self):
        pass
    
    def test_eq(self):
        x = Domino(6,5,0)
        y=Domino(6,5,0)
        self.assertEqual(x,y)
        return  True
    
    def test_nb(self):
        z = Domino(6,5,0)
        somme = 11
        self.assertEqual(somme, z.nb_point())
        return True
    
    def test_get_Value(self):
        x = Domino(6,5,0)
        num1, num2, colo = x.get_Value
        self.assertEqual(num1, 6)
        self.assertEqual(num2, 5)
        self.assertEqual(colo, 0)
        return True
    
    def test_isdouble(self):
        x = Domino(6,6)
        self.assertTrue(x.isdouble())
        return True

    def test_cherche(self):
        y=Domino(6,5)
        self.assertTrue(y.cherche(6))
        self.assertTrue(y.cherche(5))
        return True

if __name__ == "__main__":
    unittest.main()