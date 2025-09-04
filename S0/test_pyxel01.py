import pyxel
pyxel.init(128,128, title="1ère NSI")


n = 0

def saisir():
    global n
    n = int(input('Entrer un entier : '))
    

def update():
    if pyxel.btnp(pyxel.KEY_Q):
        pyxel.quit()
    if pyxel.btnp(pyxel.KEY_S):
        saisir()
        
def draw():
    pyxel.cls(0)
    pyxel.rect(10,10,20,20,11)
    pyxel.text(100, 100, str(n), 3)
    
pyxel.run(update,draw)


