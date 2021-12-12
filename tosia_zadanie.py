def p_prostokata(a,b):
    return a*b
def p_trojkata(a,h):
    return 0.5*a*h
print("Wybierz opcję\n1.Pole figur\n2.Obwody figur\n3.Pola powierzchni brył\n4.Objętości brył")
m1 = int(input())
if(m1 == 1):#wybrana opcja 1 - pole figr
    print("Wybierz figurę, której pole chcesz policzyć:\n1.Prostokąt\n2.Trójkąt\n3.Koło\n4.Trapez")
    mp = int(input())
    if(mp == 1): #pole prostokata
        print("Podaj obydwa boki prostokąta")
        a = int(input())
        b = int(input())
        P = p_prostokata(a,b)
        print("Pole tego prostokąta to " + str(P))
    if(mp == 2): #pole trojkata
        print("Podaj wysokosc trojkata, nastepnie podstawe")
        h = int(input())
        a = int(input())
        P = p_trojkata(a,h)
        print("Pole tego trojkata to " + str(P))
    if(mp == 3): #pole kola
        print("Podaj promien kola")
        r = int(input())
        P = 3.1415*r*r
        print("Pole tego kola to " + str(P))
    if(mp == 4): #pole trapezu
        print("Podaj podstawy trapezu, nastepnie jego wysokosc")
        a = int(input())
        b = int(input())
        h = int(input())
        P = 0.5*(a+b)*h
        print("Pole tego trapezu to " + str(P))