from joueur import Joueur
from terrainjeux import TerrainJeux
import math 
'''Notre joueur AI va prendre un coup comme une combinaison X Y de deux valeurs entieres'''
class JoueurAI(Joueur):
    '''Fodop'''
    def __init__(self, terain, numero):
        '''le terrain sera pris en entree du joueur, et serra mis a jour plustard'''
        super().__init__(self, numero)
        self.__terrain = terrain.copy()
        self.jeu = jeux
        self.etat_jeux = None
        self.coup =  None

    def ninmaxMin(self, prof, dominrestan, terrain):
        '''cette fonction retourne une evaluation ninimale du de la valeur Min'''
        if prof == 0 or self.mainj.size == 0:
            #on evalue dl'etat du jeux
            return eval(etat_jeux)
        
        min_val = 100000
        #on teste tous les coup possible 
        #le tableau des angles
        for dom in dominrestan:
            #pour tout les dominos de la main du joueur 
            for angle in [0,90,180,270]:
                t = terrain.copy()
                if t.placer(dom, angle) != False:
                    val = ninmaxMax(prof-1, dominrestan, t)
                    if val <min_val:
                        min_val = val
        return min_val
    
    def ninmaxMax(self,prof, dominrestan, terrain):
        '''cette fonction retourne une evaluation ninimale du de la valeur Min'''
        if prof == 0 or self.mainj.size == 0:
            return eval(etat_jeux)

        max_val = -100000
        #on teste tous les coups possibles 
        for dom in self.mainj:
            #ici in teste tous les dominos restants
            for angle in [0,90,180,270]:
                t = terrain.copy()
                if t.placer(dom, angle) != False:
                    val = ninmaxMin(prof-1, dominrestan, t)
                    if val > max_val:
                        max_val = val
        return min_val 
    
    def eval(self, t):
        u = self.mainj.get_point()
            return 1000 - u
        return self.mainj.get_point()
    
    def jouer(self, prof, dominrestan, terrain):
        terrain = self.terrain
        max_val = -100000

        meilleurDom = None
        meilleurAngle = None

        for dom in self.mainj:
            #ici in teste tous les dominos restants
            for angle in [0,90,180,270]:
                t = self.terrain.copy()
                if t.placer(dom, angle) != False:
                    val = ninmaxMin(prof-1, dominrestan, t.copy())
                    if val >max_val:
                        max_val = val
                        meilleurAngle, meilleurDom = angle , dom
        return meilleurDom, meilleurAngle