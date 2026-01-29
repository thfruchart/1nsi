# taquin-graph-init.py

# 1. exécuter une première fois le fichier
# 2. dans la fonction draw
#   a. modifier les paramètres d'affichage pour "centrer" les carrés et les chiffres
#   b. modifier la variable chiffre avec la commande :
#          chiffre = str(i) + str(j)
#      et tester le résultat
#   c. modifier la valeur de la variable "chiffre" pour faire varier les affichages
#      on fera en sorte d'afficher le contenu du tableau tab

import pyxel

########
# INIT #
########
LARG = 64
HAUT = 64

pyxel.init(LARG, HAUT, title="Taquin")
pyxel.mouse(False)

from random import randint

# tableau ordonné :
objectif = [[1,2,3],
            [4,5,6],
            [7,8,0]]

# tableau mélangé à remettre dans l'ordre en utilisant les fonctions à définir :
# haut() bas() gauche() et droite()
tab = [[2, 6, 3],
       [7, 0, 5],
       [4, 1, 8]]



# =========================================================
# == UPDATE
# =========================================================
def update():
    """mise à jour des variables (30 fois par seconde)"""
    if pyxel.btn(pyxel.KEY_Q):
        pyxel.quit()
    # COORDONNEES DE LA SOURIS
    if pyxel.btnr(pyxel.KEY_DOWN):
        print('appui sur flèche BAS')
    if pyxel.btn(pyxel.KEY_DOWN):
        print('appui sur flèche HAUT')
    
    

# =========================================================
# == DRAW
# =========================================================
def draw():
    """création des objets (30 fois par seconde)"""
    # vide la fenetre
    pyxel.cls(0)

    
    for i in range(3) :
        for j in range(3) :
            x = 16*i
            y = 16*j
            # rectangles pour représenter les 9 cases du jeu
            pyxel.rectb(x,y,16,16, 5)
            
            # textes
            chiffre = str(i)
            pyxel.text(x,y,chiffre,9)
    
#--------------------
# PROGRAMME PRINCIPAL
#--------------------
pyxel.run(update, draw)
