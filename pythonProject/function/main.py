#table de multiplication
val_min=0
val_max=11
def afficher_resultat_multiplication(n):
    for i in range(val_min,val_max):
        print (i,"*",n, "=" ,i*n)

afficher_resultat_multiplication(4)
print()
afficher_resultat_multiplication(5)


