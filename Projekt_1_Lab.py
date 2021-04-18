print("Witaj, oblicze dla Ciebie wartość wielomianu.")
def horner(wielomian, n, x):

    wynik = wielomian[0] 
    for i in range(1, n):
 
        wynik = wynik*x + wielomian[i]
  
    return wynik
# funkcja wczytująca pliki
def wczytywaniepliku():
    nazwapliku = "input.txt"
    tablica = []
    f = open(nazwapliku, 'r')
    for line in f:
        print(line, end='')
    return tablica

wczytywaniepliku()
wielomian = [2, -6, 2, -1]
#pobranie wartości x dla której ma być obliczona wartość od użytkownika
x = int(input("Podaj wartość x: "))
n = len(wielomian)
 
print("Wartość wielomianu dla x=" +str(x) + " jest równa:  " +str(horner(wielomian, n, x)))

 