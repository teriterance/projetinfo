import unittest
import math
from joueur import Joueur

class Joueur(unittest.TestCase):
    def test_doublefort(self):
        x = Domino(6,6,0)
        y=Domino(5,5,0)
        self.assertGreater(x,y)
        return  True
    
    def test_dominofort(self):
        x = Domino(6,6,0)
        y=Domino(6,5,0)
        self.assertGreater(x,y)
        return  True
    
    def test_mainj(self):
        pass
    
    def test_numero(self):
        numero= 2
        self.assertTrue(numero)
        return True
    
    def test_jouerconsole(self):
        d = Domino(6,2,0)
        val1=d[0]
        val2=d[1]
        orientation= 180
        self.assertEqual(val1,6)
        self.assertEqual(val2,2)
        return True

#    def test_jouer(self):
#        x = Domino(6,6,0)
#        y= Domino(5,5,0)
#        z = Domino(4,4,0)
#        t=Domino(3,3,0)
#        terrain=[x,y,z]
#        terrain2=[x,y,z,t]
#        self.assertEqual(terrain.placer(t,90),terrain2)
#        return True
#    
    def test_piocher(self):
        pass
    
    def test__str__(self):
        pass
    
if __name__ == "__main__":
    unittest.main()