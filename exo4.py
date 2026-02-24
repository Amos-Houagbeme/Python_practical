#  Analyseur de Logs de Sécurité 

liste_logs = ["user:admin:fail", "user:admin:fail", "user:lucas:success", "user:admin:fail", "user:admin:fail", "user:lucas:fail"] 
stats = {}
blacklist = []

for log in liste_logs:
    element = log.split(":")
    user = element[1]
    status = element[2]

    if user not in stats:
        stats[user] = 0
    
    if status == "fail":
        stats[user] += 1
    
    if stats[user] >= 3:
        blacklist.append(user)
blacklist = set(blacklist)
print(f"Stats: {stats}")
print(f"Blacklist: {blacklist}")