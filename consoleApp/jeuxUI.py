# -*- coding: utf-8-*-
import sys 
import time
from domino import Domino
from jeuxComplet import Jeux
from PyQt5 import QtGui, QtCore, QtWidgets, uic
from clikable_label import MyQLabel

class jeuxUI(QtWidgets.QMainWindow):

    def __init__(self, *args, **kargs):
        
        #on fait le constructeur de la fenetre QMAinWindow
        QtWidgets.QMainWindow.__init__(self, *args)
        #chargement de l'interface graphique
        self.ui = uic.loadUi("Jeux.ui",self)
        self.ui.terain.setStyleSheet("background-image:url(./file.jpg); background-repeat: no-repeat;")
        self.ui.actionCouleur.triggered.connect(self.changecouleur)
        self.ui.actionNouveau.triggered.connect(self.jouer)
        self.ui.ButtonJouer.clicked.connect(self.jeuxjoueur)
        self.ui.boutoPiocher.clicked.connect(self.piocher)
        self.ui.boutoPiocher.setVisible(False)
        self.ui.ButtonJouer.setVisible(False)
        self.font = QtGui.QFont('SansSerif', 24)
        self.ui.gridLayout.setSpacing(0)
        self.ui.label.setFont(self.font)

    def boitenombrejoueur(self):
        '''cette fonction nous donne le nombre de joueurs via une boite de dialogue '''
        v = ('2','3','4')
        nb, result = QtWidgets.QInputDialog.getItem(self, 'Nombre Joueur','Entrez le nombre de joeur:', v, 0, False)
        if result == True:
            return int(nb)
        else:
            return self.close()  #l'objectif est de ne pas utiliser de thread pour attendre

    def changecouleur(self):
        '''cette fonction change la couleur de la main du joueur'''
        couleur = QtWidgets.QColorDialog.getColor().name()
        self.couleurJoueur(couleur)
    
    def boiteOrientation(self, angle=None):
        '''cette fonction nous donne le nombre de joueurs via une boite de dialogue on y retire l'angle a ne pas jouer'''
        v = ['0','90','180','270']
        #v.remove(angle)
        nb, result = QtWidgets.QInputDialog.getItem(self, 'Nombre Joueur','Entrez l\'orientation pour le domino:', v, 0, False)
        if result == True:
            return int(nb)
        else:
            return self.close()

    def actuTerain(self):
        '''ici on actualise le terrain'''
        for i in range(self.jeux.terrain.taille):
            for j in range(self.jeux.terrain.taille):
                t = self.jeux.terrain[i][j]
                if t !='.':
                    if  int(t)<=6 and int(t) >=0:
                        l1 = QtWidgets.QLabel(self)
                        p = QtGui.QPixmap('dice'+str(self.jeux.terrain[i][j])+'.png')
                        l1.setPixmap(p)
                        self.ui.gridLayout.addWidget(l1,i,j)
                else:
                        l1 = QtWidgets.QLabel(self)
                        p = QtGui.QPixmap('dice.png')
                        l1.setPixmap(p)
                        self.ui.gridLayout.addWidget(l1,i,j)

    def changeJoueurnom(self):
        '''actualise le nom du joueur'''
        self.ui.label.setText(self.jeux.listeJoueur[self.jeux.joueurActuel].nomjoueur)

    def actuMain(self):
        '''cette fonction permet de faire une actualisation de la main'''
        pass
    
    def viderLayout_main(self):
        for i in range(self.jeux.terrain.taille):
            for j in range(self.jeux.terrain.taille):
                if self.ui.gridLayout_main.itemAtPosition(i,j):
                    self.ui.gridLayout_main.itemAtPosition(i,j).widget().deleteLater()

    def jouer(self):
        '''cette fonction definie le mode de fonctionnement du jeu, de son initialisation da la fin'''
        nj = self.boitenombrejoueur()
        self.jeux = Jeux(nj, 1)#on signale qu'on est en mode graphique 
        for joueur in self.jeux.listeJoueur:
            nomjoueur, result = QtWidgets.QInputDialog.getText(self, 'NOM Joueur','Entrez le nom du joeur:'+str(joueur.numero + 1))
            joueur.nomjoueur = nomjoueur
        self.partie()

    def partie(self):
        self.ui.ButtonJouer.setVisible(True)
        self.ui.boutoPiocher.setVisible(True)
        self.jeux.distribution()
        self.chargementmain()
        #introduire une cinematique 

        #fin de la cinematique
        prenierDom = self.jeux.premierJoueur()
        self.jeux.listeJoueur[self.jeux.joueurActuel].jouer(prenierDom)#jouer doit etre modifier pour prendre en entree l'angle
        self.changeJoueurnom()
        orientation =  self.boiteOrientation(self.jeux.terrain.orient)
        self.jeux.terrain.placer(prenierDom,orientation)
        self.actuTerain()
        self.jeux.joueursuivant()
        print(self.jeux.listeJoueur[self.jeux.joueurActuel])
    
    def jeuxjoueur(self):
        print("je jouer")
        if self.jeux.finjeux() == False:
            a = True
            dominojouer = Domino(1, 2) #on va recuperer le domino et l'orientation via une boite de dialogue 
            orientation  = 90
            #self.jeux.listeJoueur[self.jeux.joueurActuel].jouer(dominojouer)
            if dominojouer in self.jeux.listeJoueur[self.jeux.joueurActuel].mainj:
                #self.jeux.listeJoueur[self.jeux.joueurActuel].jouer(dominojouer)
                a = self.jeux.terrain.placer(Domino(1, 2), orientation)
            else:
                print("pret a piocher")
                self.piocher()
            print(a)
            print(self.jeux.terrain)
            if a != False:
                self.chargementmain()
                self.actuTerain()
                self.jeux.joueursuivant()
            else:# on reste sur le meme joueur.
                self.jeux.listeJoueur[self.jeux.joueurActuel].mainj.ajouter(dominojouer)
                a = True
        else:
                self.ui.ButtonJouer.setVisible(False)
                self.ui.boutoPiocher.setVisible(False)
    
    def piocher(self):
        '''salut '''
        if self.jeux.piocher()!= False:
            self.chargementmain()
            self.actuTerain() 
            self.jeux.joueursuivant()
    
    def boitejouer(self):
        """retourne le domino que le joueur a choisi de jouer"""
        domino1, domino2, x,y, orientation = input() #une boite de dialogue pour receuillier le tout 
        return Domino(domino1, domino2), x,y, orientation

    def chargementmain(self):
        """On  change l'afichage de la main Creer un layout et les domminos graphiques
        les ajoueter dans le layout ajouter le layout dans les widgets"""
        self.viderLayout_main()
        self.changeJoueurnom()
        main = self.jeux.listeJoueur[self.jeux.joueurActuel].mainj
        for i in range(len(main)):
            d = main[i]
            for j in range(2):
                l1 = MyQLabel(self,i)
                p = QtGui.QPixmap('dice'+str(d[j])+'.png')
                l1.setPixmap(p)
                self.ui.gridLayout_main.addWidget(l1, j,i)
    
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
    sys.exit(app.exec_())