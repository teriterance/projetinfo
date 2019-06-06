import unittest
import math
from mainJoueur import MainJoueur
from domino import Domino

class  Test_MainJoueur(unittest.TestCase):
    def test_init(self):
        ma = MainJoueur(1)
        self.assertEqual(len(ma), 0)
        return True
    
    def test_taille(self):
        m = MainJoueur(1)
        m.ajouter(Domino(2,3),1)
        m.ajouter(Domino(2,3),1)
        self.assertEqual(len(m), 2)
        
        m.ajouter(Domino(2,3),1)
        m.ajouter(Domino(2,3),1)
        self.assertEqual(len(m), 4)
        return True
    
    def test_ajouter(self):
        m = MainJoueur(1)
        m.ajouter(Domino(4,5),1)
        self.assertEqual(m[0], Domino(4,5))
        self.assertEqual(len(m), 1)
        return True
    
    def test_retirer(self):
        m = MainJoueur(1)
        m.ajouter(Domino(5,5,0),1)
        m.ajouter(Domino(2,2,0),1)
        m.retirer(Domino(5,5,0))
        self.assertEqual(Domino(2,2,0), m[0])
        return True
    
    def test_doublefort(self):
        m = MainJoueur(1)
        m.ajouter(Domino(5,5,0),1)
        m.ajouter(Domino(2,2,0),1)
        self.assertEqual(Domino(5,5,0), m.doublefort())
        return  True
    
    def test_dominofort(self):
        m = MainJoueur(1)
        m.ajouter(Domino(5,4,0),1)
        m.ajouter(Domino(3,2,0),1)
        m.ajouter(Domino(3,3,0),1)
        self.assertEqual(Domino(5,4,0), m.dominofort())
        return  True
    
    def test_get_point(self):
        m = MainJoueur(1)
        m.ajouter(Domino(3,3,0),1)
        m.ajouter(Domino(5,2,0),1)
        m.ajouter(Domino(1,2,0),1)
        self.assertEqual(m.get_point(),16)
        return True
        
if __name__ == "__main__":
    unittest.main()