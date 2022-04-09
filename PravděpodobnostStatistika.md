# Pravděpodobnost a statistika 

### Obsah
- [Pravděpodobnost a statistika](#pravděpodobnost-a-statistika)
    - [Obsah](#obsah)
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
  - [03 L Diskrétní náhodné veličiny](#03-l-diskrétní-náhodné-veličiny)
    - [Def: Náhodná veličina](#def-náhodná-veličina)
    - [Def: Pravděpodobnostní funkce n.v. X](#def-pravděpodobnostní-funkce-nv-x)
    - [Def: Bernouliho/Alternativní rozdělení](#def-bernoulihoalternativní-rozdělení)
    - [Def: Indikátorová n. veličina jevu A](#def-indikátorová-n-veličina-jevu-a)
    - [Def: Geometrické rozdělení](#def-geometrické-rozdělení)
    - [Def: Binomiální rozdělení](#def-binomiální-rozdělení)
    - [Def: Hyper geometrické rozdělení](#def-hyper-geometrické-rozdělení)
    - [Def: Poissonovo rozdělení](#def-poissonovo-rozdělení)
    - [Def: Poissonovo paradigma](#def-poissonovo-paradigma)
    - [Def: Střední hodnota](#def-střední-hodnota)
    - [Příklady střední hodnoty](#příklady-střední-hodnoty)
      - [Bernouliho rozdělení](#bernouliho-rozdělení)
      - [Binární rozdělení](#binární-rozdělení)
      - [Geometrické rozdělení](#geometrické-rozdělení)
      - [Hypergeometrické rozdělení](#hypergeometrické-rozdělení)
      - [Poissonovo rozdělení](#poissonovo-rozdělení)
  - [04 L](#04-l)
    - [Věta o střední hodnotě d. n. v. funkce (LOTUS)](#věta-o-střední-hodnotě-d-n-v-funkce-lotus)
    - [Věta o vlastnostech *E*](#věta-o-vlastnostech-e)
    - [Def.: Rozptyl n.v. X](#def-rozptyl-nv-x)
    - [Def.: Směrodatná odchylka](#def-směrodatná-odchylka)
    - [Věta o rozptylu a střední hodnotě](#věta-o-rozptylu-a-střední-hodnotě)
    - [Věta o rozptylu](#věta-o-rozptylu)
    - [Věta o střední hodnotě a pravděpodobmosti](#věta-o-střední-hodnotě-a-pravděpodobmosti)
    - [Def. Sdružená pravděpodobnostní funkce](#def-sdružená-pravděpodobnostní-funkce)
  - [05 L](#05-l)
    - [Def.: Nezávislost X,Y](#def-nezávislost-xy)
    - [Marginální rozdělení](#marginální-rozdělení)
    - [Věta ("o konvoluci náhodné veličiny")](#věta-o-konvoluci-náhodné-veličiny)
    - [Věta ("o konvoluci střední hodnoty")](#věta-o-konvoluci-střední-hodnoty)
    - [Věta o linearitě střední hodnoty](#věta-o-linearitě-střední-hodnoty)
    - [Věta o součinu střední hodnoty](#věta-o-součinu-střední-hodnoty)
    - [Věta o rozptylu součtu](#věta-o-rozptylu-součtu)
    - [Def.: Kovariance](#def-kovariance)
    - [Značení](#značení)
  - [06 L Obecné náhodné veličiny](#06-l-obecné-náhodné-veličiny)
    - [Def: Náhodná veličina](#def-náhodná-veličina-1)
    - [Def: Distribuční funkce](#def-distribuční-funkce)
    - [Def: Spojitá n.v.](#def-spojitá-nv)
    - [Věta X má hustotu fx](#věta-x-má-hustotu-fx)
    - [Exponenciální rozdělení](#exponenciální-rozdělení)
    - [Def: střední hodnoty](#def-střední-hodnoty)
  - [07 L](#07-l)
    - [Opakování n.v.](#opakování-nv)
    - [Linearita střední hodnoty platí i zde](#linearita-střední-hodnoty-platí-i-zde)
    - [Příklady rozdělení](#příklady-rozdělení)
      - [X ~ Exp(λ)](#x--expλ)
      - [X ~ Geom(p)](#x--geomp)
      - [X ~ ϕ(x) Standardní normální rozdělení](#x--ϕx-standardní-normální-rozdělení)
      - [Cauchyho rozdělení](#cauchyho-rozdělení)
      - [Kvartilová funkce](#kvartilová-funkce)
  - [08 L](#08-l)
    - [Věta o celkové hustotě pravděpodobnosti (o celkové střední hodnotě)](#věta-o-celkové-hustotě-pravděpodobnosti-o-celkové-střední-hodnotě)
    - [Věta](#věta-1)
    - [Věta](#věta-2)
    - [Def.: Náhodný vektor (X,Y)](#def-náhodný-vektor-xy)
    - [Def.: Vícerozměrná distribuční funkce](#def-vícerozměrná-distribuční-funkce)
    - [Vícerozměrné normální rozdělení](#vícerozměrné-normální-rozdělení)
    - [Věta](#věta-3)
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

## 03 L Diskrétní náhodné veličiny
### Def: Náhodná veličina
D.n.v. je funkce X:Omega->*R*  
1) ... Im(X) je spočetná množina  
2) ... všechna x z X : {w z Omega: X(w)=x} náleží do *F*  

Třeba máme množinu 5 čísel {a,b,c,d,e}, Omega je ta množina, X dává množině hodnoty.  

Buď pravděpodobnostní prostor (Omega, *F*, *P*)
Pak D.n.v. je funkce X:Omega->*R*, pro kterou platí, že
1) Im(X) je spočetná množina
2) pro všechna x z X : {w z Omega: X(w)=x} náleží do *F* 
Pozn.:
X: {a,b,c,d,e} -> {1,2,2,7,15}  
díky 3) definováno, že: P(X=x)  

Tím jsme mch. zavedli nový diskrétní pravděpodobnostní prostor, kde elementární jevy (w) jsou zobrazeny na Im(X) = {x1,X2,x3...}  

### Def: Pravděpodobnostní funkce n.v. X
je Px:*R* -> [0,1]  
Px(x)=P(X=x)  

Pozorování:  
{1,2,2,pi,10} ... Px(1) = 0.2, Px(2) = 0.4, ...  

### Def: Bernouliho/Alternativní rozdělení
X může být jen 1 nebo 0.
p z [0,1] -> X~Bern(p) ... X má rozdělení

Příklad:  
X ... 1/0  
1 ... padla šestka  
0 ... jinak  

### Def: Indikátorová n. veličina jevu A
I_A(w)=1 ... w z A  
I_A(w)=0 ... w není z A  

Pozorování:  
I_A ~Bern(P(A))

### Def: Geometrické rozdělení
např.: X = kolikátým hodem padla 1. šestka  
Im(X)=*N*  
p z [0,1] -> X~Geom(p)  

Px(x)=P(X=x)=0
Px(x)=(1-p)^(x-1)*p ... (x je z X)  

Kontrola ∑_(k=1)^(neonečno)(1-p)^(k-1)*p ?= 1  

pokud p/(1-(1-p)) = 1, tak platí  

### Def: Binomiální rozdělení
X = počet šestek při n nezávislých hodech  
p je z [0,1]; n z *N*  
X ~ Bin(n,p)
Px(k)= ...  
  1) 0 pokud k není z [0,n]   
  2) (n nad k)*p^k * (1-p)^n-k  

Příklad:  
X = počet šestek při n nezávislých hodech  
k krát padne s pravděpodobností:  
(n nad k)*p^k (počet možností kdy padne krát pravděpodobnost, že k-krát padne)  
to celé krát (1-p)^n-k ... pravděpodobnost, že n-k krát nepadne.  

Kontrola:  
suma přes všechna k je rovna 0. TODO :)  

Příklad s míčky:  
Máme n míčků a k krát vytáhnu.

### Def: Hyper geometrické rozdělení
Totéž jako binomická věta, ale míčky nevracím.  

n z N  
k z 1,2,...,n  

Px(k) = P(X=k) = P(vytáhnu K červených z n pokusů bez vracení).  

(Počet červených/všech) = (K nad k)(N-k nad n-k)/(N nad n).  

### Def: Poissonovo rozdělení
λ > 0, X ~ Poi(λ)  
Px(k)=e^λ(λ^(k)/k!)

limita binomického rozdělení.  

Xn~Bin(n,λ/n) n>λ

P(Xn=k) = (n nad k).(λ/n)^(k).(1-λ/n)^(n-k)  
(n nad k).(λ/n)^(k) -> λ^(k)/k!  
(1-λ/n)^n -> e^-λ  
(1-λ/n)^(-k) -> 1  

Příklad:  
X ... počet emailů za den  
n ... počet lidí, co píšou (píšou stejně často) ... <= 1 email/den každý  

λ ... typický počet emailů za den => p=λ/n  
P(1 člověk napíče email)=p  
X~Bin(n,λ/n), přibližně X~Poi(λ)  

### Def: Poissonovo paradigma
Buďte A1 ... An jsou (skoro) nezávislé jevy  
λ = ∑(P(Ai))  

Potom ∑_(i=1)^(n)I_A_i ~ Poi(λ)  

### Def: Střední hodnota
Střední hodnota d.n.v. X je  
EX=SUMA_(x z Im(X))(x.Px(x)) = SUMA(x)P(X=x)  
E ... expectation ... střední hodnota  

Poznámka:
Pokud (Omega, *F*, P) je diskrétní, můžu EX definovat i takto:
EX = SUMA_(w z Omega)(X(w).P({w}))  

### Příklady střední hodnoty
#### Bernouliho rozdělení
EX = p  
var(X)= E(X^2) - E(X)^2 = p-p^2 = p.( 1-p )

#### Binární rozdělení
EX = E(X1 + X2 + ... + Xn), kde Xi je bernouliho rozdělení.  
EX = EX1 + EX2 + ... + EXn = n.p  
var(X) = var(X1) + var(X2) + ... + var(Xn) = np(1-p)  

#### Geometrické rozdělení
EX = SUMA_(k=1)(k.(1-p)^(k).p =  
= SUMA_k=1 (SUMA_(l=1)^(k)) (1-p)^(k-1).p =  
SUMA_(l=1)(((1-p)^(l-1)*p)/(1-n-p)=1/(1-(1-p))=1/p

#### Hypergeometrické rozdělení
Příklad:  
K ... červené míčky  
N ... celkem míčky  
počet červených z n vytažených  

X = X1 + ... + Xn  
X1 ~ Bern(K/N)  

EX = EX1 + EX2 + ... EXN = n*(K/N)

#### Poissonovo rozdělení
X ~ Pois(λ)  
EX = var(X) = λ
## 04 L
Y = g(X) = g°X

g(X) je d. n. v., kdykoli X je d. n. v.
1. Im(X) je nejvýše spočetný,  
2. V y z *R* : Y^(-1)(y) z *F*
   {w:g(X(w))=y} = U_(x z R: g(x)=y x z Im(X) {w:X(w)=x})

### Věta o střední hodnotě d. n. v. funkce (LOTUS)
Law Of The Unconscious Statistitian  
E( g(X) ) = SUMA_( x z Im(X) )( g(x) . P(X=x ) )  

### Věta o vlastnostech *E*
1. P(X>=0) = 1 & E(X)=0 -> P(X=0)=1
2. E(X)>=c -> P(X>c)>0
3. E(a.X+b) = a.E(X)+b
4. E(X+Y)=E(X)+E(Y)

Dk. 2.:  
EX > c = SUMA(x.P(X=x))
Sporem: P(X>=c) = 0  
  -> Vx>=c : P(X=x)=0
  -> nenulové členy v "P(X=x)" mají x>c

Příklad:  
Házíme kostkou, při 6 házíme podruhé

### Def.: Rozptyl n.v. X
var(X) = E[ (X - E(X))^2 ]  

### Def.: Směrodatná odchylka
sigma_x = √( var(X) )  

### Věta o rozptylu a střední hodnotě
var(X) = E(X^2) - E(X)^2  

### Věta o rozptylu
var(aX+b) = a^2 . var(X)  

### Věta o střední hodnotě a pravděpodobmosti
E(X) = SUMA _od nuly ^do nekonečna ( P(X>n) )

### Def. Sdružená pravděpodobnostní funkce
Diskr. n. v. X,Y ... náh. vektor (X,Y)  
P(X,Y) : R^2 -> [0,1]  
P_x,y()


## 05 L
D.N.V. X ... fce: Px(x)=P(X=x)  
-> lze určit střední hodnota ... EX = SUMA (xPx(x)) nebo Eg(X)=SUMA (g(x)Px(x))

P_X,Y(x,y) = P(X=x & Y=y) = P( {w:X(w)=x & Y(w)=y} ), kde {w:X(w)=x & Y(w)=y} je z *F*

### Def.: Nezávislost X,Y
Dvě d. n. v. X,Y jsou nezávislé právě tehdy, když pro všechna x,y: {X=x} a {Y=y} jsou nezávislé jevy.  
To je také ekvivalentní tomu, že P(X=x & Y=y) = P(X=y)*P(Y=y)

Příklad:  
Na kostce...  
p, že i: Pi>=0, SUMA_1^6 (Pi) = 1  
P(Xi = k1, ... X6 = K6)  

To, že padnou samé jedničky není nezávislé na tom, že padnou samé dvojky

Multinomické rozdělení ... 

### Marginální rozdělení

P_X1(k_i) = SUMA_(k1...Kn) P(Xi...n) (k1 ... k6) = ... = (n nad ki).Pi^(ki).(1-p)^(n-ki)

Příklad:  
g(x,y) = x+y  
P(X+Y=3)=... konvoluce  

### Věta ("o konvoluci náhodné veličiny")
Pokud X a Y jsou nezávislé, pak P(X+Y=z) = SUMA_x (PX(x)PY(z-x)).  

### Věta ("o konvoluci střední hodnoty")
E[g(X,Y)] = SUMA (g(x,y).P(X,Y)(x,y)), má-li součet smysl.  
... protože [LOTUS](#věta-o-střední-hodnotě-d-n-v-funkce-lotus)

### Věta o linearitě střední hodnoty
E[X+Y]=E[X]+E[Y]  

Důkaz:  
g(x,y)=x+y  
E[X+Y]=E[g(X,Y)]=SUMA_(x,y) ((x+y).P(X=x & Y=y)) = SUMA_x,y (x.P(X=x, Y=y) + SUMA(y.P(...))  
= EX+EY  

### Věta o součinu střední hodnoty
Když X,Y jsou **nezávislé** náhodné veličiny, pak E(X.Y)=(EX).(EY)  

Důkaz:  
h(x,y) = x.y  
E(XY)=SUMA_(x.y) (P(X=x, Y=y)) = SUMA_x (xPx(x)).SUMA_y(yPy(y)) = EX.EY  

### Věta o rozptylu součtu
var(X+Y)=var(X) + var(y) + 2cov(X,Y)  

Dlouze:  
var( SUMA_i=1^n (Xi) ) = SUMA_i,j=1^n (cov(Xi,Xj)) =  
= SUMA_i=1^n (var(Xi)) + SUMA_i!=j (cov(Xi,Xj)) = 
= SUMA_i=1^n (var(Xi)), pokud X jsou po dvou nezávislé.

E[(X+Y)^2] = E(X^2+2XY + Y^2)
E[(X+Y)^2] = EX^2 + EY^2 + 2(EX)(EY)

### Def.: Kovariance
cov(X,Y)=E(X,Y)-E(X)(E)  

Pozorování!  

Příklad na úvod:  
X~Bin(m,p)  
Y~Bin(n,p)  
X,Y jsou n.n.v.  

Z=X+Y  
Pz=?  

Pz(k)=  

SUMA_x=0^k (Px(x).Py(k-x))=  
SUMA_x^k (m nad x).p^x.(n nad k-x).p^k-x.(1-p)^(n-(k-x))=  
p^k.(1-p)^m-n-k.SUMA_t (m nad x).(n nad k-x)=  

p^k.(1-p)^m-n-k.(m+n nad k)  

### Značení
P_(X|A) (x) = P(X=x|A)  
P_(X|A) (x|y) = P(X=x|Y=y)  


## 06 L Obecné náhodné veličiny
### Def: Náhodná veličina
X:OMEGA->*R* t.ž. Vx z *R*: {w z OMEGA: X(w)<=x} z *F*  

(Značení: {w z OMEGA: X(w)<=x}={X<=x})

Pozorování:  
{X<=x}=U_(x'<=x){X=x'}

### Def: Distribuční funkce
Fx(x)=P(X<=x)

### Def: Spojitá n.v.
X je spojítá n.v., pokud existuje fx:*R*->[0,infinity) t.ž. Fx(x) = ∫_-INFINITY^x (fx(t)) dt

### Věta X má hustotu fx
1) P(X=x)=0, Vx z *R*  
2) P(a<=X<=b) = ∫_a^b (fx(t)) dt, Va < b
3) V rozumnou A: P(X z A) = ∫_A f(x)

Příklad:  
Uniformní rozdělení U(a,b)  
pro -nek ... a -> 0  
pro a ... b -> 0,1  
pro b ... nek -> 1  

### Exponenciální rozdělení
Exp(λ)  

F(x)=  
1-e^(-λ.x) pro x>=0,  
0 pro x<=0

f(x)=F'(x) když NLSS.  
f(x)=λ.e^-λ.x

### Def: střední hodnoty
X je spojitá n.v. s hustotou *fx* .  
Pak E(X)=∫ (x.fx(x)), pokud na intervalu dává funkce smysl.  

Pro diskrétní n.v. zase suma (*xPx(x)*)

## 07 L
### Opakování n.v.
X: Omega -> *R*  
EX = ∫ _-Inf^Inf (xF_X(x)) dx  
Fx(x) = ∫ _-Inf^x (f_X(t)) dt  

### Linearita střední hodnoty platí i zde
Platí i zde. (E(aX+bY)) = aEX + bEY

### Příklady rozdělení
#### X ~ Exp(λ)  
F_X(x) = 1-e^(-λ.x)  
f_X(x) = F_X'(x) = λ.e^(-λ.x)  

test, zda f je hustota:  
INTEGRACE.

EX = ∫(od -Inf do Inf)(x.F_X(x)) = ∫(λ.x.e^-λ.x) = 1/λ  
var(X) = 2/λ^2 - 1/λ^2 = 1/λ^2  

#### X ~ Geom(p)

Y ... čas, kdy se rozpadne atom U  
Pravděpodobnost, že P(Y>nd) = (e^(-λ))

#### X ~ ϕ(x) Standardní normální rozdělení
ϕ(x) = 1/(√2π)  
φ ... primitivní funkce k funkci ϕ  

dva parametry , mí a sigma
Z = (X-mí) / sigma

#### Cauchyho rozdělení
f(x) = 1/(pí(1+x^2))  

#### Kvartilová funkce
X ... n. v.  
Q_X: [0,1] -> *R*  
Q_X(p) = min{x z *R*: p<= F_X(x)}  
F_X ... spojitá a rostoucí => Q_X = F_X^(-1)

## 08 L
### Věta o celkové hustotě pravděpodobnosti (o celkové střední hodnotě)
X ... s.n.v., B1,B2,B3 ... rozklad X  
E(X)=SUMA(PBi.E(X|Bi)) = INTEGRÁL_-inf^+inf(x.fX|Bi(x))  
= INTEGRÁL_-inf^+inf(x.fX(x))  

Příklad :)  
p ... z (0,1)  
Qx(p) = min{x náleží *R*: p<=FX(x)}   


### Věta
X je n.v. s distribucí FX=F, F je spojitá & rostoucí  
Pak F(X) ~ U(0,1)  

### Věta
F je funkce "typu distr. funkce"    
Q je odpov. kvartilová funkce.  
U ~ U(0,1), X = Q(U)  
Pak FX=F

Víme, že  
QX(p) =< x
<=>
p <= FX(x)

P(Q(U) <= x) =? F(x)

Př.:  
Exp(lambda)  
F(x) = 1-e^(-lambda.x)  

### Def.: Náhodný vektor (X,Y)
(na (OMEGA, *F*, P)) je dvojice n.v.  
t. ž. Vx,y z *R* je definována.  
F(X,Y)(x,y)=P(X<=x&Y<=y)  

### Def.: Vícerozměrná distribuční funkce
F_X,Y(x,y) = INTEGRÁL_-inf^x ( INTEGRÁL_-inf^y( f_X,Y(s,t) )dt )ds  

d^2/(dxdy) ... Derivace podle x a pak podle y

### Vícerozměrné normální rozdělení

### Věta
X,Y n.n.v. spojité  
Pak Z=X+Y je také spojitá  
a f_Z(z) = INTEGRÁL_-Inf^+Inf (f_X(x)f_Y(z-x)) dx

∫λφϕ√∑π