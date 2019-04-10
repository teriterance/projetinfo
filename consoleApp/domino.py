import numpy as np
import math

class Domino(list):
    
    def __init__(self, num1, num2, color = 0):
        '''initialisation du domino comme deux valeurs lie,
        plutard nous introduirons le concepte de couleur'''
        if (num1 <= 6 and num1>= 0) and (num2 >= 0 and num2 <= 6):
            self.append(num1)
            self.append(num2)
        else:
            print("les valeur doivent etre entre 0 et 6")
        self.__Color = color #donne les valeur par defaut de la couleur a 0

    @property
    def color(self):
        '''le getter de color'''
        return self.__Color
    
    @color.setter
    def color(self, color):
        '''le setter de color'''
        self.__Color = color

    @property
    def get_Value(self):
        ''' cette fonction permet d'atribuer les valeur des parties du domino'''
        return self
    
    def nb_point(self):
        '''cette fonction retourne le nombre de point du domino utile pour l'IA'''
        return sum(self)

    def isdouble(self):
        '''retourne la valeur du double si le domino est un double '''
        if self[0] == self[1]:
            return self[0]
        else: 
            return False