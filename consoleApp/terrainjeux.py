import numpy as np
import math
from domino import Domino

class TerrainJeux(list):
    #tableau de taille 52*52
    def __init__(self):
        '''fonciton d'initialisation
        on defini, 
        la taille du terrain
        '''
        self.taille = 18
        for i in range(self.taille):
            self.append([])
            for j in range(self.taille):
                self[i].append('.')
        self.dernierCouleur = 4 # on defini la derniere couleur qui a ete joue a 4 qui est hors de la liste
        self.boutChaine = [math.ceil(self.taille/2), math.ceil(self.taille/2)]
        self.domcol = 0.5
        self.premier = True
        self.domsterain = []
        self.orient = 111.5

    def str2(self):
        self_str = ""
        for i in range(self.taille):
            self_str  = self_str+"\n"+self[i].__str__()
        return self_str
    
    def retourner(self,domino):
        return Domino(domino[1], domino[0])
            
    def placer(self, domino, orientation, dep =0):
        
        """objectif , placer le premier domino au centre dans une direction fixe"""
        if self.boutChaine[0] < self.taille and self.boutChaine[1] < self.taille and self.boutChaine[0] > 0 and self.boutChaine[1] > 0 and self.domcol == domino[0] or self.premier:
            self[self.boutChaine[0]][self.boutChaine[1]] = domino[0]
            print(self.domcol, domino[0], self.premier)
            self.domsterain.append(domino)
            self.premier = False
        else:
            if dep <1:#eviter la recursion
                return self.placer(self.retourner(domino), orientation, 2)
            else:
                return False

        orientation = int(orientation)
        if orientation == 0 and self.orient != 180:
            if self.boutChaine[1] +1 < self.taille:
                self[self.boutChaine[0]][self.boutChaine[1] + 1] =  domino[1]
                self.boutChaine = [self.boutChaine[0], self.boutChaine[1] + 2]
                self.domcol = domino[1]
                self.orient = 0
                self.domsterain.append(domino)
        elif orientation == 90 and self.orient != 270:
            if self.boutChaine[1] -2 >= 0:
                self[self.boutChaine[0] - 1][self.boutChaine[1]] =  domino[1]
                self.boutChaine = [self.boutChaine[0] -2, self.boutChaine[1]]
                self.domcol = domino[1]
                self.orient = 90
                self.domsterain.append(domino)
        elif orientation == 180 and self.orient != 0:
            if self.boutChaine[1]  -1 < self.taille:
                self[self.boutChaine[0]][self.boutChaine[1] -1] =  domino[1]
                self.boutChaine = [self.boutChaine[0], self.boutChaine[1] - 2]
                self.domcol = domino[1]
                self.orient = 180
                self.domsterain.append(domino)
        elif orientation == 270 and self.orient != 90:
            if self.boutChaine[0] + 1 < self.taille:
                self[self.boutChaine[0] + 1][self.boutChaine[1]] =  domino[1]
                self.boutChaine = [self.boutChaine[0] + 2, self.boutChaine[1]]
                self.domcol = domino[1]
                self.orient = 270
                self.domsterain.append(domino)
        else:
            return False

    def __str__(self):
        t  = ""
        for i in range(self.taille + 4):
            t = t + "*"
        t = t+ "\n"
        for i in range(self.taille):
            t = t+ "/*"
            for j in range(self.taille):
                t = t +"'"+str(self[i][j])+"'"
            t = t + "*/" + "\n"
        for i in range(self.taille + 4):
            t = t + "*"
        return t