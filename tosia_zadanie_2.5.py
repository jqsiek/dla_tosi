#definicja tablicy
array = [1,2,3,4,5,6,7,8,9]

#a) wypisanie wszxystkich elementow listy
for a in range(len(array)):
    print(array[a])

#b) obliczanie sumy elementow ktorych indx jest podzielny przez 4
totalB = 0
for b in range(len(array)):
    if b % 4 == 0:
        totalB += array[b]

print("Suma elementów listy, których indeks jest podzielny przez 4 wynosi:",totalB)

#c) zmniejszenie o 5 elementow ktore maja wartosc wieksza od 0 
for c in range(len(array)):
    if array[c] > 0:
        array[c] -= 5

#d)wypisanie elementow ktorych indx jest nieparzysty i zawiera sie w <1;5>
for d in range(len(array)):
    if d % 2 != 0:
        if 1 <= d <= 5:
            print(array[d])

#e) obliczanie liczby emelentow listy ktorych wartosc jest zawarta w przedziale <5;21>
totalE = 0
for e in range(len(array)):
    if 5 <= array[e] <= 21:
        totalE += 1

print("Liczba elementów, których wartość jest zawarta w przedziale <5:21> wynosi:", totalE)