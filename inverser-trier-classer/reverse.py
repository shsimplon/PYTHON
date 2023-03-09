

mot="samira bonjour"

def inverser(chaine):
    n="".join(reversed(chaine))
    return n

n=inverser(mot)
print (n)

print(mot[::-1])

def reverse_string1(str):
    r = ""
    for c in str:
        r = c + r
        #r=B+""
        #r=o+B=oB
        #r=n+oB=noB
#r=j+noB
#jnoB

#ruojnoB
#
    return r

def reverse_string2(str):
    return s[::-1]


s = "Bonjour toto"
print(reverse_string1(s))

print(reverse_string2(s))