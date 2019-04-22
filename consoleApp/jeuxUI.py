# -*- coding: utf-8-*-
import sys 
from jeuxComplet import *
from PyQt5 import QtGui, QtCore, QtWidgets, uic

class jeuxUI(QtWidgets.QMainWindow):

    def __init__(self, *args, **kargs):
        
        #on fait le constructeur de la fenetre QMAinWindow
        QtWidgets.QMainWindow.__init__(self, *args)
        #chargement de l'interface graphique
        self.ui = uic.loadUi("Jeux.ui",self)
        self.ui.terain.setStyleSheet("background-image:url(\"file.jpg\"); background-repeat: no-repeat;")
        #initialisation du jeux
        #1 on creai une boite de dialogue pour avoir le nombre de joueur
        nj = self.boitenombrejoueur()
        self.jeux = Jeux(nj)
        self.untour()


    def fondJoueur(self, image):
        """cette fonction sert a definir un fond d'ecrant pour le joueur. il est a noter que on fait appel
        du CSS pour definir les atributs de classe"""
        self.ui.joueur1.setStyleSheet("background-image:url(\""+ image+".png\"); background-repeat: no-repeat;")
        self.ui.joueur2.setStyleSheet("background-image:url(\""+ image+".png\"); background-repeat: no-repeat;")
        self.ui.joueur3.setStyleSheet("background-image:url(\""+ image+".png\"); background-repeat: no-repeat;")
        self.ui.joueur4.setStyleSheet("background-image:url(\""+ image+".png\"); background-repeat: no-repeat;")

    def couleurJoueur(self, couleur = "black"):
        self.ui.joueur1.setStyleSheet("background-color: "+couleur+";")
        self.ui.joueur2.setStyleSheet("background-color: "+couleur+";")
        self.ui.joueur3.setStyleSheet("background-color: "+couleur+";")
        self.ui.joueur4.setStyleSheet("background-color: "+couleur+";")

    def untour(self):
        if self.jeux.numeroTour == 1: # cas du premier tours:
            self.jeux.distribution()
            #debut de cinematique

            #fin de cinematique
            self.chargementmain()
            
            dominopremier = self.jeux.premierJoueur()
            print("le premier domino a jouer est ")
            for i in range(self.jeux.nombreJoueur)
                self.jeux.listeJoueur[self.jeux.joueurActuel].jouer()
                #mise a jour des graphisme 

                #fin mise a jour
                self.jeux.joeursuivant() # on pass au joueur suivant

    def chargementmain(self):
        pass

    def boitenombrejoueur(self):
        v = ('2','3','4')
        nb, result = QtWidgets.QInputDialog.getItem(self, 'NOMBRE joeur','Entrez le nombre de joeur:', v, 0, False)
        if result == True:
            return int(nb)
        else:
            return self.close()  # l'objectif est de ne pas utiliser de thread pour attendre

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = jeuxUI()
    window.show()
    sys.exit(app.exec_())

