
#personnes = [
    #("Mélanie", 25, 1.6),
    #("Paul", 29, 1.8),
    #("Jacques", 35, 1.75),
    #("Martin", 16, 1.65)
#]


#cette methode n'est pas optimisé : imaginons on a des miliers de données
#def affiches_valeurs(nom, donnes):
 #   for i in donnes:
  #      if i[0]==nom:
   #         print (i)

#affiches_valeurs("Paul", personnes)

#dictionnaire


personnes_dict = {
    "Mélanie": (25, 1.6),
    "Paul": (29, 1.8),
    "Jacques": (35, 1.75),
    "Martin": (16, 1.65)
}
infos = personnes_dict.get("Martin")
if not infos:
    print("La clef n'existe pas")
else:
    print(infos)
