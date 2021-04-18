import pathlib 

def horner(wielomian, n, x):

    wynik = wielomian[0] 
    for i in range(1, n):
 
        wynik = wynik*x + wielomian[i]
  
    return wynik

# funkcja wczytujaca pliki
def wczytywaniepliku():
    sciezka = pathlib.Path(__file__).parent.absolute()
    nazwapliku = str(sciezka) +  "\input.txt"
    tablica = []
    f = open(nazwapliku, 'r')
    for line in f:
        if len(line)>0: #pomijamy puste linie
            if line[0] != '#': #pomijamy linie z komentarzem
                tablica.append(parsuj(line))
    return tablica

def parsuj(linia):
    wynik = []
    linia = linia.replace(" ", "") #usuwamy spacje ze wzoru
    miejsceznaku = linia.find('=')
    linia = linia[miejsceznaku+1:-1] #usuwamy poczatek i znak = (miesjceznaku+1) oraz znak konca linia (-1)
    start = 0
    #teraz mamy samo rownanie
    for indeks in range(len(linia)):
        if linia[indeks] == '+' or linia[indeks] == '-':
            if linia[start] == '+': start +=1 #jak mamy plus to go usuwamy, wazny jest tylko minus na przodzie
            wynik.append(linia[start:indeks])
            start = indeks
    
    #teraz jeszcze ostatni wyraz
    if linia[start] == '+': start +=1 #jak mamy plus to go usuwamy, wazny jest tylko minus na przodzie
    wynik.append(linia[start:])
    return wynik


def main():
    print("Witaj, oblicze dla Ciebie wartosc wielomianu.")
    sparsowanyplik = listawielomianow = wczytywaniepliku()
    print(sparsowanyplik)
    #teraz dla kazdej z list wczytanych z pliku trzeba zrobic tablice wielomianow jak nizej

    wielomian = [2, -6, 2, -1]
    #pobranie wartosci x dla ktorej ma byc obliczona wartosc od uzytkownika
    x = int(input("Podaj wartosc x: "))
    x=2
    n = len(wielomian)
    
    print("Wartosc wielomianu dla x=" +str(x) + " jest rowna:  " +str(horner(wielomian, n, x)))

if __name__ == "__main__":
    main()