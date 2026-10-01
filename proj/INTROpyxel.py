# Pyxel Studio

import pyxel
pyxel.init(256, 256, title="Nombres entiers")

menu = 0
n = 0

# =========================================================
def update():
    global menu, n
    """mise à jour des variables (30 fois par seconde)"""
    if pyxel.btn(pyxel.KEY_LEFT):
        menu -= 1
    if pyxel.btnr(pyxel.KEY_RIGHT):
        menu += 1
    if pyxel.btnr(pyxel.KEY_SPACE):
        n = int(input())
    
    


# =========================================================
def draw():
    """création des objets (30 fois par seconde)"""

    # vide la fenetre
    pyxel.cls(0)

    # un rectangle
    pyxel.rect(16,16, 226, 16, 1)
    txt = 'menu = '  + str(menu)
    pyxel.text(20,20, txt, 7)

pyxel.run(update, draw)