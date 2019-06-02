from joueur import Joueur
from terrainjeux import TerrainJeux
from domino import Domino
import math 
class JoueurAI(Joueur):

    def __init__(self, numero, nom):
        '''le terrain sera pris en entree du joueur, et serra mis a jour plustard'''
        super().__init__( numero, nom)

    def jouerconsole(self,terrain):
        dom_max = None
        max_val = 0
        angleMax = None
        print(self.mainj)
        for dom in self.mainj:
            #ici in teste tous les dominos restants
            t = True
            for angle in [0,90,180,270]:
                if (terrain.dombout == dom[0] or terrain.dombout == dom[1]) and t:
                    t = False
                    val = sum(dom)
                    if val > max_val:
                        max_val = val
                        dom_max = dom
                        angleMax = angle
        if dom_max != None:
            print("IA joue")
            return dom_max, angleMax
        else:
            return 9, 0