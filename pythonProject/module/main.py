# LES COLLECTIONS : LISTES / TUPLES
# Swapper deux éléments (échanger)

#          0        1        2           3           4
noms = ["Jean", "Sophie", "Martin", "Christophe", "Zoe"]

#                     Zoe      Jean
noms[0], noms[4] = noms[4], noms[0]

print(noms)


# LES COLLECTIONS : LISTES / TUPLES
# Operations sur les éléments : min, max, in, sum

#          0        1        2           3           4
noms = ["Jean", "Sophie", "Martin", "Christophe", "Zoe"]

ages = [21, 20, 30, 25, 22]

'''if 31 in ages:
    print("Présent")
else:
    print("Abscent")'''

'''found = False
for nom in noms:
    if nom == "Martin":
        found = True
        break
if found:
    print("Présent")
else:
    print("Abscent")'''

print(sum(ages))
# Tris : Sort / Sorted

def tri_longeur_caracteres(nom):
    return len(nom)

#          0        1        2           3           4
noms = ["Jean", "Sophie", "Martin", "Christophe", "Zoe"]

# tri par ordre alphabetique STR
# du plus petit au plus grand INT
#noms.sort(key=tri_longeur_caracteres, reverse=True)  # inplace
noms_tries = sorted(noms, key=tri_longeur_caracteres, reverse=True)  # créer une nouvelle liste

print(noms)
print(noms_tries)


# Append / Extend / += / Insert

noms = ["Jean", "Sophie", "Martin"]

noms_supplementaires = ["Christophe", "Zoe"]

#noms.append(noms_supplementaires)
# for e in noms_supplementaires:
#    noms.append(e)
#noms.extend(noms_supplementaires)
# noms += noms_supplementaires
# noms = noms + noms_supplementaires

# noms.append("Toto")
# noms.insert(1, "Toto")

noms = noms + noms_supplementaires

print(noms)


# Slices

#          0        1        2           3           4
noms = ["Jean", "Sophie", "Martin", "Christophe", "Zoe"]

slices_noms = noms[-2:]

#noms[0] = "Toto"

print(slices_noms)
#print(noms)



# join et split

#          0        1        2           3           4
noms = ["Jean", "Sophie", "Martin", "Christophe", "Zoe"]

# Join : Rejoindre -> coller

noms_join = ", ".join(noms)
print(noms_join)

# Split : Séparer
# a = "Paul-Marc-Emilie"
#a_split = a.split("-")
#print(a_split)

noms_resconstruits = noms_join.split(", ")
print(noms_resconstruits)

# index, find et count

#          0        1        2           3           4      5
noms = ["Jean", "Sophie", "Martin", "Christophe", "Zoe", "Martin"]


element_cherche = "Martin"
nb_occurences = noms.count(element_cherche)
print("nb_occurences", nb_occurences)
if nb_occurences > 0:
    index_occurence = 0
    for i in range(nb_occurences):
        index_occurence = noms.index(element_cherche, index_occurence)
        print(element_cherche, "trouvé à", index_occurence)
        index_occurence += 1
else:
    print("L'élément n'est pas dans la collection")


# index, find et count

#          0        1        2           3           4      5
noms = ["Jean", "Sophie", "Martin", "Christophe", "Zoe", "Martin"]


element_cherche = "Martin"
nb_occurences = noms.count(element_cherche)
print("nb_occurences", nb_occurences)
if nb_occurences > 0:
    index_occurence = 0
    for i in range(nb_occurences):
        index_occurence = noms.index(element_cherche, index_occurence)
        print(element_cherche, "trouvé à", index_occurence)
        index_occurence += 1
else:
    print("L'élément n'est pas dans la collection")


# Les compréhensions de listes

#          0        1        2           3           4      5
noms = ["Jean", "Sophie", "Martin", "Christophe", "Zoe", "Martin"]

'''longeur_noms = []
for nom in noms:
    longeur_noms.append(len(nom))'''

# longeur_noms = [len(nom) if len(nom) < 10 else 0 for nom in noms]
# noms_avec_e = [nom for nom in noms if "e" in nom]

#a = [i for i in range(11) if (i//2)*2 != i]
b = [(i, True if (i//2)*2 == i else False) for i in range(11)]

print(b)



LES COLLECTIONS : LISTES / TUPLES
# Any et All
# Any : Quelconque / n'importe quel
# All : Tous

#          0        1        2           3           4      5
noms = ["Jean", "Sophie", "Martin", "Christophe", "Zoe", "Martin"]

'''a = [True, True, True, True]
print(any(a))
print(all(a))'''


'''found = False
for nom in noms:
    if "z" in nom.lower():
        found = True
        break

if found:
    print("Trouvé")
else:
    print("Non trouvé")'''

nom_avec_un_z_existe = all([True if "e" in nom.lower() else False for nom in noms])
if nom_avec_un_z_existe:
    print("Trouvé")
else:
    print("Non trouvé")
# Tester si une chaine contient des chiffres
# any / isdigit


def chaine_contient_chiffre(chaine):
    """for c in chaine:
        if c.isdigit():
            return True
    return False"""
    return any([c.isdigit() for c in chaine])

nom = input("Quel est ton nom ? ")
if nom == "":
    print("Le nom est vide")
elif chaine_contient_chiffre(nom):
    print("Ce nom est invalide, il ne doit pas contenir de chiffres")
else:
    print("Bonjour " + nom)
# Collections : Le Set

'''noms = ["Marie", "Paul", "Jean", "Marc", "Emilie", "Marie"]
noms_sans_doublons = list(set(noms))
print(noms_sans_doublons)
print(noms_sans_doublons[0])'''

set_noms = { "Marie", "Paul", "Jean", "Marc", "Emilie", "Marie" }
print(set_noms)

# for s in set_noms:
#     print(s)
