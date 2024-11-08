import pyxel

pyxel.init(128, 128, title="Vaisseau")

# position initiale du vaisseau
vaisseau_x = 60
vaisseau_y = 60

def vaisseau_deplacement():
    """déplacement avec les touches de directions"""
    global vaisseau_x, vaisseau_y
    
    if pyxel.btn(pyxel.KEY_RIGHT):
        if (vaisseau_x < 120) :
            vaisseau_x += 1
    if pyxel.btn(pyxel.KEY_LEFT):
        if (vaisseau_x > 0) :
            vaisseau_x -= 1
    if pyxel.btn(pyxel.KEY_DOWN):
        if (vaisseau_y < 120) :
            vaisseau_y += 1
    if pyxel.btn(pyxel.KEY_UP):
        if (vaisseau_y > 0) :
            vaisseau_y  -= 1


# =========================================================
# == UPDATE
# =========================================================
def update():
    """mise à jour des variables (30 fois par seconde)"""
    if pyxel.btn(pyxel.KEY_Q):
        pyxel.quit()
    
    vaisseau_deplacement()


# =========================================================
# == DRAW
# =========================================================
def draw():
    """création des objets (30 fois par seconde)"""

    # vide la fenetre
    pyxel.cls(0)

    # vaisseau (carre 8x8)
    pyxel.rect(vaisseau_x, vaisseau_y, 8, 8, 5)

pyxel.run(update, draw)
