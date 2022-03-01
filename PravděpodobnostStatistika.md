# Pravděpodobnost a statistika I
- [Pravděpodobnost a statistika I](#pravděpodobnost-a-statistika-i)
    - [Organizace](#organizace)
    - [Sylabus:](#sylabus)
  - [01 P (EN)](#01-p-en)
    - [Independent events](#independent-events)
    - [Practice](#practice)
  - [01 P (CZ)](#01-p-cz)
  - [01 L](#01-l)
    - [Software](#software)
    - [Téma přednášky](#téma-přednášky)
      - [Ilustrace](#ilustrace)
    - [Pojmy](#pojmy)
    - [Věta 1](#věta-1)
      - [Příklady pravděpodobnostních prostorů](#příklady-pravděpodobnostních-prostorů)
    - [Podmíněná pravděpodobnost](#podmíněná-pravděpodobnost)
  - [02 P](#02-p)
  - [02 L](#02-l)
    - [Úvodní příklad](#úvodní-příklad)
    - [Věta](#věta)
    - [Věta o úplné pravděpodobnosti nebo o rozboru příkladů](#věta-o-úplné-pravděpodobnosti-nebo-o-rozboru-příkladů)
    - [Bayesova věta](#bayesova-věta)
    - [Def: Nezávislost jevu](#def-nezávislost-jevu)
    - [Vzájemně nezávislé jevy](#vzájemně-nezávislé-jevy)
    - [Def: diskrétní náhodná veličina](#def-diskrétní-náhodná-veličina)
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
     - 3. Pro A1, A2, ... z *F* platí, že jejich sjednocení je opět v *F*
3. Pravděpodobnost ... P: *F*->[0,1]
   1. pokud P(Omega)=1
   2. pokud pravděpodobností sjednocených jevů je ∑ pravděpodobností jednotlivých jevů (samostatně) (ale jevy musí být po dvou disjunktní)
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

#### Příklady pravděpodobnostních prostorů
1. klasický:
   - Omega je konečná množina
   - Gama = P(Omega)
   - P(A)=|A|/|Omega|=n-dobrých/n-všech možností
2. diskrétní
   - Omega ... spočetná množina
   - P(A) = ∑ (Pi)
   - ... prostě jevy se váží??
3. geometrický
    - Omega je podmnožina d-rozměrného prostoru nad reálnými čísly
    - P(A)=Vd(A)/Vd(Omega) ... objemy
4. spojitý
    - P(A) = ∫_A(f(x)) t.ž.
      - 0∈f(x),
      - ∫_Omega(f(x)) = 1

### Podmíněná pravděpodobnost
Def.: A,B z Gama, P(B)>0, definujeme P(A|B) = P(A^B)/P(B)

## 02 P
Podmíněná pravděpodobnost

3 Karty červené  
Výlet do Krkonoš  
Paradox Monty-Halla  

## 02 L
### Úvodní příklad
P(A|B) = 1 nebo P(B|A) = 1 pokud A=>B?  
P(B|A) = 1 je správně, protože A vytváří pravděpodobnostní prostor a pro každý jev z A platí jev B...  

### Věta
**P(A1^...^An) = P(A1).P(A2|A1). ... .P(An|A1^A2^...^An)**  

Dk.: Rozepsání vzorečku na podmíněnou pravděpodobnost. *TODO*

Příklad:  
S ... spam  
D ... detekce  
4 možnosti  
1. D^S - správně nevyhodnocený jako spam
2. D'^S - false negative
3. D^S' - false positive
4. D'^S' - správně vyhodnocený jako spam  

### Věta o úplné pravděpodobnosti nebo o rozboru příkladů
P(A) = ∑_i(P(B) . P(A|B))  
A,B náleží *F*  
B1,B2,...,Bn ... rozklad Omega ... (Bi^Bj)!=0  
vBi = Omega množin je konečný nebo spočetný počet  

Dk.: P(A) = ∑_i(P(A^Bi)) = ∑_i(P(Bi)*P(A|Bi))  
*(rozepsání vzorečku)*

Příklad 1:  
P(D) = P(S).P(D|S) + P(S')*P(D|S')  
B1 = S  
B2 = S'  
A = D  

Příklad 2: Gambler's ruin  
n náleží N,  
s náleží {0,1,2...n} ... s je startovní počet  
opakujeme hru o +-1 Kč  
férová hra ... pravděpodobnost výhry/prohry je 1  
V ... vyhrajeme ... n Kč  
V' ... prohrajeme ... 0Kč

Zjistit p(s) = P(V)  
1) 1.hra vyhraná / prohraná
P(V1) nebo P(V2)
    .
   /\
   1 0
  /\/\
2

2) P(s) = 1/2 . P(s+1) + ∑_i(P(s-1))  
3) n+1 lineárních rovnic pro n+1 neznámých  
P(S) = s/n je řešení 

### Bayesova věta
P(Bj|A) = P(Bj) . P(A|Bi) / ∑_i(P(Bi).P(A|Bi))  
Dk.: P(Bj^A) / P(A) = P(Bj)(P(A|Bj)) / P(A) a věta o úplné pravděpodobnosti!

Příklad s nemocí:  
Senzitivita ... 95%
Lidí v populaci ... 1/1000  
0.001 * 0.95 = 0.00095  

Stav světa ... B1, B2,... ,Bi...
Model světa ... P(Bi).P(A|Bi) ... A je měření

### Def: Nezávislost jevu
Jevy A,B náleží *F* jsou *nezávislé* pokud P(A^B) = P(A).P(B).

Příklad.: 2 hody mincí  
A ... první hod je P
B ... druhý bod je P
C ... hody jsou odlišné

x,P,O
P,PP,PO
O,OP,OO

### Vzájemně nezávislé jevy
Jevy jsou po dvou nezávislé, lze ověřit průnikem a produktem :)

### Def: diskrétní náhodná veličina
X ... diskrétní náhodná veličina, pokud X: Omega -> *R* t.ž.:
 - X je spočetná množina
 - pro každé x z R, že stav který zobrazuje je z *F*

P(X=x) ... popis množiny X  