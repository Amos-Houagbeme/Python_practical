# Simulateur de Vote Électronique

print("Bienvenu au centre de vote! ")
id_vote = set()
cont_candidat = {}

while True:
    identifiant = input("Entrez votre identifiant ou 'fin' pour arreter: ").lower()
    if identifiant == "fin":
        break
    else:
        identifiant = int(identifiant)
        if identifiant not in id_vote:
            id_vote.add(identifiant)
            
            candidat = input("Nom du candidat : ").strip().capitalize()
            if candidat not in cont_candidat:
                cont_candidat[candidat] = 1
            else:
                cont_candidat[candidat] += 1
        else:
            print("Déjà voté !")

if cont_candidat:
    gagnant = max(cont_candidat, key=cont_candidat.get)
    print(f"{gagnant} gagne avec {cont_candidat[gagnant]} voix.")
else:
    print("Aucun vote pour le moment! ")
print(cont_candidat)