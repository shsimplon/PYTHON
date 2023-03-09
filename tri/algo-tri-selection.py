
def selection(liste):
    min_num= 0
    
    for numbre in range (0, len(liste)):
        if numbre < liste[min_num]:
            numbre= min_num
        return numbre
        
liste=[3,19,8,2]

resullt=selection(liste)
print(resullt)