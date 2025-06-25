# =================================================================================================
# Wstęp / podsumowanie:
# 
# Omawialiśmy kilka podstawowych abstrakcyjnych struktur danych, były to:
# 1. Min/Max Heap (kopiec typu min/max) oparty na tablicy
# 2. Priority Queue (kolejka priorytetowa, najczęściej typu min, czyli pierwsze do wyjścia 
# najmniejsze klucze) oparta na kopcu
# 3. (Doubly) Linked list (Lista jedno / dwukierunkowa) - głównie zrealizowana na wykładzie z C
# 4. Hash table (tablice z hashowaniem)
# 5. BST (drzewa poszukiwań binarnych)
# 6. Red-Black Trees (drzewa czerwono-czarne)
# 
# Pozostawione bez głębszego omówienia:
# 7. Stack (stos, kolejka LIFO)
# 8. Queue (zwykła kolejka FIFO)
#
# Osobno były omawiane grafy, gdyż tam niewiele jest do powiedzenia na temat ich reprezentacji jako
# abstrakcyjnej struktury danych. Implementowaliśmy je za pomocą macierzy sąsiedztwa, bądź też listy
# sąsiedztwa, w zależności od relacji między licznością wierzchołków a licznością krawędzi.
# =================================================================================================

# =================================================================================================
# 1. Min/Max Heap:
# Kopiec binarny to drzewo, gdzie zachowana jest tzw. własność kopca, czyli rodzic ma większą 
# wartość niż jego dzieci (kopiec typ maks, analogicznie z kopcem typu min).
# Implementujemy go za pomocą tablicy 1-indexed. Można wtedy łatwo wyprowadzić makra:
# Left(idx) = 2*idx, Right(idx) = 2*idx + 1, Parent(idx) = floor(idx / 2)
# Wysokość kopca to liczba krawędzi od korzenia do najniższego liścia i wynosi floor(lgn)
# =================================================================================================
#
# =================================================================================================
# 2. Priority Queue:
# Priority Queue, czyli kolejka priorytetowa to struktura danych oparta na kopcu (omówię kolejkę
# typu maks, typu min jest analogiczna). Możemy na niej wykonywać operacje takie jak extract-max, 
# maximum, czy increase-key. "Maximum" po prostu zwraca informacje na temat aktualnego kandydata na
# opuszczenie kolejki, extract-max usuwa tego kandydata, wstawia na jego miejsce najmniejszy element
# oraz przywraca własność kopca (tak jak w heapsort) a increase-key zwiększa klucz danego elementu. To
# również może zepsuć własność kopca, więc należy ją naprawić poprzez procedurę przypominającą 
# insertion-sort - zamieniamy miejscami klucz z rodzicem dopóki nie wpadnie on na właściwe miejsce.
# =================================================================================================
#
# =================================================================================================
# 3. (Doubly) Linked list:
# Była omawiana głównie na C, więc raczej nie powinno być jej na egzaminie z algorytmów. Na razie pomijam,
# wrócę jeśli starczy czasu.
# =================================================================================================
#
# =================================================================================================
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
#
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
# =================================================================================================
#
# =================================================================================================
# 5. Drzewa BST:
# Drzewa poszukiwań binarnych są drzewami, gdzie rodzic ma dwóch potomków. Aby drzewo było BST musi ono spełniać własność 
# drzewa BST, czyli w lewym poddrzewie WSZYSTKIE elementy muszą być mniejsze od rodzica, a w prawym wszystkie muszą być 
# od niego większe lub równe. Zazwyczaj dopuszczamy duplikaty i kierujemy je do prawego poddrzewa. Na tak zdefiniowanym 
# drzewie BST można wykonywać operacje takie, jak przeszukiwanie, znajdowanie minimum i maksimum, znajdowanie
# nastęnika oraz poprzednika danego węzła, a także oczywiście wstawianie i usuwanie węzłów.
# Jeśli drzewo jest skonstruowane losowo, to czas działania wszystkich operacji na tym drzewie wynosi Theat(lgn). Jeśli drzewo
# będzie zdegenerowane do listy, to wtedy jak na liście, czyli Theta(n). Wysokość losowo zbudowanego drzewa wynosi O(lgn).
#
#   a) Przechodzenie drzewa (binary tree traversals):
# Mamy do wyboru trzy różne opcje: preorder, inorder, postorder. Różnią się one kolejnością wypisywania węzłów. Można sobie to
# bardzo dobrze zobrazować patrząc na obrazek (czerwony, zielony i niebieski odpowiadają kolejności w linijce wyżej):
# https://upload.wikimedia.org/wikipedia/commons/thumb/7/75/Sorted_binary_tree_ALL_RGB.svg/440px-Sorted_binary_tree_ALL_RGB.svg.png
# Podsumowując: preorder wypisuje wartość w węźle przed wypisaniem poddrzew, inorder wypisuje wpierw lewe poddrzewo, później wartość
# w węźle, następnie prawe, a postorder wypisuje wpierw lewe, później prawe poddrzewo, a na końcu wartość w węźle.
# Złożoność obliczeniowa jest oczywiście równa Theta(n), gdzie n to liczba węzłów. Dowód metodą podstawiania:
#
# - Dla n = 0 węzłów:
# T(0) = c, c jest stałą przetworzenia pustego drzewa
# - Dla n > 0 węzłów (n-1 węzłów w poddrzewach, bo jeden węzeł to korzeń oraz mamy k węzłów w lewym poddrzewie)
# T(n) = T(k) + T(n - k - 1) + d, d to stały czas przetworzenia aktualengo węzła
# - Podstawienie: T(n) = (c+d)*n+c
# T(0) = (c+d)*0+c = c, zgadza się
# T(n) = (c+d)*k+c + (c+d)*(n-k-1)+c + d, po wymnożeniu mamy:
# T(n) = (c+d)*n + c, ckd.
#
#   b) Przeszukiwanie drzewa:
# Z racji na rekurencyjną postać drzewa jako struktury danych, jest ono bardzo proste, bo zwyczajnie poruszamy się na prawo
# oraz na lewo aż do momentu znalezienia klucza, bądź napotkania na pusty węzeł:
#

def tree_search(node, k):
    if node == 'NIL' or node.key == k:
        return node
    if k < node.key:
        tree_search(node.left, k)
    else:
        tree_search(node.right, k)

def iterative_tree_search(node, k):
    while node != 'NIL' and node.key != k:
        if k < node.key:
            node = node.left
        else:
            node = node.right
    return node

#
# Złożoność obliczeniowa tych algorytmów jest O(h), gdzie h to wysokość korzenia, więc przeciętnie h = O(lgn).
#
#   c) Znajdowanie minimum i maksimum:
# Jest to banalnie proste, gdyż wystarczy znaleźć węzły najbardziej wysunięte na lewo, bądź na prawo. Złożoność obliczeniowa
# poniższych algorytmów to ponownie O(h) = O(lgn) w przeciętnym przypadku, gdy drzewo jest losowo tworzone.
#

def minimum(node):
    while node.left != 'NIL':
        node = node.left
    return node

def maximum(node):
    while node.right != 'NIL':
        node = node.right
    return node

#
#   d) Wstawianie węzła do drzewa:
# Wstawianie jest również bardzo intuicyjne. Wpierw szukamy odpowiedniego miejsca dla naszego nowego węzła - porównujemy jego
# klucz z kluczami węzłów z drzewa aż w końcu znajdziemy się w odpowiednim miejscu, czyli w pustym węźle. Teraz mamy dwa scenariusze
# do ogarnięcia. Albo nasze drzewo jest puste, czyli nasz pusty węzeł nie ma rodzica, albo ma rodzica, wtedy drzewo nie było puste.
# Jeśli jest puste, to czynimy nasz węzeł nowym korzeniem, a jeśli nie było puste, to podpinamy nasz węzeł do odpowiedniego dziecka.
#

# T pełne drzewo korzeń, wstawiamy node
def insert_node(T, node):
    # y będzie po wyjściu z pętli rodzicem x, x to aktualnie sprawdzany węzeł
    y = 'NIL'
    x = T.root
    while x != 'NIL':
        y = x
        if node.key < x.key:
            x = x.left
        else:
            x = x.right
    node.parent = y

    # Drzewo było puste / niepuste
    if y == 'NIL':
        T.root = node
    else:
        if node.key < y.key:
            y.left = node
        else:
            y.right = node
    
#
#   e) Znajdowanie poprzednika oraz następnika:
# Poprzednik i następnik (predecessor, successor) danego węzła są bardzo istotne ze względu na operację usuwania węzłów.
# Poprzednikiem aktualnego węzła jest największy węzeł mniejszy od aktualnego, czyli węzeł, który wystąpiłby bezpośrednio przed
# aktualnym przy wykonywaniu inorder-traversal. Z następnikiem jest analogicznie, jest to najmniejszy węzeł większy od aktualnego,
# czyli taki, który pojawiłby się następny w przypadku wykonywania inorder-traversal. Omówię tylko znajdowanie następnika, algorytm
# z poprzednikiem będzie dokładnie taki sam, tylko odbity symetrycznie.
# 
# Aby znaleźć następnik musimy rozważyć dwa scenariusze. Albo węzeł ma prawe poddrzewo, albo nie ma. Jeśli ma prawe poddrzewo, to
# z definicji będą tam same elementy większe, więc szukamy w prawym poddrzewie minimum. Jeśli nie ma, to należy przechodzić w górę
# drzewa. Zapamiętujemy węzeł aktualny i węzeł z którego przyszliśmy. Szukamy pierwszego takiego miejsca, gdzie węzeł 
# z którego przyszliśmy jest lewym potomkiem aktualnego węzła. Dlaczego? Ponieważ nasz pierwotny węzeł był największy w 
# tym lewym poddrzewie, więc następnikiem będzie korzeń lewego poddrzewa.
# 

def successor(node):
    if node.right != 'NIL':
        return maximum(node.right)
    prev = node.parent

    # korzystamy z logicznego zaprzeczenia: 
    # (przerywamy gdy node == prev.left) <=> (kontynuujemy dopóki node == prev.right)
    while prev != 'NIL' and node == prev.right:
        node = prev
        prev = prev.parent
    
    return prev

def predecessor(node):
    if node.left != 'NIL':
        return maximum(node.left)
    prev = node.parent

    while prev != 'NIL' and node == prev.left:
        node = prev
        prev = prev.parent
    
    return prev

#
# Te algortmy działają w czasie O(h), gdzie h jest wysokością drzewa.
#
#   f) Usuwanie węzła:
# Operacja usuwania węzła dzieli się na trzy scenariusze. Rozróżniamy gdy węzeł ma zero, jednego oraz dwóch potomków.
# Usuwanie w pierwszych dwóch sytuacjach jest bardzo proste, a w trzecim scenariuszu jest nieco bardziej skomplikowane.
# Podczas usuwania węzłów będziemy korzystać z pomocniczej metody 'transplant', która podmienia węzeł w drzewie na inny.
# Jest to bardzo prosta metoda, polega na wypięciu danego węzła wraz z całym potomstwem i wstawieniu nowego w to miejsce.
#

def transplant(T, u, v):
    if u.parent == 'NIL':
        T.root = v
    elif u == u.parent.left:
        u.parent.left = v
    else:
        u.parent.right = v
    if v != 'NIL':
        v.parent = u.parent

#
# Czas działania transplant to O(h)
#
# - Brak dzieci i jedno dziecko: oba scenariusze zmieścimy w jedną logikę, gdyż projektując rozwiązanie dla braku lewego
# oraz braku prawego dziecka załatwiamy również brak obu dzieci (jeśli nie ma dwóch dzieci, to nie ma też jednego z nich).
# Jeśli węzeł nie ma lewego poddrzewa, to wstawiamy na jego miejsce jego prawe poddrzewo. Analogicznie z brakiem prawego
# poddrzewa. W przypadku braku obu poddrzew wykona się operacja wstawiania prawego poddrzewa (bo brak lewego jest stwierdzony
# przed brakiem prawego) i w efekcie zostanie przeszczepiony na jego miejsce pusty węzeł, tak jak powinno być.
#
# - Dwóch potomków: tutaj sprawa nieco się komplikuje, ale mimo wszystko jest dosyć prosta. Jeśli chcemy usunąć węzeł w 
# taki sposób, aby zachowana była własność drzewa BST, to należy w miejsce starego węzła wstawić jego następnika. Dlaczego tak?
# Ponieważ wstawiając najmniejszy element większy od starego drzewa całe lewe poddrzewo będzie od niego mniejsze, a całe prawe
# poddrzewo będzie od niego większe. Należy więc znaleźć następnik starego węzła w jego prawym poddrzewie. Tutaj sytuacja 
# znów rozbija się, tym razem na dwa scenariusze. Albo następnik będzie bezpośrednim potomkiem starego węzła, albo będzie
# schowany gdzieś głębiej w prawym poddrzewie. Jeśli nastąpił pierwszy scenariusz, to robimy transplant następnika w miejsce 
# starego węzła i podpinamy do lewego potomka następnika lewe poddrzewo starego węzła (następnik zawsze będzie miał 
# node.left = NIL, więc nie ma problemu by podpiąć lewe poddrzewo). Jeśli natomiast następnik jest schowany gdzieś głębiej, to
# wpierw na jego miejsce przeszczepiamy jego prawe poddrzewo (pamiętamy, nie ma lewego, więc to jedyna rzecz jaką się trzeba
# zaopiekować), a następnie sam przeszczepiamy w miejsce starego węzła i tak jak wcześniej, podpinamy do jego lewego potomka
# lewe poddrzewo starego węzła.
#

def remove_node(T, node):
    # Zero, bądź jedno dziecko
    if node.left == 'NIL':
        transplant(T, node, node.right)
    elif node.right == 'NIL':
        transplant(T, node, node.left)
    # Dwójka dzieci, y to następnik
    else:
        y = successor(node.right)
        # Schowany głębiej w drzewie, szykujemy do wstawienia
        if y.parent != node:
            transplant(T, y, y.right)
            y.right = node.right
            y.right.parent = y
        transplant(T, node.left, y.left)
        y.left = node.left
        y.left.parent = y

#
# Czas działania remove_node to O(h)
# =================================================================================================
#
# =================================================================================================
# 6. Drzewa czerwono-czarne:
# Drzewa czerwono-czarne to samobalansujące się drzewa BST. Ze zwykłymi drzewami BST możemy napotkać się na
# problem braku zbalansowania, czyli sytuacji, w której drzewo zaczyna coraz bardziej przypominać listę, coraz
# więcej węzłów ma tylko jednego potomka. Doprowadza to do spowolnienia pracy na drzewie. Drzewo jest dobrze zbalansowane
# wtedy, gdy każdy rodzic ma dwóch potomków. Różnicą między zwykłym drzewem BST a drzewem czerwono-czarnym jest jeden dodatkowy
# bit informacji przechowywany w każdym węźle - każdy węzeł może być albo czerwony, albo czarny. Dzięki wprowadzeniu 
# odpowiednich ograniczeń na kombinację kolorów węzłów na dowolnej ścieżce możemy doprowadzić do sytuacji, gdzie najdłuższa
# możliwa ścieżka jest maksymalnie do dwóch razy dłuższa niż najkrótsza ścieżka w tym drzewie. Powoduje to przybliżone 
# zrównoważenie takiego red-black tree.
#
#   a) własności drzew czerwono-czarnych:
# I. każdy węzeł jest czerwony, bądź czarny
# II. korzeń jest czarny
# III. liście są czarne
# IV. czerwony węzeł ma czarnych potomków 
# V. każda ścieżka od danego węzła do jego liści ma taką samą czarną wysokość
# Czarna wysokość to liczba czarnych węzłów na ścieżce od danego węzła do liścia, z wykluczeniem tego węzła. Liść również
# wlicza się do czarnej wysokości, z wyjątkiem sytuacji, gdy liczymy czarną wysokość liścia, wtedy liść jest węzłem z 
# którego wychodzimy, a ten węzeł pomijamy.
#
# Red-black tree różni się od zwykłego BST również tym, iż skoro liście muszą przechowywać informację o ich czarnym
# kolorze, to nie mogą być one po prostu wartością NIL, lecz pełnoprawnym węzłem. Drzewo czerwono-czarne mające
# wiele liści marnowałoby wiele pamięci, jeśliby każdy liść miałby być traktowany osobno, więc tworzy się jeden globalny
# węzeł o czarnym kolorze i wartością 'NIL' podpięty do każdego najniższego węzła niebędącego liściem, a także do rodzica
# korzenia w tym drzewie. Do tego specjalnego węzła odwołujemy się jako T.nil.
#   
# Operacje na drzewach czerwono-czarnych są wykonywane w czasie O(h) = O(lgn). Dzieje się tak, ponieważ drzewo czerwono-
# czarne o n-węzłach ma wysokość h <= 2*lg(n+1). Można to udowodnić wpierw dowodząc w sposób indukcyjny lemat stanowiący, że
# poddrzewo o korzeniu x ma co najwyżej 2^(bh(x)) - 1 węzłów wewnętrznych i połączyć to z faktem, że bh(T) >= n/2.
# Dla drzew czerwono-czarnych należy zmodyfikować operację wstawiania oraz usuwania węzłów. Są one skomplikowane ze względu
# na ilość przypadków, które należy rozpatrzeć - szczególnie usuwanie węzłów, którego nie omówiliśmy na wykładzie, dlatego
# też nie będę o nim pisał.
#
#   b) rotacje na węźle:
# Procedura wykonująca rotację na danym węźle jest procedurą pomocniczą potrzebną do późniejszego usuwania węzłów.
# Aby wykonać rotację na danym węźle wystarczy pozmieniać wskaźniki występujące między węzłami. Weźmy przykład z wykładu:
# mamy węzeł y, który ma prawe dziecko gamma oraz lewe dziecko x, które z kolei ma dwójkę dzieci: alfa oraz beta.
# Możemy wykonać rotację w prawo na węźle y. Intuicyjnie wyobrażamy sobie, że w miejsce y wstawiamy teraz x. Problem w tym, że
# x ma już dwóch potomków, alfę oraz betę. alfa jest mniejsza a beta większa od x. Z pierwotnej sytuacji wiemy, że wszystkie
# węzły x, czyli poddrzewa alfa i beta wraz z samym x, są mniejsze od y, ponieważ x jest jego lewym poddrzewem. Możemy więc 
# dopiąć betę (prawy potomek x - wszystkie węzły wraz z betą większe od y) jako lewe poddrzewo y, a y jako prawe poddrzewo x.
#
#                                         p                       p         
#                                         |                       |         
#                                         y         RR(y)         x         
#                                        / \        ====>        / \        
#                                       x   γ       <====      α    y      
#                                      / \          LR(x)          / \     
#                                    α    β                      β    γ   
#
# Opisana powyżej rotacja to right-rotate wykonana na węźle y, gdyż rotacja oznacza, że węzeł "pójdzie do góry". Odwrócenie
# kierunku rotacji daje nam left-rotate na węźle x. Wykonanie rotacji na węźle nie zmienia kolejności przechodzenia inorder, 
# operację wykonujemy w czasie O(1).
#

def left_rotate(T, x):
    y = x.right
    # Zajęcie się betą
    x.right = y.left
    if y.left != 'NIL':
        y.left.parent = x
    y.parent = x.parent
    # x jest korzeniem / lewym poddrzewem / prawym poddrzewem
    if x.parent == 'NIL':
        T.root = y
    elif x == x.parent.left:
        x.parent.left = y 
    else:
        x.parent.right = y
    # Dopięcie x jako lewego poddrzewa
    y.left = x
    x.parent = y

# Analogicznie, zostawiam pustą funkcję by interpreter się nie czepiał w dalszej notatce 
def right_rotate(T,x):
    return

#
# Rotacja w prawo analogicznie. Złożoność obliczeniowa tych algorytmów to O(1).
#
#   c) wstawianie węzła do RB-tree:
# Wstawianie węzła może naruszyć dwie własności drzewa: własności II i IV. Dzieje się tak dlatego, że wpierw wstawiamy
# węzeł tak jak to robliśmy w BST, a następnie nasz nowy węzeł kolorujemy na czerwono. Teraz, gdy węzeł jest już na dobrym
# miejscu, należy naprawić własności drzewa poprzez odpowiednie kolorowanie reszty węzłów. Do tego przydadzą nam się procedury
# pomocnicze left-rotate i right-rotate. 
#
# Naprawianie własności drzewa czerwono-czarnego dzieli się na dwa główne scenariusze, z których każdy ma trzy scenariusze. 
# Dwa główne scenariusze są swoimi odbiciami, więc wystarczy zająć się jednym z nich. Istotnymi węzłami jest tutaj nowo-wstawiony
# węzeł (z), jego rodzic (z.parent), dziadek (z.parent.parent) a także wujek (y). Wujka oznaczamy y z tego powodu, że może on być 
# prawym dzieckiem dziadka, bądź też lewym dzieckiem. Z tych przypadków składa się pierwszy wybór dotyczący dwóch głównych scenariuszy.
# Załóżmy, że wujek jest prawym dzieckiem dziadka, a rodzic z jest jego lewym dzieckiem. Musimy sprawdzić, czy naruszyliśmy własności
# drzewa czerwono-czarnego. O czarny korzeń zadbamy na samym końcu, wpierw naprawimy dwa czerwone węzły pod rząd. Jeśli tak się
# stało, to analizujemy trzy możliwe przypadki:
#
# - wujek z jest czerwony: 
#   I. zmień kolor rodzica z oraz wujka na czarny
#   II. zmień kolor dziadka na czerwony
#   III. ustaw z = z.parent.parent, stąd kontynuujemy dalsze sprawdzanie
#
# - wujek z jest czarny, z jest prawym dzieckiem swojego rodzica: ten przypadek łatwo zapamiętać i odróżnić od trzeciego ze względu
# na kąt quasi prosty pojawiający się na rysunku (tworzą go węzły dziadek-rodzic-dziecko). W tym przypadku: 
#   I. wykonaj rotację w lewo na rodzicu z
#   II. ustaw z = z.parent i stąd kontynuuj dalsze sprawdzanie
# Doprowadza nas to do ostatniego przypadku. Uwaga, idąc do trzeciego przypadku z tego miejsca traktujemy go jako nową sytuację.
# Po wykonaniu rotacji tutaj, nasz rodzic staje się dzieckiem z, ale nie zapamiętujemy tego, patrzymy na nowo na relacje.
#
# - wujek z jest czarny, z jest lewym dzieckiem swojego rodzica: ta sytuacja odróżnia się na rysunku od drugiej tym, że mamy linię prostą,
# a nie kąt przypominający prosty. W tym scenariuszu: 
#   I. zmień kolor rodzica z na czarny 
#   II. zmień kolor dziadka na czerwony
#   III. wykonaj rotację w prawo na węźle dziadka (bez zmiany węzła z jak w dwóch poprzednich przypadkach!)
#
# Po każdym wykonanym scenariuszu wracamy do sprawdzania warunku pętli, czyli do sprawdzenia, czy rodzic naszego nowego węzła z
# jest czerwony. Na samym końcu, gdy wychodzimy z pętli, czyli rodzic z jest koloru czarnego, sprawdzamy, czy korzeń jest czerwony
# i ewentualnie naprawiamy to, kończąc procedurę. Co ważne, dwa pierwsze scenariusze podmieniają z na inny węzeł z którego kontynuujemy
# sprawdzanie, a przypadek trzeci tego nie robi. Dzieje się tak dlatego, że po wykonaniu trzeciego przypadku kończymy całą procedurę, 
# wtedy drzewo jest już naprawione. Dwa pierwsze przypadki to próba ustawienia trzeciego przypadku, będącego tym docelowym.
#

def insert_fixup(T, z):
    # Naprawiamy własność IV
    while z.parent.color == 'RED':
        # Przypadek 1: wujek po prawej
        if z.parent == z.parent.parent.left:
            y = z.parent.parent.right
            # Przypadek 1.1: wujek czerwony
            if y.color == 'RED':
                z.parent.color = 'BLACK'
                y.color = 'BLACK'
                z.parent.parent.color = 'RED'
                z = z.parent.parent
            # Przypadki 1.2 i 1.3: wujek czarny
            else:
                # Przypadek 1.2: kąt prosty
                if z == z.parent.right:
                    z = z.parent
                    left_rotate(T, z)
                # Przypadek 1.3: linia prosta
                else:
                    z.parent.color = 'BLACK'
                    z.parent.parent.color = 'RED'
                    right_rotate(T, z)
        # Przypadek 2: wujek po lewej, wszystko symetrycznie
        else:
            y = z.parent.left
            if y.color == 'RED':
                z.parent.color = 'BLACK'
                y.color = 'BLACK'
                z.parent.parent.color = 'RED'
                z = z.parent.parent
            else:
                if z == z.parent.left:
                    z = z.parent
                    right_rotate(T, z)
                else:
                    z.parent.color = 'BLACK'
                    z.parent.parent.color = 'RED'
                    left_rotate(T, z)
    # Została do naprawienia własność II:
    T.root.color = 'BLACK'

# 
# Złożoność obliczeniowa tego algorytmu to O(lgn). Na wykładzie był pokazany dowód poprzez niezmiennik pętli, ale 
# jest bardzo długi i bardzo mało prawdopodobne, by trzeba było go znać. Na razie go pomijam.
# =================================================================================================
