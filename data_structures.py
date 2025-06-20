# =================================================================================================
# Wstęp / podsumowanie:
# Omawialiśmy kilka podstawowych abstrakcyjnych struktur danych, były to:
# 1. Min/Max Heap (kopiec typu min/max) oparty na tablicy
# 2. Priority Queue (kolejka priorytetowa, najczęściej typu min, czyli pierwsze do wyjścia 
# najmniejsze klucze) oparta na kopcu
# 3. (Doubly) Linked list (Lista jedno / dwukierunkowa) - głównie zrealizowana na wykładzie z C
# 4. Hash table (tablice z hashowaniem)
# 5. BST (drzewa poszukiwań binarnych)
# 6. Red-Black Trees (drzewa czerwono-czarne)
# Pozostawione bez głębszego omówienia:
# 7. Stack (stos, kolejka LIFO)
# 8. Queue (zwykła kolejka FIFO)
# =================================================================================================

# =================================================================================================
# 1. Min/Max Heap:
# Kopiec binarny to drzewo, gdzie zachowana jest tzw. własność kopca, czyli rodzic ma większą 
# wartość niż jego dzieci (kopiec typ maks, analogicznie z kopcem typu min).
# Implementujemy go za pomocą tablicy 1-indexed. Można wtedy łatwo wyprowadzić makra:
# Left(idx) = 2*idx, Right(idx) = 2*idx + 1, Parent(idx) = floor(idx / 2)
# Wysokość kopca to liczba krawędzi od korzenia do najniższego liścia i wynosi floor(lgn)
#
# 2. Priority Queue:
# Priority Queue, czyli kolejka priorytetowa to struktura danych oparta na kopcu (omówię kolejkę
# typu maks, typu min jest analogiczna). Możemy na niej wykonywać operacje takie jak extract-max, 
# maximum, czy increase-key. "Maximum" po prostu zwraca informacje na temat aktualnego kandydata na
# opuszczenie kolejki, extract-max usuwa tego kandydata, wstawia na jego miejsce najmniejszy element
# oraz przywraca własność kopca (tak jak w heapsort) a increase-key zwiększa klucz danego elementu. To
# również może zepsuć własność kopca, więc należy ją naprawić poprzez procedurę przypominającą 
# insertion-sort - zamieniamy miejscami klucz z rodzicem dopóki nie wpadnie on na właściwe miejsce.
#
# 3. (Doubly) Linked list:
# Była omawiana głównie na C, więc raczej nie powinno być jej na egzaminie z algorytmów. Na razie pomijam,
# wrócę jeśli starczy czasu.
#
# 4. Hash table:
# Tablica z hashowaniem służy do implementacji operacji słownikowych, więc pozwala w optymistycznym
# scenariuszu i dobrej funkcji hashującej na czas wyszukiwania O(1). Możemy na nich wykonywać operacje
# insert, delete, search. Mamy do wyboru kilka implementacji hash mapy.
#
#   a) adresowanie bezpośrednie (nie jest to tablica z hashowaniem):
# Gdy nasza przestrzeń kluczy, którą oznaczymy U, jest rozsądnie mała, możemy adresować bezpośrednio nasze
# elementy. Nie pozwalamy w takiej sytuacji na duplikaty kluczy, gdyż ta implementacja to po prostu tablica
# T[0...m-1] dla U = {0, 1, ..., m-1}. Oznaczymy K zbiór faktycznie używanych kluczy, więc naturalnie K to
# podzbiór U. Wtedy w tablicy T zapełnione są komórki z indeksami z K, a dla każdego k należącego do K
# w komórce T[k] jest wskaźnik do elementu o kluczu k. 
# - Wstawianie: T[x.key] = x
# - Usuwanie: T[x.key] = NIL
# - Przeszukiwanie: return T[x.key]
# Wszystko działa w czasie O(1), złożoność pamięciowa to O(|U|).
# Minus takiej implementacji to wiele zmarnowanej pamięci w przypadku, gdy zbiór używanych kluczy K jest 
# znacznie mniejszy od przestrzeni wszystkich możliwych kluczy U.
#
#   b) tablice z hashowaniem:
# Ponownie rozważamy przestrzeń U wszystkich kluczy oraz K kluczy faktycznie używanych. Zamiast przypisywania
# elementu o kluczu k bezpośrednio do "wiaderka" T[k], przypiszemy go do T[h(k)], gdzie h(k) jest funkcją
# hashującą. Funkcje hashujące są wyznaczane często heurystycznie, zależy nam na tym, by spełniała ona
# własność prostego równomiernego hashowania, czyli aby każdy klucz miał jednakowe prawdopodobieństwo, że 
# wpadnie do danego "wiaderka" (komórki tablicy). Jeśli nam się to uda, wtedy kolizji będzie niewiele, choć przy
# wystarczająco dużej liczbie kluczy z pewnością się pojawią. Załóżmy, że nasza funkcja hashująca zwraca wartości 
# ze zbioru {0,1,...,m-1} oraz, że mamy n kluczy. Współczynnik zapełnienia tablicy to: alfa = n/m, czyli średnia
# liczba elementów, które wpadną do danego wiaderka przy założeniu prostego równomiernego hashowania. Rozwiązywanie
# kolizji poprzez dołączanie elementów do list nazywamy metodą łańcuchową.
# 
# - Wstawianie: tablica T to tablica list, więc wstawianie na początek listy to O(1)
# - Przeszukiwanie: w pesymistycznym scenariuszu O(n), bo wszystko trafiło do jednej listy. W optymistycznym
# scenariuszu O(1), ponieważ nie ma kolizji i od razu dostajemy nasz element. W przeciętnym scenariuszu O(1+alfa), 
# gdyż najpierw obliczamy h(k) co robimy w stałym czasie, a później musimy przejść przez listę zapełnioną średnio
# (przy założeniu o prostym równomiernym hashowaniu) przez alfa elementów. Gdy n = O(m), a więc liczba elementów
# jest proporcjonalna liniowo do wielkości tablicy, wtedy O(1+alfa) = O(1+O(m)/m) = O(1). Średni przypadek
# przeszukiwania hash mapy spełniającej warunek o prostym równomiernym hashowaniu wynosi O(1).
# - Usuwanie: musimy znaleźć element, a później go usunąć, czyli w praktyce pozamieniać kilka wskaźników, więc
# ponownie mamy tutaj O(1+alfa) = O(1) dla prostego równomiernego hashowania.
#   
# Jak skonstruować funkcję hashującą spełniającą warunek prostego równomiernego hashowania? Jest to w praktyce 
# często niewykonalne, gdyż nie znamy dokładnego rozkładu prawdopodobieństwa naszych kluczy, natomiast możemy
# konstruować funkcje, które w przybliżeniu spełniają tę własność. Przykłady:
# - K ~ Uniform(0,1): h(k) = floor(k*m)
# - hashowanie modularne: h(k) = k mod m. Wtedy istotne jest aby unikać pewnych wartości m, np. wszystkich potęg
# dwójki, ponieważ dla m = 2^p funkcja po prostu bierze p najmniej znaczących bitów (modulo 2^p można przedstawić
# jako maskę bitową). Nie powinno się również używać m = 2^p - 1, wytłumaczone na wykładzie.
# Załóżmy, że mamy ciąg 2000 znaków i chcemy je wstawić do hash mapy, która dopuszcza w średnim przypadku listę
# o długości 3, wtedy alfa = n/m => m = n/alfa => m = 2000 div 3 = 701. h(k) = k mod 701.
# - hashowanie przez mnożenie: wybieramy liczbę A z przedziału (0,1), np (sqrt(5)-1)/2 i mamy h(k)=floor(m*(A*k mod 1)),
# gdzie A*k mod 1 to po prostu część ułamkowa z A*k. 
#
#   c) adresowanie otwarte:
# W tej implementacji wszystko znów wyląduje w jednej tablicy, więc musimy zadbać aby alfa <= 1, w przeciwnym wypadku
# nastąpiłoby przepełnienie tablicy. W każdej komórce tablicy mamy albo wskaźnik do elementu, albo NIL. Funkcja hashująca
# w adresowaniu otwartym ma postać h: U x {0,1,...,m-1} ---> h(k). Dlaczego jest to funkcja dwóch zmiennych? Gdyż jeśli
# nasza 'zwykła' funkcja hashująca (której również będziemy używać) h'(k) zwróci nam klucz, który jest już w użyciu, czyli
# nastąpi kolizja, to należy w jakiś sposób znaleźć inne miejsce aby wstawić tam nasz element. Do tego przyda się drugi argument.
# - Wstawianie (polega na obliczaniu na nowo wartości hashy po aktualizowaniu zmiennej 'i'):
#

def hash_insert(T, k, hash):
    m = T.size
    i = 0
    while i < m:
        j = hash(k,i)
        if T[j] == 'NIL':
            T[j] = k
            return j
        else: 
            i += 1
    print("Przepełnienie tablicy")

#
# - Przeszukiwanie (ta sama zasada):
#

def hash_search(T, k, hash):
    i = 0
    j = hash(k,i)
    m = T.size
    while T[j] != 'NIL' and i < m:
        j = hash(k,i)
        if T[j] == k: 
            return j
        i += 1
    return 'NIL'

#
# - Usuwanie:
# Jest ono trudniejsze do zrealizowania, ponieważ po prostu wstawiając NIL po znalezieniu elementu, który chcemy usunąć.
# Jest tak z tego powodu, iż w ten sposób odcięlibyśmy dostęp do kluczy, które znajdują się po nim (hash_search kończy
# przeszukiwanie po napotkaniu NIL). Aby z tym sobie poradzić, należy wprowadzić nową stałą, DELETED. Jeśli funkcja hash_search
# napotka DELETED, powinna kontynuować przeszukiwanie, natomiast funkcja hash_insert powinna po napotkaniu wstawiać w to
# miejsce nowy element. Jeśli mamy do czynienia z sytuacją, gdzie będziemy chcieli usuwać klucze, to lepiej stosować metodę
# łańcuchową omówioną w wyższych punktach.
#
# Implementacja funkcji hashującej:
# Na wykładzie omawiane były trzy możliwości. Adresowanie liniowe, kwadratowe, oraz hashowanie dwukrotne. Żadna z tych opcji nie
# daje nam funkcji, która spełnia własność prostego równomiernego hashowania, gdyż choć wszystkie generują permutacje zbioru 
# {0, 1, ..., m-1}, to są w stanie tych permutacji wygenerować co najwyżej m^2, a nie m!.
# - adresowanie liniowe:    h(k,i) = (h'(k) + i) mod m
# - adresowanie kwadratowe: h(k,i) = (h'(k) + Ai + Bi^2) mod m, gdzie A != B to liczby całkowite
# - hashowanie dwukrotne:  h(k,i) = (h_1(k) + i*h_2(k)) mod m, gdzie h_1 i h_2 to dwie różne funkcje hashujące. Tutaj h_2(k) musi
# dawać wartości względnie pierwsze z m aby zagwarantować, że zdolni będziemy do przeszukiwania całej tablicy.
# Wszystkie funkcje hashujące jednej zmiennej to zwykłe funkcje hashujące, czyli takie, jakie omówione wcześniej.
#
# Wzory związane z adresowaniem otwartym (przy założeniu o prostym równomiernym hashowaniu):
# - liczba porównań w wyszukiwaniu, gdy nie ma elementu jest:        <= 1/(1-alfa)
# - liczba porównań w wyszukiwaniu, gdy element się znajduje jest:   <= (1/alfa) * ln[1/(1-alfa)]
# - liczba porównań we wstawianiu elementu do tablicy jest:          <= 1/(1-alfa)
#
