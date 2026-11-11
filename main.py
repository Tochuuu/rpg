def menu():
    ekwipunek = {
    "miecz": 1,
    "mikstura": 3,
    "zloto": 50
    }
    while True:
        print ("\n1. Pokaż przedmioty")
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
            print ("\nBŁĄD")
            continue
            
        if wybor == 1:
            print ("\nTwoje przedmioty:")
            for przedmiot in ekwipunek:
                print (przedmiot, "-", ekwipunek[przedmiot])
        elif wybor == 2:
            print("Jaki przedmiot chcesz dodać?: \n1 - Miecz\n2 - Mikstura\n3 - Złoto")
            dodaj = input(f"\nDodaj przedmiot: ")
            if dodaj == "1":
                przedmiot = "miecz"
            elif dodaj == "2":
                przedmiot = "mikstura"
            elif dodaj == "3":
                przedmiot = "zloto"
            else:
                print("Nie ma takiej opcji!")
                continue

            if przedmiot in ekwipunek:
                ekwipunek[przedmiot] += 1
            else:
                ekwipunek[przedmiot] = 1

        elif wybor == 3:
            print("Jaki przedmiot chcesz użyć?:  \n1 - Miecz\n2 - Mikstura\n3 - Złoto")
            uzyj = input("\nUżyj przedmiotu: ")
            if uzyj == "1":
                przedmiot = "miecz"
            elif uzyj == "2":
                przedmiot = "mikstura"
            elif uzyj == "3":
                przedmiot = "zloto"
            else:
                print("Nie ma takiej opcji!")
                continue
            if przedmiot in ekwipunek:
                ekwipunek[przedmiot] -= 1

                if ekwipunek[przedmiot] == 0:
                    del ekwipunek[przedmiot]

                print("Użyto przedmiotu!")
            else:
                print("Nie masz takiego przedmiotu!")

        elif wybor == 4:
            print("Jaki przedmiot chcesz sprawdzić?: \n1 - Miecz\n2 - Mikstura\n3 - Złoto")
            sprawdz = input(f"\nSprawdź przedmiot: ")
            if sprawdz == "1":
                przedmiot = "miecz"
            elif sprawdz == "2":
                przedmiot = "mikstura"
            elif sprawdz == "3":
                przedmiot = "zloto"
            else:
                print("Nie ma takiej opcji!")
                continue

            if przedmiot in ekwipunek:
                print(f"{przedmiot} - ilość: {ekwipunek[przedmiot]}")
            else:
                print(f"\nNie masz {przedmiot} w ekwipunku.")
        elif wybor == 5:
            print ("\nWychodzenie z gry...\n")
            break
        else:
            print ("Nie ma takiej opcji!\nWybierz 1-5")

menu()