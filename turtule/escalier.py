import turtle
t=turtle.Turtle()

def tortue(taille , nb ):

    for i in range(0, nb):
        t.forward(taille)
        t.left(90)
        t.forward(taille)
        t.right(90)
#si on veux decrementer à chaque boucle
        taille -= 5
#remettre droit la fleche
    t.forward(taille)

tortue(50, 5)



turtle.done()