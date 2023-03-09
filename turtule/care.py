import turtle
t=turtle.Turtle()


def carre(taille):

        for i in range(0, 4):
        
            t.forward(taille)
            t.right(90)
       
carre(90)

def carres(taille, nb):
    for i in range(1, 4):
        nombre=i*taille          
        carre(nombre)

carres(40, 10)








turtle.done()