def zapisz_zdania_do_pliku(nazwa_pliku, zdania):
    with open(nazwa_pliku, 'w', encoding='utf-8') as plik:
        for zdanie in zdania:
            plik.write(zdanie + '\n')
    print(f"Zdania zostały zapisane w pliku {nazwa_pliku}.")

def wczytaj_zdania(ile_zdan):
    zdania = []
    for i in range(ile_zdan):
        zdanie = input(f"Podaj zdanie {i+1}: ")
        zdania.append(zdanie)
    return zdania

def liczba_wystapien_slowa(zdanie, slowo):
    return zdanie.lower().split().count(slowo.lower())

def liczba_wystapien_znaku(zdanie, znak):
    return zdanie.lower().count(znak.lower())

def uszereguj_po_slowie(zdania, slowo, odwrotnie=False):
    return sorted(zdania, key=lambda x: liczba_wystapien_slowa(x, slowo), reverse=odwrotnie)

def uszereguj_po_znaku(zdania, znak, odwrotnie=False):
    return sorted(zdania, key=lambda x: liczba_wystapien_znaku(x, znak), reverse=odwrotnie)

# Część główna
def main():
    try:
        ile_zdan = int(input("Ile zdań chcesz dodać? "))
        if ile_zdan <= 0:
            print("Liczba zdań musi być dodatnia.")
            return

        zdania = wczytaj_zdania(ile_zdan)

        nazwa_pliku = 'zdania.txt'
        zapisz_zdania_do_pliku(nazwa_pliku, zdania)

        ile_zadan = int(input("Ile zadań chcesz wykonać? "))
        if ile_zadan <= 0:
            print("Liczba zadań musi być dodatnia.")
            return

        # Lista zadań
        zadania = [
            "1. Uszereguj zdania w kolejności od największej liczby wystąpień danego słowa",
            "2. Uszereguj zdania w kolejności od najmniejszej liczby wystąpień danego słowa",
            "3. Uszereguj zdania w kolejności od największej ilości danego znaku",
            "4. Uszereguj zdania w kolejności od najmniejszej ilości danego znaku"
        ]

        print("\nDostępne zadania:")
        for zadanie in zadania:
            print(zadanie)

        for i in range(ile_zadan):
            wybor_zadania = input(f"\nWybierz zadanie (wpisz numer od 1 do {len(zadania)}): ")
            
            if not wybor_zadania.isdigit():
                print("Niepoprawny wybór. Wpisz numer zadania.")
                continue

            wybor_zadania = int(wybor_zadania)

            if wybor_zadania == 1:
                slowo = input("Podaj słowo, według którego chcesz uszeregować zdania: ")
                posortowane_zdania = uszereguj_po_slowie(zdania, slowo, odwrotnie=True)
                print("\nZdania uszeregowane według liczby wystąpień słowa (malejąco):")
                for zdanie in posortowane_zdania:
                    print(zdanie)

            elif wybor_zadania == 2:
                slowo = input("Podaj słowo, według którego chcesz uszeregować zdania: ")
                posortowane_zdania = uszereguj_po_slowie(zdania, slowo, odwrotnie=False)
                print("\nZdania uszeregowane według liczby wystąpień słowa (rosnąco):")
                for zdanie in posortowane_zdania:
                    print(zdanie)

            elif wybor_zadania == 3:
                znak = input("Podaj znak, według którego chcesz uszeregować zdania: ")
                posortowane_zdania = uszereguj_po_znaku(zdania, znak, odwrotnie=True)
                print("\nZdania uszeregowane według liczby wystąpień znaku (malejąco):")
                for zdanie in posortowane_zdania:
                    print(zdanie)

            elif wybor_zadania == 4:
                znak = input("Podaj znak, według którego chcesz uszeregować zdania: ")
                posortowane_zdania = uszereguj_po_znaku(zdania, znak, odwrotnie=False)
                print("\nZdania uszeregowane według liczby wystąpień znaku (rosnąco):")
                for zdanie in posortowane_zdania:
                    print(zdanie)

            else:
                print("Niepoprawny wybór. Spróbuj ponownie.")

    except ValueError:
        print("Niepoprawne dane wejściowe. Proszę wprowadzić liczbę naturalną.")

# Uruchom program
if __name__ == '__main__':
    main()
