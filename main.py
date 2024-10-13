
def wczytaj_dokumenty(ile_dokumentow):
    dokumenty = []
    for i in range(ile_dokumentow):
        dokument = input(f"Podaj dokument {i + 1}: ")
        dokumenty.append(dokument)
    return dokumenty

def wczytaj_zapytania(ile_zapytan):
    zapytania = []
    for i in range(ile_zapytan):
        zapytanie = input(f"Podaj zapytanie {i + 1}: ")
        zapytania.append(zapytanie)
    return zapytania

def liczba_wystapien_slowa(dokument, slowo):
    return dokument.lower().split().count(slowo.lower())

def przetwarzaj_zapytania(dokumenty, zapytania):
    wyniki = []
    
    for zapytanie in zapytania:
        lista_wynikow = []

        for i, dokument in enumerate(dokumenty):
            liczba_wystapien = liczba_wystapien_slowa(dokument, zapytanie)

            if liczba_wystapien > 0:
                lista_wynikow.append((i + 1, liczba_wystapien))  

        lista_wynikow.sort(key=lambda x: (-x[1], x[0]))

        wyniki.append([doc[0] for doc in lista_wynikow])

    return wyniki

# Część Główna
def main():
    ile_dokumentow = int(input("Ile dokumentów chcesz dodać? "))

    dokumenty = wczytaj_dokumenty(ile_dokumentow)

    ile_zapytan = int(input("Ile zapytań chcesz przetworzyć? "))

    zapytania = wczytaj_zapytania(ile_zapytan)

    wyniki = przetwarzaj_zapytania(dokumenty, zapytania)

    for wynik in wyniki:
        print(" ".join(map(str, wynik)) if wynik else "Brak wyników")

# Uruchom program
if __name__ == '__main__':
    main()
