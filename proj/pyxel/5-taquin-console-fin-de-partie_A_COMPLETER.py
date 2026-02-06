# Ecrire une fonction qui permet de tester si le jeu est gagné

# Ecrire une fonction qui permet de "mélanger" le tableau 'tab'
# pour qu'une nouvelle partie puisse débuter.

tab = [[2, 6, 3],
       [7, 0, 5],
       [4, 1, 8]]

# tableau ordonné :
objectif = [[1,2,3],
            [4,5,6],
            [7,8,0]]

##########################
# les 4 mouvements de base
##########################
def zero_coord(tab):
    """renvoie l'indice de ligne (i) et l'indice de colonne (j) du 0 dans tab"""
    for i in range(3):
        for j in range(3):
            v = tab[i][j]
            #print(i,j, v) 
            if v == 0 :
                return i,j
def haut() :
    """échanger le 0 avec la valeur située juste en dessous dans tab"""
    i0, j0 = zero_coord(tab)
    if i0 + 1 < 3 :
        tab[i0][j0] = tab[i0+1][j0]
        tab[i0+1][j0] = 0
    return tab
def bas() :
    """échanger le 0 avec la valeur située juste au-dessus dans tab"""
    i0, j0 = zero_coord(tab)
    if i0 - 1 >= 0  :
        tab[i0][j0] = tab[i0-1][j0]
        tab[i0-1][j0] = 0
    return tab
def droite() :
    """échanger le 0 avec la valeur située juste à gauche dans tab"""
    i0, j0 = zero_coord(tab)
    if j0 - 1 >= 0  :
        tab[i0][j0] = tab[i0][j0-1]
        tab[i0][j0-1] = 0
    return tab
def gauche() :
    """échanger le 0 avec la valeur située juste à droite dans tab"""
    i0, j0 = zero_coord(tab)
    if j0 + 1 < 3  :
        tab[i0][j0] = tab[i0][j0+1]
        tab[i0][j0+1] = 0
    return tab
