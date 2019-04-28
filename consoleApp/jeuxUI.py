# -*- coding: utf-8-*-
import sys 
import time
from jeuxComplet import *
from PyQt5 import QtGui, QtCore, QtWidgets, uic

class jeuxUI(QtWidgets.QMainWindow):

    def __init__(self, *args, **kargs):
        
        #on fait le constructeur de la fenetre QMAinWindow
        QtWidgets.QMainWindow.__init__(self, *args)
        #chargement de l'interface graphique
        self.ui = uic.loadUi("Jeux.ui",self)
        self.ui.terain.setStyleSheet("background-image:url(./file.jpg); background-repeat: no-repeat;")
        self.ui.actionCouleur.triggered.connect(self.changecouleur)
        
        #initialisation du jeux
        #1 on creai une boite de dialogue pour avoir le nombre de joueur
    def jouer(self):
        nj = self.boitenombrejoueur()
        self.jeux = Jeux(nj)
        for joueur in self.jeux.listeJoueur:
            nb, result = QtWidgets.QInputDialog.getText(self, 'NOM Joueur','Entrez le nom du joeur:'+str(joueur.numero + 1))
            joueur.nomjoueur = nb
        self.cinematiquedebut()
        #self.couleurJoueur()
        self.partie()

    def changeJoueurnom(self):
        self.ui.label.setText(self.jeux.listeJoueur[self.jeux.joueurActuel].nomjoueur)

    def changecouleur(self):
        couleur = QtWidgets.QColorDialog.getColor().name()
        self.couleurJoueur(couleur)

    def fondJoueur(self, image):
        """cette fonction sert a definir un fond d'ecrant pour le joueur. il est a noter que on fait appel
        du CSS pour definir les atributs de classe"""
        self.ui.joueur1.setStyleSheet("background-image:url("+image+".png); background-repeat: no-repeat;")
    def couleurJoueur(self, couleur = "brown"):
        self.ui.joueur1.setStyleSheet("background-color: "+couleur+";")

    def partie(self):
        self.jeux.distribution()
        #debut de cinematique

        #fin de cinematique
        self.chargementmain()
        self.changeJoueurnom()
            
        dominopremier = self.jeux.premierJoueur()
        self.jeux.listeJoueur[self.jeux.joueurActuel].jouer(dominopremier)
        self.jeux.terrain.placer1(dominopremier)## on place le premier domino

        while self.jeux.finjeux() == False:     
            for i in range(self.jeux.nombreJoueur):
                dominojouer, x,y,orientation = self.boitejouer()
                if dominojouer in self.jeux.listeJoueur[self.jeux.joueurActuel()].mainj:
                    self.jeux.listeJoueur[self.jeux.joueurActuel].jouer(dominojouer)
                    self.jeux.terrain.placer(x,y,dominojouer, orientation)
                #mise a jour des graphisme 

                #fin mise a jour
                self.jeux.joeursuivant() # on passe au joueur suivant
        #on affiche une boite de dialogue de victoire
    
    def cinematiquedebut(self):
        """faire la cinematique au debut du jeux clignotement"""
        pass

    def boitejouer1(self):
        pass
    
    def boitejouer(self):
        """retourne le domino que le joueur a choisi de jouer"""
        domino1, domino2, x,y, orientation = input() #une boite de dialogue pour receuillier le tout 
        return Domino(domino1, domino2), x,y, orientation

    def chargementmain(self):
        """On  change l'afichage de la main
        Creer un layout et les domminos graphiques
        les ajoueter dans le layout 
        ajouter le layout dans les widgets"""
        dom = QtWidgets.QVBoxLayout(self.ui.joueur1)
        self.ui.terrainJeu.setLayout(dom)
        print(self.jeux.joueurActuel)
        for i in self.jeux.listeJoueur[self.jeux.joueurActuel].mainj:
            layout = QtWidgets.QHBoxLayout()
            print("gabin")
            l1 = QtWidgets.QLabel()
            pixmap = QtGui.QPixmap('Dice'+ str(i[0]) +'.png') 
            l1.setPixmap(pixmap)
            l2 = QtWidgets.QLabel()
            pixmap = QtGui.QPixmap('Dice'+ str(i[0]) +'.png') 
            l2.setPixmap(pixmap)
            layout.addChildWidget(l1)
            layout.addChildWidget(l2)
            dom.addChildLayout(layout)
        

    def boitenombrejoueur(self):
        v = ('2','3','4')
        nb, result = QtWidgets.QInputDialog.getItem(self, 'NOMBRE joueur','Entrez le nombre de joeur:', v, 0, False)
        if result == True:
            return int(nb)
        else:
            return self.close()  # l'objectif est de ne pas utiliser de thread pour attendre
    
    def boiteVictoire(self):
        """une boite de dialogue qui dit qui est le gagnant"""
        a = QtWidgets.QMessageBox(self)
        a.setText("victoire du joueur: ")
        a.show()
        a.exec_()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = jeuxUI()
    window.show()
    window.jouer()
    sys.exit(app.exec_())