# Le Calculateur d'Itinéraire

liste_distance =  [150, 230, 310, 80]

distance_total = sum(liste_distance)

nombre_litre = (distance_total * 8)/100
prix_consommation = round(nombre_litre * 1.90, 2)
pause = distance_total // 400

print(f"Distance total : {distance_total} Km") 
print(f"Budget carburant : {prix_consommation} €")
print(f"Pauses : {pause} (atteinte à 400km )")