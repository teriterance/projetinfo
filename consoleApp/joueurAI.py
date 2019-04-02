from joueur import *
import math 
'''Notre joueur AI va prendre un coup comme une combinaison X Y de deux valeurs entieres'''
class JoueurAI(Joueur):

    def __init__(selff, terain, numero):
        '''le terrain sera pris en entree du joueur, et serra mis a jour plustard'''
        super().__init__(self, numero)
        self.__terrain = terrain
        self.etat_jeux = None
        self.coup =  None
    
    @property
    def terrain(self):
        return self.__terrain
    
    @terain.setter
    def terrain(self, terrain):
        '''En premiere idee cette fonction n'a auccune utilite mais il est facile de se rendre compte de 
        l'interet de pouvoir attribuer un terain dans un etat precis et voir le comportement de notre bot '''
        self.__terain = terrain

    def min(self, prof):
        '''cette fonction retourne une evaluation ninimale du de la valeur Min'''
        if prof == 0 :
            return eval(etat_jeux)
        
        min_val = math.inf
        
        tailleTerain = 56 ## a modifier 
        for i in range(tailleTerain):
            for j in range(tailleTerain):
                self.simuller(x,y)
                val = Max(eta,prof-1)

                if val <min_val:
                    min_val = val
        return min_val
        
    
    def max(self,prof):
        '''cette fonction retourne une evaluation ninimale du de la valeur Min'''
        if prof == 0 :
            return eval(etat_jeux)
        
        max_val = -1 * math.inf
        
        tailleTerain = 56 ## a modifier 
        for i in range(tailleTerain):
            for j in range(tailleTerain):
                self.simuller(x,y)
                val = Max(eta,prof-1)

                if val >max_val:
                    max_val = val
        return min_val 
    
    def eval(self):
        pass

    def simuller(self):
        pass