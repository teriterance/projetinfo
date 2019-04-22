from random import randint
from domino import *

class Talon(list):
    def __init__(self, size_max = 28):
        self.__size = size_max
        typedejeu = 7   # on peut decider de metttre un jeux, 7 pour un double six, 
                        #10 pour un double neuf
        super().__init__()
        for t in range(typedejeu):
            for i in range(t, typedejeu):
                self.append(Domino(t,i))
        
    @property
    def size(self):
        return self.__size
    
    @size.setter
    def size(self, size_t):
        self.__size = size_t

    def pioche(self):
        '''utilisation de la fonction remove pour retirer un element du talon'''
        if self.size >= 0:
            self.size = self.size - 1
            return self.pop(0)

    def mix(self):
        '''utilisation pour melanger'''
        for i in range(self.size):
            tmp = randint(0,self.size-1) #ongenere un  nombre aleatroire entre 0 et la taille et on echange les positions
            tmpDomino = self[tmp]
            self[tmp] = self[i]
            self[i] = tmpDomino

