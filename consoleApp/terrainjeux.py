import numpy as np
from domino import Domino

class TerrainJeux(list):
    #tableau de taille 52*52
    def __init__(self):
        '''fonciton d'initialisation'''
        self.taille = 15
        for i in range(self.taille):
            self.append([])
            for j in range(self.taille):
                self[i].append('.')
    
    def __str__(self):
        self_str = ""
        for i in range(self.taille):
            self_str  = self_str+"\n"+self[i].__str__()
        return self_str
    
    def jouer(self, coordonee, domino, orientation):
        
        [x, y] = coordonee
        self[x][y] = domino[0]
        if orientation = 0:
            self[x+1][y] = domino[0]
        elif orientation = 90:
            self[x][y+1] = domino[0]
        elif orientation = 180:
            self[x-1][y] = domino[0]
        elif orientation = 270:
            self[x][y-1] = domino[0]

        


if __name__ == "__main__":
    t = TerrainJeux()
    print(t[2][4])