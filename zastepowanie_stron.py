from FIFO import fifo
from AlgorytmOptymalny import algorytm_optymalny
from LRU import lru
from LFU import lfu
from MFU import mfu
# from AlgorytmDrugiejSzansy import algorytm_drugiej_szansy
from secondChance import algorytm_drugiej_szansy


def wyswietl_tabelke(tab):
    for element in tab:  # wypisanie elementów tablicy
        print(element, end=" | ")
    print()


def podanie_danych():
    print("Witaj w algorytmie zastępowania stron")

    # podanie danych przez użytkownika
    try:
        ilosc_ramek = int(input("Podaj liczbe dostępnych ramek:"))
    except ValueError:
        print("Podano niepoprawne dane")
        exit(-1)

    if(ilosc_ramek < 1):
        print("Podano niepoprawne dane")
        exit(-1)

    # wczytywanie danych podanych przez użytkownika
    print("Podaj wszystkie odwołania - wprowadz 0 aby zakończyć:")

    odwolania = []

    _input = 1
    cnt = 1
    while _input > 0:
        try:
            _input = int(input("Podaj odwolanie [" + str(cnt) + "]: "))
        except ValueError:
            print("Podano niepoprawne dane")
            exit(-1)

        if(_input < 0):
            print("Podano niepoprawne dane")
            exit(-1)
        if(_input > 0):
            odwolania.append(_input)
            cnt += 1

    # to zobaczy użytkownik żeby sprawdzić czy dobrze dane wprowadził
    print()
    print("Wprowadzone dane:")
    print()
    wyswietl_tabelke(odwolania)
    liczba_odwolan = len(odwolania)
    return ilosc_ramek, liczba_odwolan, odwolania


# wybór użytkownika i wywołanie danego algorytmu

ilosc_ramek, liczba_odwolan, odwolania = podanie_danych()
wybor = 0
ilosc_brakow_stron = 0

while(wybor != 8):
    print()
    print()
    print("Założenia:")
    print("----------")
    print()
    print("Jak mamy do wyboru usuniecie strony z danej ramki")
    print("I mamy sytuację że każda ramka nadaje sie do usunięcia z niej storny")
    print()
    print("TO:")
    print("---------------------------------------------------------------------------")
    print("  - Wybieramy ramkę z najmniejszym indeksem!")
    print("    ( np. z ramek 1,2,3,4 bierzemy ramkę 1 )")
    print("")
    print("  - Dodatkowo jeśli mamy tą samą sytuację ale ramka 1 już wcześniej była użyta to wybierze ramkę 2")
    print("---------------------------------------------------------------------------")

    print()
    print("Wybierz jaki algorytm chcesz użyć:")
    print("1.FIFO")
    print("2.Algorytm optymalny")
    print("3.LRU ( Least Recently Used )")
    print("4.LFU ( Least Frequently Used )")
    print("5.MFU ( Most Frequently Used )")
    print("6.Algorytm drugiej szansy")
    print("7.Chcę zmienić dane ( ponieważ mam inne odwołania, lub inne dane )")
    print("8.Koniec")

    pom_odwolania = odwolania.copy()

    try:
        wybor = int(input(">>>>:"))
    except:
        print("Nie podałeś inta")

    print()

    if(wybor == 1):
        print("FIFO:")
        fifo(ilosc_ramek, liczba_odwolan, pom_odwolania)

    if(wybor == 2):
        print("Algorytm optymalny:")
        algorytm_optymalny(ilosc_ramek, liczba_odwolan, pom_odwolania)

    if(wybor == 3):
        print("LRU ( Least Recently Used ):")
        lru(ilosc_ramek, liczba_odwolan, pom_odwolania)

    if(wybor == 4):
        print("LFU ( Least Frequently Used ):")
        lfu(ilosc_ramek, liczba_odwolan, pom_odwolania)

    if(wybor == 5):
        print("MFU ( Most Frequently Used ):")
        mfu(ilosc_ramek, liczba_odwolan, pom_odwolania)

    if(wybor == 6):
        print("Algorytm drugiej szansy:")
        algorytm_drugiej_szansy(ilosc_ramek, liczba_odwolan, pom_odwolania)

    if(wybor == 7):
        ilosc_ramek, liczba_odwolan, odwolania = podanie_danych()
