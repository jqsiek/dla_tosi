#definiowanie tablicy
array = [1,2,3,4,5,6,7,8,9]

#wczytanie liczby od użytkownika
numA = int(input())

#a) wypisanie ilosci liczb w tablicy równej wczytanej od użytkownika (i szybkie liczenie)
print("W liście znajduje się", array.count(numA), "liczb, równych wczytanej z klawiatury")

#b) obliczanie sredniej arytmetycznej elementow z listy
total = 0
for b in range(len(array)):
    total += array[b]

mean = total / len(array)
print("Średnia arytmetyczna liczb w tablicy wynosi:", mean)

#c) srednia arytmetyczna liczb nieparzystych
meanB = 0
totalB = 0
numB = 0
for c in range(len(array)):
    if c % 2 != 0:
        totalB += array[b]
        numB += 1

meanB = totalB / numB
print("Średnia arytmetyczna liczb nieparzystych w tablicy wynosi:", mean)