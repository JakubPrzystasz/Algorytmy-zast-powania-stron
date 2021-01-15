def wyswietl_tabelke(tab):
    for element in tab: # wypisanie elementów tablicy
        
        if( len(str(element)) == 2 ): # do oznaczania miejsc braków storn
            print(element, end="| ")
            continue
        
        print(element, end=" | ")
        
    print()

def wypelnij(tab,il_ramek,il_odwolan,i): # wypełnia cała prawą stronę ramek od i ich liczbami wskazanymi przez i
    for y in range(il_ramek): # dana ramka
        liczba = tab[y][i] # liczba którą wypełni
        for x in range(i,il_odwolan): # dane odwolanie w ramce
            tab[y][x] = liczba


    

def fifo(ilosc_ramek,liczba_odwolan,odwolania):
    
    # definiowanie rozmiarów list
    ramki = [[" " for x in range(liczba_odwolan)] for y in range(ilosc_ramek)]


    czas_bycia = [0 for x in range(ilosc_ramek)] # ile dana strona jest w pamięcii

    # algorytm
    braki_stron = 0
    x = 0
    id_ramki = 0  # numer ramki
    pom_id = 0


    aktualne_strony = []

    for znacznik in range(liczba_odwolan):  # zawsze na początku żadna ramka nie będzie zajęta
        # wypełnia na początku ramki
        if (id_ramki > ilosc_ramek - 1):  # przekroczono ilosc ramek
            id_ramki = 0

        if( ramki[id_ramki][x] == " " ):
            ramki[id_ramki][x] = odwolania[x]
            aktualne_strony.append(odwolania[x]) # dodaje na koniec listy
            wypelnij(ramki, ilosc_ramek, liczba_odwolan, x)
            braki_stron = braki_stron + 1
            ramki[id_ramki][znacznik] = str(odwolania[znacznik]) + "."  # żeby zaznaczyć że jest błąd strony, wywołuje 2 raz
                                                            # bo funkcja wypełnij by skopiowała to zaznaczenie na inne warotści
            id_ramki += 1
            x += 1
            continue


        if( odwolania[x] in aktualne_strony): # jeśli mamy stronę w ramce to ją zostawiamy
            x += 1
            continue

        else: # musimy dodać nową stronę do ramki
            strona = aktualne_strony.pop(0)  # usuwa najstarsza strone czyli z poczatku listy

            for i in range(len(ramki)): # pętla po ramkach w elu znalezienia ramki z daną stroną
                if (ramki[i][x] == strona): # znaleziono stronę w ramce

                    ramki[i][x] = odwolania[x] # przypisanie nowej strony do ramki
                    wypelnij(ramki, ilosc_ramek, liczba_odwolan, x)
                    braki_stron = braki_stron + 1
                    ramki[i][x] = str(odwolania[znacznik]) + "."
                    #ramki[id_ramki][znacznik] = str(odwolania[znacznik]) + "."  # żeby zaznaczyć że jest błąd strony, wywołuje 2 raz
                                                            # bo funkcja wypełnij by skopiowała to zaznaczenie na inne warotści

                    aktualne_strony.append(odwolania[x])  # dodaje na koncu listy
                    break






        x += 1  # kolejne chwile czasu

    # else
    #   strona = aktualne_strony.pop(0) # usuwa najstarsza strone czyli z poczatku listy
    #   for i in range(len(ramki))
    #
    #           ramki[i][x] == odwolania[x]
    # aktualne_strony.append(odwolania[x]) # dodaje na koncu listy
    #aktualne_strony.append(odwolania[x])



 
    '''
    for znacznik in range(liczba_odwolan): # zawsze na początku żadna ramka nie będzie zajęta
        if (id_ramki > ilosc_ramek - 1):  # przekroczono ilosc ramek
            id_ramki = 0

        #pom_id = id_ramki
        pom_id = 0
        for i in range(0,ilosc_ramek): # sprawdza czasy istnienia danych w ramkach
            if( i == id_ramki-1 ): # bo spr. inne bramki niż aktualna
                pom_id = pom_id + 1  # spr. kolejną ramkę
                continue
            if( czas_bycia[i] == 1 ):
                id_ramki = pom_id
                czas_bycia[id_ramki] = 0 # zerujemy czas ramki bo została wybrana
                break # ta ramka ma być wybrana pierwsza
            pom_id = pom_id + 1 # spr. kolejną ramkę
        
        if( id_ramki > ilosc_ramek-1 ): # przekroczono ilosc ramek
            id_ramki = 0

        if( x != 0 ): # no pierwsza wpisana wartość nigdy nie będzie się powtarzać
            if( ramki[id_ramki][znacznik-1] == odwolania[znacznik] ): #ramka ma już w pamięci to odwołanie
                czas_bycia[id_ramki] = czas_bycia[id_ramki] + 1 # ramka z tymi danymi zostaje w pamięci i starzeje się
                x = x + 1
                id_ramki = id_ramki + 1
                continue

        ramki[id_ramki][znacznik] = odwolania[znacznik] #ramka nie ma w pamięci tego odwołania
        # pojawia się tu błąd strony
        wypelnij(ramki,ilosc_ramek,liczba_odwolan,x)
        braki_stron = braki_stron + 1

        ramki[id_ramki][znacznik] = str(odwolania[znacznik]) + "." # żeby zaznaczyć że jest błąd strony, wywołuje 2 raz
                                                       # bo funkcja wypełnij by skopiowała to zaznaczenie na inne warotści
        id_ramki = id_ramki + 1 # zmiana bramki
        x = x + 1 # kolejne odwołanie
        
    '''
    # wypisanie danych

    print("Kropka wskazuje miejsce wystąpienia błedy braku strony")
    print()
    
    print("Odwołania:")
    wyswietl_tabelke(odwolania)
    print()
    for y in range(ilosc_ramek):
        print("Ramka " + str(y+1) + ":")
        wyswietl_tabelke(ramki[y])

    print()

    print("Braki stron:")    
    print(braki_stron)
                



#o = [1,2,3,4,1,2,5,1,2,3,4,5]
#fifo(3,12,o)
#fifo(4, 12, o)

#o = [5,4,3,2,5,4,1,3,2,4,5,4,2,5,1]
#fifo(3,15,o)