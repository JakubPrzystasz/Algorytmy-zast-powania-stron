def wybierz_odpowiednia_ramke(odwolania, ramki, oprocz,x):  # oprocz - nie moze wybrac tej samej ramki bo sie zapętli
    dostepne_strony = []

    for i in range(len(ramki)):  # przepisuje wszystkie strony jakie zawierają ramki
        dostepne_strony.append(ramki[i][x])  # indeksy dostepne_strony odpowiadają indeksom ramki

    najdalsza = 0 # zmienna pomocnicza zawirajaca index najdalszego odwołania
    id_ramki = 0 # jaka ramka ma byc wybrana
    indeks = 0 # przechowuje aktualny indeks

    for i in range(len(ramki)):
        if( not(dostepne_strony[i] in odwolania[x:]) ): # jeśli już nie ma tej strony w odwołaniach
            id_ramki = i # no to zastępujemy stronę z tej ramki
            return  id_ramki


        indeks = odwolania[x:].index(dostepne_strony[i]) # znajduje pierwsze wystąpienie strony w odwolaniach
        if( indeks > najdalsza ): # jeśli indeks strony którą przechowuje ramka jest większy niż indeks strony poprzedniej ramki
            id_ramki = i # wybieramy tę ramkę
            najdalsza = indeks # ten indeks jest najdalszy



    return id_ramki


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

#o = [1,2,3,4,1,2,5,1,2,3,4,5]
#algorytm_optymalny(4, 12, o)

#o = [5,4,3,2,5,4,1,3,2,4,5,4,2,5,1]
#algorytm_optymalny(3, 15, o)