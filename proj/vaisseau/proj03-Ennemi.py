#####################################################
# 1. créer un ENNEMI
#    nouvelle variable
#
# 2. dessiner l'ennemi
#    => fonction draw
#
# 3. déplacement de l'ennami
#    => fonction update
#####################################################

import pyxel

pyxel.init(256, 256, title="SPACE BATTLE")

vaisseau = [60,60]

tir_list = []

ennemi = ... 

# =========================================================
# == UPDATE
# =========================================================
def update():
    """mise à jour des variables (30 fois par seconde)"""
    if pyxel.btn(pyxel.KEY_LEFT):
        vaisseau[0] -= 1
    if pyxel.btn(pyxel.KEY_RIGHT):
        vaisseau[0] += 1
    if pyxel.btn(pyxel.KEY_UP):
        vaisseau[1] -= 1
    if pyxel.btn(pyxel.KEY_DOWN):
        vaisseau[1] += 1
        
    # TIR avec barre d'espace
    if pyxel.btnp(pyxel.KEY_SPACE, 10,10):
        tir =  [ vaisseau[0]+16 , vaisseau[1]+8 ]
        tir_list.append(tir)
    
    # animation des tirs
    for tir in tir_list : 
        tir[0] += 3
    


# =========================================================
# == DRAW
# =========================================================
def draw():
    """création des objets (30 fois par seconde)"""
    # vide la fenetre
    pyxel.cls(0)
    # vaisseau
    pyxel.rect(vaisseau[0], vaisseau[1], 16, 16, 12)
    # affichage TIRS
    for tir in tir_list :
        x1, y1 = tir[0], tir[1]
        x2, y2 = x1 + 8 , y1
        col = 10
        pyxel.line(x1, y1, x2, y2, col)
    
    

pyxel.run(update, draw)