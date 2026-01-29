# taquin-graph-init.py


# 1. exécuter une première fois le fichier
# 2. a.modifier la fonction update pour qu'un appui sur une flèche (haut/bas)
#    fasse varier l'unique valeur contenue dans tab_test
#    b. modifier la fonction draw pour afficher en haut de l'écran la valeur
#    contenue dans tab_test. Tester en appuyant sur les touches haut/bas


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

tab_test = [0]

# =========================================================
# == UPDATE
# =========================================================
def update():
    """mise à jour des variables (30 fois par seconde)"""
    if pyxel.btn(pyxel.KEY_Q):
        pyxel.quit()
    # GESTION DES FLECHES DU CLAVIER
    if pyxel.btnr(pyxel.KEY_DOWN):
        print('appui sur flèche BAS')
    if pyxel.btn(pyxel.KEY_UP):
        print('appui sur flèche HAUT')


# =========================================================
# == DRAW
# =========================================================


def draw():
    """création des objets (30 fois par seconde)"""
    # vide la fenetre
    pyxel.cls(0)

    # rectangle
    pyxel.rect(10,20,30,40, 5)

    # texte
    chiffre = '0'
    pyxel.text(20,30,chiffre,9)

#--------------------
# PROGRAMME PRINCIPAL
#--------------------
pyxel.run(update, draw)
