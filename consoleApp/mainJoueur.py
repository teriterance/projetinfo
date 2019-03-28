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
    
    @taille.setter
    def taille(self, taille):
        '''On reste un peut dubitatif quant a l'usage de cette fonction'''
        self.__taille = taille

    def ajouter(self, domino):
        '''redefinition de la fonction d'ajout pour ajouter un nouvel ellement dans notre main'''
        super().append(domino)
        self.taille = self.taille + 1
        return domino
    
    def retirer(self, domino):
        '''utilisation de la fonction remove pour retirer un element de la main'''
        if self.taille >= 0:
            return self.remove(domino)
        return False
    
    def get_point(self):
        '''compte tous les point de la main, important pour la fonction d'evaluation du minimax'''
        tmp = 0
        for domino in self:
            tmp = domino.nb_point() + tmp
        return tmp