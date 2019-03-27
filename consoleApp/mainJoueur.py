from domino import *

class MainJoueur(list):
    def __init__(self,joueur):
        ''' '''
        self.__Joueur = joueur
        self.__size = 0
        super().__init__()

    @property
    def size(self):
        return self.__size
    
    @size.setter
    def size(self, size_t):
        self.__size = size_t

    def append(self, domino):
        '''redefinition de la fonction d'ajout pour ajouter un nouvell ellement dans notre main'''
        super().append(domino)
        self.size = self.size + 1
        return domino
    
    def retirer(self, domino):
        '''utilisation de la fonction remove pour retirer un element de la main'''
        if self.size >= 0:
            self.remove(domino)
        return domino
    
    def get_point(self):
        '''compte tous les point de la main, important pour la fonction d'evaluation du minimax'''
        tmp = 0
        for domino in self:
            tmp = domino.nb_point() + tmp
        return tmp