# Pyxel Studio

import pyxel, random
pyxel.init(256, 256, title="Chute libre")
pyxel.mouse(False)

couleur_fond = 0
# position initiale (si la souris est à l'extérieur de l'écran)
xm,ym = -100,-100
vies = 3


# cible [xc, yc, rc, vitesse, dr]
cible = [120, 0,  8,       1, -1]

# chaque tir aura 2 valeurs : x_tir, y_tir 
tir_list = [] # initialement, il n'y a aucun tir

# vitesse des tirs
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
    global  xm, ym, score, meilleur_score, couleur_fond,x_tir, y_tir, vies, x_adv, y_adv,dernier_tir_adverse, perdu, clip 
    """mise à jour des variables (30 fois par seconde)"""
    if perdu : # un appui sur ESPACE ré-initialise la partie
        if pyxel.btn(pyxel.KEY_SPACE) :
            perdu = False
            cible[1]=-cible[2]
            cible[0] = random.randint(20,236)
            cible[3] = 1
            score = 0
            vies = 3
            couleur_fond = 1- couleur_fond
        return
    
    # évolution de la cible
    cible[1] += cible[3] # mouvement vertical
    cible[2] += cible[4] # changement du rayon
    if cible[2]<4 or cible[2]>12: 
        cible[4] = -cible[4]  # alterner grossir et réduire le rayon de la cible

    # déplacement des tirs
    for tir in tir_list : 
        tir[1] -= v_tir
    
    # tir adverse
    y_adv += v_tir + cible[3]
    
    #déplacement de la souris
    xm,ym = pyxel.mouse_x, pyxel.mouse_y
    
    # NOUVEAU TIR DU JOUEUR
    if pyxel.btnr(pyxel.MOUSE_BUTTON_LEFT) :
        nouveau_tir =  [xm,ym]
        tir_list.append(nouveau_tir)

    # TIR touche vaisseau ?
    for tir in tir_list : 
        xt,yt = tir[0], tir[1]-5
        if (xt-cible[0])**2+(yt-cible[1])**2<cible[2]**2:
            cible[1] = -cible[2]
            cible[0] = random.randint(20,236)
            cible[3] += 0.25
            xm,ym = -100,-100
            score += 1
            # suppression du tir
            tir_list.remove(tir)

    # CONTACT
    if (xm-cible[0])**2+(ym-cible[1])**2<=(cible[2]+3)**2:
        vies -= 1
        if vies > 0 :
            cible[1] = -cible[2]
            cible[0] = random.randint(20,236)

    # nouveau tir adverse :
    if dernier_tir_adverse + 30 < pyxel.frame_count  :
        if abs(cible[0]-xm)<4 :
            x_adv, y_adv = cible[0], cible[1]
            dernier_tir_adverse = pyxel.frame_count

            
    if score > meilleur_score :
        meilleur_score = score

    if cible[1] > 256 or vies <= 0:
        perdu = True 


# =========================================================
def draw():
    """création des objets (30 fois par seconde)"""

    # vide la fenetre
    pyxel.cls(couleur_fond)
    
    # CERCLES
    #cible
    pyxel.circ(cible[0], cible[1], cible[2], 9)
    #joueur
    pyxel.circ(xm, ym, 4, 5+couleur_fond)
    # TIRS
    # tir joueur
    for tir in tir_list :
        pyxel.line(tir[0],tir[1], tir[0],tir[1]-5,10)
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