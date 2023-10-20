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
    - 
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


- 