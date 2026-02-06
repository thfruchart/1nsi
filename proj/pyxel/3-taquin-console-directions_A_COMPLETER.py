# tableau mélangé à remettre dans l'ordre en utilisant les fonctions à définir :
# haut() bas() gauche() et droite()
tab = [[2, 6, 3],
       [7, 0, 5],
       [4, 1, 8]]


def zero_coord(tab):
    """renvoie l'indice de ligne (i) et l'indice de colonne (j) du 0 dans tab"""
    for i in range(3):
        for j in range(3):
            if tab[i][j] == 0 :
                return i,j

def haut() :
    """échanger le 0 avec la valeur située juste en dessous dans tab
    """
    i0, j0 = zero_coord(tab)
    if i0 + 1 < 3 :
        tab[i0][j0] = tab[i0+1][j0]
        tab[i0+1][j0] = 0
    return tab

def bas() :
    """échanger le 0 avec la valeur située juste au-dessus dans tab
    """
    i0, j0 = zero_coord(tab)
    if ...   :
        tab[i0][j0] = tab[...][j0]
        tab[...][j0] = 0
    return tab

def droite() :
    """échanger le 0 avec la valeur située juste à gauche dans tab
    """
    i0, j0 = zero_coord(tab)
    if ...  :
        tab[i0][j0] = tab[i0][...]
        tab[i0][...] = 0
    return tab

def gauche() :
    """échanger le 0 avec la valeur située juste à droite dans tab
    """
    i0, j0 = zero_coord(tab)
    if ...  :
        tab[i0][j0] = tab[i0][...]
        tab[i0][...] = 0
    return tab