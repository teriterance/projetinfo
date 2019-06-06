from joueur import Joueur
from terrainjeux import TerrainJeux
from domino import Domino
import math 
import random
class JoueurAI(Joueur):

    def __init__(self, numero, nom):
        '''le terrain sera pris en entree du joueur, et serra mis a jour plustard'''
        super().__init__( numero, nom)

    def jouerconsole(self,terrain):
        dom_max = None
        max_val = 0
        angleMax = None
        angleAlea = random.randint(0,3)
        angle = [0, 90, 180, 270]
        print(self.mainj)
        for dom in self.mainj:
            #ici in teste tous les dominos restants
            t = True
            for j in range(4):
                if (terrain.dombout == dom[0] or terrain.dombout == dom[1]) and t and j == angleAlea: 
                    if (terrain.boutChaine[0] > terrain.taille - 2) and angle[j] == 270:
                        continue
                    elif (terrain.boutChaine[1] > terrain.taille - 2) and angle[j] == 0:
                        continue
                    elif (terrain.boutChaine[0] <= 1) and angle[j] == 90:
                        continue
                    elif(terrain.boutChaine[1] <= 1) and angle[j] == 180:
                        continue

                    t = False
                    val = sum(dom)
                    if val > max_val:
                        max_val = val
                        dom_max = dom
                        angleMax = angle[j]
        if dom_max != None:
            print("IA joue")
            return dom_max, angleMax
        else:
            return 9, 0