from mainJoueur import MainJoueur

class Joueur():
    def __init__(self, numero):
        '''initialisation du joueur, son numero et sa main'''
        self.__numero = numero #identifiant du joueur 
        self.__mainj  = MainJoueur(self.numero)
    
    def doublefort(self):
        '''renvoi le double le plus fort dela main'''
        return self.__mainj.doublefort()

    def dominofort(self):
         '''kdvalbvdlknda'''
         return self.__mainj.dominofort()

    @property
    def numero(self):
        return self.__numero

    def jouer(self):
        '''Fonction de jeux dans le terrain'''
        x, y, orientation = 0, 0, 0 #la position du domino dans le terrain et son orientation( valeurs comprises dans 0, 90, 180, 270)
        print("entrez votre domino a jouer")
        val1, val2 = input()#recuperation des valeurs du domino a jouer
        #on va ajouter le teste de sa presence dans la main 
        self.__mainj.retirer(Domino(val1, val2))#on le suprime de la main
        print("entrez les coordonees x et y du domino")
        x = input()#on lit les coordonee x
        y = input()#on lit les coordonee y
        print("entrez son orientation 0, 90, 180, 270")
        orientation = input()#on lit l'orientation 
        return x,y,orientation

    def piocher(self, talon):
        "Permet de faire une pioche"
        self.mainj.append(talon.pioche())
        return talon
    
    def __str__(self):
        '''On affiche le joueur, juste sa main et son numero'''
        return numero.__str__()+" "+ self.mainj.__str__()