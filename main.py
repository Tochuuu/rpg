
def pokaz_przedmioty(ekwipunek):
    print("\nTwoje przedmioty:")
    for przedmiot in ekwipunek:
        if przedmiot == "zloto":
            print("Złoto -", ekwipunek[przedmiot])
        else:
            dane = ekwipunek[przedmiot]
            print(przedmiot, "-", dane["ilosc"])

def wybierz_przedmiot(komunikat):
    print(komunikat)
    wybor = input("\nWybierz przedmiot: ")

    if wybor == "1":
        return "miecz"
    elif wybor == "2":
        return "mikstura"
    elif wybor == "3":
        return "zloto"
    else:
        print("Nie ma takiej opcji!")
        return None


def kup_przedmiot(ekwipunek, przedmiot, cena):
    if ekwipunek.get("zloto", 0) >= cena:
        ekwipunek["zloto"] -= cena

        if ekwipunek["zloto"] == 0:
            del ekwipunek["zloto"]

        if przedmiot in ekwipunek:
            ekwipunek[przedmiot] += 1
        else:
            ekwipunek[przedmiot] = {
                "ilosc": 1,
                "waga": waga,
                "wartosc": cena
            }

        print("Zakupiono przedmiot!")
    else:
        print("Nie masz wystarczającej ilości złota!")

def sprzedaj_przedmiot(ekwipunek):
    print("\nCo chcesz sprzedać?")
    print("1 - Miecz (10 złota)")
    print("2 - Mikstura (2 złota)")
    print("3 - Powrót")

    wybor = input("\nWybierz przedmiot: ")

    if wybor == "1":
        przedmiot = "miecz"
        cena = 10
    elif wybor == "2":
        przedmiot = "mikstura"
        cena = 2
    elif wybor == "3":
        return
    else:
        print("Nie ma takiej opcji!")
        return

    if przedmiot in ekwipunek:
        ekwipunek[przedmiot]["ilosc"] -= 1
        ekwipunek["zloto"] = ekwipunek.get("zloto", 0) + cena

        if ekwipunek[przedmiot]["ilosc"] <= 0:
            del ekwipunek[przedmiot]

        print("Sprzedano przedmiot!")
        print("Otrzymano", cena, "złota!")
    else:
        print("Nie masz takiego przedmiotu!")
    
def sklep(ekwipunek):
    print("\nSklep 'Szop'")
    print("1. Kup przedmiot")
    print("2. Sprzedaj przedmiot")
    print("3. Wyjdź ze sklepu")

    wybor = input("\nWybierz opcję: ")

    if wybor == "1":
        print("\nCo chcesz kupić?")
        print("1 - Miecz (20 złota)")
        print("2 - Mikstura (5 złota)")

        zakup = input("\nWybierz przedmiot: ")

        if zakup == "1":
            kup_przedmiot(ekwipunek, "miecz", 20, 7)
        elif zakup == "2":
            kup_przedmiot(ekwipunek, "mikstura", 5, 2)
        else:
            print("Nie ma takiej opcji!")

    elif wybor == "2":
        sprzedaj_przedmiot(ekwipunek)

    elif wybor == "3":
        print("Wychodzisz ze sklepu...")

    else:
        print("Nie ma takiej opcji!")


def uzyj_przedmiot(ekwipunek):
    przedmiot = wybierz_przedmiot(
        "Jaki przedmiot chcesz użyć?: \n1 - Miecz\n2 - Mikstura\n3 - Złoto"
    )

    if przedmiot is None:
        return

    if przedmiot == "zloto":
        print("Nie możesz użyć złota!")
        return

    if przedmiot in ekwipunek:
        ekwipunek[przedmiot]["ilosc"] -= 1

        if ekwipunek[przedmiot]["ilosc"] == 0:
            del ekwipunek[przedmiot]

        print("Użyto przedmiotu!")
    else:
        print("Nie masz takiego przedmiotu!")


def sprawdz_przedmiot(ekwipunek):
    przedmiot = wybierz_przedmiot(
        "Jaki przedmiot chcesz sprawdzić?: \n1 - Miecz\n2 - Mikstura\n3 - Złoto"
    )

    if przedmiot is None:
        return

    if przedmiot == "zloto":
        print(f"Złoto - ilość: {ekwipunek.get('zloto', 0)}")
    elif przedmiot in ekwipunek:
        print(f"{przedmiot} - ilość: {ekwipunek[przedmiot]['ilosc']}")
    else:
        print(f"\nNie masz {przedmiot} w ekwipunku.")


def menu():
    ekwipunek = {
    "miecz": {
        "ilosc": 1,
        "waga": 7,
        "wartosc": 20
    },
    "mikstura": {
        "ilosc": 3,
        "waga": 2,
        "wartosc": 5
    },
    "zloto": 50
    }

    while True:
        print("\n1. Pokaż przedmioty")
        print("2. Idź do sklepu")
        print("3. Użyj przedmiotu")
        print("4. Sprawdź przedmiot")
        print("5. Wyjdź")

        try:
            wybor = int(input("\n"))

            if wybor > 5 or wybor < 1:
                print("\nBŁĄD")
                continue

        except ValueError:
            print("\nBŁĄD")
            continue

        if wybor == 1:
            pokaz_przedmioty(ekwipunek)

        elif wybor == 2:
            sklep(ekwipunek)

        elif wybor == 3:
            uzyj_przedmiot(ekwipunek)

        elif wybor == 4:
            sprawdz_przedmiot(ekwipunek)

        elif wybor == 5:
            print("\nWychodzenie z gry...\n")
            break


menu()
