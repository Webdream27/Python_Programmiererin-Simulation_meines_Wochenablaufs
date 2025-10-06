from time import sleep
import random

# Mein Wochen-Tagesablauf 
print("Mein Wochen-Tagesablauf \n============================")

# Aktivitäten 
def programmieren():
    print("Programmieren.")
    print("Ist Magie und schön inspirierend. \n")
    return True

def kaffee():
    print("Kaffee trinken.")
    print("Tut Herz und Gehirn gut. \n")
    return True

def essen(gericht):
    print(f"{gericht} essen. \n")
    return True

def naturpause():
    print("Pause in der Natur.")
    print("Fahrrad fahren, spazieren gehen.")
    print("Erholung für Körper und Seele. \n")
    return True

def schlafen():
    print("Schlafenszeit.")
    print("Regeneration beginnt. \n")
    sleep(1) # 8 Stunden Schlaf. (Simulation der Zeit mit 1 Sekunde Pause.)
    return True

def freizeit():
    ideen = [
        "Wandern gehen in den Alpen.",
        "Spazieren gehen im Park.",
        "Ein gutes Buch lesen.",
        "Ins Kino gehen.",
        "Musik hören.",
        "Gleitschirmfliegen."
    ]
    auswahl = random.choice(ideen)
    print(f"Freizeitaktivität: {auswahl} \n")
    return True

# Ablauf für 7 Tage
for tag in range(1, 8):
    print(f"\n==== Tag {tag} beginnt ====")
    
    if tag <= 5:
        print("Arbeitstag")
        if kaffee(): print("Kaffee erledigt. \n")
        if programmieren(): print("Programmieren erledigt. \n")
        if essen("Spaghetti Bolognese"): print("Essen erledigt. \n")
        if naturpause(): print("Pause erledigt. \n")
        if schlafen(): print("Schlaf erledigt. \n")
    else:
        print("Wochenende")
        if freizeit(): print("Freizeit erledigt. \n")
        if essen("Pizza"): print("Essen erledigt. \n")
        if schlafen(): print("Schlaf erledigt. \n")

print("\n ====Woche abgeschlossen!====")

