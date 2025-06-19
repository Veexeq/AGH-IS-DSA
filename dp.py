
# =================================================================================================
# Wstęp / podsumowanie teorii 
#
# Programowanie dynamiczne to metoda podobna do 'Divide and Conquer', ale
# w 'Divide and Conquer' podproblemy są niezależne, a tutaj są zależne.
# Oszczędzamy czas poprzez spamiętywanie (memoization) rozwiązań podproblemów,
# albo poprzez rozwiązywanie ich metodą wstępującą (jeśli istnieje naturalny porządek).
#
# DP należy kojarzyć z problemami optymalizacyjnymi, znajdujemy rozwiązanie maksymalizując
# bądź minimalizując koszt. Optymalnych rozwiązań może być kilka. Znajdujemy zazwyczaj jedno.
#
# Etapy projektowania algorytmu DP:
# 1. Znajdź optymalną podstrukturę w problemie (tzn., że aby rozwiązać problem optymalnie,
# mniejsze podproblemy z których się składa, równiez muszą być rozwiązane optymalnie)
# 2. Zdefiniuj równanie rekurencyjne opisujące koszt
# 3. Znajdź naturalny porządek i rozwiąż podproblemy sekwencyjnie, wstępująco (np. aby obliczyć
# n-tą liczbę Fibonacciego wpierw obliczymy n-1 i n-2)
# 4. (Opcjonalnie) Zmodyfikuj algorytm tak, by dało się skonstruować optymalne rozwiązanie
# (np. zapisz w których miejscach podzieliliśmy tablicę)
#
# Kilka zdań podsumowania z wykładu:
# Problem posiada optymalną podstrukturę, jeśli jego rozwiązanie jest funkcją optymalnie
# rozwiązanych podproblemów. Jeśli mamy optymalną podstrukturę, to czasem problem można również
# rozwiązać strategią zachłanną (greedy).
# Aby znaleźć optymalną podstrukturę należy wpierw pokazać, że problem polega na dokonaniu pewnego
# wyboru, który zostawia nas z jednym, bądź więcej podproblemami do rozwiązania. Nie musimy znać tego
# wyboru od razu, ale musimy być pewni, że jest wśród rozważanych.
# Optymalne podstruktury zależą od liczby podproblemów, które pozostawia wybór, a także liczbą podproblemów
# które należy rozważyć, by wybrać dobrą opcję.
#
# Memoization vs bottom-up:
# Jeśli problem ma intuicyjną strukturę i podproblemy da się rozwiązać w naturalnej kolejności, to łatwiej jest
# użyć konstrukcji rozwiązania wstępującego. Jeśli natomiast mamy z tym trudności, bądź wiemy, że nie potrzeba
# nam rozwiązywać wszystkich podproblemów (tak robi bottom-up), to możemy skonstruować rozwiązanie używającego
# spamiętywania. Będzie to ciut wolniejsze ze względu na rekurencję, ale ostatecznie może wyjść nam na lepsze,
# jeśli trafimy na scenariusze opisane powyżej.
#
# Problemy rozwiązywane na wykładzie i laboratoriach:
# 1. Matrix Chain Multiplication (MCM) - problem polegający na tym, aby znaleźć
# optymalne nawiasowanie ciągu macierzy, czyli zminimalizować liczbę operacji
# 2. Triangulacja wielokąta - problem równoważny na mocy bijekcji z MCM, polega na znalezieniu
# optymalnego podziału wielokąta na trójkąty mając daną funkcję kosztu (np. odległość wierzchołków)
# 3. Diamenty - znalezienie optymalnej ścieżki przejścia po tablicy 2D, by zebrać jak najwięcej
# diamentów po drodze.
# 4. Dyskretny problem plecakowy (0/1 Knapsack)
# 5. Problem wydawania reszty
# =================================================================================================

# =================================================================================================
# Kod i wyjaśnienia:
#
# Matrix Chain Multiplication:
# Mamy macierze A_1, A_2, ..., A_n, iloczyn macierzy A_i * A_(i+1) * ... * A_j oznaczymy A_(i,j)
# Dzielimy A_(i,j) na A_(i,k) * A_(i+1,j), k musi być optymalnie wybrane, żeby mnożenie było optymalne
#
# 1. Optymalna podstruktura: aby mnożenie A_(i,k) * A_(k+1,j) było optymalne, nawiasowanie w obu tych
# macierzach musi być optymalne, czyli na optymalne rozwiązanie problemu składa się optymalne rozwiązanie
# jego podproblemów.
#
# Tworzymy tabelę m[1...n,1...n], gdzie m[i,j] oznacza optymalny koszt do pomnożenia ciągu A_(i,j)
# m[i,i] = 0, bo nie trzeba wykonywać żadnych mnożeń, to po prostu macierz A_i
#
# 2. Równanie rekurencyjne: optymalny koszt pomnożenia macierzy A_(i,j) to:
#   a) m[i,j] = 0, i = j
#   b) m[i,j] = min(m[i,k] + m[k+1] + p_(i-1) * p_k * p_j), i != j
# Jest tak, ponieważ optymalizujemy wybór k (i <= k < j) i musimy dodać sam koszt pomnożenia macierzy
# A_1 ma koszt p_0 * p_1, A_2 ma koszt p_1 * p_2, A_i ma koszt p_(i-1) * p_i, gdzie p mamy dane
#
# 3. Naturalny porządek i konstrukcja algorytmu wstępująco: istnieje oczywisty naturalny porządek, gdyż
# szukając m[i,k] oraz m[k+1,j] muszą one już istnieć. Zaczynamy od obliczenia kosztów pojedynczych macierzy,
# później ciągu dwóch macierzy, a mając obliczone wszystkie koszty ciągów dwóch macierzy, możemy na ich podstawie
# skonstruować wszystkie ciągi trzech macierzy itd.
# 
# 4. Umożliwienie rekonstrukcji optymalnego rozwiązania: wystarczy dodać tablicę s[n,n], gdzie
# s[i,j] będzie zapamiętywało indeks k dla podziału m[i,j]
#
# Kod w Pythonie (jak pseudokod)

INF = 2**31 - 1
p = [30, 35, 15, 5, 10, 20, 25]

def mcm(p, INF):
    n = len(p)-1

    # Dwie tablice (n+1)x(n+1), ale indeksujemy od 1
    m = [[0 for _ in range(n+1)] for _ in range(n+1)]
    s = [[0 for _ in range(n+1)] for _ in range(n+1)]
    
    for i in range(1, n+1):
        m[i][i] = 0

    # Dla każdej długości ciągu - 2, 3, ..., n
    for v in range(2, n+1):
        # Początkowy indeks ciągu, bierzemy pod uwagę długość ciągu
        for i in range(1, n-v+2):
            # Końcowy indeks ciągu
            j = i + v - 1
            m[i][j] = INF
            for k in range(i, j):
                q = m[i][k] + m[k+1][j] + p[i-1]*p[k]*p[j]
                if q < m[i][j]:
                    m[i][j] = q
                    s[i][j] = k

    print(f"Koszt: {m[1][n]}")
    return m, s

def print_parenthesis(s, i, j):
    if i == j: print(f"A_{i}", end='')
    else:
        k = s[i][j]
        print("(", end='')
        # Wypisz lewe nawiasowanie i prawe nawiasowanie (oba są w nawiasach)
        print_parenthesis(s, i, k)
        print("*", end='')
        print_parenthesis(s, k+1, j)
        print(")", end='')

m, s = mcm(p, INF)
print_parenthesis(s, 1, len(p) - 1)
print() # Wyłącznie dla testowania w konsoli

# Złożoność obliczeniowa:
# Bez DP sprawdzamy każdą możliwość, więc dla ciągu n macierzy jest to n-1 liczba Catalana, więc
# P(n) = O(4^n) to sensowne ograniczenie od góry. Na wykładzie był natomiast dowód, że rekurencyjny algorytm bez 
# spamiętywania jest ograniczony od doły Omega(2^n).
# Z DP sprowadzamy ten algorytm do:
#   a) Time Complexity: Theta(n^3) - uwaga, na wykładzie było Omega(n^3), nie wiem dlaczego
#   b) Space Complexity: Theta(n^2)

# Triangulacja wielokąta:
# Mamy n-kąt, który podzielimy na trójkąty. Liczba wynikowych trójkątów jest równa n-2, więc problem triangulacji
# n+1 kąta (na n-1 trójkątów) odpowiada problemowi nawiasowania n macierzy (n-1 mnożeń). Dane są punkty A_1, A_2, ..., A_n.
#
# 1. Optymalna podstruktura: Mamy wielokąt A_(i,j). Dzielimy go na dwa wielokąty, oraz trójkąt. Wielokąty to A_(i,k) oraz
# A_(k,j), więc pozostały trójkąt to trójkąt o wierzchołkach i-k-j. Jeśli mówimy o wielokącie A_(i,j) to mamy na myśli wielokąt,
# który ma wszystkie krawędzie A_(i,i+1), A_(i+1,i+2), ..., A_(j-1,j).
# Właśność optymalnej podstruktury polega na tym, że gdy już podzielimy wielokąt na dwa wielokąty i trójkąt, to generuje nam
# to dwa podproblemy, które również muszą być rozwiązane optymalnie.
# ... ... ... 

# Dyskretny problem plecakowy: dysponujemy n przedmiotami, każdy ma wagę w_i oraz wartość v_i. Mamy także plecak zdolny do 
# zapakowania W kilograrmów. Musimy tak dobrać przedmioty, aby w tym plecaku była jak najbardziej wartościowa ich kombinacja.
# 
# 1. Optymalna podstruktura: załóżmy, że wiemy, że przedmiot k jest najbardziej optymalnym wyborem. Pozostaje nam wtedy w plecaku
# W - w_k miejsca, które również musimy zużyć w optymalny sposób.
# Tworzymy tablicę dp[0...n,0...W], gdzie dp[i,w] oznacza maksymalny zysk jaki można uzyskać mając do dyspozycji wagę 'w' i wkładając 
# do plecaka przedmioty spośród 'i' pierwszych przedmiotów.
# 
# 2. Równanie rekurencyjne:
#   a) dp[i,w] = 0, i = 0 (0 pierwszych przedmiotów) lub w = 0 (0 pojemności)
#   b) dp[i-1,w], w_i > w
#   c) dp[i,w] = max(dp[i-1,w], v_i + dp[i-1,w-w_i]), w_i <= w 
# Najpierw zajmujemy się warunkami brzegowymi, później konstruujemy rozwiązanie od zera - wiersz po wierszu, gdzie wiersze to 'i',
# czyli branie pod uwage 'i' pierwszych przedmiotów
# 
# 3. Bottom-up approach: albo bierzemy i-ty przedmiot, albo nie. Na etapie wyboru mamy już wszystkie potrzebne informacje, czyli 
# w praktyce po prostu optymalny zysk dla obu scenariuszy.
#
# 4. Rekonstrukcja rozwiązania: należy użyć backtracking-u. Zaczynamy od dp[n][W] i sprawdzamy, czy dany przedmiot był użyty, czy nie.
# Na podstawie tego podemujemy decyzję i wyświetlamy rozwiązanie rekursywnie dla odpowiedniego scenariusza.

W = 5
N = 4
# Dodajemy 0 na początku aby tablice były 1-indexed
v = [0, 12, 10, 20, 15]
w = [0, 2, 1, 3, 2]

def discrete_knapsack(W, N, v, w):
    # Inicjalizujemy pustą tablicę dp[0...N,0...W]
    dp = [[0 for _ in range(0, W+1)] for _ in range(0, N+1)]

    for i in range(1, N+1):
        for cw in range(1, W+1):
            # Przedmiot mieści się w plecaku - podejmujemy decyzję
            if w[i] <= cw:
                dp[i][cw] = max(v[i] + dp[i-1][cw-w[i]], dp[i-1][cw])
            else:
                dp[i][cw] = dp[i-1][cw]
    
    print(f"Maksymalny zysk: {dp[N][W]}")
    return dp

dp = discrete_knapsack(W, N, v, w)

# Złożoność obliczeniowa:
#   a) Time Complexity: Theta(N*W)
#   b) Space Complexity: Theta(N*W)
# Można to uprościć do Theta(n^2), ale pierwszy zapis jest dokładniejszy  

# Problem wydawania reszty: mamy do dyspozycji nieskończenie wiele nominałów o wartościach z tablicy N.
# Chcemy wydać kwotę K za pomocą jak najmniejszej liczby monet z tablicy N. Liczba różnych nominałów to length(N) = L.
#
# 1. Optymalna podstruktura: jeśli wiemy, że naszym pierwszym krokiem do wydania kwoty K jest użycie monety
# N[k], to wtedy kwota K - N[k] również musi być wydana za pomocą jak najmniejszej liczby nominałów.
# Jest to bliźniaczy problem do 0/1 Knapsack. Niech dp[0...L,0...K], wtedy dp[i,j] oznacza minimalną liczbę nominałów potrzebną
# do wydania kwoty j za pomocą pierwszych i monet w tablicy N.
#
# 2. Równanie rekurencyjne:
#   a) dp[i,j] = INF, i = 0, j != 0 - to dla przypadku, gdy nie używamy żadnych monet (nie da się uzyskać kwoty)
#   b) dp[i,j] = 0, j = 0 - to dla przypadku, gdzie mamy do wydania kwotę 0s
#   c) dp[i,j] = min(dp[i-1,j], dp[i,j-N[i]])
# Tutaj największa różnica. Zakładając, że mamy do wyboru nieskończenie wiele monet, możemy pozostać w jednej linii
# (nawet jeśli weźmiemy monetę, to możemy wziąć ją ponownie, więc uzupełniamy kwotę K-N[i] za pomocą wciąż 'i' pierwszych monet)

N = [0, 2, 5, 7] # 0 aby tablica była 1-indexed
K = 27
L = len(N) - 1

def coin_change(N, L, K):
    dp = [[INF for _ in range(0, K+1)] for _ in range(0, L+1)]
    for i in range(L+1): dp[i][0] = 0

    for i in range(1, L+1):
        for j in range(1, K+1):
            if N[i] > j:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = min(dp[i-1][j], dp[i][j-N[i]] + 1)
    
    if dp[L][K] == INF: 
        print(f"Nie da się uzyskać tej kwoty")
        return dp

    print(f"Minimalna liczba monet potrzebna: {dp[L][K]}")
    return dp

coin_change(N, L, K)

# Złożoność obliczeniowa:
#   a) Time Complexity: Theta(K*L)
#   b) Space Complexity: Theta(K*L)

# Inne typowe problemy używające DP:
# 1. Floyd-Warshall - najkrótsze ścieżki między wszystkimi parami wierzchołków grafu ważonego
# 2. Problem komiwojażera - znajdowanie cykli Hamiltona w grafach
# 3. Bellman-Ford - najkrótsze ścieżki od źródła do wszystkich innych wierzchołków w grafie 
# =================================================================================================
