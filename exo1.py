# Programmer le système de filtrage à l'entrée d'un club

print("Bienvenue au club !")
age = int(input("Quel est votre âge ? ")) 
membre = input("Êtes-vous membre du club ? (oui/non) ")
membre = membre.lower()

if age < 18:
    print("Accès refusé.")
elif age >= 18 and age < 21 and membre == "non":
    print("Accès autorisé, bracelet rouge.")
elif age >= 21 or (membre == "oui" and age >= 18):
    print("Accès autorisé, bracelet vert.")