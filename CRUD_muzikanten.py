import gegevens_muzikanten

muz = gegevens_muzikanten.muzikanten


def display_menu():
    title = "Onze muzikanten".upper()
    print(title)
    print(len(title) * "=", "\n")
    print("Opties:")
    print("1       => toon alle muzikanten en de instrumenten die ze bespelen")
    print("2       => toon alle muzikanten die een door jou gekozen instrument bespelen")
    print("3       => voeg een instrument toe aan een muzikant die reeds in de lijst staat")
    print("4       => voeg een muzikant toe, met minstens 1 instrument")
    print("stop    => verlaat de applicatie")
    print()
    print("Kies een commando door het overeenkomstige getal " +
          "\nin te voeren. Om de applicatie te verlaten " +
          "\ntyp je \"stop\".")
    print()


def toon_muzikanten(lijst):
    print("Onze muzikanten en de instrumenten die ze bespelen:\n")
    # werkt maar is omslachtig
    # for item in lijst:
    #     for v in item.values():
    #         if not type(v) == list:
    #             print(v + ":", end=" ")
    #         else:
    #             print(" | ".join(v))

    if len(lijst) >= 1:
        for item in lijst:
            print("\t" + item["naam"] + ": " + " | ".join(item["instrumenten"]))
    else:
        print("Deze lijst is leeg.")
    print()
    
    
def toon_instrumentbespelers(lijst):
    while True:
        gekozen_instrument = input("Typ het instrument in waarvan je alle bespelers wil zien: ")
        gekozen_instrument = gekozen_instrument.lower()
        bespelers = []
        for item in lijst:
            if gekozen_instrument in item["instrumenten"]:
                bespelers.append(item["naam"])
        if len(bespelers) == 0:
            print("We hebben geen muzikant die dit instrument bespeelt, voer een ander instrument in.")
            print()
            continue
        if len(bespelers) == 1:
            print(f"Je koos voor het instrument {gekozen_instrument}." +
                   "\nAlleen " + bespelers[0] + " bespeelt dit instrument.")
            break
        elif len(bespelers) > 1:
            print("Volgende muzikanten bespelen dit instrument: " + " | ".join(bespelers))
            break
    print()


def add_instrument(lijst):
    while True:
        muzikant = input("Voor welke muzikant wil je een instrument toevoegen?: ")
        muzikant = muzikant.title()
        namen = []
        for item in lijst:
            if item["naam"] == muzikant:
                namen.append(item["naam"])
        if len(namen) == 0:
            print("Deze naam komt niet voor in de lijst. Voer een andere naam in!")
            print()
            continue
        elif len(namen) == 1:
            while True:
                instrument = input("Voeg voor " + muzikant + " dit instrument toe: ")
                instrument = instrument.lower()
                while_lus_verlaten = ""
                for item in lijst:
                    if item["naam"] == muzikant and instrument not in item["instrumenten"]:
                        item["instrumenten"].append(instrument)
                        print(f"Het instrument {instrument} werd toegevoegd aan muzikant {muzikant}.")
                        while_lus_verlaten = True
                        break
                    elif item["naam"] == muzikant and instrument in item["instrumenten"]:
                        print("Dit instrument werd reeds eerder toegevoegd voor deze muzikant." +
                              "\nTyp een ander instrument in!")
                        while_lus_verlaten = False 
                        break
                if while_lus_verlaten is True:
                    print()
                    break
                elif while_lus_verlaten is False:
                    print()
                    continue
        break


def add_musician(lijst):
    while True:
        name_musician = input("Naam die je wil toevoegen: ")
        name_musician = name_musician.title()
        namen = []
        for item in lijst:
            namen.append(item["naam"])
        if name_musician in namen:
            print("Deze naam staat reeds in de lijst.")
            print()
            continue
        else:
            lijst.append({"naam": name_musician, "instrumenten": []})
            print(f"Naam {name_musician} werd toegevoegd aan de lijst.")
            for item in lijst:
                print(item["naam"])
            choice = "j"
            while choice.lower() == "j":
                instrument = input("Voeg dit instrument toe aan de nieuwe muzikant: ")
                instrument = instrument.lower()
                for item in lijst:
                    if item["naam"] == name_musician and instrument in item["instrumenten"]:
                        print("Dit instrument werd reeds toegevoegd voor deze muzikant. Probeer het eventueel opnieuw!")
                        break
                    elif item["naam"] == name_musician and instrument not in item["instrumenten"]:
                        item["instrumenten"].append(instrument)
                        print(f"Instrument {instrument} werd toegevoegd voor muzikant {name_musician}.") 
                        break
                print()
                choice = input("Wil je nog een instrument toevoegen? Typ \"j\" indien ja!!: ")
            break
    print()


def del_musician(lijst):
    while True:
        te_verwijderen_naam = input("Typ de naam van de muzikant die je uit de lijst wil verwijderen: ")
        te_verwijderen_naam = te_verwijderen_naam.title()
        namen = []
        for item in lijst:
            namen.append(item["naam"])
        if te_verwijderen_naam not in namen:
            print("Deze naam staat niet in de lijst, probeer het opnieuw!")   
            print()
            continue
        for item in lijst:
            if te_verwijderen_naam == item["naam"]:
                lijst.pop(lijst.index(item))
                print(f"Muzikant {te_verwijderen_naam} werd uit de lijst verwijderd.")
                print(lijst)
                print()
                break
        break
                
        
def main():
    display_menu()
    while True:
        commando = input("Mijn commando: ")
        commando = commando.upper()
        if commando == "1":
            toon_muzikanten(muz)
        elif commando == "2":
            toon_instrumentbespelers(muz)
        elif commando == "3":
            add_instrument(muz)
        elif commando == "4":
            add_musician(muz)
        elif commando == "5":
            del_musician(muz)
        elif commando == "STOP":
            break
        else:
            print("Dit is geen geldig commando. Probeer het aub opnieuw.\n")
    print("\nBedankt en tot ziens!")


if __name__ == "__main__":
    main()
