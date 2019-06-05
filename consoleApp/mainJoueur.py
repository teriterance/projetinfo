from domino import Domino

class MainJoueur(list):
    def __init__(self,joueur):
        '''fonction d'initilisation de la main du joueur qui fait le lien entre le joeur et ses dominos'''
        self.__Joueur = joueur
        self.__taille = 0
        super().__init__()

    @property
    def taille(self):
        '''utilise pour connaitre la taille de la main du joueur
        utilisation: 
        - verifier que la main n'est pas vide 
        '''
        return self.__taille

    def ajouter(self, domino, num):
        '''Permet d'ajouter un domino dans la main du joueur
        uitilsation: 
        - fonction de pioche dans le talon
        - test des fonctions dominofort et doublefort
        '''
        print("je pioche le domino "+str(domino))
        print("\n\n\n"+str(num))
        domino.color = num
        if super().append(domino):
            return True
        else: 
            return False
    
    def retirer(self, domino):
        '''Permet de retirer un ellement dela main du joueur
        utilisation:
        - fonciton qui permet de faire le retrait d'un domino quant il a ete place
        '''
        if len(self) > 0:
            print("je joue le domino "+ str(domino))
            return self.remove(domino)
        return False

    def doublefort(self):
        '''Permet de donner le domino (double) le plus fort present dans la main du joueur'''
        doublemax = [0,0]
        for domino in self:
            if  domino.isdouble() and sum(domino) > sum(doublemax):
               doublemax = domino 
        print("le domino double le plus fort du jeux est: "+str(doublemax))
        return doublemax

    def dominofort(self):
        '''retourne le domino le plus fort
        utilisation:
        - s'utilise en lieu et place de la fonction double max si elle retrourne le domino [0,0]'''
        maxval = 0
        dominomax = 0
        for domino in self:
            x = domino.nb_point()
            if maxval < x:
                dominomax = domino
                maxval = x
        return dominomax

    def get_point(self):
        '''compte tous les point de la main
        utilisation:
        - permet de compter le nombre de point total des dominos presents dans la main du joueur
        '''
        tmp = 0
        for domino in self:
            tmp = domino.nb_point() + tmp
        return tmp

    def __str__(self):
        '''retroune une version console de la main du joueur
        utilisation:
        - test 
        - version console du jeux
        '''
        t = ""
        for i in self:
            t = t + str(i)
        return t 