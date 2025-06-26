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
# 4.1. Las zbiorów rozłącznych (nie algorytm, a struktura danych dla zbiorów rozłącznych)
# 5. Najkrótsze ścieżki z jednym źródłem, algorytm Bellmana-Forda, Dijkstry
# 6. Najkrótsze ścieżki między wszystkimi parami wierzchołków, algorytm Floyda-Warshalla
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
# nieskierowany, a jego krawędzie mają wagi. Chcemy znaleźć minimalne drzewo rozpinające (MST), które łączy wszystkie n wierzchołków
# używając minimalnej liczby krawędzi (n-1) o minimalnej sumarycznej wadze. Tych drzew może być kilka, jeśli jest kilka wariantów
# wyboru tych krawędzi, nas jednak interesuje jakieś jedno rozwiązanie. Aby stworzyć takie rozwiązanie, wpierw spójrzmy na pewien
# "generyczny" algorytm, który później uzbroimy w konkretne kryteria:
#
# - Niech A będzie zbiorem, który trzyma krawędzie minimalnego drzewa rozpinającego. Na początku A jest zbiorem pustym
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
# w zrozumieniu logiki stojącą za znajdowaniem krawędzi, którą dodamy do zbioru A. Przekrojem grafu nazywamy podział tego grafu
# na dwa podgrafy, a precyzyjniej ujmując sprawę, podział jego wierzchołków. W efekcie tego podziału mamy dwa zbiory: S oraz V-S.
# Przekrój grafu należy sobie wyobrazić jako linię oddzielającą jedną partię wierzchołków od drugiej. Pochylmy się teraz nad
# sytuacją związaną z krawędziami:
#
# - krawędź (u,v) jest taka, że jeden wierzchołek należy do S a drugi do V-S, to krawędź krzyżuje się z przekrojem. Takie krawędzie
# nazywamy krawędziami lekkimi.
# - krawędź (u,v) jest taka, że nie krzyżuje się z przekrojem, czyli należy do jednej ze stron przekroju. Takie krawędzie mają prawo
# należeć do zbioru A (mają prawo, bo nie muszą jeszcze należeć - przypomnijmy, zbiór A to aktualny podzbiór tworzący MST). 
# Mówimy, że przekrój uwzględnia zbiór A.
#
# Teraz możemy zrozumieć następujące twierdzenie: 
# Jeśli A to podzbiór MST dla grafu G(V,E), (S,V-S) będzie dowolnym przekrojem uwzględniającym A, (u,v) będzie krawędzią lekką
# krzyżującą się z przekrojem (S,V-S), to (u,v) jest krawędzią bezpieczną.
#
# Dowód tego twierdzenia jest na wykładzie, ale trudno go tu streścić bez rysunków. Z resztą, jest on chyba nieco trudniejszy do
# zrozumienia niż inne, pewnie nie pojawi się na egzaminie. 
#
# Wnioski, jakie można wysnuć z tego twierdzenia są takie: jeśli mamy podzbiór A, który jest zawarty w MST (jeszcze go nie
# tworzy) to jest on acykliczny, więc jest on zbiorem drzew. Las drzew można przedstawić za pomocą zbioru G_A = (V,A), co ma 
# dużo sensu, bo bierzemy wszystkie wierzchołki z grafu i łączymy tylko te, które aktualnie są w A - powstawje nam las drzew.
# Jeśli weźmiemy spójną składową, czyli jedno z drzew C = (V_C,E_C), to jeśli stworzymy krawędź (u,v) łączącą drzewo C z 
# innym drzewem w lesie G_A, to (u,v) jest krawędzią bezpieczną. Jest tak dlatego, że przekrój (C, V-C) uwzględnia A. 
#
# Wracając do generycznego algorytmu MST, teraz go napiszmy w pseudokodzie:
#

# G to graf, w to funkcja wagi
def generic_mst(G, w):
    # A to zbiór pusty
    A = set()
    while A != 'MST':
        (u,v) = G.find_safe_edge(w)
        A.add(u,v)

#
# W każdej chwili działania tego algorytmu, krawędzie z A są zawsze acykliczne. G_A = (V,A) jest lasem, gdzie każda spójna składowa
# jest drzewem, choćby gdyby składały się z jednego wierzchołka (to też spójna składowa). Dodając (u,v) dalej A jest acykliczne, bo
# łączymy dwa drzewa jedną krawędzią, czyniąc z nich jedno spójne drzewo. Konkretnymi algorytmami, które zajmują się wyborem krawędzi
# (u,v) to algorytm Kruskala i algorytm Prima. Algorytm Kruskala operuje na lesie G_A, zawsze wybiera najlżejsze krawędzie łączące
# dwa drzewa. Algorytm Prima operuje na pojedynczym drzewie. Do A zawsze dodawane są krawędzie bezpieczne łączące drzewo A z 
# pozostałymi wierzchołkami spoza drzewa. Teoretycznie powinienem wpierw powiedzieć o części wykładu opisującej strukturę danych dla
# zbiorów rozłącznych (disjoint set, union find), ponieważ na tym opiera się algorytm Kruskala, lecz nie mam zbyt dużo czasu, a
# zrozumienie algorytmu Kruskala nie wymaga dokładnej znajomości, tylko raczej intuicji.
#
#   a) Algorytm Kruskala dla znajdowania MST:
#

def mst_kruskal(G, w):
    # A to zbiór krawędzi tworzących MST
    A = set()
    # G_a to las drzew z wierzchołków G.V
    G_a = set()
    # Dla każdego wierzchołka stwórz osobne drzewo rozłączne,
    # teraz G_a składa się z pojedynczych drzew rozłącznych
    for v in G.V:
        G_a.make_set(v)
    G.E.sort('increasing', w)

    # Idziemy po każdej krawędzi w kolejności rosnącej (wpierw
    # dodajemy najlżejsze krawędzie)
    for (u,v) in G.E:
        # Jeśli wierzchołki należą do różnych drzew rozłącznych
        if G_a.find_set(u) != G_a.find_set(v):
            # Aktualizuj MST oraz połącz dwa drzewa w jedno drzewo
            A.add((u,v))
            G_a.union(u,v)
    
    return A

#
# Czas działania zależy od tego, jak zaimplementujemy strukturę danych dla zbiorów rozłącznych. Sortowanie krawędzi to
# O(|E|*lg|E|). Złożoność obliczeniowa tego algorytmu jest dosyć trudna do ustalenia, więc po prostu podam wnioski:
# Złożoność obliczeniowa: O(|E|*lg|E|), a jeśli przyjmiemy, że |E| < |V|^2, to O(|E|*lg|V|)
#
#   b) Algorytm Prima dla znajdowania MST:
# 

# Nie tylko graf i funkcja wagi, ale też korzeń (wybrany dowolnie)
def mst_prim(G, w, r):
    # Najpierw ustaw wszystkie wierzchołki jako nieprzetworzone
    # Każdy wierzchołek ma atrybuty: klucz (waga krawędzi łącząca go z drzewem
    # oraz rodzica, czyli z kim ma ową krawędź)
    for v in G.V:
        v.key = 'INF'
        v.parent = 'NIL'
    # Korzeń drzewa, od niego zaczynamy
    r.key = 0
    # Q to kolejka priorytetowa typu min, korzeń jest pierwszy
    Q = []
    Q.add(G.V)

    # W kolejce Q są węzły, których jeszcze nie ma w MST
    while Q.empty != 'True':
        # Wybierz następny wierzchołek do dodania
        node = Q.extract_min
        # Zaaktualizuj każdego z jego sąsiadów...
        for neighbor in node.neighbors:
            # ...który jeszcze nie został przetworzony i krawędź łącząca aktualny
            # węzeł z tym sąsiadem jest mniejsza niż jakaś inna krawędź łącząca ten
            # wierzchołek z drzewem
            if neighbor in Q and w(node, neighbor) < neighbor.key:
                # Teraz ten sąsiad ma aktualne informacje na swój temat, ma rodzica, 
                # czyli węzeł, który łączy go z drzewem w najbardziej optymalny sposób
                neighbor.parent = node
                # Zmiana klucza tutaj aktualizuje pozycje tego wierzchołka w kolejce, być
                # może stanie się kolejnym elementem do dodania
                neighbor.key = w(node, neighbor)
    
#
# Dowód poprawności przez niezmiennik pętli:
# Niezmiennik: przed wykonaniem każdej pętli while zachodzą:
# - A = {(node, node.parent): node należy do V - {r} - Q}, czyli na MST składają się krawędzie stworzone z wierzchołków
# oraz ich rodziców zdefiniowanych w algorytmie, które nie należą do kolejki, a także nie są korzeniem (on ma rodzica 'NIL')
# - Dla każdego node należącego do Q, node.key to koszt krawędzi łączącej go z aktualnym poddrzewem MST, a node.parent to
# węzeł przez który się łączy (jeśli obie wartości istnieją, mogą jeszcze nie istnieć).
#
# Złożoność obliczeniowa algorytmu Prima: opiera się ona na kopcu binarnym, który tworzy się w czasie O(|V|), naprawia w czasie
# O(lg|V|), aktualizuje klucz w czasie O(|V|), pętlę główną mst_prim wykonujemy |V| razy. Z racji na to, że długość wszystkich
# list sąsiedztwa (które przetworzymy w pętli for) to 2|E|, to wykonanie pętli for to O(|E|). Łączny czas to:
#           O(|V|) (budowa) + O(|V|lg|V|) (|V| razy extract) + O(|E|lg|V|) (|E| razy zmiana klucza) = O(|E|lg|V|)
# Jest to asymptotycznie czas taki sam, jak w algorytmie Kruskala.
# =================================================================================================

# =================================================================================================
# 5. Najkrótsze ścieżki z jednym źródłem:
# Z racji na niewiele czasu przed egzaminem, pominę formalizm i teorię związaną z tymi zagadnieniami, a raczej ograniczę ją do
# minimum. Po pierwsze, problem znajdowania optymalnej ścieżki między dwoma wierzchołkami posiada własność optymalnej podstruktury.
# Oznacza to, że jeśli mamy ścieżkę <p_i,p_(i+1),...,p_(j-1),p_j> to każda podścieżka w niej musi być optymalna, by cała ścieżka
# była optymalna. Po drugie, wierzchołki w grafie będą miały dodatkowe atrybuty na potrzebę znajdowania ścieżek. Po pierwsze, będą
# miały klucz, który przechowuje koszt dotarcia ze źródła do danego węzła, po drugie, będą miały rodzica, czyli wierzchołek z 
# którego przyszliśmy. Jeśli już znajdziemy optymalną ścieżkę, to możemy ją wyświetlić w sposób rekurencyjny. Zaczynamy od wierzchołka
# do którego mieliśmy dojść i podejmujemy decyzję: czy jesteśmy już u źródła? Jeśli tak, to wypisz źródło. Jeśli nie, to wpierw 
# wypisz element z którego przyszliśmy, a później ten aktualny. 
#

def print_path(G, v, s):
    if v == s:
        print(s)
    elif v.parent != 'NIL':
        print_path(G, v.parent, s)
        print(v)
    else:
        print(f'Brak ścieżki z {s} do {v}')

#
# Nie musimy pochylać się nad złożonością tego algorytmu, lecz jest on oczywiście ograniczony przez długość ścieżki, czyli |V|-1.
# Dlaczego jednak długość ścieżki jest równa |V|-1? To stwierdzenie zakłada, że nie możemy mieć w grafach cyklu, czyli rozważamy
# skierowane acykliczne grafy (DAG - directed acyclic graphs). Jeśli graf miały cykl, który sumarycznie dawałby ścieżkę o ujemnej
# wadze, to zawsze moglibyśmy znaleźć "optymalniejszą" ścieżkę powiększając graf o ten cykl, więc nie rozważamy ujemnych cykli.
# Co natomiast z dodatnimi cyklami? Cóż, jeśli ze ścieżki usuniemy cykl o dodatniej długości, to uzyskamy ścieżkę, która jest bardziej
# optymalna, więc nasza najkrótsza ścieżka będzie ścieżką prostą - bez cykli.
#
# Aby znaleźć najkrótsze ścieżki z jednego źródła do każdego wierzchołka (nie tylko do jednego, takie założenie algorytmów z tego
# punktu) należy rozważyć dwa przypadki. Albo dopuszczamy krawędzie o ujemnych wagach, albo tego nie robimy. W pierwszym przypadku
# będziemy używać algorytmu Bellmana-Forda, który jest algorytmem opartym na DP. Jeśli jednak nie mamy w grafie ujemnych krawędzi,
# to okazuje się, że algorytm Dijkstry, będący algorytmem zachłannym radzi sobie z problemem wystarczająco. Oba algorytmy opierają
# się na dwóch procedurach pomocniczych: initialize_source oraz relax. Dlaczego tak jest? Wpierw musimy przygotować nasz graf do
# pracy z algorytmami, aby to zrobić inicjalizujemy źródło przy pomocy pierwszej procedury:
#

def initialize_single_source(G, s):
    for v in G.V:
        v.key = 'INF'
        v.parent = 'NIL'
    s.key = 0

#
# Jest to dosyć oczywista procedura. Na początku, gdy jeszcze nie pracowaliśmy z grafem i wszystkie wierzchołki były nierozpatrzone
# to mają wartość w kluczu 'INF', co oznacza, że nie istnieje jeszcze krawędź łącząca dany wierzchołek ze źródłem. Rodzic danego węzła
# jest równy 'NIL', co oznacza, że nie ma poprzednika z którego byśmy przyszli do danego węzła od źródła. Klucz w źródle jest równy
# zero, ponieważ nie potrzebujemy się poruszać po żadnej krawędzi aby dotrzeć do źródła.
#
# Drugą procedurą jest tak zwana procedura relaksacji wierzchołka. Gdy będziemy odwiedzali dany wierzchołek, relaksacja jest formą
# aktualizowania informacji na jego temat. Dajmy na to, że z wierzchołka u odwiedzamy wierzchołek v. Jeśli nie był on wcześniej
# przetworzony, to ma atrybuty v.parent = 'NIL' oraz v.key = 'INF'. Zmieniamy je odpowiednio na 'u' oraz u.key + w(u,v), czyli 
# koszt dotarcia do tego wierzchołka to koszt dotarcia do 'u', a później koszt przejścia po krawędzi (u,v). Jeśli jednak był on już
# wcześniej przetworzony, to musimy sprawdzić, czy stary sposób dotarcia do tego wierzchołka jest bardziej, czy mniej optymalny od 
# naszego nowego sposobu, z węzła 'u'.
#

def relax(u, v, w):
    if v.key > u.key + w(u,v):
        v.key = u.key
        v.parent = u

#
# Teraz, uzbrojeni w te dwie metody pomocnicze możemy podjąć się wyzwania znalezienia najkrótszej ścieżki. Zaczniemy od bardziej
# ogólnego algorytmu, który dopuszcza krawędzie z ujemnymi wagami.
#
#   a) Algorytm Bellmana-Forda:
# Algorytm Bellmana-Forda opiera się na programowaniu dynamicznym, choć nie do końca widać to na pierwszy rzut oka. Służy on nie
# tylko do znajdowania najkrótszej ścieżki, ale daje również odpowiedź na pytanie o istnienie cyklu o ujemnej wartości w danym grafie.
# W jaki sposób to robi? W pesymistycznym przypadku uda nam się zrelaksować docelowo (po danej relaksacji uzyskać już globalnie optymalne
# rozwiązanie w danym węźle) tylko i wyłącznie wierzchołki, które oddalone są o jeden wierzchołek od już aktualnie docelowo zrelaksowanych
# wierzchołków, więc jeśli chcemy dotrzeć do docelowego wierzchołka oddalonego maksymalnie od źródła (o |V|-1 krawędzi) to potrzebujemy
# maksymalnie |v|-1 iteracji pętli, która zaraz pojawi się w kodzie. Jeśli więc przekroczymy maksymalną iterację i wejdziemy w kolejną,
# to jest to sygnał, że wciąż za każdym razem relaksujemy na nowo pewne węzły, ergo występuje cykl o ujemnej wadze. Wychwytywanie
# najkrótszych ścieżek polega na tym, by podczas każdej z (maksymalnie) |V|-1 iteracji pętli zrelaksować wszystkie możliwe krawędzie.
# W ten sposób uda nam się znaleźć optymalne rozwiązanie dla każdego wierzchołka. Warto ten algorytm wyposażyć jeszcze w mechanizm
# aby wyjść przedwcześnie, jeśli okaże się, że podczas danej iteracji nic nie zrelaksowaliśmy, co oznacza, że mamy już optymalne 
# rozwiązanie naszego problemu.
#

def bellman_ford(G, w, s):
    initialize_single_source(G, s)
    # Główna pętla, szukamy optymalnego rozwiązania
    for i in range(1, G.V.count):
        for (u,v) in G.E:
            relax(u, v, w)
    # Jeśli znajdziemy jakąkolwiek krawędź, którą wciąż można
    # zrelaksować, zwracamy False (nie ma rozwiązania)
    for (u,v) in G.E:
        if v.key > u.key + w(u,v):
            return False
    # W przeciwnym wypadku, rozwiązanie istnieje (jest
    # zakodowane w rodzicach wierzchołków, mamy napisaną 
    # procedurę służącą do wyświetlania tej ścieżki)
    return True

#
# Złożoność obliczeniowa algorytmu (zakładamy reprezentację grafu przy użyciu list sąsiedztwa) to O(V^2 + VE), a jeśli mamy przypadek
# że E = Omega(V), czyli E jest ograniczone od dołu V, to złożoność redukuje się do O(VE).
#
#   b) Najkrótsze ścieżki w DAG:
# Jeśli mamy acykliczny graf skierowany (uwaga, Bellman-Ford i Dijkstra radzą sobie z cyklami, Bellman-Ford nawet z ujemnymi, tutaj
# zakładamy, że nie ma cyklu), to możemy na nim zrobić sortowanie topologiczne, co sprowadzi go (wizualnie, oczywiście) do pewnej
# listy zależności. Możemy w szybki sposób obliczyć najkrótsze ścieżki przy pomocy 'listy' zwracanej przez sortowanie topologiczne:
#

def DAG_shortest_path(G, s, w):
    g_list = G.topological_sort
    # Dla każdego wierzchołka w kolejności topologicznej
    for u in g_list:
        # Dokonaj relaksacji na jego sąsiadach
        for neighbor in u.neighbors:
            relax(u, neighbor, w)

#
# Dokonanie relaksacji na sąsiadach wystarczy, gdyż o to chodzi w sortowaniu topologicznym, by ustawić wierzchołki w takiej 
# kolejności, by każdy wierzchołek x miał przed sobą wierzchołki od których zależy. W ten sposób pominiemy wszystkie wierzchołki
# nieosiągalne ze źródła, później relaksujemy wierzchołki w naturalnej kolejności, biorąc pod uwagę ich poprzedników.
#
# Złożoność obliczeniowa: Theta(V+E)
#
#   c) Algorytm Dijkstry:
# Algorytm Dijkstry jest uogólnieniem BFS. W przeszukiwaniu wszerz używaliśmy kolejki FIFO opartej na jednostkowej odległości węzła
# od źródła, co tutaj nie wystarczy. Musimy zamienić atrybut 'distance' na 'key', tak jak to robiliśmy w Bellmanie-Fordzie, oraz
# wprowadzić kolejkę priorytetową. Dijkstry używamy, gdy mamy do czynienia z grafem o samych dodatnich krawędziach co sprawia, że
# możemy zastosować strategię zachłanną. Za każdym razem wyciągamy z kolejki priorytetowej element o najmniejszyym kluczu i 
# relaksujemy jego sąsiadów, co przypomina też algorytm Prima.
#

def dijkstra(G, s, w):
    initialize_single_source(G, s)
    # S to już odwiedzone wierzchołki
    S = set()
    # Q to kolejka priorytetowa typu min, dodaj
    # wszystkie wierzchołki
    Q = create_queue(G.V)
    while Q.empty != True:
        u = Q.dequeue()
        S.add(u)
        # Relaksacja każdego sąsiada, aktualizacja
        # kolejki priorytetowej
        for v in u.neighbors:
            relax(u, v, w)

#
# Złożoność obliczeniowa algorytmu Dijkstry zależy od implementacji kolejki priorytetowej. Dla zwykłej tablicy będzie ona wynosiła
# O(V^2), dla kopca binarnego (klasyka) będzie wynosiła O((V+E)lgV). Jest jeszcze jakiś kopiec Fibonacciego, lecz nawet nie będę
# o nim pisać, bo nie był on zbytnio omawiany.
# =================================================================================================

# =================================================================================================
# 6. Najkrótsze ścieżki między wszystkimi parami wierzchołków:
# 