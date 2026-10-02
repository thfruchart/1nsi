# Pyxel Studio

import pyxel
pyxel.init(256, 256, title="Chute libre")
pyxel.mouse(True)

vitesse = 1

# =========================================================
def update():
    global vitesse
    """mise à jour des variables (30 fois par seconde)"""
    if pyxel.btnr(pyxel.MOUSE_BUTTON_LEFT) :
        x,y = pyxel.mouse_x, pyxel.mouse_y
        print(x,y)


# =========================================================
def draw():
    """création des objets (30 fois par seconde)"""
    # vide la fenetre
    pyxel.cls(0)
    # un cercle
    pyxel.circ(60, 60, 8, 9)
    

pyxel.run(update, draw)