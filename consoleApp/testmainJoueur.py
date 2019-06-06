import unittest
import math
from mainJoueur import MainJoueur

class  MainJoueur(unittest.TestCase):
    def test_init(self):
        m = MainJoueur(1)

    
    def test_taille(self):
        taille=3
        self.assertTrue(3)
        return True
    
#    def test_ajouter(self):
#        x= Domino(4,5,0)
#        y= Domino(3,2,0)
#        z= Domino(2,1,0)
#        MainJoueur1 =[x,y,z]
#        MainJoueur2=[y,z]
#        self.assertEqual(MainJoueur1,MainJoueur2.ajouter(x))
    
#    def test_retirer(self):
#        x= Domino(5,5,0)
#        y= Domino(2,2,0)
#        z= Domino(3,3,0)
#        MainJoueur1 =[x,y,z]
#        MainJoueur2=[x,y]
#        self.assertEqual(MainJoueur1.retirer(z),MainJoueur2)
#        return True
    
    def test_doublefort(self):
        x = Domino(4,4,0)
        y=Domino(3,3,0)
        self.assertGreater(x,y)
        return  True
    
    def test_dominofort(self):
        x = Domino(3,2,0)
        y=Domino(2,1,0)
        self.assertGreater(x,y)
        return  True
    
    def test_get_point(self):
        x= Domino(3,3,0)
        y= Domino(5,2,0)
        z= Domino(1,2,0)
        MainJoueur =[x,y,z]
        nb_point= x[0]+x[1]+y[0]+y[1]+z[0]+z[1]
        self.assertEqual(nb_point,16)
        return True
    
#    def test__str__(self):
#        x= Domino(3,3,0)
#        t=str(x)
#        self.assertEqual(t,"3")
#        return True
        
        
if __name__ == "__main__":
    unittest.main()