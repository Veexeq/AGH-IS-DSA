# =================================================================================================
# Wstęp / podsumowanie teorii
#
# Algorytmy zachłanne działają na zasadzie wybierania za każdym razem lokalnego ekstrermum, z
# nadzieją, że doprowadzi to do globalnego ekstremum. Jeśli problem da się rozwiązać podejściem
# zachłannym, to mówimy, że ma on własność wyboru zachłannego.
#
# Algorytmy zachłanne stosujemy, gdy nasz problem optymalizacyjny sprowadza się do dokonania
# optymalnego wyboru, który zostawia jeden podproblem do rozwiązania. Należy dowieźć, że wybór 
# zachłanny jest bezpieczny.
#
# Problemy rozwiązywane na wykładzie oraz na laboratoriach:
# 1. Problem przydziału zajęć
# 2. Kodowanie Huffmana
# 3. Ciągły problem plecakowy (na tyle intuicyjny, że ne będę go opisywał)
# =================================================================================================

# =================================================================================================
# Kod i wyjaśnienia:
# 
# Problem przydziału zajęć:
# Mamy pewien zasób, niech to będzie sala wykładowa, który chcemy wykorzystać do granic możliwości -
# w tym przypadku będzie to zmieszczenie jak największej liczby zajęć do grafiku tej sali.
# Mamy dany zbiór S = {a_1, a_2, ..., a_n}, gdzie a_i to pewne zajęcia. Każde zajęcia mają godzinę
# rozpoczęcia oraz godzinę zakończenia, kolejno s[i] oraz f[i] takie, że 0 <= s[i] < f[i] < INF.
# Wybierając zajęcia a_i zajmujemy salę wykładową na czas [s[i], f[i]).
# 
# 1. Optymalna podstruktura oraz wspólne podproblemy:
# Niech S_(i,j) będzie oznaczał zbiór wszystkich zajęć, które zaczynają się po skończeniu zajęć a_i 
# oraz kończą przed rozpoczęciem zajęć a_j. Naszym problemem jest (w ogólnym przypadku) znaleźć zbiór 
# A_(i,j), czyli zbiór największej liczby wzajemnie zgodnych zajęć z S_(i,j).
# Aby go stworzyć, wybieramy pewne zajęcia a_k, które zakładamy, że jest optymalne. Teraz mamy podział na
# dwa podproblemy, czyli znaleźć optymalny wybór zajęć w A_(i,k) oraz A_(k,i). Nasz wynikowy zbiór
# będzie w takim wypadku spełniał taką własność: |A_(i,j)| = |A_(i,k)| + 1 + |A_(k,i)|
# Jak widać, moglibyśmy rozwiązać ten problem przy użyciu DP, ale nie będziemy tego robili, ponieważ
# ten problem posiada wybór zachłanny.
#
# 2. Wybór zachłanny:
# Wybierając lokalne minimum - zajęcia kończące się najwcześniej - pozostawiamy najwięcej czasu na 
# "upakowanie" reszty zajęć, co w tym problemie prowadzi do uzyskania globalnego minimum.
# Należy więc posortować zbiór zajęć po czasie zakończenia i wybierać zawsze najmniejszą opcję.
# Dlaczego tak jest? Ponieważ wybierając zajęcia kończące się najwcześniej, a także korzystając z faktu,
# iż te zajęcia musiały zacząć się wcześniej niż skończyć, nie jesteśmy w stanie wybrać lepszej opcji.
# Wybierając zajęcia, które rozpoczynają się najwcześniej, uzyskalibyśmy późniejszy czas zakończenia,
# więc nie uda nam się wstawić więcej zajęć "z przodu", natomiast zostawiamy tylko mniej czasu na 
# zajęcia po skończeniu tych. 

# Zajęcia indeksujemy od 1, zerowe zajęcia to narzędzie, "blokada"
s = [0, 1, 3, 0, 5, 8, 5]
f = [0, 4, 5, 6, 7, 9, 9]
n = len(s) - 1

def recursive_activity_selector(s, f, k, n):
    # Szukamy najwcześniej kończących się zajęć, które zaczynają się wcześniej, niż f[k]
    m = k+1
    while m <= n and s[m] < f[k]: 
        m += 1

    # Jeśli znaleźliśmy takie zajęcia, to dodajemy do rozwiązania
    if m <= n:
        return [m] + recursive_activity_selector(s, f, m, n)
    else:
        return []
    
def iterative_activity_selector(s, f):
    n = len(s) - 1
    ans = [1]
    i = 1

    for m in range(2, n+1):
        if s[m] >= f[i]:
            ans.append(m)
            i = m
    return ans

A = recursive_activity_selector(s, f, 0, n)
B = iterative_activity_selector(s, f)
print(f"A: {A}\nB: {B}")

# Złożoność obliczeniowa:
#   a) Time Complexity: Theta(N)
#   b) Space Complexity: Theta(N)
# To przy założeniu, że zbiór jest od razu posortowany, inaczej sortowanie jest
# oczywiście przeważające w notacji asymptotycznej.

# Kodowanie Huffmana:
# Jest to efektywna metoda kompresji danych. Mając dany pewien alfabet, tworzymy słowa bitowe składające
# się z tzw. kodów prefiksowych, czyli takich kodów, że żaden inny kod nie rozpoczyna się danym kodem. Jest
# to przypadek ze zmienną długością kodów, gdyż możemy również zrobić kody o stałej długości, wtedy jest
# to prostsze, ale mniej optymalne. Optymalny kod o zmiennej długości to taki, którego drzewo prefiksowe jest
# zbalansowane - ma zawsze dwóch potomków.
#
# 1. Tworzenie drzewa kodów prefiksowych:
# Wpierw musimy posortować nasz alfabet malejąco względem liczby wystąpień danej litery w naszym pliku.
# Najczęściej występujące litery będą miały najkrótsze kody, by zminimalizować rozmiar wyjściowego kodu.
# Z naszych liter tworzymy kolejkę priorytetową typu min, więc pierwsze do wyjścia są najrzadsze elementy.
# Pobieramy z kolejki dwa elementy i robimy z nich drzewo (nie jest to drzewo BST!), które w rodzicu ma wartość sumy 
# wystąpień tych elementów, a następnie wrzucamy je do kolejki. Jeśli jest już element o takim samym kluczu, to 
# wstawiamy nowo utworzone drzewo przed nie. Powtarzamy to aż do momentu, gdy kolejka jest pusta. Wynikowym drzewem o 
# korzeniu w sumarycznej liczności liter alfabetu jest drzewo kodów prefiksowych. Jak z niego korzystać? Zasada jest prosta:
# jeśli chcemy stworzyć kod, to idąc w lewo dodajemy do niego 0, a w prawo - 1. Nie będę pisał kodu, bo więcej
# pracy z definiowaniem klas i technicznych rzeczy, niż samej logiki.
#
# 2. Odszyfrowanie kodu:
# Aby odszyfrować dany kod musimy poruszać się po drzewie bit-po-bicie tak, jak w punkcie pierwszym, a gdy dojdziemy do
# węzła, który nie ma potomków, to oznaczać będzie, że dotarliśmy do naszego znaku. Odczytujemy znak, wracamy na początek
# drzewa i kontynuujemy dopóki mamy dane do odszyfrowania.
#
# Złożoność obliczeniowa dla tworzenia drzewa:
#   a) Time Complexity: Theta(nlgn)
#   b) Space Complexity: Theta(n)
#
# Właściwość wyboru zachłannego: podczas tworzenia drzewa zawsze wybieramy dwa lokalnie najmniejsze węzły i robimy z nich
# poddrzewo, które następnie wstawiamy do głównego drzewa.
# Właściwość optymalnej podstruktury: wynikowe drzewo składa się z optymalnie stworzonych poddrzew
#
# Inne typowe problemy stosujące strategię zachłanną:
# 1. Algorytmy Kruskala i Prima - tworzenie minimalnych drzew rozpinających
# 2. Algorytm Dijkstry - najkrótsza ścieżka z pojedynczego źródła w grafie o nieujemnych wagach 
# =================================================================================================
