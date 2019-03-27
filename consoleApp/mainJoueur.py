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
        ''' '''
        super().append(domino)
        self.size = self.size + 1
        return domino
    
    def retirer(self, domino):
        ''' '''
        if self.size >= 0:
            self.remove(domino)
        
        return domino
    
    def get_point(self):
        ''' '''
        tmp = 0
        for domino in self:
            tmp = domino.nb_point()+tmp
        return tmp