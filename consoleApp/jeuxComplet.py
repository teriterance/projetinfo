from domino import Domino
from joueur import Joueur
#from joueurAI import JoueurAI
from talon import Talon
from terrainjeux import TerrainJeux

class Jeux:
    def __init__(self, nbj, t = 0):
        "cette fonction initilaise le jeu"
        self.numeroTour = 1
        self.nombreJoueur = nbj
        self.terrain = TerrainJeux()
        if t == 0:
            self.listeJoueur = [Joueur(i, input("entrez le nom du joueur "+str(i)+" ")) for i in range(self.nombreJoueur)]
        else:
            self.listeJoueur = [Joueur(i) for i in range(self.nombreJoueur)]    
        self.talon = Talon()
        self.talon.mix()
        self.__joueurActuel =0

    def distribution(self):
        "cette fonction fait la distribution des dominos aux joueurs"
        #on fait la distribution des dominos aux joueurs pour ce faire on 
        #passe dans deux boucles qui vont donner les dominos aux joueurs 
        for i in range(self.nombreJoueur):
            for j in range(7):
                print(self.listeJoueur[i].piocher(self.talon))
    
    def premierJoueur(self):
        "cette fonction retourne le premier joueur et le domino qu'il dois jouer"
        #on cherche le joueur qui a le double le plus fort
        # en meme temp celui qui a la main la plus forte  
        maxdouble =  [0,0]
        maxdoublejoueur = 0 #initialisation du joueur hors de la liste  
        maxval = [0,0]
        maxValJoueur = 0 #initialisation du joueur hors de la liste
        #on parcour la liste des joueurs
        for i in range(self.nombreJoueur):
            doubleTmp = self.listeJoueur[i].doublefort()
            if sum(doubleTmp) > sum(maxdouble):
                maxdouble = doubleTmp
                maxdoublejoueur = i
            valTmp = self.listeJoueur[i].dominofort()
            if sum(valTmp) > sum(maxval):
                maxval = valTmp
                maxValJoueur = i
            print(i,maxdouble, maxval,maxdoublejoueur, maxValJoueur)
        if maxdouble == [0,0]:#si il n'y a pa de double
            self.__joueurActuel = maxValJoueur
            return maxval
        else:
            self.__joueurActuel = maxdoublejoueur
            return maxdouble

    @property
    def joueurActuel(self):
        return self.__joueurActuel
    
    def joueursuivant(self):
        "permet de passer au joueur suivant sans faire en sorte que le parametre soit accessible a l'exterieur de la classe"
        self.__joueurActuel = (self.__joueurActuel + 1 )% self.nombreJoueur
        print("+",self.__joueurActuel,"+")

    def piocher(self):
        print(str(self.joueurActuel))
        t = self.listeJoueur[self.joueurActuel].mainj.ajouter(self.talon.pioche())
        self.joueursuivant()
        return t

    def nouveaujeux(self, nbjoueur):
        #on creait le terrain 
        self.terrain = TerrainJeux()
        #on cree la pioche ou talon
        self.talon = Talon()
        #on demande le nombre de joueur ceci se fera dans une boite de dialogue 
        self.nombreJoueur = 0
        #on creai les joueru 
        self.listeJoueur = [Joueur(i) for i in range(self.nombreJoueur)]
        #on deffinit le joueur actuel
        self.__joueurActuel = 0

    def finjeux(self):
        for joueur in self.listeJoueur:
            if len(joueur.mainj) == 0:
                self.gagnant = joueur.numero
                return True
        t =  True
        for dom in self.talon:
            if dom.cherche(self.terrain.domcol):
                t = False     
        for i in range(self.nombreJoueur):
            for j in self.listeJoueur[i].mainj:
                if j.cherche(self.terrain.domcol):
                    t = False 
        return False or t 

    def jouer(self):
        self.terrain. self.listeJoueur[self.joueurActuel].jouerconsole()
        self.joueursuivant()
        
    def partie(self):

        print(self.talon)
        print(self.terrain)
        self.distribution()
        prenierDom = self.premierJoueur()
        self.listeJoueur[self.joueurActuel].jouer(prenierDom)
        print(str(self.joueurActuel))
        orientation = input("entrez lorientation du premier domino")
        t = self.terrain.placer(prenierDom,orientation)
        print(self.terrain)
        self.joueursuivant()
        while self.finjeux() == False:
            for i in range(self.nombreJoueur):
                a = True
                print(self.listeJoueur[self.joueurActuel])
                dominojouer,orientation = self.listeJoueur[self.joueurActuel].jouerconsole()
                if dominojouer in self.listeJoueur[self.joueurActuel].mainj:
                    self.listeJoueur[self.joueurActuel].jouer(dominojouer)
                    a = self.terrain.placer(dominojouer, orientation) != False
                    print(a)
                else:
                    self.listeJoueur[self.joueurActuel].piocher(self.talon)
                if a== True:
                    self.joueursuivant()
                    print(self.terrain)
                else:# on reste sur le meme joueur.
                    i = i-1
                    self.listeJoueur[self.joueurActuel].mainj.ajouter(dominojouer)
                    a = True
        print("jeux termine")

if __name__ == "__main__":
    jeu = Jeux(2)
    jeu.partie()