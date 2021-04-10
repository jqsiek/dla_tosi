#pobranie od użytkownika 10 elementow tablicy
array = []
for a in range(10):
    array.append(int(input()))

#a) wypisanie wszystkich elementow listy
for a2 in range(10):
    print(array[a2])

#b)suma elementow listy ktorych wartosc > 6
totalB = 0
for b in range(len(array)):
    if array[b] > 6:
        totalB += array[b]

print("Suma elementów listy, których wartość jest większa od 6 wynosi:", totalB)

#c) wypisanie elementow listy ktorych index jest w <3;7>
for c in range(len(array)):
    if 3 <= c <= 7:
        print(array[c])

#d)wyzerowanie elementow listy, ktorych indx jest podzielny przez 3
for d in range(len(array)):
    if d % 3 == 0:
        array[d] = 0

#e) obliczanie sredniej arytmentycznej listy i wypisanie elementow mniejszych od sredniej
mean = 0
total = 0 
for e in range(len(array)):
    total += array[e]

mean = total / len(array)
print("Średnia arytmetyczne elementów w liście wynosi:", mean)
print("Elementy listy, które są mniejsze od średniej:")

for f in range(len(array)):
    if array[f] < mean:
        print(array[f])
