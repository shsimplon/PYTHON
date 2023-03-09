# FICHIERS TEXTE : EXERCICE
# "Ecrire des nombres"

# nombres.txt
# 1
# 2
# 3
# for
# 10 lignes

# f = open("nombre.txt", "w")

# for i in range(0,12):
#     # print(i+1)
#     f.write(str(i)+"\n")

# f.close()
try:
    f = open("nombre.txt", "r")
    
except FileNotFoundError:
    print('pas ouvert')
else:
    tesxt= f.read()
    print (tesxt)
    f.close()
    