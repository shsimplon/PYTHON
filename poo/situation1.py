# POO EXERCICE DE MISE EN SITUATION 1
# genre
#   False : Femme
#   True  : Homme
class Personne:
    def __init__(self, nom: str, age: int, genre: bool):
        self.nom = nom   # crée une variable d'instance : nom
        self.age = age
        self.genre = genre

    def SePresenter(self):
        # Bonjour, je m'appelle Jean, j'ai 30 ans
        # Je suis majeur

        genre_str="masculin" if self.genre else "feminin"   
        print(f"Genre : {genre_str}")
        print("Bonjour, je m'appelle " + self.nom + ", j'ai " + str(self.age) + " ans")
            
        eOpetionnel="" if self.genre else "e"      
        if self.EstMajeur():
            print(f"Je suis majeur{eOpetionnel}")
        else:
            print(f"Je suis mineur{eOpetionnel}")
        print()
            

    def EstMajeur(self):
        return self.age >= 18
   

personne1 = Personne("Jean", 25,True)
personne2 = Personne("Emilie", 17,False)
personne1.SePresenter()


personne2.SePresenter()
