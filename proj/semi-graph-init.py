# semi-graph-init.py

import pyxel

########
# INIT #
########
LARG = 256
HAUT = 128
pyxel.init(LARG, HAUT, title="SEMIS")
pyxel.mouse(True)

NB_CASES = 7
plateau = [0]*NB_CASES



# =========================================================
# == UPDATE
# =========================================================
def update():
    """mise à jour des variables (30 fois par seconde)"""
    if pyxel.btn(pyxel.KEY_Q):
        pyxel.quit()
    # COORDONNEES DE LA SOURIS
    if pyxel.btnr(pyxel.MOUSE_BUTTON_LEFT):
        print(pyxel.mouse_x, pyxel.mouse_y)
    # TEST 0 : les entiers tous à 0
    if pyxel.btnr(pyxel.KEY_KP_0):
        for i in range(NB_CASES):
            plateau[i] = 0
        print(plateau)
    # TEST 1 : les entiers de 1 à NB_CASE
    if pyxel.btnr(pyxel.KEY_KP_1):
        for i in range(NB_CASES):
            plateau[i] = i+1
        print(plateau)
    # TEST 2 : toutes les cases avec 2 grains
    if pyxel.btnr(pyxel.KEY_KP_2):
        for i in range(NB_CASES):
            plateau[i] = 2
        print(plateau)
    
       
    


# =========================================================
# == DRAW
# =========================================================

def case(i,nb):
    """dessine la case d'indice i avec la quantité de grains : nb"""
    l_case = (3*LARG) // (NB_CASES * 4)
    h_case = HAUT//2
    x_case = LARG // 8 + i * l_case
    y_case = HAUT//4
    pyxel.rect(x_case+4, y_case+4, l_case-8, h_case-8,1)
    
        
    
    

def draw():
    """création des objets (30 fois par seconde)"""
    # vide la fenetre
    pyxel.cls(0)

    # plateau 
    pyxel.rect(LARG // 8, HAUT//4, LARG//4*3, HAUT//2, 5)
    
    # cases
    for i in range(NB_CASES):
        case(i,plateau[i])
    
    
pyxel.run(update, draw)

