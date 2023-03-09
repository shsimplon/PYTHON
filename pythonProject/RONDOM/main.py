import random


def demander_nombre_magique(nb_min, nb_max):
    nombre_magique_int = 0
    while nombre_magique_int == 0:
        nombre_magique_entrer = input(f"rentrez un nombre magique entre {nb_min} et {nb_max} ? ")
        # essaye commeca
        try:
            nombre_magique_int = int(nombre_magique_entrer)
        # sinon capte l'erreur
        except:
            print('ERROR: renter un chiffre')
        else:
            if nombre_magique_int < nb_min or nombre_magique_int > nb_max:
                print(f" ERROR: le nombre doit etre  entre {nb_min} et {nb_max} reesayer :")
                # pour ne pas continuer directement on doit le forcer à reboucler
                nombre_magique_int = 0

    return nombre_magique_int


nb_min = 1
nb_max = 10
nombre_magique = random.randint(nb_min, nb_max)
nombre = 0
nb_vie = 4
vie=nb_vie
while not nombre_magique == nombre and vie>0:
    print(f"il vous rest{vie} de vies ")
    nombre = demander_nombre_magique(1, 10)
    if nombre == nombre_magique:
        print("bravo trouvé")
    elif nombre < nombre_magique:
        print(f"donner un chiffre superieur à {nombre}")
        vie-=1
    else:
        print(f"donner un chiffre inférieur à {nombre}")
        vie -= 1
if vie==0:
    print(f"perdu , tu as utilisé toutes les vies ; Ooops le nombre magique etait {nombre_magique} ")