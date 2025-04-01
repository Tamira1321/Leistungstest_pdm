def get_user_data():
    name = input("Wie heißt du? ")
    alter = int(input("Wie alt bist du? "))
    
    zeiten = []
    print("Gib deine 3 Sprintzeiten ein:")
    for i in range(3):
        zeit = float(input(f"Zeit {i+1}: "))
        zeiten.append(zeit)

    return name, alter, zeiten

def auswerten(zeiten):
    durchschnitt = sum(zeiten) / len(zeiten)
    beste_zeit = min(zeiten)

    if beste_zeit < 7.3:
        niveau = "Sehr gut"
    elif beste_zeit < 7.6:
        niveau = "Gut"
    else:
        niveau = "Ausbaufähig"

    return durchschnitt, beste_zeit, niveau

if __name__ == "__main__":
    name, alter, zeiten = get_user_data()
    durchschnitt, beste_zeit, niveau = auswerten(zeiten)

    print("\n--- Auswertung ---")
    print(f"Athletin: {name} ({alter} Jahre)")
    print(f"Durchschnittszeit: {durchschnitt:.2f} Sekunden")
    print(f"Beste Zeit: {beste_zeit:.2f} Sekunden")
    print(f"Leistungsniveau: {niveau}")