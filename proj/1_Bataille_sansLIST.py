# Pyxel Studio

import pyxel, random
pyxel.init(256, 256, title="Chute libre")
pyxel.mouse(False)

couleur_fond = 0
# position initiale (si la souris est à l'extérieur de l'écran)
xm,ym = -100,-100
vies = 3


# objet tombant = CIBLE
xc = 120
yc = 0
rc = 8
vitesse = 1
dr = -1 # variation du rayon de la cible


# tir
x_tir, y_tir = -10,-10 # initialement hors de l'écran
v_tir = 3

# tir adverse
x_adv, y_adv = 300,300 # initialement hors de l'écran
dernier_tir_adverse = pyxel.frame_count


# scores
score = 0
meilleur_score = 0
perdu = False

# =========================================================
def update():
    global xc,yc,rc, vitesse,dr, xm, ym, score, meilleur_score, couleur_fond,x_tir, y_tir, vies, x_adv, y_adv,dernier_tir_adverse, perdu, clip 
    """mise à jour des variables (30 fois par seconde)"""
    if perdu : # un appui sur ESPACE ré-initialise la partie
        if pyxel.btn(pyxel.KEY_SPACE) :
            perdu = False
            yc=-rc
            xc = random.randint(20,236)
            vitesse = 1
            score = 0
            vies = 3
            couleur_fond = 1- couleur_fond
        return
    
    if pyxel.btnr(pyxel.KEY_C) :
        clip = not clip 
    yc += vitesse
    rc += dr
    if rc<4 or rc>12: 
        dr = -dr
    # déplacement des tirs
    y_tir -= v_tir
    y_adv += v_tir + vitesse
    xm,ym = pyxel.mouse_x, pyxel.mouse_y
    if pyxel.btn(pyxel.MOUSE_BUTTON_LEFT) :
        x_tir, y_tir = xm,ym
    # TIR touche vaisseau
    xt,yt = x_tir, y_tir-5
    if (xt-xc)**2+(yt-yc)**2<rc**2:
        yc=-rc
        xc = random.randint(20,236)
        vitesse += 0.25
        xm,ym = -100,-100
        x_tir, y_tir = -10,-10
        score += 1
    # CONTACT
    if (xm-xc)**2+(ym-yc)**2<=(rc+3)**2:
        vies -= 1
        if vies > 0 :
            yc=-rc
            xc = random.randint(20,236)

    # nouveau tir adverse :
    if dernier_tir_adverse + 30 < pyxel.frame_count  :
        if abs(xc-xm)<4 :
            x_adv, y_adv = xc, yc
            dernier_tir_adverse = pyxel.frame_count

            
    if score > meilleur_score :
        meilleur_score = score

    if yc > 256 or vies <= 0:
        perdu = True 


# =========================================================
def draw():
    """création des objets (30 fois par seconde)"""

    # vide la fenetre
    pyxel.cls(couleur_fond)
    
    # CERCLES
    #cible
    pyxel.circ(xc, yc, rc, 9)
    #joueur
    pyxel.circ(xm, ym, 4, 5+couleur_fond)
    # TIRS
    # tir joueur
    pyxel.line(x_tir,y_tir, x_tir,y_tir-5,10)
    # tir adverse
    pyxel.line(x_adv, y_adv, x_adv, y_adv+5,8)
    # AFFICHAGES
    # affichage des scores
    pyxel.text(20,240, "PV : "+ str(vies)+ ' Score : ' + str(score) +  "   meilleur score : " + str(meilleur_score), 7)
    # affichage si PERDU
    if perdu :
        pyxel.text(120,128, "PERDU", 7)
        pyxel.text(20,200, "APPUYER SUR <ESPACE>", 7)
    
    

pyxel.run(update, draw)