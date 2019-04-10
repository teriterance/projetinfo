from domino import Domino
from joueur import Joueur
from joueurAI import JoueurAI
from talon import Talon
from terrainjeux import TerrainJeux

class Jeux():
    def __init__():
        #on creait le terrain 
        self.terrain = TerrainJeux()
        #on cree la pioche ou talon
        self.talon = Talon()
        #on demande le nombre de joueur ceci se fera dans une boite de dialogue 
        self.nombreJoueur = 0
        #on creai les joueru 
        self.listeJoueur = [Joueur(i) for i in range(self.nombreJoueur)]
        #on deffinit le joueur actuel
        self.__joueurActuel = 0

    def distribution(self):
        "cette fonction fait la distribution des dominos aux joueurs"
        #on fait la distribution des dominos aux joueurs pour ce faire on 
        #passe dans deux boucles qui vont donner les dominos aux joueurs 
        for i in range(self.nombreJoueur):
            for i in range(7):
                self.talon = self.listeJoueur[i].(self.talon)
    
    def premierJoueur(self):
        "cette fonction retourne le premier joeur et le domino qu'il dois jouer"
        #on cherche le joueur qui a le double le plus fort
        # en meme temp celui qui a la main la plus forte  
        maxdouble =  0
        maxDoubleJoueur = self.nombreJoueur #initialisation du joueur hors de la liste  
        maxval = 0
        maxValJoueur = self.nombreJoueur#initialisation du joueur hors de la liste
        #on percour la liste des joueurs
        for i in range(self.nombreJoueur):
            doubleTmp = self.listeJoueur[i].doublefort()
            if doubleTmp > maxdouble:
                maxdouble = doubleTmp
                maxdoublejoueur = i
            valTmp = self.listeJoueur[i].dominofort()
            if valTmp > maxdouble:
                maxval = valTmp
                maxValJoueur = i
        if maxDoubleJoueur < self.nombreJoueur:
            self.__joueurActuel = maxDoubleJoueur
        else:
            self.__joueurActuel = maxDoubleJoueur

    def joeursuivant(self):
        
        slef.__joueurActuel = self.__joueurActuel + 1

                        