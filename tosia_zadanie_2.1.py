#definiowanie tablicy
array = [1,2,3]

#a) wyswietlanie wszystkich elementów tablicy
for a in range(len(array)):
    print(array[a])

#b) liczba elementów których numer jest parzysty (0 nie jest parzyste)
#liczba elementow parzysta
if (len(array)) % 2 == 0:
    evens = int((len(array)) / 2)
    print("Liczba elementów, których numer jest parzysty:", evens)


#liczba elementow nieparzysta
if (len(array)) % 2 != 0:
    evens = int((len(array) - 1) / 2)
    print("Liczba elementów, których numer jest parzysty:", evens)

#c)Zwiekszenie o 2 wartosci tych elementow listy, których wartość < 5
for c in range(len(array)):
    if int(array[c]) < 5:
        array[c] += 2

#d)obliczanie iloczynu tych elementow listy, ktorych wartosc == 3
arrayProduct = []
for d in range(len(array)):
    if int(array[d]) == 3:
        arrayProduct.append(3)

product = 3 ** len(arrayProduct)
print("Iloczyn liczb z tablicy, których wartość to 3 jest równy:", product)

#e) Obliczanie sumy tych elementow ktorych numer jest podzielny przez 3
total = 0
for e in range(len(array)):
    if e % 3 == 0:
        total += array[e]

print("Suma elementów, których numer jest podzielny przez 3 wynosi:", total)