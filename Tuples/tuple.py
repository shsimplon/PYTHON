#collection: contenir plusieur element : 
# tableaux = array: notion retrouver dans les bibliotheque en python
#  tuples= c'est fixe pas d'ajout d'elements: non modifiable => immutable
# listes: on peut ajouter: modifiable ==>mutable

#tuples
personnes=("sam", "amelia","yazid")
for i in personnes:
    print (i)
    print(len(i)) #claculer le nombre de caractere de chaque i , il se comporte comme un tableau
print(len(personnes))
print(personnes[-1])        #recuperer le derinier element

#liste
personnes=["sam", "amelia","yazid"]  
personnes.append("you")
print(personnes)


#function et tuples

def afficher_infos():
    return "samira " , 37  , 1.64 
infos=afficher_infos()
print(infos)      #affiche un tuple
print(*infos)      #affiche les valeurs



#.......................slices....................................#

personnes=("sam", "amelia","yazid","yes","waw")

#[start:stop:step]
#for i in personnes[0::1]:     #affiche tous
#for i in personnes[::2]:  # affiche 1/2  : sam , yazid , waw
#for i in personnes[::-1]:     #affihce tous en passant par le dernier
for i in personnes[::-2]:       #affiche 1/2 en commencant par le dernier

    print (i)