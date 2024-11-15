import pyxel
L_ECRAN = 256
H_ECRAN = 128
pyxel.init(L_ECRAN, H_ECRAN, title="Vaisseau")

# position initiale du vaisseau
vaisseau_x = 60
vaisseau_y = 60
# liste des tirs
tirs_vaisseau = []

# liste initiale d'ennemis
ennemis_list = [ [L_ECRAN - 60, 60 ] ]

# liste d'explosions
explose_list = []

def vaisseau_deplacement():
    """déplacement avec les touches de directions"""
    global vaisseau_x, vaisseau_y
    
    if pyxel.btn(pyxel.KEY_RIGHT):
        if (vaisseau_x +8 < L_ECRAN) :
            vaisseau_x += 1
    if pyxel.btn(pyxel.KEY_LEFT):
        if (vaisseau_x > 0) :
            vaisseau_x -= 1
    if pyxel.btn(pyxel.KEY_DOWN):
        if (vaisseau_y + 8 < H_ECRAN) :
            vaisseau_y += 1
    if pyxel.btn(pyxel.KEY_UP):
        if (vaisseau_y > 0) :
            vaisseau_y  -= 1


def nouveau_tir():
    if pyxel.btnr(pyxel.KEY_SPACE):
        tir = [ vaisseau_x+8 , vaisseau_y+4]
        tirs_vaisseau.append(tir)
        print(tirs_vaisseau)

def deplacement_tirs() :
    for tir in tirs_vaisseau :
        tir[0]+= 1
        if tir[0] > L_ECRAN:
            tirs_vaisseau.remove(tir)
    
def explosions():
    # pour chaque ennemi
    for ennemi in ennemis_list :
        x_e, y_e = ennemi[0], ennemi[1]
        # l'un des tirs a-t-il touché l'ennemi?
        


# =========================================================
# == UPDATE
# =========================================================
def update():
    """mise à jour des variables (30 fois par seconde)"""
    if pyxel.btn(pyxel.KEY_Q):
        pyxel.quit()
    
    vaisseau_deplacement()
    nouveau_tir()
    deplacement_tirs()
    explosions()


# =========================================================
# == DRAW
# =========================================================
def draw():
    """création des objets (30 fois par seconde)"""
    # vide la fenetre
    pyxel.cls(0)
    # vaisseau (carre 8x8)
    pyxel.rect(vaisseau_x, vaisseau_y, 8, 8, 5)
    # ennemis (carré 8x8 couleur 6)
    for ennemi in ennemis_list : 
        pyxel.rect(ennemi[0], ennemi[1], 8, 8, 6)
    # tirs
    for tir in tirs_vaisseau :
        pyxel.line( tir[0],tir[1],tir[0]+4,tir[1],10)
        
    

pyxel.run(update, draw)

