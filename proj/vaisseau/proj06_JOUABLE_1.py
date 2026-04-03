#####################################################
# 1. tester si un tir touche l'ennemi
#   => fonction exploser
# 2. gérer ensuite les affichages... 
#####################################################

import pyxel
import random

pyxel.init(256, 256, title="SPACE BATTLE")

vaisseau = [60,60]
DEPLACEMENT = 2

tir_list = []
VITESSE_TIR = 4

ennemi_list = [ [240,128] ]


def exploser(ennemi, tir):
    if ennemi[0] <= tir[0]+8 < ennemi[0] +16:
        if ennemi[1] <= tir[1] < ennemi[1] + 16 :
            return True
    return False
# =========================================================
# == UPDATE
# =========================================================
def update():
    """mise à jour des variables (30 fois par seconde)"""
    if pyxel.btn(pyxel.KEY_LEFT):
        vaisseau[0] -= DEPLACEMENT
    if pyxel.btn(pyxel.KEY_RIGHT):
        vaisseau[0] += DEPLACEMENT
    if pyxel.btn(pyxel.KEY_UP):
        vaisseau[1] -= DEPLACEMENT
    if pyxel.btn(pyxel.KEY_DOWN):
        vaisseau[1] += DEPLACEMENT
        
    # TIR avec barre d'espace
    if pyxel.btnp(pyxel.KEY_SPACE, 10,10):
        tir =  [ vaisseau[0]+16 , vaisseau[1]+8 ]
        tir_list.append(tir)
    
    # animation des tirs
    for tir in tir_list : 
        tir[0] += VITESSE_TIR
    # création d'un ennemi
    if pyxel.frame_count % 50 == 0 :
        en = [256, random.randint(10,240)]
        ennemi_list.append(en)
    # déplacement des ennemis
    for ennemi in ennemi_list : 
        ennemi[0] -= 1
    # détection des tirs
    for tir in tir_list :
        for ennemi in ennemi_list :
            if exploser(ennemi,tir):
                print('touché')
                ennemi_list.remove(ennemi)
        
    # suppression des valeurs inutiles
    for tir in tir_list:
        if tir[0] < 0:
            tir_list.remove(tir)
    for ennemi in ennemi_list :
        if ennemi[0] < 0 :
            ennemi_list.remove(ennemi)


# =========================================================
# == DRAW
# =========================================================
def draw():
    """création des objets (30 fois par seconde)"""
    # vide la fenetre
    pyxel.cls(0)
    # vaisseau
    pyxel.rect(vaisseau[0], vaisseau[1], 16, 16, 12)
    # affichage ennemi
    for ennemi in ennemi_list : 
        pyxel.rect(ennemi[0], ennemi[1], 16, 16, 11)
    # affichage TIRS
    for tir in tir_list :
        x1, y1 = tir[0], tir[1]
        x2, y2 = x1 + 8 , y1
        col = 10
        pyxel.line(x1, y1, x2, y2, col)
    
    

pyxel.run(update, draw)