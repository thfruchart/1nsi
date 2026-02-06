# Compléter la fonction update pour que l'appui sur les flèches modifie le tableau
import pyxel


##########################
# les 4 mouvements de base
##########################
def zero_coord(tab):
    """renvoie l'indice de ligne (i) et l'indice de colonne (j) du 0 dans tab"""
    for i in range(3):
        for j in range(3):
            v = tab[i][j]
            #print(i,j, v)
            if v == 0 :
                return i,j
def haut() :
    """échanger le 0 avec la valeur située juste en dessous dans tab"""
    i0, j0 = zero_coord(tab)
    if i0 + 1 < 3 :
        tab[i0][j0] = tab[i0+1][j0]
        tab[i0+1][j0] = 0
    return tab
def bas() :
    """échanger le 0 avec la valeur située juste au-dessus dans tab"""
    i0, j0 = zero_coord(tab)
    if i0 - 1 >= 0  :
        tab[i0][j0] = tab[i0-1][j0]
        tab[i0-1][j0] = 0
    return tab
def droite() :
    """échanger le 0 avec la valeur située juste à gauche dans tab"""
    i0, j0 = zero_coord(tab)
    if j0 - 1 >= 0  :
        tab[i0][j0] = tab[i0][j0-1]
        tab[i0][j0-1] = 0
    return tab
def gauche() :
    """échanger le 0 avec la valeur située juste à droite dans tab"""
    i0, j0 = zero_coord(tab)
    if j0 + 1 < 3  :
        tab[i0][j0] = tab[i0][j0+1]
        tab[i0][j0+1] = 0
    return tab



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
    # APPUI SUR UNE DES FLECHES
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
    # grand cadre du jeu
    pyxel.rectb(6,6,51,51, 5)
    # affichage des éléments du tableau 'tab'
    for i in range(3) :
        for j in range(3) :
            # valeur du tableau correspondant à la case (i,j), convertie en texte
            chiffre = str( tab[i][j]  )
            if chiffre != "0" : # 0 correspond à la case vide => pas affiché
                x = 16*j + 8
                y = 16*i + 8
                # rectangles pour représenter les 9 cases du jeu
                pyxel.rect(x,y,15,15, 5)
                # textes
                pyxel.text(x+7,y+5,chiffre,9)

#--------------------
# PROGRAMME PRINCIPAL
#--------------------
pyxel.run(update, draw)
