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
# 