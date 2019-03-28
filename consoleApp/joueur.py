from mainJoueur import *
from terrainjeux import *

class Joueur():
    def __init__(self, numero):
        self.numero = numero #identifiant du joueur 
        self.main   = MainJoueur(self.numero)
    
    def jouer(self):
        pass
    
    def t(self):
        pass