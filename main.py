import re

def podaj_dokumenty_i_pytania():
    dok = int(input("Podaj liczbę dokumentów: "))
    dokumenty = [input(f"Dokument {i + 1}: ") for i in range(dok)]

    pyt = int(input("Podaj liczbę pytań: "))
    pytania = [input(f"Pytanie {j + 1}: ").strip().lower() for j in range(pyt)]

    return dokumenty, pytania

def licz(slowo, dokument):
    slowa = re.findall(r'\b\w+\b', dokument.lower())
    return slowa.count(slowo.lower())

def spr(dokumenty, pytania):
    wyniki = []

    for pytanie in pytania:
        wystapienia = [(indeks, licz(pytanie, dokument)) for indeks, dokument in enumerate(dokumenty)]

        filtr = [element for element in wystapienia if element[1] > 0]

        posortowane = sorted(filtr, key=lambda x: (-x[1], x[0]))

        indeksy = [indeks for indeks, _ in posortowane]

        wyniki.append(indeksy)

    return wyniki

def main():
    dokumenty, pytania = podaj_dokumenty_i_pytania()
    wyniki = spr(dokumenty, pytania)

    print("\nWyniki dla zapytań:")
    for wynik in wyniki:
        if wynik:
            print(f"[{', '.join(map(str, wynik))}]")
        else:
            print("Brak wyników")

if __name__ == '__main__':
    main()
