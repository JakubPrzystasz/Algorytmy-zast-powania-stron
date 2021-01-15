def wybierz_odpowiednia_ramke(odwolania, ramki, oprocz,x):  # oprocz - nie moze wybrac tej samej ramki bo sie zapętli
    dostepne_strony = []
    indeks = 0
    pom_j = 0 # tu będzie trzymane najdalsze odwołanie
    czy_kilka = 0 # czy powtarzają się maxima jeśli nie to zmienna oprócz musi wynosić -1 bo jej nie używamy
    czy_znalaziono = 1 # jeśli strona występująca w ramce nie wystąpi w dalszych odwołaniach to usuwamy stronę z ramki

    for i in range(len(ramki)):  # przepisuje wszystkie strony jakie zawierają ramki
        dostepne_strony.append(ramki[i][x])  # indeksy dostepne_strony odpowiadają indeksom ramki

    #for i in range(len(ramki)): # jeśli strona występująca w ramce nie wystąpi to usuwamy stronę z ramki
     #   pass

    for i in range(len(ramki)): # iteruje po naszych ramkach
        czy_znalaziono = 0 # zakładamy że nie znaleziono
        for j in range(len(odwolania)-1, x, -1):  # iteruje od ostatniej wartości w tablicy odwołania do x-owej
                                                # dzięki temu określi, do której strony z listy dostępne_strony nastąpi najpóźniej odwołąnie

            if (odwolania[j] == dostepne_strony[i]): # znalazło najdalsze odwołanie w odwołaniach, które wystąpiło w ramce
                czy_znalaziono = 1
                if( j > pom_j ): # and i != oprocz ): # znaleziono jeszcze dalsze odwołanie
                    pom_j = j # to jest nowe najdalsze odwołanie
                    indeks = i  # ma wtedy zastąpić tę stronę w ramce | wykona sie to wiele razy aż znajdzie najdalsze odwołanie
        if( czy_znalaziono == 0 ): # nie ma w odwołaniach tej strony więc usuwamy ją z ramki
            indeks = i
            return  indeks

    return indeks


def sprawdz_ramki(ramki, wartosc, x):
    for y in range(len(ramki)):
        if (ramki[y][x] == wartosc):
            return 1
    return 0


def wyswietl_tabelke(tab):
    for element in tab:  # wypisanie elementów tablicy

        if (len(str(element)) == 2):  # do oznaczania miejsc braków storn
            print(element, end="| ")
            continue

        print(element, end=" | ")

    print()


def wypelnij(tab, il_ramek, il_odwolan, i):  # wypełnia cała prawą stronę ramek od i ich liczbami wskazanymi przez i
    for y in range(il_ramek):  # dana ramka
        liczba = tab[y][i]  # liczba którą wypełni
        for x in range(i, il_odwolan):  # dane odwolanie w ramce
            tab[y][x] = liczba




def algorytm_optymalny(ilosc_ramek,liczba_odwolan,odwolania):
    # definiowanie rozmiarów list
    ramki = [[" " for x in range(liczba_odwolan)] for y in range(ilosc_ramek)]

    # algorytm
    braki_stron = 0
    x = 0
    id_ramki = 0  # numer ramki
    oprocz = -1

    for znacznik in range(liczba_odwolan):  # zawsze na początku żadna ramka nie będzie zajęta

        if (id_ramki > ilosc_ramek - 1):  # przekroczono ilosc ramek
            id_ramki = 0


        if (ramki[id_ramki][znacznik] == " "):  # ramka nic nie ma w sobie, wypełniamy wszystkie ramki
            ramki[id_ramki][znacznik] = odwolania[znacznik]
            # strony_odwolania[odwolania[znacznik]] += + 1
            wypelnij(ramki, ilosc_ramek, liczba_odwolan, x)
            ramki[id_ramki][znacznik] = str(odwolania[znacznik]) + "."  # żeby zaznaczyć że jest błąd strony, wywołuje 2 raz
            # bo funkcja wypełnij by skopiowała to zaznaczenie na inne warotści
            id_ramki += 1
            x = x + 1
            braki_stron = braki_stron + 1
            continue

        else:  # już po zainicjowaniu ramek

            if (sprawdz_ramki(ramki, odwolania[x], x) == 1):  # ramka ma już tę stronę
                pass
                # jest odwołanie do strony więc ją odmładzamy
                #strony_odwolania[odwolania[znacznik]] = 0
                # break
            else:  # ramka nie ma strony z odwolania
                id_ramki = wybierz_odpowiednia_ramke(odwolania, ramki, oprocz,x)

                ramki[id_ramki][znacznik] = odwolania[znacznik]
                wypelnij(ramki, ilosc_ramek, liczba_odwolan, x)


                braki_stron = braki_stron + 1

                ramki[id_ramki][znacznik] = str(odwolania[znacznik]) + "."

                #oprocz = id_ramki chyba nie musi być
                # break

        x += 1

    # wypisanie danych

    print("Kropka wskazuje miejsce wystąpienia błedy braku strony")
    print()

    print("Odwołania:")
    wyswietl_tabelke(odwolania)
    print()
    for y in range(ilosc_ramek):
        print("Ramka " + str(y + 1) + ":")
        wyswietl_tabelke(ramki[y])

    print()

    print("Braki stron:")
    print(braki_stron)

o = [1,2,3,4,1,2,5,1,2,3,4,5]
# fifo(3,12,o)
algorytm_optymalny(4, 12, o)
