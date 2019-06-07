import unittest
import math
import numpy as np
from terrainjeux import TerrainJeux
from domino  import Domino

class Test_TerrainJeux(unittest.TestCase):
    '''Fodop'''
    def test_init(self):
        t = TerrainJeux()
        self.assertEqual(len(t), 18)
        self.assertEqual(len(t[1]), 18)
        self.assertEqual(t.tableauCouleur, np.ones([t.taille,t.taille], int)*7)
    
    def test_retourner(self):
        t = TerrainJeux()
        d = Domino(6,5,0)
        self.assertEqual(t.retourner(d),Domino(5,6,0))
        return True
    
    def test_placer(self):
        t = TerrainJeux()
        t2= TerrainJeux()
        t.placer(Domino(6,5,0), 0)
        self.assertNotEqual(t,t2)# on a bien place
        t2.placer(Domino(6,5,0), 90)
        self.assertNotEqual(t,t2)# on a bien place avec des angles different 
        return True

if __name__ == "__main__":
    unittest.main()