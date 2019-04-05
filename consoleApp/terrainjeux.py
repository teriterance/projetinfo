import numpy as np
from domino import Domino

class TerrainJeux(list):
    #tableau de taille 52*52
    def __init__(self):
        '''fonciton d'initialisation'''
        self.taille = 52
        for i in range(self.taille):
            self.append([])
            for j in range(self.taille):
                self[i].append('.')
        self.dernierepos = None ## vas etre utile pour jouer la version avancee
        self.tableaucouleur = [[]] ## on definit un tableau de couleur
    def __str__(self):
        self_str = ""
        for i in range(self.taille):
            self_str  = self_str+"\n"+self[i].__str__()
        return self_str
    
    def placer(self, x, y, domino, orientation):
        '''cette fonction retourne si on peut placer le domino en une position sur le terrain si oui elle le place'''
        '''on cherche si il y a un nombre au voisinage de la partie 1 du domino en fonction de l'orientation'''
        t = False
        if orientation == 0 :
            if self[x][y-1] = domino[0] or self[x][y+1] = domino[0] or self[x-1][y] = domino[0]:
                t = True
                self[x][y] = domino[0]
                self[x + 1][y] = domino[1]
        elif orientation == 180 :
            if self[x][y-1] = domino[0] or self[x][y+1] = domino[0] or self[x+1][y] = domino[0]:
                t = True
                self[x][y] = domino[0]
                self[x + 1][y] = domino[1]
        elif orientation == 90 :
            if self[x-1][y] = domino[0] or self[x+1][y] = domino[0] or self[x][y-1] = domino[0]:
                t = True
                self[x][y] = domino[0]
                self[x + 1][y] = domino[1]
        elif orientation == 270 :
            if self[x-1][y] = domino[0] or self[x+1][y] = domino[0] or self[x][y+1] = domino[0]:
                t = True
                self[x][y] = domino[0]
                self[x + 1][y] = domino[1]
        
        '''on cherche si il y a un nombre au voisinage de la partie 2 du domino en fonction de l'orientation'''
        if t == False:
            if orientation == 0 :
                if self[x+1][y-1] = domino[1] or self[x+1][y+1] = domino[1] or self[x+2][y] = domino[1]:
                    t = True
                    self[x][y] = domino[0]
                    self[x + 1][y] = domino[1]
            elif orientation == 180 :
                if self[x-1][y-1] = domino[1] or self[x-1][y+1] = domino[1] or self[x-2][y] = domino[1]:
                    t = True
                    self[x][y] = domino[0]
                    self[x + 1][y] = domino[1]
            elif orientation == 90 :
                if self[x-1][y+1] = domino[1] or self[x+1][y+1] = domino[1] or self[x][y+2] = domino[1]:
                    t = True
                    self[x][y] = domino[0]
                    self[x + 1][y] = domino[1]
            elif orientation == 270 :
                if self[x-1][y-1] = domino[1] or self[x+1][y-1] = domino[1] or self[x][y-2] = domino[1]:
                    t = True
                    self[x][y] = domino[0]
                    self[x + 1][y] = domino[1]
        return t