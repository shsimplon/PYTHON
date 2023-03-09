#les fonctions: poser votre question
import random
def poser_question(pays="",r1="",r2="",r3="",choix_de_reponse=""):
    global score
    print(f"quel est la capitale du {pays} : ")
    print(f"{r1}")
    print(f"{r2}")
    print(f"{r3}")
    reponse = input("votre reponse est : ")
    if reponse == choix_de_reponse:
        print("resultat correct !")
        score+=1
    else:
        print("mauvaise reponse")
    print()
score=0
poser_question("france", "paris", "nice","limoge", "paris")

poser_question("italie", "rome", "madrid","venise", "rome")

print (f"votre score est de {score}")






