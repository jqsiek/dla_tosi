#pobranie od użytkownika 12 elementow tablicy
array = [1,2,3,4,5,6,7,8,9,10,11,12]
#for a in range(12):
#    array.append(int(input()))

#a) wypisanie wszystkich elementow listy
for a2 in range(12):
    print(array[a2])

#b) obliczanie liczby elementow listy, ktorych numer jest podzielny przez 5
div5 = 0
for b in range(12):
    if b % 5 == 0:
        div5 += 1

print("Liczba elementów, których numer jest podzielny przez 5 wynosi:", div5)

#c) zwiekszanie o 2 wartosci tych elementow listy ktore maja nieparzysty numer zawarty w przedziale od 3 do 9 wlacznie
for c in range(12):
    if 3 <= c >= 9:
        if c % 2 != 0:
            array[c] += 2
        
#d)obliczanie iloczynu tych elementow listy, ktorych wartosc == 5
arrayProduct = []
for d in range(len(array)):
    if int(array[d]) == 5:
        arrayProduct.append(5)

product = 5 ** len(arrayProduct)
print("Iloczyn liczb z tablicy, których wartość to 5 jest równy:", product)

#e) obliczanie liczby elementow ktore nie zawieraja sie w przedziale <5,8>
numE = 0
for e in range(len(array)):
    if array[e] < 5 or array[e] > 8:
        numE += 1

print("Liczba elementów, których wartość nie zawiera się w przedziale <5;8> wynosi:", numE)