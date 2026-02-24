# Transformer une liste d'utilisateurs mal saisie en liste propre.

liste_depart = ["alice", "BOB", "charlie", "ALICE", "Eve", "DAN"]
utilisateurs_propre = []
element_arret= "eve"

for element in liste_depart:
    element = element.strip().lower()
    if element != element_arret:
        if element not in utilisateurs_propre: 
            utilisateurs_propre.append(element)
    else:
        break
print(utilisateurs_propre)