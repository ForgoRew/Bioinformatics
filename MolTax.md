## 1  Introduction, taxonomy, molecular characters, sekvencing of DNA (Hampl)
(2. 10.)
- [stránky předmětu](https://web.natur.cuni.cz/~vlada/moltax/)
- [SIS](https://is.cuni.cz/studium/predmety/index.php?id=8beb51c264f7ea1e2dbc022d010b1e3b&tid=&do=predmet&kod=MB160P21&skr=2023)
- [moodle](https://dl2.cuni.cz/course/view.php?id=2132)
  - heslo "moltax"

- motivace
  - taxonomie organizmů se dělá pomocí jejich fylogenetiky
  - předpoklad - existuje cosi jako "Tree of Life"
    - úplný fylogenetický strom všech organizmů
    - nevytváříme "TOL", ale jen hypotézu, jak asi mohl vypadat
    - kritérium pro to, že jsou **dva organizmy ve stejné skupině** je, že **sdílí společného předka**

- **TAXA**
  - **monofyletické** - ptáci + plazi (ty hledáme)
  - parafyletické - plazi - ptáci (někdy stačí tyto)
  - polyphyletické - algae (mají plastidy, nic to neříká o jejich společném předku)

- na základě fylogenetického stromu je možné vytvářet taxony, ale není praktické ustanovovat všechny monofyletické taxony - je jich příliš mnoho

- characters
  - **character** (např. přední končetina)
    - quasi-independent
    - znak, který můžeme vyčlenit z organizmu a je jakoby nezávislý na zbytku těla
  - **character-state** - jak vypadá konkrétní končetina, např. velryby nebo psa
  - molecular characters - každé "písmeno" v sekvenci např. DNA je *character*
    - character state na dané pozici je konkrétní reziduum (adenin, guanin...)

- homology
  - definice - **Riedl and Hazsprunar**
  - podobnost mezi komplexními strukturami (podobnost mezi křídly létavých obratlovců)
  - podmínkou pro označení "homologie" je, že je podobnost zapříčeněná evolučně
  - homology of character × homology of character state
    - !!
  - homologii indikuje
    - podobná pozice v sekvenci u alignmentu
    - podobnost v detailech
  - homologii rozbíjí
    - přítomnost dvou stavů

- brain excercise

- homology of character states
  - auxiliary principle -> homologie mezi dvěma character states je indikována jejich podobností
  - proti tomu může stát to, že v kontextu dalších character states je homologie nepravděpodobná

- fenetics (similarity)
  - používá

- plesiomorphy - znaky předka
- synapomorphy - pro dané skupiny se společným předkem se ve společném předkovi znak změnil
- synplesiomorphy - inverzní synapomorphy - v synapomorphii jsou skupiny, které naopak nemají společný znak
- autapomorphy - jako synapomorphy, jen pro jednu skupinu
- homoplázie - falešná homologie - u dvou nezávislých taxonů se objeví stejný znak

- approaches - character state usage in phylogenetics
  - numerical taxonomy (1960)
  - phenetic approach - míchání znaků dohromady, hledání jejich podobností
  - maximum parsimony

- molecular taxonomy
  - taxonomy (systematics) using molecular characters
  - DNA/protein

- drift
  - neutrální alely (frekvence v populaci) se pohybují náhodně


## 2. Sequence alignment
- alignment
  - informace o funkci
  - o struktuře
  - o evoluci sekvence

- když najdeme podobné sekvence
  - náhoda
  - analogie
  - homologie

- 2 nehomologní proteiny
  - pokud mají alespoň 100 AK ...
  - tak jejich sekvenční identita je téměř jistě menší než 35%
    - >35% ... likely homolog
    - 20-35% ... "twilight zone"
    - <20% ... midnight zone
  - homologie je tranzitivní relace

- proteiny jsou lepší než DNA
  - DNA je by chance mnohem podobnější než proteiny
  - genetický kód je degenerovaný
  - někdy ale není vyloženě jiná možnost

- skórovací matice
  - PAM ... Margaret Dayhoff
    - log odds ratio
  - BLOSUM
    - derived from blocks of sequences
    - number means the percentage of identities between sequences in the blocks
  - PAM 120 ~ BLOSUM 62

- Needleman & Wunsch 1970
  - alignment table
  - backtracking
    - zjišťování, z jaké pozice jsem pro danou pozici vyšel

- MSA
  - ClustalW, T-Coffee
  - Clustal Omega
  - MAFFT - used for phylogeny
    - FAMSA - derived from MAFFT
  - HMM methods ... HHMER, HH_suite
  - Machine Learning methods..?

- structure alignment (better than sequence alignment..?)
  - Foldseek/structural alignment ... works?

- sometimes we need to modify the alignment by ourselves

## 3.

### Whole genome
- nemožnost alignovat celý genom
- pro taxonomii jsou jiné metody, které umožňují porovnávat genomy a vytvářet stromy

- databáze
  - zpravidla veřejné - není samozřejmost
  - easy to find
  - FAIR
    - findable,
    - accessible,
    - interoperable - enough data to identify relations of the item (connect with e.g. the same item in different database/old experiment),
    - reusable
  - attributes
    - frequency of data update - might be a red flag
    - frequency of software update - might be a red flag too
    - redundancy
    - tools to analyze the data
      - databases are novadays not only bunches of data
    - annotation of data

- examples
  - DNA databases
    - GenBank (NCBI)
    - ENA (EBI)
    - DDJB (Japonsko)
  - genome databases
    - lot of them, e.g.
    - Ensembl (EBI)
      - high quality genomes
      - many tools
      - divided into groups
        - Plants, Fungi, Protist, Bacteria, Metazoa...
    - PGD (Pineapple Genomic Database)
    - VGP
      - all vertebrates (~70 000 genomes)
      - data on Amazon cloud
    - Earth Biogenome Project
      - 60PB of data
  - protein databases
    - UniProtKB
      - SwissProt (annotated)
      - TrEMBL (not human-curated)
    - BFD - Big Fantastic Database
      - 10x bigger than UniProt
    - MGnify
      - also 10x bigger than Uniprot

- Database search
  - FASTA
  - BLAST
    - BLOSSOM 62 table

- P-value
  - probability, that the two sequences are similar randomly
- E-value (database P-value)
  - = P-value×[size of database]
  - probability, that the databases are found randomly in a database of given size

* Chris Sander
  * sequence identity of
    * random alignments - 5.6%
    * remotely homologous alignments - 8.5%

* Smith-Waterman
  * local-alignment

* Better tools than BLAST
  * profiles - families - PSI-BLAST
    * Marian popisuje jiný styl dělání skóre pro PSSM
  * HMM models
    * umí zahrnout i insert a delete stavy
    * HMMER
      * vlastní webovky
      * může se hledat i mezi jednotlivými HMM pro jednotlivé rodiny
      * MMseqs2
        * vyhledá pomocí HMM 10000 sekvencí, ty zalignují pomocí SW a drtivou většinu zahodí
        * podobná senzitivita jako BLAST, ale 10x rychlejší
        * výhodné pro giga databáze (BFD, MGnify)

## 04 Other methods to obtain molecular data

### DNA-DNA hibridization
- Jak dobře na sebe nasednou různé DNA sekvence
  - 5% sekvenční rozdíl
  - pro 30% pokles **Tm** (medium melting temperature = kdy jsou schopné řetězce na sebe nasednout)
  - **heteroduplex** - dvě různá DNA na sebe spárovaná
    - měří se **Tm**
  - pracné, musí se měřit každá sekvence s každou z datasetu

### ORGI (Overall genome relatedness indices)
- jednoduchá metoda na to, jak moc jsou si blízké sekvence
- lepší (a rychlejší) než DNA-DNA hibridization

- počítání metrik nad alignmenty/sekvencemi
  - **ANI** index - dá se převést na výsledky DNA-DNA hibridizace
    - průměrná sekvenční identita všech homologních regionů, které jsou zjištěné pomocí BLASTN
    - hledají se frekvence 4-merů nukleotidů
  - **GBDP** - průměrná genetická vzdálenost
  - **MUMi** - ratio regionů, které se plně shodují
    - počet regionů s perfektní sekvenční identitou děleno délkou sekvence

### Restriction analyses
- analýza, která zahrnuje štěpení DNA v určitých místech

- **fingerprintové** analýzy
  - postup:
    - štěpení endonukleázou - přesně definovaná místa štěpení
    - elektroforéza - separace - vznikne pattern, vypadá jako barcode, říká se mu **fingerprint**
    - porovnávání různých fingerprintů
  - nedá se moc používat na velké molekuly DNA - moc vysoká komplexita, fingerprint by byl jen velká čára

- **VNTR**
  - variable number of tandem repeats
  - hledáme počty tandemových repetic v určitých místech a porovnáváme navzájem
  - postup:
    - rozštěpíme (lidskou DNA)
    - labelujeme fragmenty obsahující repetice
    - dáme na elektroforézu
    - ty co doputují dál mají méně repetic
    - zobrazí se nám jen repeticové úseky
  - pomocí toho zjistíme příbuznost - repetice (počet) se dědí mendelovsky

### Microsatelites
- **Microsatelites** = **STR - short tandem repeats**
- velmi často se na nich polymeráza "sklouzne" a prodlouží je
- velmi precizní separace na délku
  - polyacrylamide gel, fragment analysis
- dobré pro **populační studie**
- postup:
  - PCR
  - fluorescenční label
  - zjištění kvantity
    - kvůli slidu polymerázy z PCR vyjdou range více peaků - mírně různé počty repetic

### RAPD
- Random Amplified Polymorphic DNA
- amplification - short random fragments
- not good reproducibility - each run different results, not used today

### AFLP
- Amplified Fragment Length Polymorphism

- využití Sangerovy kapilární elektroforézy

- pro velmi blízce příbuzné druhy

### Protein mass fingerprint
- identifikace organismů

- postup:
  - organismus (bacteria)
  - napipetovat je na něco - to rozšmelcuje, i peptidy jsou rozsekány na nějaké kusy
  - udělá se hmotnostní spektrometrie fragmentů peptidů
    - actually možná se ty peptidy nešmelcujou a zůstanou v původní délce
  - získá se **fingerprint**
    - ten je specifický pro každý druh organismu

- často používané v nemocnici! -> jednoduchá a docela levná metoda

### Presence of SINE elements
- to, že je někde SINE ukazuje na synapomorfii -> sdílející druhy jsou pravděpodobně příbuzné
- velmi dobře se díky tomu vytvářejí fylogenetické stromy

### SNPs
- single nucleotide polymorphism
- na jednom místě v genomu druhu je variabilita
- existuje databáze pro modelové i jiné organismy (NLPH of NCBI)

- kategorizace
  - hibridizace - **molecular beacon**
    - hibridizace je indikovaná fluorescencí, proběhne pouze pro danou alelu SNP

- existuje pro to čip, který charakterizuje cca 10^6 SNP v jednom experimentu
- je možné snadno porovnat a najít spoustu SNPs

## 05 Genetic distance estimation
- distance from the fingerprints
  - máme vzdálenost podle
  - Identita - 2*(M - both fingerprints sharind)/(M all in first + M all in second)
  - vzdálenost D ... 1-I

- distance from alele frequencies
  - **Roger's distance**
    - postup:
      - převedení homo/heterozygotů ma frekvenci alel
      - výpočet ze čtverců rozdílů mezi frekvencemi jednotlivých alel
      - $D = \sqrt{\frac{1}{2}\sum(x_{Ai}-x_{Bi}^2)}$
- from sequences
  - **p-distance**
  - **Poisson-Corrected distance**
    - lambda - očekávaný počet mutací za daný interval
    - 
  - Jukes-Cantor
    - potřebujeme pravděpodobnost záměn - získáme z p-distance
  - Kimura - tranzice, transverze
  - 

```py
a='acdse'
b='lcdge'
diff = lambda a,b : sum(1 for x,y in zip(a, b) if x != y)
p_dist = lambda a,b: diff(a,b)/len(a)
#2, 0.4

from math import e, factorial
poiss = lambda l, k: (l**k * e**(-l))/factorial(k)

jukes_cantor_dist = lambda u, t: (-3/4)*log(1-4/3*p)


```

## 6 Nucleotide frequencies & trees
- **Kimura's model**
- **F84 model**
  - equilibrium nucleotide frequencies
    - *pi* values for every nucleotide
    - then we multiply the Kimura matrix by the *pis*
- **GTR**
  - každá ze šesti možných mutací má vlastní parametr
  - frekvence nukleotidů má také vlastní parametry

- **LongDet distance**
  - matice $F_{xy}$
    - počty všech záměn do matice
    - normalizae hodnot na počet
  - pak $d_{xy} = -\ln(\det F_{xy})$

- **PAM**
  - jak vzniká, pro různé hodnoty (PAM 1, PAM 250)

- rooted vs. unrooted tree
- what is the best tree?
  - scoring etc.

- how to find the best tree?
  - algorithms & heuristics

- **UPGMA**
  - postup
    - získání matice vzdáleností mezi vstupními taxony
    - pro každý krok (od 1 do počtu sekvencí)
      - vybereme sekvence s nejmenší vzdáleností
      - vytvoříme jejich rodiče
      - spočítáme vzdálenosti všech sekvencí k rodičovi jako aritmetický průměr vzdáleností původních sekvencí
  - má nevýhody - předpokládá stejnou rychlost evoluce

- **Least Squares**
  - dneska jen jak se počítají vzdálenosti
  - čtverec vzdáleností mezi jedním a druhým stromem

- **Minimum Evolution**
  - vzdálenosti celkem ve stromu

- **Neighbor Join**
  - algorithm for minimum evolution
  - starting with an unresolved tree
  - creating inner branching
  - we make a grouping, which minimises the distances in a tree

# 07
- site substitution rates differ a lot
  - some are more conserved e.g. because of the natural selection
- rozdělení pozic na více kategorií
  - každá kategorie má vlastní rychlost mutace

- **Jin & Nei model**
  - Jukes-Cantor model pro 2 různé rychlosti mutací

### How to search tree space
- někam dáme zkušební
- podíváme se po okolí + popojdeme
- jak se chodí?
  - **NNI**
    - vygeneruje pro daný strom sesterské stromy tím, že prohodí větve
    - ale pro každý "internal node"
  - **SPR**
    - rozdělí strom na dvě části
    - každou část zkusí dát na jiné místo (trochu nechápu)
  - **TBR**
    - podobný jako SPR, trochu jinýý (taky nechápu)
  - **how to choose** the **starting point?**
    - branch & bound space

### Maximum parsimony
- hledá nejmenší množství záměn pro alignment sekvencí
- **Fitch algorithm**
  - pracuje dobře pro rooted i unrooted tree
- **Weighted-Parsimony**
  - jiné skóre pro různé typy záměn
- **Dollo parsimony**
  - používá se pro něco v morfologii
- **Camin-Sokal parsimony**
  - změny pouze v jednom směru (zná původní stav a jak se to později vyvinulo, odhaduje, co se stalo mezi tím)

## 9
* consistent value for maximum likelihood is only in one region while counting the lengths
  * Felsenstein zone

* jak vylepšit (relaxovat modely)?
  * rozdělení míst v sekvenci do několika kategorií - pro každou vytvořím substituční matici
  * kovariace - MrBayes
    * relaxing and freezing
      * různé větve mohou prostě zamrznout na určitých pozicích - pak už nemutují

* consensus tree
  * můžeme střihnout větev stromu
  * nápíšeme si, co za množiny taxonů se nám vytvořilo
  * pokud pro různé stromy vyjdou stejné množiny, jedná se o stejné stromy
  * můžeme vytvořit pomocí 3 pravidel
    * strict consensus - pro více stromů musí být splity úplně stejné, jinak zůstane "unresolved"
    * majority rules
    * extended majority rule

* resampling methods
  * změníme permutací vstupní data
  * mnohokrát (1000x)
  * porovnáme, kolikrát náš první strom bude přítomen
  * some positions will be there multiple times
  * some will be absent

* bootstrap
  * uděláme resampling (cca 1000x)
  * zjistíme, v kolika procentech případů byl přítomen daný split
  * procenta nejsou p-value, ale můžeme je do p-value transformovat (adjustedBP)
  * nevýhody
    * velmi time-consuming
      * kompenzuje např. UFboot

* jackknife
  * jako bootstrapping
  * jen se jenom vyhazují určitý sloupce
  * není už používaný

* Testy stromů
  * delta test - rozdíl likelihoodů dvou stromů
  * můžeme udělat AU test
    * spočítáme likelyhoodů pro jednotlivé části stromů
    * mnohokrát spočítáme celkový likelyhood s resamplingovanými množinami likelihoodů
    * z toho uděláme delta test
    * procento případů, kdy delta vyšší než nula je p-value
