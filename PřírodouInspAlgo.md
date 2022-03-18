# Přírodou inspirované algoritmy
Martin Pilát
[Stránky předmětu](http://ktiml.mff.cuni.cz/~pilat/cs/prirodou-inspirovane-algoritmy/)

Kačka Macková
[Stránky cvičení](https://github.com/kackamac/Prirodou-inspirovane-algoritmy)
katerina.mackova@ktiml.mff.cuni.cz

### Obsah
[Přírodou inspirované algoritmy](#přírodou-inspirované-algoritmy)
 - [01 Úvod a algoritmy obecně](#01-úvod-a-algoritmy-obecně)
 - [Zpětnovazebné učení](#02-zpětnovazebné-učení)
 - 

### Podmínky
- zápočet za cvičení
  - 3 úkoly (5, 8 a 11 cvičení)
- zkouška ... [požadavky](http://ktiml.mff.cuni.cz/~pilat/cs/prirodou-inspirovane-algoritmy/pozadavky/)
  - obecně výběr techniky a způsob řešení problému

### Zdroje
Každá přednáška má souvislý text!

## 01 Úvod a algoritmy obecně
[přednáška](http://ktiml.mff.cuni.cz/~pilat/cs/prirodou-inspirovane-algoritmy/umela-inteligence-vypocetni-inteligence-aplikace/)

### Co je AI?
 - vytváří agenty, které jsou schopny se samostatně chovat
 - AI má nějaké vstupy a má nějaký cíl
#### Symbolická AI
 - využívá formální popis světa, na základě toho AI reaguje
 - využívá plánování
   - S ... počet stavů
   - A ... akce (jméno, předpoklady, + efekty, - efekty)

#### Výpočetní AI
 - Machine Learning
   - Stromy, k-means, etc.
   - neurální sítě ... hluboké učení
 - Evoluční algoritmy (EA), přírodou inspirované algoritmy

#### Obecná AI
 - není specifická, má hodně obecný záběr

### Neurální síť ... NS
 - neurony ... x vstupů, funkce, výstup
   - vstupy vydráždí neuron, neuron dá něco na výstup
   - mají ***lineární funkce***
Příklad:
```txt
neuron ... n
vstupy ... x1...x4
funkce neuronu ... sgn(SUM_Vx(xi))
```

***Často používané funkce***
 - Sigmoida ... sigmoid(x) = 1/(1+e^(-lx))
   - l ... parametr
 - Rectified Linear Unit ... ReLU(x) = max(0,x)

### Historie

#### Historie perceptronů
***1959 Rosenblat***
- vymýšlí "perceptron" (typ základní komponenty NS)
***1970-85***
***Martin Minsky***
 - argumentuje proti perceptronu... nedokáže např. XOR!?
  - jde obejít tím, že se dá víc perceptronů dohromady
  - Minsky si ale myslí, že nikdy nebude algoritmus, který by NS učil sám

1985 ... obnovení zájmu
2000 + ... nejlepší výsledky v AI

#### Historie evolučních algoritmů
- už konec 70. let
- genetický algoritmus cca polovina 80. let
- dnes se používají i k návrhu elektrických obvodů etc.

### Strojové učení a optimalizace
 - jde o to nastavit **parametry** tak, aby co nejlépe **odpovídaly datům**
 - dělení (3):
   - *s učitelem*
   - *bez učitele*
   - *zpětnovazebné učení*

#### Učení s učitelem
 - jsou zadané objekty a jsou známé výstupy
 - algoritmus musí najít model, který pro daný objekt najde správný výstup
 - kategorické učení ... jde o to rozlišit kategorii objektu
 - regrese ... jde o to najít číselnou hodnotu pro daný objekt (ocenění domu etc.)

#### Učení bez učitele
 - jsou zadány objekty, ale ne výstupy
 - cílem je
   - naučit sdružovat objekty do skupin (shlukování)
   - generování nových objektů (generativní modely)

#### Zpětnovazebné učení
 - cíl je naučit agenta, aby došel k co nejlepšímu výsledku
 - využívání předchozích pokusů a porovnávání jejich výsledků

### Aplikace a výsledky
 - megaaa!
 - SuperMario,
 - Evoluční anténa,
 - popisky obrázků,
 - GO, StarCraft a další!

### Třídicí algoritmy
 - 

## 02 Zpětnovazebné učení
 - agent dělá akce v prostředí a získává zpětnou vazbu
 - cyklus ... (stav st, odměna rt) -> akce at -> t = tm
 - Mountain Car

### Typy prostředí
 - spojité x diskrétní
 - prozkoumatelné x neprozkoumatelné
 - statické (deterministické) x dynamické
 - ...

### Markovské rozhodovací procesy
MDP ... Markovovské rozhodovací procesy
*(S,A,P,R)* ... (stavy, akce, přechodová funkce, odměny (Ra(s,s')))  
*P* ... pro stavy *s*,*s'* a akci *a* je přechod mezi nimi pravděpodobnost *P_a(s,s')*  
Pravděpodobnost musí splňovat Markovskou podmínku.  
strategie ... pí(s,a) ... pravděpodobnost, že ve stavu *s* provedu akce *a*  

> Pokud píšu něco jiného než co říkám, raději mi to řekněte. Správně je totiž pravděpodobně to, co si myslím, což je možná něco úplně jiného. -- Martin Pilát. 24/2/2022

### Výroba optimální strategie
Jde o to maximalizovat odměnu, kterou agent dostane.
Dělá se to pomocí strategie. Ohodnocení strategie je dané vzorečkem:  
![vzorecek strategie](OhodnoceniStrategieMarkovovskeUceni.png)  
Cílem učení je pak najít nejlepší strategie.  

Cíl je najít strategii *pí\** takovou, aby V^pí* = max_pí(V^pí(s))

### Monte-Carlo metody

### Q-učení

## 02 P
Přechodové funkce -- ***S,A,P,R*** -> *Markovský rozhodovací proces*  

## 03 L Ještě strojové učení a úvod do evolučních algoritmů

### Problém: OneMAX
Máme posloupnost {0,1}^n, maximální počet jedniček.
0101101001 ... 5
1011101111 ... 8
1111111111 ... 10  ... hey!

Každá posloupnost ... jedinec  
Počet jedniček ... fitness funkce  
Jde o to: (... genetické učení)   
1. vygenerovat populaci,
2. selektovat nejlepší jedince,
3. skřížit nejlepší jedince ... např. jednobodové - v jednom bodě crossover (1011 + 1101 -> 1001 + 1111)
4. mutace (flipování)
5. jít na `1.`

### Selekce  
+ ruletová selekce
  + Pi=(fi)/∑(fj) ... ale fitness musí být >= 0)
  + malé rozdíly ve fitness mají poměrně malé rozdíly v šanci být přijaty
+ spravedlivá ruletová selekce
  + je vybrán 1. jedinec a druhý je vybrán pomocí jiné funkce
+ turnajová selekce
  + vybere se lepší ze dvojice jedinců (s určitou pravděpodobnoctí)

+ ***elitismus*** ... necháme rodiče také ve skupině pro selekci
+ *explorace* ... jak moc jdeme do prostoru
+ *exploatace* ... vylepšování nalezeného místa v prostoru

### Křížení
+ bodové (+ dvoubodové, tříbodové ...) ... zvolí se bod a prohodí se příslušné sekvence obou jedinců
  + uniformní křížení ... rozhodování pro každou pozici v sekvenci

## 04 L Spojitá a kombinatorická optimalizace

### Celočíselné kódování
- kódování jedince pomocí celých čísel
- většina věcí u celočíselného kódování se neliší od binárního kódování

***Příklad:***  
Jde o to rozdělit čísla z množinu A na k podmnožin se stejným součtem.  

Množina A obsahuje N přirozených čísel čísel,  
pro n z A platí, že leží v intervalu <0,k-1>  
k je přirozené číslo  

Pozice i ve vektoru jedince pak reprezentuje číslo z A a hodnota na dané pozici určuje, v jaké podmnožině se číslo nachází.  

### Permutační kódování
 - speciální případ celočíselného kódování
 - jedinec je kódován opět jako seznam čísel od 0 do k, zároveň se ale musí v jedinci objevit jen právě jednou

Příklad:  
Problém obchodního cestujícího, permutace dává pořadí vrcholů.  

- permutační kódování se ale používá i pro jiné problémy, nebo jako součást řešení většího problému

Příklad:  
Bin packing problém ... naskládání objektů daných velikostí (mezi 0 a 1) do přihrádek velikosti 1.  
Heuristika ... postupné přidávání objektů, permutace dává pořadí objektů  

- problém je vytvoření operátorů
- mutace může prohazovat dvě různé pozice, invertovat část jedince, nebo přesunout větší celky na jiné místo
- křížení
  - Order Crossover ... prohodí prostřední část rodičů
    - zbylé pozice doplní podle jejich pořadí v rodičích
  - Partially Mapped Crossover (PMX) ... prohodí se prostřední část rodičů, doplní se chybějící pozice, to, co je duplicitní nahradíme hodnotou z rodiče 
- Edge Recombination ... pro problém obchodního cestujícího
  - kombinace hran řešení, nikoli vrcholů
  - postupuje se podle toho, kolik má daný vrchol sousedů - od nejmenšího po největší

### Spojitá optimalizace - kódování pomocí reálných čísel
Optimalizace funkcí *R*^n -> *R*  

- mutace
  - biased ... vychází z hodnoty na dané pozici. Např. podle gaussovského rozdělení.
  - unbiased ... prostě generace nového čísla
- křížení ... aritmetické křížení / n bodové mutace

- separabilní funkce - je možné je optimalizovat po složkách
  - hledání umístění elipsy -- osy rovnoběžné s osami -> separabilní, jinak neseparabilní

## 05 Evoluční algoritmy - genetické programování
Složitější, než jedinec = vektor.  

### Genetické programování
- programy pomocí evolučních algoritmů automatiky

#### Lineární genetické programování
 - jedinec jako posloupnost instrukcí,
 - jedinci nemusí mít stejnou délku, ale jinak operace fungují docela normálně

#### Kartézské genetické programování
 - jedinec kóduje program na mřížce *r* × *l*,
 - jedinec je vektor r x l genů
 - gen
   - jméno funkce, kterou počítá
   - indexy do předchozích vrstev, odkud bere vstupy
 - jedinec bere vstupy do první vrstvy
 - na každý výstup jedinec obsahuje index, kde se v něm tento výstup počítá

 - mutace většinou mění funkci a její vstupy / výstupy

#### Gramatická evoluce
- využívá se formální zápis syntaxe jazyka pomocí bezkontextové gramatiky
- jedinec jako posloupnost čísel, která udává pravidlo gramatiky
- když je jedinec moc krátký a po jeho zpracování zbudou ještě nějaké terminály - pak nemůže být vyhodnocen
  - snažíme se generovat delší jedince
  - rodiče vždy vytvoří validního potomka

#### Stromové genetické programování
- "běžné" genetické programování
- jedinec je strom s funkcemi v uzlech (neterminály) a v listech vstupy a výstupy (terminály)
- mutace prohazují hrany, podstromy etc.
- jak s číselnými konstantami?
  - základní konstanty ... 0,1,2,...
  - operátory podobné jako u spojité optimalizace
- automaticky definované funkce - vytváříme vlastní funkce

#### Evoluce pravidel
- strojové učení a evoluce klasifikačních pravidel
- jedinec ... množina pravidel pro klasifikaci zadaných vstupů
- vstup ... vektor n čísel -> jedinec ... (c1,c2,cn)->*k*
  - pokud pri každé i z n platí podmínka ci, pak objekt je třídy *k*
- když vstup splňuje více pravidel
  - můžeme nechat pravidla hlasovat
  - zvolíme tu nejčastější třídu
  - nebo můžeme zvolit první možnost
- křížení ... kombinace pravidel rodičů
- mutace ... měnit třídu pro dané pravidlo, podmínky, měnit váhy pravidel



