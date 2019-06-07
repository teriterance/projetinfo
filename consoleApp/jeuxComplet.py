from domino import Domino
from joueur import Joueur
from joueruIAmax import JoueurAI
#from joueurAI import JoueurAI
from talon import Talon
from terrainjeux import TerrainJeux

class Jeux:
    '''Fodop'''
    def __init__(self, nbj, nbIA = 0, consoleGraphique = 0):
        "cette fonction initilaise le jeu"
        self.numeroTour = 1
        self.nombreJoueur = nbj
        self.terrain = TerrainJeux()
        if consoleGraphique == 0:
            # 0 pour le jeux en console les autres valeurs pour le jeux graphique 
            self.listeJoueur = [Joueur(i, input("entrez le nom du joueur "+str(i)+"\n")) for i in range(self.nombreJoueur-nbIA)]
            self.listeJoueur.extend([JoueurAI(i + self.nombreJoueur - nbIA, "Ordi "+str(i)) for i in range(nbIA)])
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
    def joueurprecedent(self):
        "permet de revenir au joueur precedent sans faire en sorte que le parametre soit accessible a l'exterieur de la classe"
        self.__joueurActuel = (self.__joueurActuel - 1 )% self.nombreJoueur

    def piocher(self):
        "appeler pour garantir que le joeur a bien piocher, on passe au joueur suivant"
        print(self.listeJoueur[self.joueurActuel].mainj)
        pupiocher = self.listeJoueur[self.joueurActuel].mainj.ajouter(self.talon.pioche(), self.listeJoueur[self.joueurActuel].numero)
        return pupiocher

    def nouveaujeux(self, nbjoueur):
        #on creait le terrain 
        self.terrain = TerrainJeux()
        #on cree la pioche ou talon
        self.talon = Talon()
        self.talon.mix()
        #on demande le nombre de joueur ceci se fera dans une boite de dialogue 
        self.nombreJoueur = 0
        #on creai les joueru 
        self.listeJoueur = [Joueur(i) for i in range(self.nombreJoueur)]
        #on deffinit le joueur actuel
        self.__joueurActuel = 0
        #on reinitialise le gagnant 
        self.gagnant = None
        self.nbpointgagnant = None

    def finjeux(self):
        if self.talon.size == 0:
            #si le talon est vide on a une fin possible du jeux 
            smax = 100
            for joueur in self.listeJoueur:
                s = 0
                for dom in joueur.mainj:
                    s = s + sum(dom)
                if s <smax:
                    smax, self.gagnant= s, joueur.numero
                else:
                    self.nbpointgagnant = s
            return True

        # le cas ou le jeux est bloque
        if self.terrain[self.terrain.boutChaine[0]][self.terrain.boutChaine[1]] !='.':
            self.joueurprecedent()
            self.gagnant = self.joueurActuel
            s =0
            for joueur in self.listeJoueur:
                    for dom in joueur.mainj:
                        s = s + sum(dom)
            self.nbpointgagnant = s
            return True

        for joueur in self.listeJoueur:
            #si la main d'un joueur est vide 
            if len(joueur.mainj) == 0:
                s = 0
                for joueur in self.listeJoueur:
                    for dom in joueur.mainj:
                        s = s + sum(dom)
                self.nbpointgagnant = s
                self.gagnant = joueur.numero
                return True

        #cas ou il n'y a plus de possibilite de completer la chaine de domino
        if self.talon.estDans(self.terrain.dombout):
            #on cherche dans le talon un domino pouvant le faire
            return False
        for joueur in self.listeJoueur:
            #on cherche dans les mains des joueurs
            for dom in joueur.mainj:
                if dom.cherche(self.terrain.dombout):
                    return False 
        return True 

    def jouer(self):
        self.terrain. self.listeJoueur[self.joueurActuel].jouerconsole()
        self.joueursuivant()
        
    def partie(self):
        # on affiche le terrain  et effectue les premiers traitements
        print(self.terrain)
        self.distribution()
        prenierDom = self.premierJoueur()
        self.listeJoueur[self.joueurActuel].jouer(prenierDom)
        print(str(self.joueurActuel))
        #meme si le joueur est une IA c'est un joueur humain qui place le premier domino
        orientation = input("entrez lorientation du premier domino, les possibilite sont \n 0 pour a plat de gauche a droite \n 90 de bas en haut \n 180 de droite a gauche \n 270 de haut en bas\n")
        t = self.terrain.placer(prenierDom,orientation)
        print(self.terrain)
        self.joueursuivant()
        # on debute la boucle de jeux
        while self.finjeux() == False:
            for i in range(self.nombreJoueur):
                a = True
                print(self.listeJoueur[self.joueurActuel])
                #ici on demande au joueur le domino et son orientation 
                dominojouer,orientation = self.listeJoueur[self.joueurActuel].jouerconsole(self.terrain)
                #si il ne peut jouer il nous envoi 9 et donc pioche
                if dominojouer == 9:
                    self.listeJoueur[self.joueurActuel].piocher(self.talon)
                    self.joueursuivant()
                else:   
                    #si il peut jouer il est place sont domino sur le terrain
                    if dominojouer in self.listeJoueur[self.joueurActuel].mainj:
                        if self.terrain.placer(dominojouer, orientation) != False:
                            #ici on lui retire de la main le domino a jouer
                            if self.listeJoueur[self.joueurActuel].jouer(dominojouer) != False:
                                self.joueursuivant()
                                print(self.terrain)
                            else:
                                print(" impossible de jouer ce domino, veuillez piocher")
                        else:
                            print(" impossible de placer ce domino, essayer un autre piocher")
        print("jeux termine\n le gangnant est le joueur: ", self.gagnant, self.nbpointgagnant)

if __name__ == "__main__":
    jeu = Jeux(2, 1)
    jeu.partie()