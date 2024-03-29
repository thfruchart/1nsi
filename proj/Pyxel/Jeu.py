import pyxel
from random import randint


LARG = 128
HAUT = 128
CASE = 8
VECT_DIR = {'Haut':(0,-1), 'Bas':(0,1), 'Gauche':(-1,0), 'Droite':(1,0)}

pyxel.init(LARG, HAUT)
pyxel.load("monfichier.pyxres")
delai = 10
pomme = [0,0]
serpent = [(10,1),(11,1),(12,1)]
direction = 'Gauche'
gameover = False
score = 0

def new_pomme():
    x = randint(0, LARG//CASE-1)
    y = randint(0, HAUT//CASE-1)
    while (x,y) in serpent :
        x = randint(0, LARG//CASE-1)
        y = randint(0, HAUT//CASE-1)
    pomme[0] = x
    pomme[1] = y

new_pomme()


def reinitialiser():
    global serpent, direction, gameover, score, delai
    serpent = [(10,1),(11,1),(12,1)]
    direction = 'Gauche'
    gameover = False
    score = 0
    delai = 10
    

def update():
    global direction
    global gameover
    global delai
    global score
    if gameover :
        if pyxel.btn(pyxel.KEY_N) :
            pyxel.quit()
        elif pyxel.btn(pyxel.KEY_O):
            reinitialiser()
        else :
            return
    if pyxel.btn(pyxel.KEY_DOWN) and direction != 'Haut' :
        direction = 'Bas'
    if pyxel.btn(pyxel.KEY_UP) and direction != 'Bas':
        direction = 'Haut'
    if pyxel.btn(pyxel.KEY_LEFT) and direction != 'Droite':
        direction = 'Gauche'
    if pyxel.btn(pyxel.KEY_RIGHT) and direction != 'Gauche':
        direction = 'Droite'
    if pyxel.frame_count % delai == 0 :
        #coordonnée du premier élément du serpent
        x,y = serpent[0]
        #coordonnées du déplacement
        u,v = VECT_DIR[direction]
        #nouvelles coordonnées
        tete = (x+u, y+v)
        #ajout en tete du serpent
        serpent.insert(0,tete)
        #le serpent mange-t-il la pomme ?
        if tete == (pomme[0], pomme[1]):
            score += 1
            new_pomme()
            if delai > 2:
                delai -=1
        else : 
            serpent.pop()
        if tete[0]<0 or tete[0] >= LARG//CASE :
            gameover = True
        if tete[1]<0 or tete[1] >= HAUT//CASE :
            gameover = True
        if tete in serpent[1:]:
            gameover = True
        
            
    return

def draw():
    if gameover :
        pyxel.text(10,10,"GAME OVER",6)
        pyxel.text(LARG // 3, HAUT //2 ,"REJOUER (O/N)?",6)
        return
    pyxel.cls(0)
    pyxel.text(0,0,"Score : "+ str(score),6)
    # pomme
    pyxel.blt(pomme[0]*CASE, pomme[1]*CASE, 0,16,0,CASE, CASE)
    for i in range(len(serpent)):
        element = serpent[i]
        x, y = element
        if i == 0:
            if direction in ('Haut', 'Bas'):
                x_img,y_img,w_img,h_img = 8,8,8,8
                if direction == 'Bas':
                    h_img *= -1
            if direction in ('Gauche', 'Droite'):
                x_img,y_img,w_img,h_img = 0,8,8,8
                if direction == 'Gauche':
                    w_img *= -1
        else :
            x_img,y_img,w_img,h_img = 8,0,8,8
        pyxel.blt(x*CASE, y*CASE,0,x_img,y_img,w_img,h_img)

    
pyxel.run(update, draw)