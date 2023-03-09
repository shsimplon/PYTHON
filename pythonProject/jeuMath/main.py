import random

nb_min = 1
nb_max = 5


def reponder_aux_question():
    a = random.randint(nb_min, nb_max)
    b = random.randint(nb_min, nb_max)
    # faire aleatoire soir une multiplication soit une addition
    o = random.randint(0, 1)
    operator_addition = "+"
    if o == 1:
        operator_addition = "*"
    # addition
    resStr = input(f"claculer {a}{operator_addition}{b}= ")
    resInt = int(resStr)
    addition = a+b
    multiplication= a*b

    if resInt == addition or resInt==multiplication:
        print("reponse correct")
        return True
    else:
        print("reponse false")
        return False


nb_reponses = 0
NB_questions = 4
moyenne = int(NB_questions / 2)

for i in range(0, NB_questions):
    print(f"Question n° {i + 1} sur 4 :")
    if reponder_aux_question():
        nb_reponses += 1
    print()

    # nobre de reponse
print(f"nombre de reponses est egale {nb_reponses} / {NB_questions}")

if nb_reponses == 0:
    print("revisez")
elif NB_questions == nb_reponses:
    print("excelent")
elif nb_reponses >= moyenne:
    print("pas mal")
else:
    print("peut mieux faire")
