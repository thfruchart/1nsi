# Pyxel Studio

import pyxel, random
pyxel.init(256, 256, title="Chute libre")
pyxel.mouse(False)

couleur_fond = 0
# cible
xc = 120
yc = 0
rc = 8


# position hors écran
xm,ym = -100,-100
# score
score = 0

# =========================================================
def update():
    global xc,yc,rc, xm, ym, score, couleur_fond
    """mise à jour des variables (30 fois par seconde)"""
    yc += 1
    # position de la souris
    xm,ym = pyxel.mouse_x, pyxel.mouse_y
    # détection du clic :
    if pyxel.btn(pyxel.MOUSE_BUTTON_LEFT) :
        print("click")
    # CHOC
    if (xm-xc)**2+(ym-yc)**2<=(rc+3)**2:
        print('choc')
        
            
    if yc > 300 :
        yc=-rc
        xc = pyxel.rndi(20,236)
        vitesse = 1
        xm,ym = -100,-100
        score = 0
        couleur_fond = 1- couleur_fond

        
            
        
    
    
    


# =========================================================
def draw():
    """création des objets (30 fois par seconde)"""

    # vide la fenetre
    pyxel.cls(couleur_fond)

    # CERCLES
    #cible
    pyxel.circ(xc, yc, rc, 9)
    #mouse
    pyxel.circ(xm, ym, 4, 6)
    # affichage
    txt = ' Score : ' + str(score)
    pyxel.text(20,240, txt  , 7)
    
    

pyxel.run(update, draw)