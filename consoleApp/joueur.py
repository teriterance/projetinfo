from mainJoueur import MainJoueur
from domino import Domino

class Joueur():
    def __init__(self, numero, nom= ""):
        '''initialisation du joueur, son numero et sa main'''
        self.__numero = numero #identifiant du joueur 
        self.__mainj  = MainJoueur(self.numero)
        self.nomjoueur = nom
    
    def doublefort(self):
        '''renvoi le double le plus fort dela main'''
        return self.__mainj.doublefort()

    def dominofort(self):
         '''kdvalbvdlknda'''
         return self.__mainj.dominofort()
    @property
    def mainj(self):
        return self.__mainj
    
    @property
    def numero(self):
        '''le numero du joueur code la couleur '''
        return self.__numero

    def jouerconsole(self, terrain):
        '''Fonction de jeux dans le terrain'''
        print("voulez vous piocher Oui(O) Non(N)")
        val1 = input()
        if val1 == "O":
            return 9, 0
        print("entrez le domino a jouer, valeur 1 entrer puis valeur 2")
        val1 = int(input())
        val2 = int(input())
        print("entez son orientation, 0, 90, 180, 270")
        orientation = input() 
        d = Domino(val1, val2)
        return d ,orientation

    def jouer(self, domino):
        ''''depose le domino choisi par le joueur sur le terrain'''
        if self.mainj.retirer(domino) != False:
            return True
        else:
            return False

    def piocher(self, talon):
        "Permet de faire une pioche"
        self.mainj.ajouter(talon.pioche())
        return talon
    
    def __str__(self):
        '''On affiche le joueur, juste sa main et son numero'''
        return str(self.numero)+" "+ self.nomjoueur.__str__()+" "+ str(self.mainj)