


#trier de plus petit vars le plus grand 
def word_in_increasing(words):
    # mettre dans un tableau
    liste=words.split()
    ##trier pardre alpha
    liste.sort()
    #trier en function de la lengueur
    result = sorted(liste, key = len)
    return result
    


#trier le mot le plus petit et le plus grand 
def word_max_min(words):
    # mettre dans un tableau
    liste=words.split()
    liste.sort()
    #trier
    max_word=(max(liste, key=len)) 
    min_word=(min(liste, key=len))
    return max_word,min_word
   
#trier le plus petit ou grand par ordre alpha et les prendres tous 
def word_max_min_sorted(sentence):
    words=sentence.split()
    max_word,min_word=word_max_min(sentence)
    all_min_word=[word for word in words if len(word)==len(min_word)]   
    all_max_word=[word for word in words if len(word)==len(max_word)]
    all_min_word.sort()
    all_max_word.sort()    
    return all_min_word, all_max_word

   
      
n=" samira moi yesj  aa ff gggggg  "
max_word,min_word=word_max_min(n)
max_word,min_word=word_max_min_sorted(n)
min_word_to_max_word=word_in_increasing(n)

print(f' la liste de plsu petit vers le plus grand {min_word_to_max_word}')

print(f'le mot le plus petit est : {min_word}')
print(f'le mot le plus grand est : {max_word}')
