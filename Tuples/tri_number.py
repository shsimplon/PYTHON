nom_chauffeur =       ["Patrick", "Paul", "Marc", "Jean", "Pierre", "Marie", "Maxime"]

distance_chauffeur_km = [1.5,    2.2,   0.7,        0.9,   7.1,     1.1,     0.6]
#afficher le trjet le chauffeur le plus proche 
#admittant que la distance la plus proche est le premier element du tableau 
distance_min=distance_chauffeur_km[0]
for distance in distance_chauffeur_km:
    if distance < distance_min:   
       distance_min=distance
       index_distance = distance_chauffeur_km.index(distance_min) 
       index_chauffeur=nom_chauffeur[index_distance]  
      

       
print("distance la plus proche est de : ",   distance_min ,"km qui corresond au chauffeur " ,index_chauffeur  )  # type: ignore