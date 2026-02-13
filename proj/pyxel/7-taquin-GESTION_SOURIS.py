# 7-taquin-GESTION-SOURIS.py

# Activer la vue de la souris avec pyxel.mouse(True)  => ligne 17

# observer le code de la fonction update
# -  tester le clic gauche de la souris
# -  faire afficher les coordonnées (i,j) du clic



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


# =========================================================
# == UPDATE
# =========================================================
def update():
    """mise à jour des variables (30 fois par seconde)"""
    if pyxel.btn(pyxel.KEY_Q):
        pyxel.quit()
    # COORDONNEES DE LA SOURIS
    if pyxel.btnr(pyxel.MOUSE_BUTTON_LEFT):
        x = pyxel.mouse_x
        y = pyxel.mouse_y
        print("click", x, y)
        
    
    

# =========================================================
# == DRAW
# =========================================================
def draw():
    """création des objets (30 fois par seconde)"""
    # vide la fenetre
    pyxel.cls(0)

    
    for i in range(3) :
        for j in range(3) :
            x = 16*j + 8
            y = 16*i + 8
            # rectangles pour représenter les 9 cases du jeu
            pyxel.rect(x,y,15,15, 5)
            
            # textes
            chiffre = str(i) +","+ str(j)
            pyxel.text(x+2,y+5,chiffre,9)
    
#--------------------
# PROGRAMME PRINCIPAL
#--------------------
pyxel.run(update, draw)
