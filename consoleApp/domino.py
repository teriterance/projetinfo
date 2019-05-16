import numpy as np
import math

class Domino(list):
    
    def __init__(self, num1, num2, color = 0):
        '''initialisation du domino 
        le domino est vu comme trois valeur, deux numerique et une couleur
        couleur par defaut 0 pour le cas du jeux sans couleur
        '''
        if (num1 <= 6 and num1>= 0) and (num2 >= 0 and num2 <= 6):
            self.append(num1)
            self.append(num2)
        else:
            print("erreur: les valeur doivent etre comprises entre 0 et 6")
        self.__Color = color

    @property
    def color(self):
        '''Permet de connaitre la couleur d'un domino'''
        return self.__Color
    
    @color.setter
    def color(self, color):
        '''Permet de redefinir la couleur d'un domino'''
        self.__Color = color

    @property
    def get_Value(self):
        ''' cette fonction retourne les valeur des parties du domino ainsi que sa couleur'''
        return self[0], self[1], self.color
    
    def nb_point(self):
        '''cette fonction retourne le nombre de point du domino
        utilisation:
        - permet de verifier le gagnant du jeux 
        - utile pour le joueur intelligence artificiel'''
        return sum(self)

    def isdouble(self):
        '''retourne la valeur du double si le domino est un domino double '''
        if self[0] == self[1]:
            return self[0]
        else: 
            return False
    
    def cherche(self,a):
        '''Au cas ou on recherche une valeur dans un domino'''
        if self[0]== a or self[1]== a:
            return True
        else:
            return False