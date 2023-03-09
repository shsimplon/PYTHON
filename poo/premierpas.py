###
# VOS PREMIERS PAS EN POO (PROGRAMMATION ORIENTÉE OBJET)
###
# - Différence programmation impérative / objet
# - Le plus simple possible
# - Exercices, mises en situation

# Personne  (entité -> class)
#    Données : nom, age
#    Actions :  (méthodes)
#       - SePresenter()
#       - DemanderNom() / input
#  [Personne "Jean"]     [Personne "Paul"]

# def afficher_informations_personne(nom, age):
#     print(f"La personne s'appelle {nom}, son age est {age} ans")

# def demanger_nom_personne():
#     nom = input("Quel est votre nom ?")
#     return nom

# nom1 = "Jean"
# age1 = 30

# nom2 = "Paul"
# age2 = 25

# afficher_informations_personne(nom1, age1)
# afficher_informations_personne(nom2, age2)

# nom3 = demanger_nom_personne()
# age3 = 18
# afficher_informations_personne(nom3, age3)


#difinition de la class

class Personne:

    #constructeur
    def __init__(self, nom:str="", age:int=0):
        self.nom=nom
        self.age=age
        self.rentrerTonNom()


    #methodes


    def sepresenter(self):
       
        print(f"je m'appelle {self.nom} et j'ai {self.age } ans" )
        # if self.age>18:
        #     print("majeur")
        # else:
        #     print("mineur")

        if  self.estIlMajeur:
            print("majeur")
        else:
             print("mineur")

    def rentrerTonNom(self):
        self.nom=input("quel votre nom?")
        self.age=input("quel votre age?")

    def estIlMajeur(self):
        return int(self.age) >= (18)

#utilisation
#grace au self on cree un objet en mémoire
# personne1=Personne( 'tous',30) 
# personne1.sepresenter()
personne2=Personne()
personne2.sepresenter()
