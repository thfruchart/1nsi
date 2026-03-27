import pyxel

pyxel.init(256, 256, title="SPACE BATTLE")

vaisseau = [60,60]

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


# =========================================================
# == DRAW
# =========================================================
def draw():
    """création des objets (30 fois par seconde)"""
    # vide la fenetre
    pyxel.cls(0)

    # vaisseau (carre 8x8)
    pyxel.rect(vaisseau[0], vaisseau[1], 16, 16, 12)
    

pyxel.run(update, draw)