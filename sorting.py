# =================================================================================================
# Wstęp / podsumowanie:
#
# Sortowanie jest podstawowym i jednym z prostszych zagadnień w algorytmice. Często zaczyna się od niego naukę 
# algorytmów ze względu na to, że można w ten sposób przyswoić na nietrudnych przykładach fundanenty związane z konstruowaniem
# algorytmów, takie jak np. niezmiennik pętli, czy tworzenie funkcji rekurencyjnych. Z sortowaniem wiąże się kilka
# kluczowych pojęć istotnych w kontekście egzaminu. Z pewnością jest to na pewno twierdzenie o rekurencji uniwersalnej, gdyż
# większość z sortowań, które były omawiane, są rekurencyjne. Oprócz tego ważna jest też złożoność obliczeniowa, która 
# w algorytmach opierających się na porównywaniu elementów nie może być mniejsza, niż Theta(nlgn). Sortowanie może być
# również wykonane "w miejscu", co oznacza, że nie używamy żadnej dodatkowej pamięci proporcjonalnej do rozmiaru danych,
# czyli możemy jej użyć co najwyżej O(1). Kolejnym bardzo istotnym pojęciem jest "stabilność" sortowania. Jeśli sortowanie
# jest stabilne, to oznacza, że mając dwa takie same klucze (mogą być to zupełnie inne elementy, ale klucze po których sortujemy
# mają takie same) po sortowaniu pozostaną w tej samej kolejności. Czyli gdyby te klucze jakoś rozróżnić i nazwać X_1 i X_2, to jeśli
# przed sortowniem mamy ...X_1,...X_2,... to po sortowaniu będzie ...X_1,X_2...
# 
# Na wykładzie i laboratoriach omówiliśmy następujące algorytmy sortowania:
# 1. Sortowanie przez wstawianie (insertion sort)
# 2. Sortowanie przez proste wybieranie (selection sort)
# 3. Sortowanie przez scalanie (merge sort)
# 4. Sortowanie przez kopcowanie (heap sort)
# 5. Sortownie szybkie (quick sort)
# 6. Sortowania niewykorzystujące porówań (counting sort, radix sort)
# =================================================================================================

# =================================================================================================
# 1. Sortowanie przez wstawianie (insertion sort):
# Insertion sort to bardzo podstawowy algorytm sortowania, który można sobie zwizualizować za pomocą przekładania kart trzymanych
# w ręce podczas gry. Zaczynamy od drugiej karty, znajdujemy dla niej miejsce (może zostać na swoim miejscu, albo iść przed pierwszą).
# W ten sposób mamy ciąg dwóch kart z lewej strony, który jest posortowany. Korzystając z tego faktu możemy powiększyć ciąg posortowanych
# kart o jeszcze jeden element. Bierzemy więc trzecią kartę. Czy jest mniejsza od drugiej? Załóżmy, że tak, więc zamieniamy drugą kartę
# i trzecią kartę miejscami. Czy jest mniejsza od pierwszej? Załóżmy, że nie, więc zostawiamy kartę w miejscu. W ten sposób karta została
# wstawiona w odpowiednie miejsce. Gdy po raz pierwszy odpowiemy negatywnie na pytanie "czy karta X jest mniejsza od karty Y", to wiemy,
# że jest na właściwym miejscu i należy przerwać procedurę. Tak dokładnie działa insertion sort, wstawia klucz do tablicy w odpowiednie
# miejsce, robi to poprzez ciągłe zamienianie kluczy miejscami. Przesuwamy się tak długo, jak nie jesteśmy na odpowiednim miejscu.
#

def insertion_sort(arr):
    n = arr.length
    # Dla tablicy 1-indexed: sprawdzamy "karty" na indeksach 2...n
    for i in range(2, n+1):
        # Zaczynamy porównywać liczby stojące przed arr[i]
        key = arr[i]
        j = i - 1
        # Przekładamy karty o jedno miejsce do góry
        while j >= 1 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        # key > arr[j]
        arr[j+1] = key
    return arr
    
#
#   a) Złożoność obliczeniowa tego algorytmu jest akurat jedną z mniej oczywistych ze wszystkich algorytmów sortujących. 
# Rozważmy przypadki:
# - optymistyczny: tablica jest posortowana, wtedy nigdyd nie wchodzimy do pętli while. Na każde wykonanie pętli for przypada O(1) 
# czasu, a wykonań jest n-1, więc Theta(n). Ostatecznie, optymistyczny przypadek to Theta(n).
# - średni: sprawdzamy połowę elementów w while za każdym razem. Pętla for wykonuje się Theta(n) razy, pętla while Theta(n/2) = Theta(n).
# Ostatecznie uzyskujemy czas Theta(n^2).
# - pesymistyczny: tablica posortowana w odwrotnej kolejności. Pętla while za każdym razem przechodzi od i-1 do 1. Złożoność
# obliczeniowa to suma ciągu arytmetycznego 1, 2, 3, ..., n = n(n+1)/2 = Theta(n^2).
#
#   b) Złożoność pamięciowa jest tutaj O(1), ponieważ nie alokujemy żadnej nowej pamięci proporcjonalnej do rozmiaru danych 
# wejściowych. Jedyne co tu alokujemy to pojedyncze zmienne zajmujące stałą pamięć. Jest to algorytm w miejscu.
#
#   c) Można również udowodnić, że algorytm ten jest stabilny.
#
#   d) Dowód poprawności algorytmu z użyciem niezmiennika pętli:
# Ze względu na prostotę algorytmu oraz jego iteracyjność możemy łatwo skonstruować dwa niezmienniki pętli, któe udowodnią nam,
# że algorytm spełnia własności o deterministyczności, poprawności i skończoności. Wpiew zajmiemy się pętlą for.
#
# Niezmiennik pętli: na początku każdej iteracji pętli for, tablica arr[1...i-1] składa się wyłącznie z elementów znajdujących
# się pierwotnie w niej, lecz w porządku posortowanym.
# - inicjalizacja: przed pierwszą iteracją pętli i=2, więc tablica arr[1...1] jest jednoelementowa, więc oczywiście posortowana.
# - utrzymanie: przed i-tą iteracją pętli arr[1...i-1] jest posortowana. W pętli while przesuwamy elementy o jeden indeks wyżej,
# aż do momentu, gdy znajdziemy miejsce na nasz element. Wstawiamy go, w efekcie arr[1...i] jest posortowana. Inkrementacja
# zmiennej 'i' w następnej iteracji pętli przywrarca niezmiennik (znów arr[1...i-1] jest posortowana).
# - zakończenie: pętla się kończy, gdy i = n+1, więc z niezmiennika wiemy, że tablica arr[1...n] jest posortowana.
# Algorytm jest więc poprawny.
# =================================================================================================

# =================================================================================================
# 2. Sortowanie przez proste wybieranie:
# Selection sort to chyba najprostszy algorytm sortowania, polega na tym, aby dla podtablic o malejącym rozmiarze znaleźć
# najmniejszy element i wstawić go na początek aktualnie rozważanej tablicy. Wpierw przeszukujemy arr[1...n], gdy znaleźlśmy
# już globalne minimum (bądź też jedno z globalnych minimów) i wstawiliśmy je na arr[1], możemy przeszukiwać arr[2...n],
# a jej najmniejszy element wstawiamy na arr[2]. Robimy tak aż do tablicy arr[n-1...n], która po wstawieniu minimalnego elementu
# na jej początek zostawia największy element na samym końcu, nie ma sensu robić przejśca dla arr[n...n].
#

def selection_sort(arr):
    n = arr.length
    # Dla tablic 1-indexed, szukamy od arr[1...n] do arr[n-1...n]
    for start in range(1,n):
        minimum = start
        for idx in range(start+1, n+1):
            if arr[idx] < arr[minimum]:
                minimum = idx
        # Zamień najmniejszy element z początkowym (jeśli potrzeba)
        if minimum != start:
            arr.swap(start, minimum)
    return arr

#
# Złożoność obliczeniowa: Theta(n^2)
# Złożoność pamięciowa: O(1), w miejscu
# Sortowanie nie jest stabilne, przykład:
#
# PRZED: | (5_1) | (3) | (4) | (5_2) | (1)   | (7) | Klucz 5_1 przed kluczem 5_2, swap (5_1) z (1)
# PO:    | (1)   | (3) | (4) | (5_2) | (5_1) | (7) | Klucz 5_1 po kluczu 5_2 
# =================================================================================================

# =================================================================================================
# 3. Sortowanie przez scalanie:
# Merge sort to rekurencyjny algorytm sortowania. Działa w ten sposób, że wpierw sortuje pierwszą połowę tablicy, następnie
# sortuje drugą połowę tablicy, a na końcu łączy dwie posortowane tablice w jedną. Aby kod był bardziej klarowny, dzieli się go
# na dwie procedury - scalającą, oraz sortującą. Jak wiemy, że doszliśmy już do momentu posortowania tablicy? Innymi słowy, kiedy
# należy rozpocząć procedurę scalania? Robimy to wtedy, gdy tablica jest jednoelementowa, gdyż taka zawsze jest posortowana. Z
# tablic jednoelementowych przez scalanie budujemy tablice dwuelementowe, następnie z dwuelementowych czteroelementowe i 
# kontynuujemy do momentu scalenia całej tablicy. 
# 
# Delikatny problem, który wymaga rozważenia to sytuacja, w której długość tablicy
# nie jest potęgą dwójki. Wtedy dostaniemy podtablice o rozmiarach nieparzystych, a co za tym idzie, problem z podzieleniem 
# takiej podtablicy na pół. Jak rozwiązujemy taki problem? W prosty sposób. Dzielimy tablicę arr[i...j] na arr[i...k] oraz
# arr[k+1...j]. Wiemy z tego, że k+1 <= j, więc k < j. Wzór na indeks k to k=(i+j) div 2, gdzie 'div' oznacza dzielenie całkowite.
# Spójrzmy na przykłady:
#
# arr = [1,2,3,4,5], k = (1+5) div 2 = 3, k+1 = 4
# arr_1 = [1,2,3], arr_2 = [4,5].
#
# arr = [1,2,3,4,5,6], k = (1+6) div 2 = 3, k+1 = 4
# arr_1 = [1,2,3], arr_2 = [4,5,6]
#
# arr = [1,2,3], k = (1+3) div 2 = 2, k+1 = 3
# arr_1 = [1,2], arr_2 = [3]
#
# arr = [1,2], k = (1+2) div 2 = 1, k+1 = 2
# arr_1 = [1], arr_2 = [2]
#
# arr = [1], k = (1+1) div 2 = 1, k+1 = 2
# arr_1 = [1], arr_2 = ???
#
# Jak widać ostatni przykład generuje problem, którym musimy się zająć. Warunek z ustawianiem naszego k musi być dodatkowo 
# zabezpieczony, by wykrywał sytuację, gdy dotarliśmy do już posortowanej tablicy (jednoelementowej). Rozwiązanie jest bardzo proste,
# wystarczy zwyczajnie dołożyć instrukcję warunkową sprawdzającą, czy indeks i jest mniejszy niż indeks j - tylko wtedy będziemy
# sortować lewą oraz prawą część tablicy.
#
# Teraz możemy zająć się mechanizmem łączenia podtablic, a następnie skonstruować już cały mechnizm sortowania. Załóżmy, że mamy
# dwie podtablice: a[i...k] oraz b[k+1...j]. Są one już posortowane, chcemy je połączyć w jedno. Gdy wywołujemy merge sort 
# rekurencyjnie, to operujemy na indeksach, nie przekazujemy tablicy przez wartość, a nasza procedura scalająca również nie zwraca
# nowej tablicy, tylko bezpośrednio operuje na oryginalnej. Jeśli chcemy więc poprzestawiać w łatwy sposób elementy rozróżniając
# co należało do tablicy 'a', a co należało do tablicy 'b', naszym pierwszym krokiem jest skopiowanie ich elementów do nowych tablic,
# które nazwiemy L oraz R, kolejno left i right.     Tablice L i R są posortowane, więc możemy zastosować prosty algorytm
# two-pointer: ustawiamy wskaźniki na pierwsze elementy obu tablic i porównujemy, który z nich jest większy. Załóżmy, że 
# lewa tablica left ma element, którego szukamy. Wstawiamy go na miejsce w tablicy arr[i] (pamiętajmy, łączymy elementy by w efekcie
# uzyskać posortowaną podtablicę arr[i...j]), a następnie przesuwamy wskaźnik w left na następną pozycję. Powtarzamy sytuację, 
# zapełniamy tym razem komórkę arr[i+1]. Kontynuujemy, aż wstawimy wszystkie elementy do tablicy.
#
# Scalanie można zaimplementować na dwa sposoby. Pierwszy jest z pętlą while, których warunkiem wykonania jest zadbanie, by wskaźniki
# w tablicach L oraz R nie wyszły poza tablice, a następnie, w przypadku, gdy wypisaliśmy już wszystkie elementy z jednej
# tablic, wpisanie reszty z drugiej. Drugi sposób korzysta z pojęcia tzw. strażników (sentinels), którzy tutaj sygnalizują, że dotarliśmy
# na koniec tablicy. Będą to wartości tak duże, że na pewno nie pojawią się w tablicy, którą sortujemy, więc porównanie strażnika z 
# drugim elementem zawsze zwróci drugi element. Jest to drugi sposób na scalenie wszystkich elementów bez wychodzenia poza tablice.
# Na wykładzie implementowany był sposób ze strażnikami, więc tu też tak zrobię.
#

# strażnik
INF = 2 ** 31 - 1

def merge_sort(arr, i, j):
    if i < j:
        # k to taki indeks, że dzieli arr na arr[i...k] oraz arr[k+1...j]. i <= k < j
        k = (i+j) // 2
        # sortujemy lewą połowę, prawą połowę i scalamy obie
        merge_sort(arr, i, k)
        merge_sort(arr, k+1, j)
        merge(arr, i, k, j)

def merge(arr, i, k, j):
    # obliczamy rozmiar tablic:
    l_size = k - i + 1  # to na arr[i...k]
    r_size = j - k      # to na arr[k+1...j]
    # alokujemy dwie tablice:
    L = []              # L[1...l_size+1], bo L[l_size+1] jest miejscem na strażnika
    R = []              # R[1...r_size+1], bo R[r_size+1] jest miejscem na strażnika

    # kopiujemy podtablice arr[i...k], arr[k+1...j]
    for idx in range(i, k+1):
        L.append(arr[idx])
    for idx in range(k+1, j+1):
        R.append(arr[idx])
    # dodajemy strażników
    L.append(INF)
    R.append(INF)
    
    # puszczamy two-pointer, mamy do wypełnienia podtablicę arr[i...j]
    l = 1, r = 1
    for idx in range(i, j+1):
        if L[l] <= R[r]:
            arr[idx] = L[l]
            l += 1
        else:
            arr[idx] = R[r]
            r += 1

#
# Złożoność obliczeniowa tego algorytmu to Theta(n*lgn). Dlaczego tak jest? Możemy to pokazać rozwiązując równanie
# rekurencyjne zadane wzorem (gdzie n jest długością tablicy do posortowania):
#
#         / Theta(1), gdy n = 1
# T(n) = |  
#        \  2*Theta(n/2) + Theta(n), gdy n > 1
#
# Teraz rozwiążmy 2*Theta(n/2) + Theta(n) twierdzeniem o rekurencji uniwersalnej (master theorem, CLRS)
# Budujemy watershed function: f(n) = n^(log_2(2)) = n^1 = n
# Rozważamy trzy przypadki twierdzenia o rekurencji uniweralnej:
#   a) Theta(n) = O[n^(1-eps)]. Nie istnieje taki epsilon, by Theta(n) była ograniczona od góry n^(1-eps)
#   b) Theta(n) = Theta(n*lg^(k)(n)). Istnieje k = 0 dla którego Theta(n*lg^(0)(n)) = Theta(n)
#   c) Theta(n) = Omega[n^(1+eps)]. Nie istnieje taki epsilon dla którego Theta(n) byłaby ograniczona od dołu n^(1+eps)
# Wniosek, zachodzi przypadek II master theorem, więc naszym wynikiem jest T(n) = Theta(n*lgn) (bo używamy k+1 do logarytmu).
#
# Dlaczego równanie rekurencyjne ma taką postać? Dla n = 1 po prostu sprawdzamy instrukcję warunkową i nic nie robimy. Dla 
# n > 1 dzielimy na pół i rozwiązujemy dwa podproblemy o wielkości n/2, a następnie je scalamy, co robimy w czasie liniowym.
# Ten opis nie jest dokładny, tyczy się wyidealizowanego scenariusza, gdzie n jest potęgą dwójki, bo w innym przypadku
# musielibyśmy bawić się w wrzucanie podłóg do T(n/2), ale dokłada to tylko trudności ze strony matematycznej, nie zmienia 
# wyniku, więc takie rozwiązanie jest wystarczające.
#
# Złożoność pamięciowa to Theta(n), ponieważ w operacji scalania tworzymy dwie tablice o długości Theta(n).
#
# Sortowanie przez scalanie jest sortowaniem stabilnym, ponieważ dwa identyczne klucze są wstawiane przy scalaniu w takiej
# samej kolejności, w jakiej zostały dodane do tablicy L bądź też R.
#
# Na koniec przeprowadzimy dowód poprawności algorytmu scalania:
# Niezmiennik pętli for: przed każdą iteracją pętli, podtablica arr[i...idx-1] składa się z idx - i najmniejszych elementów
# elementów z tablic L oraz R.
# - inicjalizacja: przed pierwszą iteracją idx = i, więc tablica arr[i...i-1] jest pusta. Niezmiennik jest spełniony.
# - utrzymanie: na początku każdej iteracji zakładamy, że niezmiennik jest spełniony. Na miejsce idx wstawiamy nowy, najmniejszy
# element wybierany na podstawie instrukcji warunkowych. Teraz tablica arr[i...idx] zawiera idx - i + 1 najmniejszych posortowanych
# elementów spośród tablic L oraz R. Inkrementacja idx zachowuje niezmiennik pętli.
# - zakończenie: po zakończeniu pętli idx = r + 1. Tablica arr[i...idx-1] = arr[i...r] jest posortowana i składa się z 
# idx - i = r - l + 1 najmniejszych elementów spośród tablic L oraz R.
# =================================================================================================

# =================================================================================================
# 4. Sortowanie przez kopcowanie:
# Heap sort to algorytym, który również posiada pesymistyczną złożoność O(n*lgn), lecz działa a w miejscu. Jest jednakże nieco
# wolniejszy od merge sorta, ale można również powiedzieć, że prostszy w implementacji. Sortowanie przez kopcowanie, jak sama
# nazwa wskazuje, opiera się na strukturze danych zwaną kopcem binarnym. Kopiec binarny to drzewo, które jest jednak typowo
# zaimplementowane nie poprzez strukturę z dowiązaniami (przy użyciu wskaźników), lecz poprzez zwyczajną płaską tablicę.
# Kopiec posiada tzw. własność kopca - potomkowie danego węzła mają wartości mniejsze lub równe od rodzica. Jest to własność
# kopca typu max, można również zrobić symetryczną definicję dla kopca typu min. W kopcu typu max, największy element znajduje
# się w korzeniu, czyli w arr[1]. Z racji na tablicową implementacje możemy stworzyć wygodne makra służące do poruszania się po kopcu:
#

def parent(idx):
    return idx/2
def left(idx):
    return 2*idx
def right(idx):
    return 2*idx+1

#
# Jak odbywa się sortowanie przez kopcowanie? Wpierw należy kopiec stworzyć, wtedy największy element będzie na samej górze. Później
# zamieniamy największy element z ostatnim elementem w tablicy (więc jednym z najmniejszych, znajdujących się w liściach kopca),
# a następnie zmniejszamy rozmiar kopca (w ten sposób odłączamy największy element od kopca, teraz na kopiec składa się tylko
# podtablica arr[1...n-1]). Nasz kopiec został w ten sposób zepsuty, teraz największy element nie znajduje się już na samej górze
# drzewa, dlatego należy przywrócić własność kopca. Służy do tego procedura heapify, którą wywołujemy dla korzenia. Jak działa?
# Działa w taki sposób, że porównuje, czy któreś z dzieci są większe od niej. Jeśli tak, to zamieniamy większe dziecko z danym węzłem,
# lecz w ten sposób mogliśmy zepsuć własność kopca w poddrzewie, którego to dziecko było rodzicem. Aby to naprawić, wywołujemy
# rekurencyjnie procedurę naprawczą na nowo podmienionym węźle.
#
# A w jaki sposób należy utworzyć kopiec typu max, aby w ogóle zacząć sortowanie? Zauważmy, że po pierwsze, tablica o n wartościach
# tworzy kopiec o wysokości Theta(lgn). Dalej zauważmy, że w tablicy, która jest 1-indexed, podtablica arr[n div 2 + 1...n] zawiera
# same liście. Dlaczego tak jest? Spójrzmy na element o indeksie n div 2 + 1:
#
#                                                   n div 2 + 1         > n div 2
#                                                   2*(n div 2 + 1)     > n
#                                                   2*(n div 2 + 1) + 1 > n + 1 
#
# Pokazuje to, że potomki elementu o indeksie n div 2 + 1 muszą być poza tablicą o długości n, więc ich nie ma. Wniosek z tego jest
# taki, że arr[1...n div 2] to podtablica węzłów, które nie są liśćmi. Jest to serce algorytmu związanego z budową kopca. 
# Wystarczy bowiem wywołać heapify na każdym węźle niebędącym liściem - w ten sposób przywrócimy własność kopca, choć w tym przypadku
# lepiej pasuje określenie, że zbudujemy go od zera.
#

def heapify(arr, i):
    l = left(i)
    r = right(i)

    # Sprawdzamy, czy większy element kryje się w lewym potomku
    if l <= arr.heapsize and arr[l] > arr[i]:
        largest = l
    else:
        largest = i
    # Musimy sprawdzić z nowym, aktualizowanym indeksem
    if r <= arr.heapsize and arr[r] > arr[largest]:
        largest = r
    
    if largest != i:
        arr.swap(i, largest)
        heapify(arr, largest)

def build_max_heap(arr):
    # To pierwszy raz jak korzystamy z kopca, więc rozmiar kopca jest
    # równy długości tablicy
    arr.heapsize = arr.length
    # Odpowiednik for i = arr.length / 2 down to 1
    for i in range(arr.length // 2, 1, -1):
        heapify(arr, i)

#
# Złożoność obliczeniowa: procedura heapify jest ograniczona przez wysokość drzewa i wynosi O(h). h natomiast jest ograniczone
# przez ilość węzłów 'n' i wynosi h = (lgn). W efekcie asymptotyczna złożoność heapify wynosi O(lgn). Build_max_heap natomiast
# przeczy intuicji i wcale nie ma czasu O(n*lgn), tylko O(n). Dowód:
# na wysokości h drzewa znajduje się ceil[n/[2^(h+1)]] węzłów. Maksymalna wysokość to floor(lg(n))
# w najgorszym przypadku każde z tych węzłów przejdzie na sam dół w czasie heapify, czyli O(h).
#
#       T(n) = SUM[h=0, floor(lg(n))] {n/[2^(h+1)] * O(h)} = O(n*SUM[h=0, floor(lg(n))] {h/2^(h+1)})
#               Z teorii szeregów można sprawdzić, że szereg sum częściowych h/2^h = 1, więc:
#                                           T(n) = O(n*1) = O(n)
#
# Wszystko to jest w miejscu, czyli złożoność pamięciowa to O(1).
# 

def heapsort(arr):
    build_max_heap(arr)
    # Usuwamy z kopca już posortowane elementy
    for i in range(arr.length, 2, -1):
        arr.swap(1, i)
        # Zmniejszając rozmiar kopca zostawimy już posortowane elementy "w spokoju"
        arr.heapsize -= 1
        heapify(arr, 1)

#
# Złożoność obliczeniowa: pętla wywołuje się Theta(n) razy, każde wywołanie heapify ma złożoność O(lgn), więc złożoność
# heapsort wynosi O(n*lgn). 
# Złożoność pamięciowa to O(1), czyli sortowanie następuje w miejscu.
#
# Ze względu na operacje swap, sortowanie to nie jest stabilne.
# =================================================================================================

# =================================================================================================
# 5. Sortowanie szybkie:
# Quick sort to jeden z najpopularniejszych algorytmów do sortowania. Choć ma taką samą złożoność obliczeniową w przeciętnym
# przypadku co merge sort oraz heap sort, a pesymistyczną złożoność nawet O(n^2), to ze względu na stałe czynniki jest on i tak
# w praktyce najszybszy z nich. Sortowanie szybkie działa w ten sposób, że dzieli tablicę arr[i...j] na dwie podtablice
# arr[i...q-1] oraz arr[q+1...j] tak, że wszystko w pierwszej z nich jest mniejsze niż arr[q], a wszystko w drugiej z nich jest
# większe niż arr[q]. Ze względu na to, że przestawia on elementy na bierządzo w trakcie wykonywania tej partycji, to nie jest
# konieczne by te dwie podtablice łączyć, gdyż są one już posortowane. Partycjonowanie można zrobić na wiele sposobów, dwa z 
# najpopularniejszych to partycja Lomuto oraz Hoare. Hoare był pierwszy ze swoim pomysłem, jego procedura jest szybsza od Lomuto, 
# lecz nieco trudniejsza w zaimplementowaniu. Wpierw zajmiemy się procedurą dzielącą Lomuto. 
#
# Załóżmy, że mamy partycjonowania podtablicę arr, niech będzie arr[p,r]. Partition Lomuto działa ona na tej 
# zasadzie, że trzyma dwa indeksy, 'i' oraz 'j', które dzielą tablicę na trzy części:
# - arr[p...i]: elementy mniejsze niż pivot
# - arr[i+1...j-1]: elementy większe niż pivot
# Gdzie pivot jest tym elementem rozgraniczającym, który może zostać losowo wybrany. Na ten moment niech to będzie ostatni element
# tablicy arr[p...r], więc arr[r]. Jest to w zasadzie niezmiennik pętli, ale do tego dojdziemy za jakiś czas. 
# Zaczynamy partycjonowanie od ustawienia 'i' przed pierwszym elementem, oraz 'j' na pierwszym elemencie. Idziemy z indeksem j
# w pętli aż dojdziemy do przedostatniego elementu, gdyż pivota nie będziemy porównywać. W trakcie przejścia po naszej pętli będziemy
# dokonywać wyboru:
# - arr[j] <= pivot: aktualnie sprawdzany element jest mniejszy od pivota, w takim wypadku należy przesunąć indeks i o kolejne miejsce,
# tym samym zaznaczając większy obszar w tablicy, a następnie zamienić arr[i] z arr[j]. Dlaczego następuje zamiana? Rozważmy
# dwa scenariusze:
#   a) arr[i...j] pusta, jeszcze nie znaleźliśmy elementów większych od pivota, zamiana nic nie robi, bo i=j
#   b) arr[i+1...j] ma k elementów, które są większe od pivota. Po zwiększeniu indeksu 'i', będzie on wskazywał na pierwszy element z
# tej podtablicy, więc robiąc zamianę wstawiamy arr[j] (które jest mniejsze od pivota) w do tablicy arr[p...i], a ten pierwszy
# większy element idzie do sekcji, która ma już przetworzone elementy większe od pivota.
# - arr[j] > pivot: wtedy nie robimy nic, po prostu powiększa się podtablica arr[i+1...r].
#

def partition_lomuto(arr, p, r):
    # Tablica jednoelementowa jest już posortowana
    pivot = arr[r]
    i = p-1
    # Idziemy z j aż do r-1
    for j in range(p, r):
        if arr[j] <= pivot:
            i += 1
            arr.swap(i,j)
    arr.swap(i+1, r)
    # Na zakończeniu mamy tablicę arr[p...i] <= pivot, arr[i+1] to pivot,
    # a arr[i+2...r] >= pivot. Zwracamy pivot.
    return i+1

def quick_sort(arr, p, r):
    # Tablica jednoelementowa jest już posortowana 
    if p < r:
        # Podział tablicy na arr[p...q-1] i arr[q+1...r]
        q = partition_lomuto(arr, p, r)
        quick_sort(arr, p, q-1)
        quick_sort(arr, q+1, r)

#
# Złożoność obliczeniowa: procedura dzieląca Lomuto ma złożoność liniową, gdyż posiada jedną pętle wykonującą się Theta(n) razy,
# a w tej pętli działania zajmują O(1) czasu. Działa ona w miejscu. Quick sort ma złożoność obliczeniową różną w zależności od przypadku:
#
# - Jeśli dostaniemy podziały, które są względnie równomierne, my założymy optymistyczny scenariusz, to wtedy nasz algorytm opisuje
# relacja rekurencyjna T(n) = 2*T(n/2) + Theta(n) = Theta(n*lgn). 
#
# - W pesymistycznym przypadku jest jednak inaczej, gdyż mamy równanie rekurencyjne 
#               T(n) = T(n-1) + O(1) + Theta(n) = T(n-1) + Theta(n) 
# Nietrudno to rozwiązać, choćby metodą podstawiania, albo za pomocą indukcji. Asymptotyczne ograniczenie tej relacji to Theta(n^2). 
# 
# Warto jednak nadmienić, że dla każdego skończonego stosunku podziału na te dwie podtablice, otrzymamy równanie typu 
#                   T(n) = T(k*n) + T((1-k)*n) + Theta(n), gdzie k należy do (0,1) 
# które asymptotycznie rozwiązuje się T(n) = O(n*lgn). Dla przeciętnego przypadku występuje raz pesymistyczny podział, raz 
# optymistyczny, ale w efekcie się to równoważy i otrzymujemy T(n) = O(n*lgn). Przykładem danych wejściowych zwracających pesymistyczny 
# przypadek jest posortowana tablica.
#
# Dowód poprawności procedury dzielącej Lomuto poprzez niezmiennik pętli:
# Na początku każdej iteracji pętli for, podtablica arr[p...i] zawiera elementy mniejsze od pivota, podtablica arr[i+1...j-1]
# elementy większe od pivota, natomiast podtablica arr[j...r-1] nieprzetworzony jeszcze fragment tablicy.
# - Inicjalizacja: przed pierwszą iteracją i = p-1, j = p. Podtablice arr[p...p-1] oraz arr[p...p-1] są puste, więc spełniają 
# niezmiennik pętli. Podtablica arr[p...r-1] zawiera nieprzetworzone elementy. Wszystko się zgadza.
# - Utrzymanie: mamy do rozpoznania dwa scenariusze. Albo przetwarzany element (arr[j]) jest <= od pivota, albo większy.
#   a) arr[j] <= pivot: inkrementujemy 'i' przez co wskazuje na pierwszy element z podtablicy większych od pivota, wykonujemy
# swap dzięki czemu nowy arr[i] jest mniejszy <= od pivota, a arr[j] jest > od pivota. Inkrementacja 'j' przywraca niezmiennik, bo
# po niej znów arr[i+1...j-1] ma same elementy większe od pivota.
#   b) arr[j] > pivot: nie robimy nic, dalej arr[p...i] jest <= pivot (nic się nie zmieniło), natomiast inkrementacja 'j' sprawia, że
# na nowo przed kolejną iteracją arr[i+1...j-1] jest > pivot.
# - Zakończenie: na końcu pętli j = r, więc arr[p...i] wciąż ma elementy mniejsze od pivota, arr[i+1...j-1] = arr[i+1...r-1] ma
# elementy większe od pivota.
# Na końcu algorytmu zamieniamy element arr[i+1] z arr[r], co w efekcie daje nam to, czego oczekiwaliśmy.
#
# Teraz możemy pochylić się nad pierwotną procedurą dzielącą, czyli procedurą Hoare. Działa ona w ten sposób, że wybieramy pivot,
# choć tutaj nie jest on zazwyczaj na końcu, a na początku tablicy. Ustawiamy dwa wskaźniki, i = p-1 oraz j = r+1. Następnie
# wchodzimy w nieskończoną pętlę, która wyposażona jest w mechanizm wymieniania elementów tablicy aż do momentu, gdy mamy
# podział na elementy >= od pivotu, oraz <= od pivotu. Jak się znajduje taki podział? Jest to paradoksalnie bardzo proste, poruszamy
# wskaźnikami 'i' oraz 'j' tak, aby szły do siebie. Jeśli arr[j] <= pivot, wtedy szukamy arr[i] >= pivot, a następnie wymieniamy
# te dwa elementy za sobą. W efekcie mamy arr[p...i] <= pivot oraz arr[j...r] >= pivot. Zamieniamy te elementy, przy jednym
# założeniu - takim, że i < j. W przeciwnym wypadku należy zwrócić j jako punkt rozgraniczający te dwie podtablice. 
#

def hoare_partition(arr, p, q):
    while True:
        i = p-1, j = q+1
        pivot = arr[p]
        # Znajdź indeksy i,j
        while True:
            j -= 1
            if arr[j] <= pivot:
                break
        while True:
            i += 1
            if arr[i] >= pivot:
                break
        # Jeśli nie spartycjonowaliśmy całej tablicy, to i < j. 
        # Zamieniamy elementy ze sobą znów mając arr[p...i] <= pivot
        # oraz arr[j...r] >= pivot
        if i < j:
            arr.swap(i,j)
        else:
            return j

def hoare_quick_sort(arr, p, r):
    if p < r:
        q = hoare_partition(arr, p, r)
        # Nie jest to błąd, ze względu na sposób partycjonowania Hoare
        # musimy tutaj wywołać quick sort w taki sposób
        hoare_quick_sort(arr, p, q)
        hoare_quick_sort(arr, q+1, r)

#   
# Złożoność pamięciowa: quick sort z jednej strony jest sortowaniem w miejscu, gdyż nie alokujemy pamięci proporcjonalnej do rozmiaru
# danych, natomiast z drugiej strony rozmiar stosu wywołań rekurencyjnych jest tutaj równy O(lgn), więc można to potraktować jako
# złożoność pamięciową.
#
# Nie jest to algorytm sortujący stabilnie.
#
# Aby zadbać o to, by zminimalizować ryzyko obcowania z pesymistycznym scenariuszem, możemy uzbroić algorytm quick sort w prostą 
# modyfikację - wystarczy zamiast pivotu na końcu tablicy (bądź na początku, dla Hoare) wybrać losowy pivot, a następnie wstawić go
# na odpowiednie dla funkcji partycjującej miejsce. W ten sposób sprowdzimy szansę na O(n^2) do marginalnie niskiej.
# =================================================================================================

# =================================================================================================
# 6. Sortowania niewykorzystujące porównań:
# Na wykładzie wykazano, że jeśli dane sortowanie wykorzystuje porównania, to najbardziej optymalny czas w jakim może wykonać swoją
# pracę jest asymptotycznie równy O(n*lgn). Da się to udowodnić korzystając z tzw. drzew decyzyjnych, ale nie będę tutaj tego
# przepisywał, dowód nie jest trudny, ale raczej mało istotny, jest na wykładzie o quick sort.
#
# Są jednak nawet bardzo proste algorytmy, które sortują tablicę n elementów w czasie O(n). Problem tylko jest taki, że zajmują one
# znacznie więcej pamięci. Omówię w skrócie kilka z takich algorytmów:
#
#   a) Sortowanie przez zliczanie (counting sort):
# Counting sort jest algorytmem, który wpierw zlicza w pomocniczej tablicy ile razy wystąpił dany element, a następnie w tej ustawia
# pomocniczą tabelę tak, że C[i] to liczba wystąpień liczby 'i', lub mniejszej. Następnie do tablicy wynikowej wstawia elementy
# na odpowiednie miejsca. Łatwiej to sobie wyobrazić na przykładzie:
# - Weźmy, przykładowo, że nasza tablica z danymi wejściowymi wygląda tak: A = [4,3,5,5,1,3,2], n = 7. 
# - Teraz stwórzmy pomocniczą tablicę C, taką, że spełnia wartość wymienioną powyżej:
# C = [0,1,2,4,5,7], ponieważ C jest 0-indexed oraz np. liczba 4 wystąpiła jeden raz i była poprzedzona czterema liczbami (1,2,3,3).
# - Teraz powstaje pytanie: gdzie należy wstawić tę liczbę w wynikowej tablicy B[1...n]? Wstawimy ją na miejscu 5, ponieważ ma cztery
# liczby, które są przed nią, jak mówi tablica C. Ważne jest aby pamiętać, by później w tablicy zdekrementować liczność liczb <=
# tej czwórce, gdyż gdyby pojawiła się następna czwórka, to chcemy ją wstawić o jedno miejsce niżej. 
#

# B to pomocnicza tablica, już dla nas zaalokowana, k to
# zakres kluczy: {0,1,2,...,k}
def counting_sort(arr, B, k):
    n = arr.length
    # Inicjalizacja C[0...k], same zera
    C = []
    for i in range(0, k+1):
        C[i] = 0
    # Wypełnienie C, pierwszy etap, liczności pojedynczych elementów
    for i in range(1, n+1):
        C[arr[i]] = 0
    # Wypełnienie C, drugi etap, liczność elementów <= od danego
    for i in range(1, k+1):
        C[arr[i]] += C[arr[i-1]]
    
    # Wstawienie elementu na odpowiednie miejsce, dekrementacja liczności
    for i in range(n, 1, -1):
        elem = arr[i]
        B[C[elem]] = elem
        C[elem] -= 1

#
# Złożoność obliczeniowa tego algorytmu to O(k + n + k) = O(n) gdy k = O(n). 
# Złożoność pamięciowa to O(n+k) = O(n) dla tego samego założenia. Nie działa w miejscu oczywiście.
# Algorytm jest stabilny.
#
#   b) Sortowanie pozycyjne (radix sort):
# Sortowanie pozycyjne jest również bardzo prostym algorytmem. Jeśli dysponujemy kluczami, które są d-cyfrowymi liczbami całkowitymi
# to radix sort na tym, by wpierw posortować liczby po cyfrach jedności, później po dziesiątek itd. Warunkiem koniecznym jest aby
# sortowanie którego używamy na każdej pozycji było stabilne, inaczej radix sort nie ma prawa działać.
#

def radix_sort(arr, d):
    # Zakładamy, że pozycja 1 to cyfra jedności,
    # 2 to cyfra dziesiątek itd.
    for i in range(1, d):
        arr.positionsort(position = i)

#
# Przeanalizujmy złożoności obliczeniowe i pamięciowe, gdy korzystamy z sortowania przez zliczanie dla każdej pozycji klucza.
# Złożoność obliczeniowa: sortujemy 'd' razy tablicę, której klucze są zakodowane w alfabecie o 'k' znakach, więc mamy 'k' możliwości
# dla każdego elementu. Długością tablicy jest 'n', więc ostatecznie złożoność to Theta(d*(n+k)) = Theta(n), bo d-stała, k=O(n).
# Złożoność pamięciowa: O(n), tak jak w counting sort.
# =================================================================================================