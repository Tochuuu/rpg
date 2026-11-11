
def pokaz_przedmioty(ekwipunek):
    print("\nTwoje przedmioty:")
    for przedmiot in ekwipunek:
        print(przedmiot, "-", ekwipunek[przedmiot])


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


def dodaj_przedmiot(ekwipunek):
    przedmiot = wybierz_przedmiot(
        "Jaki przedmiot chcesz dodać?: \n1 - Miecz\n2 - Mikstura\n3 - Złoto"
    )

    if przedmiot is None:
        return

    if przedmiot in ekwipunek:
        ekwipunek[przedmiot] += 1
    else:
        ekwipunek[przedmiot] = 1

    print("Dodano przedmiot!")


def uzyj_przedmiot(ekwipunek):
    przedmiot = wybierz_przedmiot(
        "Jaki przedmiot chcesz użyć?: \n1 - Miecz\n2 - Mikstura\n3 - Złoto"
    )

    if przedmiot is None:
        return

    if przedmiot in ekwipunek:
        ekwipunek[przedmiot] -= 1

        if ekwipunek[przedmiot] == 0:
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

    if przedmiot in ekwipunek:
        print(f"{przedmiot} - ilość: {ekwipunek[przedmiot]}")
    else:
        print(f"\nNie masz {przedmiot} w ekwipunku.")


def menu():
    ekwipunek = {
        "miecz": 1,
        "mikstura": 3,
        "zloto": 50
    }

    while True:
        print("\n1. Pokaż przedmioty")
        print("2. Dodaj przedmiot")
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
            dodaj_przedmiot(ekwipunek)

        elif wybor == 3:
            uzyj_przedmiot(ekwipunek)

        elif wybor == 4:
            sprawdz_przedmiot(ekwipunek)

        elif wybor == 5:
            print("\nWychodzenie z gry...\n")
            break


menu()
