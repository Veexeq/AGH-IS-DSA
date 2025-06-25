# =================================================================================================
# Wstęp / podsumowanie:
# 
# Grafy można zaimplementować na przynajmniej dwa sposoby - listy sąsiedztwa i macierz sąsiedztwa. Listę
# sąsiedztwa konstruujemy w taki sposób, że dla każdy wierzchołek grafu ma swoją listę, na której znajdziemy
# wierzchołki z którymi jest bezpośrednio połączony. Macierz sąsiedztwa działa tak, że dla każdego wierzchołka
# mamy wiersz tabeli 2D, gdzie kolumnami są 0 lub 1, w zależności od tego, czy jest on połączony z danym 
# innym wierzchołkiem. Przykładowo, arr[i,j] = 1 oznacza, że wierzchołek i jest połączony z j, czyli mówiąc
# precyzyjniej, istnieje krawędź miedzy wierzchołkami 'i' oraz 'j'. Graf symbolicznie możemy zapisać jako
# para zbiorów wierzchołków, oraz krawędzi (G = (V,E)). Będzie to przydatne przy obliczaniu złożoności, gdyż
# jeśli naszym inputem jest graf, to nie mamy tutaj już żadnego jednego ładnego 'n', by napisać np. O(n).
#
# Listy sąsiedztwa są stosowane dla grafów rzadkich, a więc kiedy następuje warunek |E| << |V|^2.
# Macierz sąsiedztwa jest stosowana dla grafów gęstych, czyli gdy |E| ~ |V|^2.
# Jeśli graf jest ważony (każda krawędź ma wagę i załóżmy, że jest ona nieujemna) to wagi są przechowywane 
# w tych strukturach danych. Dla list sąsiedztwa nie przechowujemy tylko wierzchołków, ale parę wierzchołek + waga,
# a dla macierzy sąsiedztwa jedną z możliwych implementacji jest taka, by przechowywać wagi > 0 zamiast jedynek 
# (oznacza to, że istnieje krawędź), a gdy krawędzi nie ma, pozostajemy przy 0. 
#
# Grafy mogą być skierowane, bądź nieskierowane. Oprócz oczywistej różnicy widocznej na pierwszy rzut
# oka, różnią się one równeż w złożoności pamięciowej. 
# - Graf skierowany: ma liczność wszystkich krawędzi |E|, wierzchołków jest |V|, więc reprezentacja listowa (tablica
# wierzchołków zawierająca listy krawędzi) ma złożoność O(V+E). 
# - Graf nieskierowany: ma liczność wszystkich krawędzi 2|E|, wierzchołków jest |V|, więc idąc poprzednim tokiem
# rozumowania złożoność wynosi O(V+2E), lecz pomijamy stałe, więc wychodzi również na O(V+E).
# Oba przypadki mają tę samą złożoność obliczeniową dla reprezentacji macierzowej i wynosi ona Theta(V^2).
# Jak widać, implementacje listowe są ograniczone tylko od góry, bo przy małej ilości krawędzi możemy zejść o 
# poziom niżej w wymaganej pamięci, natomiast reprezentacja macierzowa ma ścisłe ograniczenie - od góry i od dołu.
#
# Algorytmy jakie omawialiśmy na grafach to:
# 1. Algorytmy przechodzenia po grafach: BFS, DFS
# 2. Sortowanie topologiczne
# 3. Wyznaczanie silnie spójnych składowych (strongly connected components)
# 4. Minimalne drzewo rozpinające (minimum spanning tree), algorytm Kruskala, Prima
# 5. Las zbiorów rozłącznych (nie algorytm, a struktura danych dla zbiorów rozłącznych)
# 6. Najkrótsze ścieżki z jednym źródłem, algorytm Bellmana-Forda, Dijkstry
# 7. Najkrótsze ścieżki między wszystkimi parami wierzchołków, algorytm Floyda-Warshalla
# =================================================================================================

# =================================================================================================
# 1. Przechodzenie po grafach:
#
# Przechodzenie grafu można zrobić z dowolnego wierzchołka tej struktury. Drzewa, to również grafy, lecz tam mieliśmy
# wyróżniony punkt startowy (korzeń) z którego zazwyczaj zaczynaliśmy nasze przejście. W ogólności jest inaczej, możemy
# obrać sobie dowolny punkt startowy i z poziomu tego wierzchołka rozpocząć przechodzenie. Załóżmy, że wybieramy wyróżniony
# wierzchołek 's' - jest to od teraz tzw. źródło grafu. Możemy teraz ten graf przejść na dwa sposoby.
#
#   a) BFS (breadth-first-search), przeszukiwanie wszerz:
# BFS to algorytm, który przechodzi graf "layer-by-layer". Zasadniczą rolę pełni tutaj odległość wierzchołka od źródła, gdyż
# aby odwiedzić wierzchołek oddalony o k krawędzi od 's', musimy wpierw odwiedzić wszystkie wierzchołki znajdujące się w
# odległości k-1. Intuicyjnie działa to tak: zaznacz wszystkie wierzchołki sąsiadujące z 's' i je wypisz. W miarę wypisywania
# zaznaczaj wszystkie wierzchołki osiągalne z tego wierzchołka. Gdy wypiszemy wszystkie wierzchołki z danego poziomu, zaczynamy
# wypisywać (bądź operować w dowolny inny sposób, wypisywanie jest najprostrzym przykładem) wierzchołki z następngo. Jak
# można się domyślić, rozsądnym pomysłem jest by wprowadzić kolejkę i dodawać do niej wierzchołki z następnych poziomów.
# Na tym też opiera się algorytm BFS. Pozostaje jeszcze jedna bardzo ważna kwestia - grafy w ogólności mogą być dowolnie połączone,
# więc może nadarzyć się sytuacja, że wierzchołek o odległości 5 jest połączony z wierzchołkiem o odległości 2. Nie chcemy
# ponownie wypisywać już wcześniej wypisanego wierzchołka, więc należy trzymać informacje o stanie przetworzenia każdego z nich.
# Posłużymy się kolorami - biały wierzchołek jest jeszcze nieodwiedzony, szary wierzchołek jst odwiedzony a czarny wierzchołek
# jest przetworzony (unvisited, visited, explored). Jeśli z szarego wierzchołka trafimy na biały, to kolorujemy go na szaro. Jeśli
# z szarego wierzchołka trafimy na czarny, to wiemy, że jest on już odwiedzony. Szary oznacza, że aktualnie pracujemy na danym
# wierzchołku, jest on w trakcie przetwarzania. Kolor zmienia się w czarny, gdy już wszyscy sąsiedzi zostani dodani do kolejki.
#

# BFS oparty na liście sąsiedztwa, każdy wierzchołek ma rodzica, dystans oraz kolor
def BFS(G, s):
    # Przygotuj wierzchołki - oznacz jako nieodwiedzone
    for node in G.V - s:
        node.colour = 'WHITE'
        node.distance = 'INF'
        node.parent = 'NIL'
    
    # Odwiedź źródło
    s.colour = 'GRAY'
    s.distance = 0
    s.parent = 'NIL'

    Q = create_queue()
    ENQUEUE(Q, s)

    while Q.empty != True:
        u = DEQUEUE(Q)
        # Dla każdego sąsiada 'v' z listy 'u'...
        for v in u.neighbors:
            # ...jeśli jest nieodwiedzony, odwiedź
            if v.colour == 'WHITE':
                v.colour = 'GRAY'
                v.distance = u.distance + 1
                v.parent = u
                ENQUEUE(v)
        # Zakończ przetwarzanie aktualnego wierzchołka
        u.colour = 'BLACK'

# Atrapy funkcji, aby interpreter się nie czepiał w IDE że piszę pseudokod w Pythonie
def create_queue():
    return
def ENQUEUE():
    return
def DEQUEUE():
    return

#
# Dowód poprawności algorytmu BFS możemy przeprowadzić poprzez niezmiennik pętli while. Jest on następujący:
# Na początku każdej iteracji pętli while, kolejka Q posiada wszystkie odwiedzone wierzchołki, czekające na przetworzenie.
# - Inicjalizacja: Przed pierwszą iteracją w Q jest tylko szare źródło
# - Utrzymanie: Podczas każdej iteracji dodajemy nowe wierzchołki pokolorowane na szaro. Jedynym szarym wierzchołkiem pozostaje
# usunięty z kolejki w linijce 81 'u'. Przywracamy niezmiennik poprzez pokolorowanie go na czarno - ponownie wszystkie szare
# wierzchołki znajdują się w kolejce.
# - Zakończenie: Po przetworzeniu ostatniego wierzchołka z kolejki jest ona pusta, nie ma już żadnych wierzchołków do przetworzenia.
#
# Złożoność obliczeniowa: Każdy wierzchołek raz dodajemy i usuwamy z kolejki w czasie O(1), w sumie przechodzimy wszystkich listach
# sąsiedztwa, a suma długości list sąsiedztwa wynosi |E|. W efekcie dostajemy złożoność O(V+E) - liniowa złożoność zależna
# od rozmiaru implementacji listowewj grafu.
#
#   b) DFS (depth-first-search), przeszukiwanie w głąb:
# Ponownie, tak samo jak w BFS, wybieramy źródło 's' - nasz punkt startowy do przechodzenia grafu. Kolejnym podobieństwem jest
# również kwestia implementacji, gdyż znów skorzystmy z list sąsiedztwa. Mechanizm postępowania jest intuicyjnie prosty, gdyż
# to co robimy, to dla każdego sąsiada 's' idziemy coraz głębiej, na coraz wyższe odległości od naszego wierzchołka startowego.
# Poprzestajemy dopiero wtedy, gdy wierzchołek nie ma już połączonych ze sobą żadnych innych sąsiadów - wtedy następuje backtracking
# i wracamy się do wierzchołka wciąż mającego nieodwiedzonych sąsiadów. Najłatwiej jest to sobie wyobrazić na drzewach BST, wtedy
# DFS to po prostu tree-traversal. Z grafami jest już trudniej, gdyż możemy napotkać różne scenariusze, które należy odróżnić.
#
# Aby to zrobić, nasze wierzchołki będą opisywane dodatkowymi metrykami. W BFS mieliśmy ich kolor, rodzica oraz odległość
# od źródła, w DFS natomiast będziemy mieli kolor, rodzica oraz czas odwiedzenia, a także czas przetworzenia. Etykiety czasowe
# będą należały do zbioru {1,2,...,2|V|} i czas odwiedzenia będzie zawsze mniejszy niż czas przetworzenia. Dlaczego to wszystko 
# robimy? Omówię to za chwilę, na razie jednak skupmy się na tym, jak powinien wyglądać sam algorytm, ustalmy kolorowanie.
#
# Zaczynamy od źródła, kolorujemy je na szaro i czas jego odwiedzenia ustawiamy na 1. Dla każdego sąsiada tego wierzchołka, jeśli
# tylko kolor sąsiada jest biały, więc nie jest już częscią pewnej ścieżki odwiedzonych węzłów, ustawiamy rodzica sąsiada na węzeł
# 's' i wywołujemy na nim DFS. Rekurencja dalej będzie następować, ale aby sobie to łatwiej wyobrazić, możemy powiedzieć, że po jej
# wykonaniu przeszliśmy maksymalnie w głąb dla tego konkretnego sąsiada - tamta część jest już przetworzona. Po powtórzeniu tego
# dla każdego sąsiada, możemy powiedzieć, że 's' jest przetworzone, więc ustawiamy jego kolor na czarny, ustawiamy też odpowiednio
# czas przetworzenia. W skrócie: dla każdego sąsiada wierzchołka o białym kolorze przejdź jego podgraf w głąb, a następnie oznacz
# wierzchołek za przetworzony. 
#
# Jest jeszcze jedna bardzo istotna różnica względem BFS. W przechodzeniu grafu wszerz ustaliliśmy źródło odgórnie i od niego
# rozpoczęliśmy przejście. W przypadku DFS zazwyczaj zakładamy, że graf nie musi być spójny, więc ze względu na przyszłe aplikacje
# tego algorytmu, przyjęło się, że wywołujemy go na każdym białym wierzchołku. Co to znaczy? Załóżmy, że mamy graf podzielony na 
# trzy spójne podgrafy. Wpierw przejdziemy po grafie pierwszym, następnie pominiemy wszystkie wierzchołki w tym grafie (nie przechodzimy
# go dwa razy, gdyż ma już wszystkie czarne wierzchołki) więc robimy w efekcie DFS na drugim podgrafie, później na trzecim. W ten
# sposób przejdziemy cały graf. 
# 

time = 0

def DFS(G):
    # Przygotowanie wierzchołków
    for node in G.V:
        node.colour = 'WHITE'
        node.parent = 'NIL'

    # Zadbanie o odwiedzenie każdej składowej grafu, w razie gdyby
    # był on niespójny.
    for node in G.V:
        if node.colour == 'WHITE':
            DFS_VISIT(node)

# Główna funkcja, 'prawdziwe' przechodzenie
def DFS_VISIT(node):
    # Rozpocznij pracę na węźle
    node.colour = 'GRAY'
    time += 1
    node.visit_time = time
    
    # Przejdź w głąb na każdym białym sąsiedzie, ustaw relację dziecko-rodzic
    for neighbor in node.neighbors:
        if neighbor.colour == 'WHITE':
            neighbor.parent = node
            DFS_VISIT(neighbor)

    # Zakończ pracę na tym wierzchołku
    node.colour = 'BLACK'
    time += 1
    node.finish_time = time

#
# Złożoność obliczeniowa tego algorytmu: w funkcji DFS mamy pętlę idącą po każdym wierzchołku należącym do grafu, więc 
# mamy już Theta(V). Efektem wykonania całej pętli jest przejście po każdej krawędzi, a że jest ich |E|, to sumarycznie
# poświęcamy na to Theta(E) czasu. Wniosek jest taki, iż złożoność obliczeniowa DFS to Theta(V+E).
#
# Teraz możemy wrócić do napoczętego wcześniej tematu różnych przypadków związanych z przechodzeniem grafu w głąb. Zaczniemy
# od zauważenia, iż dla wierzchołka 'u' czasy u.visit_time oraz u.finish_time mają strukturę nawiasową. Co to znaczy? Jeśli
# wyobrazimy sobie standardową oś czasu biegnącą w prawo, to będzie to wyglądało mniej więcej tak: (u... ...u), gdzie "(u"
# oznacza czas odwiedzenia, a "u)" oznacza czas zakończenia. Załóżmy teraz, że nasz graf wygląda tak:
#
#   A ----> B                                                                       
#   |       |   DFS daje następujące czasy odwiedzenia i przetworzenia:          Nowo powstałe drzewo DFS:
#   |       |   A(1,8), B(2,5), C(3,4), D(6,7)                                             A
#   |       |                                                                             / \
#   |       |   To z kolei przekłada się na strukturę nawiasową:                         B   D
#   |       |    1  2  3 4  5   6 7  8                                                  /
#   v       v   (A (B (C C) B) (D D) A)                                                C
#   D ----- C
#
# Teraz, mając już intuicję stojącą za strukturą nawiasową, a także widzimy jak powstaje drzewo DFS (analogicznie jak BFS),
# możemy zrozumieć twierdzenie, które pomoże nam sklasyfikować krawędzie w grafie. Mówi ono, że dla każdej pary wierzchołków 
# (u,v), mogą nastąpić trzy scenariusze:
# - (u...u) oraz (v...v) są całkowicie rozłączne
# - (v...v) jest całkowicie zagnieżdżone w (u...u) oraz v jest potomkiem u w drzewie (niekoniecznie bezpośrednim)
# - (u...u) jest całkowicie zagnieżdżone w (v...v) oraz u jest potomkiem v w drzewie (niekoniecznie bezpośrednim)
# 
# Przechodzimy do klasyfikacji krawędzi. Wyobraźmy sobie, że przeprowadzamy zwykły DFS. Jeśli napotykamy biały wierzchołek, to 
# jest to "krawędź drzewowa", najczęstsza, tworząca drzewo DFS. Jeśli napotkamy na szary wierzchołek, to jest to krawędź powrotna,
# czyli taka, że znów trafilibyśmy na tę samą ścieżkę. Jeśli trafimy na czarny kolor, to powstają dwa scenariusze:
# - jeśli u.visit_time < v.visit_time, to najpierw odwiedziliśmy wierzchołek 'u', z jego poziomu zakończyliśmy przetwarzanie 'v',
# a teraz ponownie odwiedzamy 'v', bezpośrednio z 'u'. Krawędź (u,v) nazywamy "krawędzią w przód".
# - jeśli u.visit_time > v.visit_time, to znaczy, że jest też prawdziwe u.finish_time > v.visit_time. Wniosek jest taki, że
# przetworzyliśmy już węzeł v, a więc także cały podgraf z nim związany. Oznacza to, że w drzewie DFS ten wierzchołek znajduje się w 
# innym poddrzewie, więc krawędź (u,v) nazywamy "krawędzią poprzeczną".
# Najłatwiej jest to zobaczyć patrząc na drzewo DFS, tam jasno widać, która krawędź byłaby "w przód", która "powrotna",
# a krawędzie "poprzeczne" to krawędzie (u,v) w sytuacji, gdy 'v' nie jest potomkiem 'u' - należy do innego poddrzewa.
# 
# Ostatnią rzeczą na temat krawędzi jest twierdzenie dotyczące sytuacji, gdy mamy do czynienia z grarfem nieskierowanym:
# Wykonując DFS na grafie nieskierowanym, każda krawędź będzie albo drzewowa, albo powrotna.
# =================================================================================================

# =================================================================================================
# 2. Sortowanie topologiczne:
# Sortowanie topologiczne dotyczy grafów skierowanych acyklicznych. Polega to na tym, że sprowadzamy wszystkie krawędzie
# tego grafu do jednej linii prostej. Jeśli w grafie występuje krawędź (u,v), to wierzchołek 'u' musi być na liście 
# wynikowej sortowania topologicznego ustawiony przed wierzchołkeim 'v'. Przykładem zastosowania grafów skierowanych
# acyklicznych jest określanie kolejności wykonywania czynności (zrób A przed B, C przed A, D wymaga zrobienia wcześniej 
# A i C itd...), więc sortowanie topologiczne będzie tu bardzo przydatne - określi co należy wykonać przed każdą jedną czynnością.
#
# Algorytm sortowania topologicznego jest wbrew pozorom niezwykle prosty, gdyż skorzystamy ze zdefiniowanych uprzednio
# czasów przetworzenia danych wierzchołków. Jeśli bowiem wierzchołek kolorujemy na czarno, czyli jest on przetworzony, to nie 
# ma z jego poziomu żadnych krawędzi do innych wierzchołków, które mogłyby od niego "zależeć", jeśli kontynuujemy motyw ustawiania 
# czynności w odpowiedniej kolejności. Cały algorytm polega na tym, aby wykonać DFS na grafie, a gdy przetworzymy już jakiś wierzchołek,
# to dodajemy go na początek listy. Tak więc pierwszzy przetworzony wierzchołek (od którego nic dalej nie zależy) wyląduje na
# samym końcu, a źródło grafu (jeśli oczywiście będzie spójny) będzie na samym początku, gdyż wszystko od niego zależy.
#

time = 0

def topological_sort(G):
    # Tutaj wszystko tak, jak w DFS
    for node in G.V:
        node.colour = 'WHITE'
        node.parent = 'NIL'

    # Lista wierzchołków, wynik sortowania
    res = []

    for node in G.V:
        if node.colour == 'WHITE':
            DFS_TOPO_VISIT(node, res)

    return res

def DFS_TOPO_VISIT(node, res):
    node.colour = 'GRAY'
    time += 1
    node.visit_time = time
    
    # Bazujemy na liście sąsiedztwa
    for neighbor in node.neighbors:
        if neighbor.colour == 'WHITE':
            neighbor.parent = node
            DFS_TOPO_VISIT(neighbor, res)
    
    node.colour = 'BLACK'
    time += 1
    node.finish_time = time

    # Różnica względem normalnego DFS_VISIT, dodajemy na początek listy
    res.insert(0, node)

#
# Złożoność obliczeniowa tego algorytmu jest taka sama jak w przypadku DFS, czyli Theta(V+E). Złożoność
# pamięciowa to długość nowo utworzonej listy, więc Theta(V).
# =================================================================================================

# =================================================================================================
# 3. Silnie spójne składowe:
# Silnie spójna składowa (strongly connected component) to podzbiór wierzchołków taki, że dla każdej pary wierzchołków (u,v)
# możemy przejść po grafie zarówno z wierzchołka u do v, jak i na odwrót. Podział grafu na silnie spójne skłaadowe to podstawowe
# zagadnienie, często będące jednym z pierwszch kroków w bardziej zaawansowanych algorytmach grafowych. Z samej definicji wynika, że
# podział na silnie spójne składowe, tak samo jak sortowanie topologiczne, dotyczy grafów skierowanych (ale nie acyklicznych jak w topo).
# Aby zająć się znajdowaniem silnie spójnych składowych, wpierw musimy zrozumieć czym jest transpozycja grafu. Jest to bardzo
# proste zagadnienie, gdyż wykonując transpozycję po prostu zamieniamy kolejność krawędzi, czyli z krawędzi (u,v) robi się (v,u).
# Silnie spójne składowe są niezmiennicze ze względu na transpozycję, czyli transpozycja nie modyfikuje silnie spójnych składowych.
# Aby znaleźć silnie spójnie składowe należy w zasadzie wykonać trzy kroki:
#
# - Wykonaj DFS, ponieważ będziemy potrzebować czasu przetworzenia każdego węzła
# - Transponuj graf
# - Wykonaj DFS na grafie transponowanym, lecz w pętli w algorytmie DFS (nie DFS_VISIT) gdzie idziemy po wszystkich wierzchołkach,
# idź po wierzchołkach od największego do najmniejszego czasu przetworzenia. Przed rozpoczęciem kolejnej iteracji tej głównej pętli
# w DFS, czyli na końcu aktualnej iteracji nasz zbiór wierzchołków przetworzonych przez DFS_VISIT to SCC.
# 
# Dlaczego to działa? Z twierdzenia, które mówi o niezmienności SCC ze względu na transpozycje wiemy na pewno, że po transpozycji
# wciąż uda nam się przejść po wszystkich wierzchołkach danej składowej. Czego się jednak nie uda, to wyjść poza nią, dlatego, że
# jeśli w grafie G mieliśmy "wyjście" z danej silnie spójnej składowej, to w grafie G^T to wyjście zamieniło się na "wejście", więc
# nie uda nam się wyjść poza silnie spójną składową. Idziemy w kolejności od największego czasu przetworzenia, bo to oznacza, że
# jesteśmy w najgłębszym miejscu dla danej silnie spójnej składowej.
# 
#             A ---> B ---> E                     A <--- B <--- E
#             ^      |           Transpozycja     |      ^
#             |      v             ======>        v      |
#             D <--- C                            D ---> C 
#
# W powyższym przykładzie mamy dwie SCC, zbiór C_1 = {A,B,C,D} oraz zbiór C_2 = {E}. Oba to podzbiory V.
# Złożoność obliczeniowa algorytmu szukającego silnie spójnych składowych to Theta(V+E), gdyż wykorzystujemy DFS, który ma 
# właśnie taką złożoność obliczeniową. Poprawność algorytmu jest wykazywana indukcyjnie. Jeśli się nie mylę, to zamysł jest taki,
# że jeśli jedno drzewo DFS dla grafu G^T tworzy silnie spójną składową, to każde drzewo DFS obliczone w kroku wykonywania DFS na 
# G^T tworzy silnie spójną składową.
# =================================================================================================

# =================================================================================================
# 4. Minimalne drzewo rozpinające (minimum spanning tree):
# Minimalne drzewo rozpinające to klasyczny problem / algorytm grafowy. Mamy dany graf G(V,E), który ma n wierzchołków, jest 
# skierowany, a jego krawędzie mają wagi. Chcemy znaleźć minimalne drzewo rozpinające (MST), które łączy wszystkie n wierzchołków
# używając minimalnej liczby krawędzi (n-1) o minimalnej sumarycznej wadze. Tych drzew może być kilka, jeśli jest kilka wariantów
# wyboru tych krawędzi, nas jednak interesuje jakieś jedno rozwiązanie. Aby stworzyć takie rozwiązanie, wpierw spójrzmy na pewien
# "generyczny" algorytm, który później uzbroimy w konkretne kryteria:
#
# - Niech A zbiorem, który będzie trzymał krawędzie minimalnego drzewa rozpinającego. Na początku A jest zbiorem pustym
# - Dopóki A nie tworzy MST:
#   - Znajdź krawędź, która jest "bezpieczna", dodaj ją do A
# 
# Co znaczy, że krawędź jest bezpieczna? Musi ona spełniać jakieś warunki, które sprawią, że dana krawędź nie zepsuje aktualnie
# tworzonego MST. Okazuje się, że istnieją takie warunki, które omówimy za chwilę. Wpierw jednak należy spojrzeć na dowód poprawności
# tego algorytmu generycznego.
#
# Niezmiennik pętli: na początku każdej iteracji pętli while, A tworzy podzbiór krawędzi z minimalnego drzewa rozpinającego
# - Inicjalizacja: przed pierwszą iteracją A jest zbiorem pustym, więc spełnione
# - Utrzymanie: niezmiennik jest zachowany, gdyż dodajemy same bezpieczne krawędzie
# - Zakończenie: zbiór A zawiera wszystkie krawędzie tworzące pewne MST
#
# Wróćmy teraz do zagadnienia bezpiecznych krawędzi. Zacznijmy od wprowadzenia pojęcia przekroju grafu. Będzie ono kluczowe
# w zrozumieniu logiki stojącą za znajdowaniem krawędzi, którą dodamy do zbioru A. Przekrojem grafu 
