# -*- coding: utf-8 -*-
"""
Created on Wed May 29 16:10:00 2019

@author: fonenswi
"""

#les tests unitaitres

import unittest
import math
from terrainjeux import *

class TerrainJeux(unittest.TestCase):
    def test_init(self):
        pass
    
    def test_str2(self):
        y=Domino(5,5,0)
        t="domino"
        s=t+str(y[1])
        self.assertEqual(s,"domino5")
        return True
        
    
    def test_retourner(self):
        x=Domino(6,5,0)
        self.assertEqual(x[0],6)
        self.assertEqual(x[1],5)
        return True
    
    def test_placer(self):
        x=Domino(6,5,0)
        placer1=(x,180,0)
        placer2=(x,180,0)
        self.assertEqual(placer1,placer2)
        return True
    
#    def  test__str__(self):
#        y=Domino(5,5,0)
#        t="domino*"
#        s=t+str(y[1])
#        self.assertEqual(s,"domino*5")
#        return True

if __name__ == "__main__":
    unittest.main()