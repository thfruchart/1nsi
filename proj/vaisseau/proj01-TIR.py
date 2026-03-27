#####################################################
# 1. créer un tir lors d'un appui sur la barre d'espace
#    => fonction update
#
# 2. dessiner le tir
#    => fonction draw
#
# 3. animer le tir
#    => fonction update
#####################################################

import pyxel

pyxel.init(256, 256, title="SPACE BATTLE")

vaisseau = [60,60]

tir = [-100,-100]  # valeurs en dehors de la fenêtre

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
    if pyxel.btn(pyxel.KEY_SPACE):
        tir[0] = ...
        tir[1] = ... 
    


# =========================================================
# == DRAW
# =========================================================
def draw():
    """création des objets (30 fois par seconde)"""
    # vide la fenetre
    pyxel.cls(0)
    # vaisseau
    pyxel.rect(vaisseau[0], vaisseau[1], 16, 16, 12)
    # affichage TIR
    x1, y1 =
    x2, y2 =
    col = ... 
    pyxel.line(x1, y1, x2, y2, col)
    
    

pyxel.run(update, draw)