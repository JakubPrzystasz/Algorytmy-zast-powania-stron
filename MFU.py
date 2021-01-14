def znajdz_maximum_slownik(strony_odwolania, ramki, oprocz,x):  # oprocz - nie moze wybrac tej samej ramki bo sie zapętli
    dostepne_strony = []
    indeks = 0
    czy_kilka = 0 # czy powtarzają się maxima jeśli nie to zmienna oprócz musi wynosić -1 bo jej nie używamy

    for i in range(len(ramki)):  # przepisuje wszystkie strony jakie zawierają ramki
        dostepne_strony.append(ramki[i][x])  # indeksy dostepne_strony odpowiadają indeksom ramki

    max = strony_odwolania[dostepne_strony[0]]  # zakładamy że to jest najwieksza wartość

    for j in range(len(dostepne_strony)):  # znajduje wartość największa
        if (max <= strony_odwolania[dostepne_strony[j]]):
            max = strony_odwolania[dostepne_strony[j]]

    for j in range(len(dostepne_strony)):  # znajduje ile razy wystąpiła wartość największa
        if (max == strony_odwolania[dostepne_strony[j]]):
            czy_kilka += 1

    if(czy_kilka == 1 ): # bo jeżeli jest jedna wartość maximum no to musimy ją wziąść nie mamy wyboru
        oprocz = -1

    for k in range(len(dostepne_strony)):  # sprawdza 1 wystąpienie wartości maximum, omijając indeks oprócz
        if (strony_odwolania[dostepne_strony[k]] == max and k != oprocz):
            indeks = k
            break

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


def mfu(ilosc_ramek,liczba_odwolan,odwolania):
    # definiowanie rozmiarów list
    ramki = [[" " for x in range(liczba_odwolan)] for y in range(ilosc_ramek)]

    czas_bycia = [0 for x in range(ilosc_ramek)]  # ile dana strona jest w pamięcia

    # tablica 2D zawierający strony
    strony_odwolania = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0, 13: 0, 14: 0,
                        15: 0, 16: 0, 17: 0, 18: 0, 19: 0}

    # algorytm
    braki_stron = 0
    x = 0
    id_ramki = 0  # numer ramki
    # pom_id = 0
    oprocz = -1

    for znacznik in range(liczba_odwolan):  # zawsze na początku żadna ramka nie będzie zajęta

        if (id_ramki > ilosc_ramek - 1):  # przekroczono ilosc ramek
            id_ramki = 0

        if (ramki[id_ramki][znacznik] == " "):  # ramka nic nie ma w sobie, wypełniamy wszystkie ramki
            ramki[id_ramki][znacznik] = odwolania[znacznik]
            strony_odwolania[odwolania[znacznik]] += + 1
            wypelnij(ramki, ilosc_ramek, liczba_odwolan, x)

            ramki[id_ramki][znacznik] = str(
                odwolania[znacznik]) + "."  # żeby zaznaczyć że jest błąd strony, wywołuje 2 raz
            # bo funkcja wypełnij by skopiowała to zaznaczenie na inne warotści
            id_ramki += 1
            x = x + 1
            braki_stron = braki_stron + 1
            continue

        else:  # już po zainicjowaniu ramek
            # for i in range (ilosc_ramek): # iteruje po ramkach i sprawdza jakie zawierają strony
            # if( ramki[i][x] == odwolania[x] ): # ramka ma już tę stronę

            if (sprawdz_ramki(ramki, odwolania[x], x) == 1):  # ramka ma już tę stronę
                strony_odwolania[odwolania[znacznik]] += + 1
                # break
            else:  # ramka nie ma strony z odwolania
                id_ramki = znajdz_maximum_slownik(strony_odwolania, ramki, oprocz, x)

                ramki[id_ramki][znacznik] = odwolania[znacznik]
                wypelnij(ramki, ilosc_ramek, liczba_odwolan, x)
                strony_odwolania[odwolania[znacznik]] += + 1
                braki_stron = braki_stron + 1
                ramki[id_ramki][znacznik] = str(odwolania[znacznik]) + "."
                oprocz = id_ramki
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
# fifo(3,12,o)
#mfu(4, 12, o)
