# POO EXERCICE DE MISE EN SITUATION 4

# ---
class Personne:
    def __init__(self, nom: str):
        self.nom = nom

    def SePresenter(self):
        print("Bonjour, je m'appelle " + str(self.nom))

# ---
nombre_personne=3
noms = []
for i in range(nombre_personne):
    nom=(input("nom de la personne "+ str(i) + ": "))
    noms.append(Personne(nom))
for personne in noms:
   personne.SePresenter()
