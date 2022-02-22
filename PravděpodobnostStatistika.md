# Pravděpodobnost a statistika I
### Organizace
 [stránky předmětu](https://iuuk.mff.cuni.cz/~samal/vyuka/2122/PSt1/)

 [kvízy](https://api.socrative.com/rc/AhrYBB)

 Heslo: PRAVDASTAT
### Sylabus:
Pravděpodobnost:
- Axiomy pravděpodobnosti, základní příklady (diskrétní a spojité). Podmíněná pravděpodobnost, věta o úplné pravděpodobnosti, Bayesova věta. 

- Náhodné veličiny s diskrétním rozdělením: střední hodnota, rozptyl, linearita střední hodnoty a její použití. Základní diskrétní distribuce. 

- Spojité náhodné veličiny: popis pomocí hustoty pravděpodobnosti. Základní spojitá rozdělení. 

- Nezávislé náhodné veličiny. Náhodné vektory (marginální distribuce). Kovariance, korelace. 

- Zákony velkých čísel, základní nerovnosti (Markov, Čebyšev, Chernoff), Centrální limitní věta. 

Statistika:

- Bodové odhady: nestranné odhady, intervaly spolehlivosti. 

- Testování hypotéz, hladina významnosti. Dvouvýběrové testy. 

- Test dobré shody, test nezávislosti. 

- Neparametrické odhady. 

- Bayesovský a frekventistický přístup. Metoda "maximum a posteriori", odhad "least mean square". 

- Metoda maximální věrohodnosti. Bootstrap resampling. 

Simulace, generování náhodné veličiny z distribuce. Simulace Monte Carlo.

Informativně Markovovy řetězce. 

## 01 P (EN)
### Independent events
Events A,B are independent, if:
 - P[A^B]=P[A]*P[B]
 - P[A|B]=P[A], P[B|A]=P[B]
 - P[AvB]=P[A]+P[B]-P[A]*P[B]

We can sum up these in the formula P[A|B]=P[A^B]/P[B]

### Practice
Events A,B,C are mutually independent if:
 - P[A^B^C] = P[A].P[B].P[C]
 - A, B, C are pairwise independent

Events E are mutually independent if:
 - product of probabilities of events are equal to probability of intersect of the events
 - all the k events, k = |E|-1 are mutually independent
 - all the events are pairwise independent

Dies - O1={1,2,3,4,5,6}
For two throws:
O2={(1,1),(1,2),...,(6,6)}

Event A: You roll a total of 9 on two times.
A={(4,5),(5,4),(3,6),(6,3)}
|A|=4
P[A]=4/36=1/9

Event B: You roll even number both times.
Are A and B independent?
P[A^B]=0
P[A].P[B]=1/18
No.

O3 ... prob. space o 3times tossing of a coin
O3 = {(0,0,0), (0,0,1), ..., (1,1,1)}
X ... number of heads obtained = {0,1,2,3} ... 1/8,3/8,3/8,1/8
E[X]=SUM_a(a.P[X=a])=3/8+2*3/8+3*1/8=12/8=3/2

## 01 P (CZ)

*hod 3 kostkami*
Je větší pravděpodobnost, že součet bude 11 nebo že bude 12?
1 1 1
1 1 2
...
1 1 6
...
1 2 1

6 6 6

## 01 L

### Software
- je možné programovat v R a v Pythonu

### Téma přednášky
 - modely náhody a pozorování
 - pravděpodobnost
   - zadaný model náhody
   - získat pravděpodobnost pozorování
 - statistika
   - zadaná pozorování
   - získat model náhody

#### Ilustrace
Dány polynomy f a g
Zjišťujeme, jestli f==g
g ... zadán jako součin dvou polynomů g1 a g2

Přímo: vynásobíme g1 a g2, získáme g, porovnáme koeficienty g a f

Rychleji:
pro koeficient x0 porovnáme rovnost polynomů
rovnají se -> x0 je kořen součinu f.g


nerovnají se -> f != g

pokud nevyjde, že se nerovnají, rovnají se s určitou pravděpodobností

Hod kostkou - házíme dokud padá šestka

Hod šipkou na terč

počet emailů za den

čas běhu programu

### Pojmy
1. Omega ... množina elementárních jevů (sample space)
   - kostka ... {1,2,...,6}
   - šipky ... kruh
   - počet emailů za den ... *N0* (přirozená čísla)
   - čas běhu programu ... *R*
2. Prostor jevů ... *Gamma*?
   - def.: *F* -> P(Omega) je prostor jevů, patří do něj systém všech podmnožin Omega. Musí tvořit *Sigma-algebru*
     - 1. Množina 0 je v *F*
     - 2. Pro každou množinu A z *F* platí, že Omega bez A také náleží do *F*
     - 3. Pro A1, A2, ... z *F* platí, že jejich sjednocení je opět v F
3. Pravděpodobnost ... P: *F*->[0,1]
   1. pokud P(Omega)=1
   2. pokud pravděpodobností sjednocených jevů je suma pravděpodobností jednotlivých jevů (samostatně) (ale jevy musí být po dvou disjunktní)
4. Pravděpodobnostní prostor ... (Omega, Gamma, P)
   1. Omega != 0 ... libovolná množina
   2. Gamma = P(Omega) ... prostor jevů
   3. P: Gamma -> [0,1] ... pravděpodobnost
5. Jistý jev ... A je *jistý jev*, pokud P(A) = 1 <=> A nastává skoro jistě
6. Nemožný jev ... A je *nemožný jev*, pokud P(A) = 0

### Věta 1
1. P(A) + P(A^C) = 1 (T.ODO: dokázat)
2. A ... podmnožina B
   1. -> P(A) <= P(B)
   2. -> P(B/A) = P(B)-P(A)
3. P(AvB) = P(A)+P(B)-P(A^B)
4. P(A1vA2v...) <= suma pravděpodobností dohromady
   1. důkaz -- zdizjunktnění (T.ODO: zkus si dokázat)

#### Příklady
1. klasický:
   - Omega je konečná množina
   - Gama = P(Omega)
   - P(A)=|A|/|Omega|=n-dobrých/n-všech možností
2. diskrétní
   - Omega ... spočetná množina
   - P(A) = Suma (Pi)
   - ... prostě jevy se váží??
3. geometrický
    - Omega je podmnožina d-rozměrného prostoru nad reálnými čísly
    - P(A)=Vd(A)/Vd(Omega) ... objemy

### Podmíněná pravděpodobnost
Def.: A,B z Gama, P(B)>0, definujeme P(A|B) = P(A^B)/P(B)
