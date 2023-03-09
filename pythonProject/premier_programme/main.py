def demander_age(nom_personne):
    age = 0
    while age == 0:
        ageStr = input("quel est votre age " + nom_personne)
        try:
            age = int(ageStr)
        except:
            print("ERREUR: rentrer un chiffre")
    return age


def demander_nom():
    nomEmty = ""
    while (nomEmty == ""):
        nomEmty = input("quel est votre nom ")
    return nomEmty


def affichage(nomPersonne, agePersonne):
    print()
    print("vous vous appeler  " + nomPersonne + " , vous avez " + str(agePersonne) + " ans")
    print("l'année prochaine vous aurez " + str(agePersonne + 1))
    if 18 <= agePersonne <= 69:
        print("vous etes majeur")
    elif 10 < agePersonne < 18:
        print("mineur")
    elif agePersonne >= 70:
        print("vieux")
    else:
        print("vous etes ENFANT ")


#nomPersonne = demander_nom()
# nomPersonne1 = demander_nom()


#agePersonne = demander_age(nomPersonne)
# agePersonne1 = demander_age(nomPersonne1)


#affichage(nomPersonne, agePersonne)
# affichage(nomPersonne1 , agePersonne1)

for i in range(0, 3):
    nom = "personne "+ str(i + 1)
    age = demander_age(nom)
    affichage(nom, age)

