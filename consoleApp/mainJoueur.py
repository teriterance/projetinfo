from domino import Domino

class MainJoueur(list):
    def __init__(self,joueur):
        ''' '''
        self.__Joueur = joueur
        self.__taille = 0
        super().__init__()

    @property
    def taille(self):
        '''utilise pour connaitre la taille de la main du joueur'''
        return self.__taille

    def ajouter(self, domino):
        '''redefinition de la fonction d'ajout pour ajouter un nouvel ellement dans notre main'''
        super().append(domino)
        self.taille = self.taille + 1
        return domino
    
    def retirer(self, domino):
        '''utilisation de la fonction remove pour retirer un element de la main'''
        if self.__taille >= 0:
            self.__taille = self.__taille - 1
            return self.remove(domino)
        return False

    def doublefort(self):
        '''retourne le domino le plus fort si il exite et false si non'''
        doublemax = [0,0]
        for domino in self:
            if  domino.isdouble() and sum(domino) > sum(doublemax):
               doublemax = domino 
        return doublemax
            

    def dominofort(self):
        '''retourne le domino le plus fort si il exite et false si non
        elle doit etre utilise en lieu et place de la fonction double max si elle retrourne false'''
        maxval = 0
        dominomax = 0
        for domino in self:
            x = domino.nb_point()
            if maxval < x:
                dominomax = domino
                maxval = x
        return dominomax

    def get_point(self):
        '''compte tous les point de la main, important pour la fonction d'evaluation du minimax'''
        tmp = 0
        for domino in self:
            tmp = domino.nb_point() + tmp
        return tmp