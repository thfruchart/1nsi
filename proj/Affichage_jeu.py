import pyxel
######### INIT #########
LARGEUR_FENETRE = 256
HAUTEUR_FENETRE = 256
pyxel.init(LARGEUR_FENETRE, HAUTEUR_FENETRE, title="Jeu de cartes")
pyxel.mouse(True)

##### chargement du fichier .pyxres  ####
pyxel.load("monfichier.pyxres")
#####################################################
# pour éditer ce fichier, sélectionner dans le menu #
# Outils/Ouvrir la console du système               #
# puis taper la commande                            #
# pyxel edit monfichier.pyxres                      #
#####################################################



##### affichage en mode console ####
dico_couleur = {'Pique' : '\u2660' , 'Coeur': '\u2665', 'Carreau' : '\u2666' , 'Trèfle' : '\u2663', 'A':'a', 'B':'b', 'C':'c', 'D':'d'}
dico_valeur = { i : ' '+str(i)  for i in range(2,10)}
dico_valeur[10]='10'
dico_valeur[0]=' ?'


def valeur(carte):
    return carte[0]
def couleur(carte):
    return carte[1]
def aff_carte_console(carte):
    print(dico_valeur[valeur(carte)]+dico_couleur[couleur(carte)], end=' ')

### exemples de tableaux de jeu ###
t1 = [[(7, 'Coeur'), (10, 'Trèfle'), (6, 'Trèfle'), (7, 'Pique'), (4, 'Carreau'), (5, 'Coeur'), (2, 'Coeur'), (3, 'Coeur'), (6, 'Coeur'), (0, 'A')],
      [(7, 'Carreau'), (6, 'Carreau'), (8, 'Trèfle'), (3, 'Trèfle'), (8, 'Coeur'), (6, 'Pique'), (3, 'Pique'), (8, 'Pique'), (2, 'Trèfle'), (0, 'B')],
      [(3, 'Carreau'), (9, 'Pique'), (7, 'Trèfle'), (4, 'Coeur'), (10, 'Coeur'), (2, 'Pique'), (10, 'Carreau'), (10, 'Pique'), (9, 'Trèfle'), (0, 'C')],
      [(8, 'Carreau'), (4, 'Pique'), (5, 'Trèfle'), (2, 'Carreau'), (4, 'Trèfle'), (5, 'Pique'), (5, 'Carreau'), (9, 'Coeur'), (9, 'Carreau'), (0, 'D')]]

t2 = [[(10, 'Pique'), (9, 'Pique'), (8, 'Pique'), (7, 'Trèfle'), (6, 'Trèfle'), (5, 'Trèfle'), (4, 'Trèfle'), (3, 'Trèfle'), (2, 'Trèfle'), (3, 'Carreau')],
      [(10, 'Trèfle'), (2, 'Coeur'), (8, 'Trèfle'), (2, 'Pique'), (3, 'Coeur'), (2, 'Carreau'), (0, 'A'), (0, 'C'), (0, 'B'), (0, 'D')],
      [(10, 'Carreau'), (9, 'Carreau'), (8, 'Carreau'), (3, 'Pique'), (6, 'Pique'), (5, 'Pique'), (4, 'Pique'), (9, 'Trèfle'), (5, 'Carreau'), (4, 'Carreau')],
      [(10, 'Coeur'), (9, 'Coeur'), (8, 'Coeur'), (7, 'Coeur'), (6, 'Coeur'), (5, 'Coeur'), (4, 'Coeur'), (7, 'Carreau'), (6, 'Carreau'), (7, 'Pique')]]


def affiche_jeu_console(tab):
    for i in range(4) :
        for j in range(10) :
            carte = tab[i][j]
            aff_carte_console(carte)
        print()
    print()


##### affichage avec pyxel ####
MARGE = 16
LARGEUR_CASE = (LARGEUR_FENETRE - 2*MARGE) // 10
LARGEUR_CARTE = 16

HAUTEUR_CASE =  (HAUTEUR_FENETRE - 2*MARGE) // 4
HAUTEUR_CARTE = 16

coord = {'Pique' :  (0,0),
         'Trèfle' : (16,16),
         'Coeur' :  (16,0) ,
         'Carreau': (0,16) ,
         'A' : (0,32), 
         'B' : (0,32) ,
         'C' : (0,32) ,
         'D' : (0,32) 
        }
def dessine_carte(carte, i, j):
    pyxel.rect(MARGE + j*LARGEUR_CASE, MARGE +i*HAUTEUR_CASE, LARGEUR_CARTE, HAUTEUR_CARTE,1+(i+j)%15)
    x_img,y_img,w_img,h_img = MARGE + j*LARGEUR_CASE, MARGE +i*HAUTEUR_CASE, LARGEUR_CARTE, HAUTEUR_CARTE
    # valeur de la carte
    coordx, coordy = 32, 16*carte[0]
    if carte[1] in ('Pique','Trèfle'):
        pyxel.rect(x_img,y_img,w_img,h_img,0)
    else :
        pyxel.rect(x_img,y_img,w_img,h_img,8)
    pyxel.blt(x_img,y_img, 0,coordx, coordy,w_img,h_img, 5)
    # couleur de la carte
    coordx, coordy = coord[carte[1]]
    pyxel.blt(x_img,y_img+16, 0,coordx, coordy,w_img,h_img)
    
    

def dessine_jeu(tab):
    for i in range(4) :
        for j in range(10) :
            carte = tab[i][j]
            dessine_carte(carte, i, j)


def update():
    pass

def draw():
    pyxel.cls(0)
    pyxel.text(MARGE,0,"jeu de cartes",10)
    #pyxel.rect(MARGE , MARGE, LARGEUR_CASE, HAUTEUR_CASE,1)
    #pyxel.rect(MARGE , MARGE, LARGEUR_CARTE, HAUTEUR_CARTE,2)
    #pyxel.rect(MARGE +  LARGEUR_CASE, MARGE, LARGEUR_CASE, HAUTEUR_CASE,1)
    #pyxel.rect(MARGE +  LARGEUR_CASE, MARGE, LARGEUR_CARTE, HAUTEUR_CARTE,2)
    
    #dessine_carte((10, 'Pique'), 0, 1)
    #dessine_carte((10, 'Pique'), 0, 1)
    dessine_jeu(t1)
    dessine_carte((10, 'Pique'), 0, 1)
    


pyxel.run(update, draw) 

