import unittest
import math
from talon import Talon

class TestTalon(unittest.TestCase):
    def test_init(self):
        t = Talon()
        self.assertEqual(len(t), t.size)
    
    def test_pioche(self):
        t = Talon()
        t2 = Talon()
        self.assertEqual(t, t2)# on doit verifier que les listes soit bien egales
        t.pioche()
        self.assertNotEqual(len(t), len(t2))
        return True
    
    def test_mix(self):
        t = Talon()
        t2 = Talon()
        self.assertEqual(t, t2)# on doit verifier que les listes soit bien egales
        t2.mix()
        self.assertNotEqual(t, t2)
        return True
    
    def test_EstDans(self):
        t = Talon()
        self.assertTrue(not t.estDans(6))# est dans renvoi false pour true

if __name__ == "__main__":
    unittest.main()