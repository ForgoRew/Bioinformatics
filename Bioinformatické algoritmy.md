# Bioinformatics algorithms
![](https://images.theconversation.com/files/17729/original/md78kkzd-1353034364.jpg?ixlib=rb-1.1.0&rect=0%2C48%2C500%2C243&q=45&auto=format&w=1356&h=668&fit=crop)

- [Bioinformatics algorithms](#bioinformatics-algorithms)
    - [Poznámky:](#poznámky)
- [Otázky ke studiu](#otázky-ke-studiu)
    - [02](#02)
    - [03](#03)
    - [04](#04)
    - [05](#05)
    - [06](#06)
    - [07](#07)
    - [08](#08)
    - [09](#09)
    - [10](#10)
    - [11 Protein structure similarity](#11-protein-structure-similarity)
    - [12 Protein structure prediction](#12-protein-structure-prediction)
- [01 Introduction and overview](#01-introduction-and-overview)
    - [Sequence](#sequence)
    - [Structure](#structure)
    - [Molecular actors](#molecular-actors)
    - [Central dogma of molecular biology](#central-dogma-of-molecular-biology)
    - [Structure (of Peptide)](#structure-of-peptide)
    - [Mathematical description of molecules](#mathematical-description-of-molecules)
    - [Structure-function correlation](#structure-function-correlation)
    - [Similarity principle](#similarity-principle)
    - [Function Example –G-Protein Coupled Receptors](#function-example-g-protein-coupled-receptors)
    - [Course overview -existing nucleotide and protein databases and data formats](#course-overview--existing-nucleotide-and-protein-databases-and-data-formats)
    - [Course overview - dynamic programming](#course-overview---dynamic-programming)
    - [Course overview – sequence alignment](#course-overview--sequence-alignment)
    - [Course overview - MSA (Multiple-Sequence Alignment)](#course-overview---msa-multiple-sequence-alignment)
    - [Motifs](#motifs)
    - [Phylogenetic trees](#phylogenetic-trees)
    - [Protein structure similarity](#protein-structure-similarity)
    - [Protein structure prediction](#protein-structure-prediction)
- [02 DATA sources and formats](#02-data-sources-and-formats)
    - [Sequence databases and file formats](#sequence-databases-and-file-formats)
    - [GenBank](#genbank)
    - [Searching GenBank with Entrez](#searching-genbank-with-entrez)
    - [Searching with FTP](#searching-with-ftp)
    - [File Formats](#file-formats)
        - [GenBank Flat File Format](#genbank-flat-file-format)
          - [Sample of GBFFF](#sample-of-gbfff)
        - [FASTA](#fasta)
        - [VCF](#vcf)
        - [FASTQ](#fastq)
        - [Next](#next)
    - [Protein data banks](#protein-data-banks)
        - [SwissProt](#swissprot)
        - [TrEMBL](#trembl)
        - [PIR](#pir)
        - [UniProt](#uniprot)
        - [ProSite](#prosite)
        - [Pfam](#pfam)
        - [InterPro](#interpro)
    - [Structure databases and data formats](#structure-databases-and-data-formats)
        - [PDB (Protein DataBank)](#pdb-protein-databank)
          - [PDB Format](#pdb-format)
        - [mmCIF](#mmcif)
    - [Protein similarity classification](#protein-similarity-classification)
        - [SCOP - Structural Classification of Protein Structures](#scop---structural-classification-of-protein-structures)
        - [CATH (Class, Architecture, Topology, Homologous superfamily)](#cath-class-architecture-topology-homologous-superfamily)
    - [Programmatic access to data](#programmatic-access-to-data)
- [03 Dynamic programming](#03-dynamic-programming)
    - [Outline](#outline)
    - [Recursion](#recursion)
    - [Dynamic programming](#dynamic-programming)
    - [Dimension of DP problem](#dimension-of-dp-problem)
    - [Matrix Product Ordering (MPO)](#matrix-product-ordering-mpo)
    - [Longest Common Subsequence](#longest-common-subsequence)
- [04 Pairwise sequence alignment](#04-pairwise-sequence-alignment)
    - [Outline](#outline-1)
    - [Motivation](#motivation)
    - [Biological sequences](#biological-sequences)
    - [Hamming distance](#hamming-distance)
    - [Alignments](#alignments)
    - [Editation distance](#editation-distance)
    - [Backtracking](#backtracking)
    - [Operation weighted ED (OWED)](#operation-weighted-ed-owed)
    - [Alphabet-Weight editation distance (AWED)](#alphabet-weight-editation-distance-awed)
    - [Global Sequence Alignment (GA)](#global-sequence-alignment-ga)
    - [Gap penalization in alignments](#gap-penalization-in-alignments)
    - [Needleman-Wunsch](#needleman-wunsch)
    - [Local Sequence Alignment (LA)](#local-sequence-alignment-la)
    - [Smith-Waterman (SW)](#smith-waterman-sw)
    - [Optimizations](#optimizations)
    - [Some flavors of prewiously said](#some-flavors-of-prewiously-said)
    - [Evolutionary nature of sequence alignment](#evolutionary-nature-of-sequence-alignment)
    - [Scoring systems](#scoring-systems)
        - [Probabilistic model](#probabilistic-model)
          - [Random model](#random-model)
          - [Match model](#match-model)
        - [Issues on probabilistic models](#issues-on-probabilistic-models)
        - [PAM matrices](#pam-matrices)
        - [Computation of PAM matrices](#computation-of-pam-matrices)
        - [BLOSSOM matrices](#blossom-matrices)
- [05 Multiple Sequence Alignment](#05-multiple-sequence-alignment)
    - [Outline](#outline-2)
    - [Motivation](#motivation-1)
    - [Hand-made MSAs](#hand-made-msas)
    - [Not "computed" MSAs](#not-computed-msas)
    - [Scoring](#scoring)
    - [Multidimensional dynamic programming](#multidimensional-dynamic-programming)
    - [Computational complexity of MSA](#computational-complexity-of-msa)
    - [Heuristic Algorithms](#heuristic-algorithms)
    - [Progressive alignment methods](#progressive-alignment-methods)
    - [Star alignment](#star-alignment)
    - [SA – time complexity](#sa--time-complexity)
    - [Feng & Doolitle](#feng--doolitle)
    - [Profile/MSA alignment](#profilemsa-alignment)
    - [ClustalW](#clustalw)
    - [Clustal Omega](#clustal-omega)
    - [T-Coffee](#t-coffee)
    - [Iterative refinement](#iterative-refinement)
    - [Barton-Stenberg](#barton-stenberg)
    - [Block-based alignment](#block-based-alignment)
    - [DIALIGN](#dialign)
    - [MAFFT](#mafft)
        - [Version 5:](#version-5)
        - [Version 6:](#version-6)
    - [MUSCLE](#muscle)
    - [BAliBase](#balibase)
- [06 Speeding Up Similarity Search In Protein Databases](#06-speeding-up-similarity-search-in-protein-databases)
    - [Outline](#outline-3)
    - [Motivation](#motivation-2)
    - [Hashing](#hashing)
    - [Chaining](#chaining)
    - [FAST(A)](#fasta-1)
    - [BLAST](#blast)
    - [HSP - High Score Pair](#hsp---high-score-pair)
    - [E-value](#e-value)
    - [Indexing](#indexing)
    - [BLAT](#blat)
    - [SSAHA](#ssaha)
    - [FT#N](#ftn)
    - [Parallelization](#parallelization)
- [07 Hidden Markov Models](#07-hidden-markov-models)
    - [Viterbi algorithm](#viterbi-algorithm)
    - [Forward algorithm](#forward-algorithm)
- [08 Probabilistic alignment](#08-probabilistic-alignment)
    - [FSA - based view of pairwise alignment](#fsa---based-view-of-pairwise-alignment)
    - [Significance of matches](#significance-of-matches)
    - [Waterman & Eggert](#waterman--eggert)
- [09 Patterns, Profiles and Motifs](#09-patterns-profiles-and-motifs)
    - [Consensus sequence](#consensus-sequence)
    - [Patterns](#patterns)
    - [Position specific scoring matrix for profiles](#position-specific-scoring-matrix-for-profiles)
    - [PSSM - weighting](#pssm---weighting)
    - [PSI-BLAST](#psi-blast)
    - [Operating Instructions](#operating-instructions)
    - [Profile Hidden Markov Models](#profile-hidden-markov-models)
    - [Protein Family Databases](#protein-family-databases)
    - [Prosite](#prosite-1)
    - [CDD](#cdd)
    - [Pfam](#pfam-1)
    - [InterPro](#interpro-1)
- [10 Phylogenetics](#10-phylogenetics)
    - [Outline](#outline-4)
    - [Phylogenetics](#phylogenetics)
    - [Trees](#trees)
    - [Phylogeny-related terminology](#phylogeny-related-terminology)
    - [Tree rooting](#tree-rooting)
    - [Phylogenetic tree representation](#phylogenetic-tree-representation)
    - [Phylogenetics procedure](#phylogenetics-procedure)
    - [Molecular markers](#molecular-markers)
    - [Sequence alignment](#sequence-alignment)
    - [Evolutionary distances](#evolutionary-distances)
    - [Fractional alignment difference (p-distance)](#fractional-alignment-difference-p-distance)
        - [Drawbacks](#drawbacks)
    - [Poisson corrected distance](#poisson-corrected-distance)
    - [Jukes-Cantor model](#jukes-cantor-model)
    - [Tree building methods](#tree-building-methods)
    - [UPGMA](#upgma)
    - [Neighbor joining](#neighbor-joining)
        - [NJ – Algorithm](#nj--algorithm)
        - [Star decomposition](#star-decomposition)
    - [Parsimony](#parsimony)
    - [Weighted (generalized) parsimony](#weighted-generalized-parsimony)
    - [Traditional parsimony](#traditional-parsimony)
    - [Boostrapping](#boostrapping)
- [11 Protein structure similarity](#11-protein-structure-similarity-1)
    - [Background](#background)
    - [Pairwise protein structure similarity task](#pairwise-protein-structure-similarity-task)
    - [RMSD](#rmsd)
    - [Superpositional algorithms](#superpositional-algorithms)
    - [Typical workflow of superposition approaches](#typical-workflow-of-superposition-approaches)
    - [Classical Approaches](#classical-approaches)
    - [DALI](#dali)
        - [DALI - Algorithm](#dali---algorithm)
          - [DALI – Monte Carlo (step 5)](#dali--monte-carlo-step-5)
        - [DALI - Scoring](#dali---scoring)
    - [CE](#ce)
        - [CE - Algorithm](#ce---algorithm)
    - [PROSUP, STRUCTAL (TN)](#prosup-structal-tn)
    - [MAMMOTH](#mammoth)
        - [MAMMOTH (cont.)](#mammoth-cont)
    - [FATCAT](#fatcat)
- [12 Protein structure prediction](#12-protein-structure-prediction-1)
    - [Outline](#outline-5)
    - [Motivation](#motivation-3)
    - [Structure → function](#structure--function)
    - [Protein structure prediction tasks](#protein-structure-prediction-tasks)
    - [Protein structure determination](#protein-structure-determination)
      - [X-ray crystallography](#x-ray-crystallography)
        - [X-ray crystallography – quality measures](#x-ray-crystallography--quality-measures)
      - [NMR spectroscopy](#nmr-spectroscopy)
        - [NMR spectroscopy – quality measures](#nmr-spectroscopy--quality-measures)
      - [3D cryo-EM](#3d-cryo-em)
    - [Protein folding](#protein-folding)
    - [Anfinsen’s dogma](#anfinsens-dogma)
    - [Levinthal’s paradox](#levinthals-paradox)
    - [Template existence dependency of tertiary structure prediction approaches](#template-existence-dependency-of-tertiary-structure-prediction-approaches)
    - [Template-less prediction](#template-less-prediction)
### Poznámky:
Pokud najdete label "DANGER ZONE" u některého nadpisu, znamená to, že jsem dost možná nepochopil hlavní pointu toho tématu, takže je to jen nástřel a je fajn se podívat na to do prezentace :D
# Otázky ke studiu
Co bylo u zkoušky?
threading
Affinsenovo dogma
Levinthalův paradox
parsimonie
prohloubení pochopení důležitých MSA algoritmů - ClustalW
výpočet evoluční vzdálenosti
### 02
 - jaké jsou databáze pro genomy?
 - jaké jsou databáze pro proteiny -- a jaká jsou jejich specifika?
 - jaké se používají formáty pro uložení dat o proteinech, genomech, jejich sekvencích a funkcích?
 - proč může být PDB databáze trochu messy?
 - jak se jmenují 2 způsoby taxonomizace proteinů a čím se liší?

### 03
 - jak se projeví dimenze DP problému na složitosti výpočtu?
 - co je to MPO (Matrix Product Ordering)?
 - proč je u MPO výhodnější DP než prostá rekurze?

### 04
 - kolik je AK?
 - jaké jsou jednopísmenné značky AK?
 - jak je definována Hammingova vzdálenost dvou stringů?
 - co je alignment?
 - existuje víc možných alignmentů?
 - co je Levenstheinova vzdálenost?
 - jak spočítat editační vzdálenost?
 - proč se dělá po výpočtu editační vzdálenosti backtracking?
 - dokázal/a bys sama reprodukovat algoritmus pro backtracking?
 - co je to OWED a jak se liší od běžného ED?
 - zkus si udělat cvičení pro OWED, pak půjdeš do alignmentů najisto!
 - jaký je přínos AWED oproti OWED pro dělání alignmentů?
 - jaké jsou 2 rozdíly GA (Global Sequence Alignment) oproti AWED?
 - jak se liší algoritmus pro GA (např. pomocí Needleman-Wunsche) oproti AWEDu?
 - proč je vhodnější použít LA spíš než GA např. pro zjišťování funkce proteinu?
 - jaký je hlavní rozdíl mezi algoritmy NW a SW?
 - jak se jmenuje způsob na zlepšení paměťové složitosti LA na O(n+m)?
 - je výše uvedený způsob ten nejlepší možný?
 - jak se jmenuje způsob na vylepšení časové složitosti a na jakou třídu ji zlepší?
 - co je to "biologically correct alignment"?
 - proč se klade takový důraz na kvalitní "scoring system"?
 - jak se vytvoří skórovací matice pro "probabilistic model"?
 - jaké jsou typy skórovacích matic pro "probabilistic models"?
 - na co se dá použít Random model a na co Match model?
 - na jakém principu jsou vytvořeny substituční matice?
 - je PAM přesná matice? Za jakých podmínek je dostačující?
 - proč vznikl BLOSSOM?
 - jak se BLOSSOM sestrojí? V čem je jiný než PAM?

### 05
 - proč se dělá MSA?
 - jaké jsou dva hlavní způsoby, jak ohodnotit MSA a v čem spočívají?
 - co je hlavní problém DP u MSA?
 - jaké existují typy heuristických MSA?
 - jak funguje progresivní alignment?
 - co je to Star alignment?
 - proč nejspíš vyjde progresivní alignment pokaždé jinak, když různě zvolíme počáteční sekvenci?
 - jakou metodou je možné udělat ten nejlepší "Star alignment"?
 - v čem je lepší Feng & Doolittle než Star alignment?
 - jaké jsou hlavní nevýhody algoritmu Feng & Doolittle?
 - co je Profile/MSA alignment a proč se používá?
 - v čem je vylepšení ClustaluW oproti Feng & Doolittle?
 - co je T-Coffee a jak řeší problém ClustaluW
 - v čem spočívá "iterative refinement"?
 - jak využívá "iterative refinement" metoda Barton-Sternberg?
 - co je hlavní myšlenka "block-based alignment" a co dokáže lépe než předchozí metody?
 - jak přibližně funguje DIALIGN a v čem je podobný "block-based alignmentu"
 - kromě toho, že se v MAFFTu používá FFT - jak vypadá průběh programu?
 - v čem se MAFFT vylepšil ve verzi 5 a 6?
 - jaké jsou 3 hlavní fáze MUSCLE? O co v nich cca jde?
 - co je to BAliBase?

### 06
 - co je hashování?
 - čemu hashování pomáhá?
 - jak funguje chaining?
 - jak funguje algoritmus FASTA?
 - používá se FASTA při každém dotazu na všech proteinech v databázi?
 - jaký "základní" algoritmus FASTA využívá?
 - proč je tak důležitá HSP u vyhledávání v databázích?
 - co je to E-value?
 - k čemu slouží indexing?
 - v čem je BLAT lepší než BLAST?
 - co je to SSAHA?
 - co je to FT#N?

### 07
 - co je to HMM?
 - jak se jmenuje procedura pro odhalování stavu pravděpodobností?
 - co je forward algorithm?
 - jak se najde stav v každém kroku?
 - jak nastavit pravděpodobnosti bez trénovacích dat?

### 08
 - co je to FSA?
 - co dělá algoritmus Waterman&Egghert? A jak funguje?
 - je W&E vůbec na něco dobrý?
 - dá se odhadnout, jestli probabilistický alignment je pravděpodobný?

### 09
 - jak najdeme "Consenzus sequence"? Jaké má výhody a nevýhody?
 - jak vytvoříme "pattern"? (slide 8)
 - jak funguje PSSM?
 - jaký je postup pro PSI-BLAST a jaké má výhody?

### 10
 - co je to ...
   - taxon
   - clade
   - lineage
   - phylogeny
   - bifurcating tree
   - co je kladogram, fylogram a "Newick format"?
 - jakým postupem je možné zakořenit fylogenetický strom?
 - co je potřeba pro "pravdivé" midgroup zakořenění stromu?
 - jak funguje a kdy se hodí "outgroup" zakořenění stromu? evoluce?
 - proč bodová změna nukleotidu v DNA nutně neznamená změnu AK v peptidu?
 - při vytváření fylogen. stromu se vytváří MSA. Jak se jeho tvorba liší od klasického MSA?
 - jak odhadnout "Evolutionary (pairwise) distance" u dvou sekvencí?
 - na základě vlastností mutací při evoluci a znalosti principu p-value (p=D/L) zkus domyslet 3 problémy (drawbacks), které mohou vznikat při delší evoluční době nebo u kratších mutací a při porovnávání délek evoluce dvou různých skupin organizmů
 - jak Poisson corrected p-value umožňuje obejít "drawbacks" u p-value?
 - na jakém principu funguje Jukes-Cantor model?
 - jaké jsou metody pro budování fylogenetických stromů?
 - UPGMA - co tento název označuje?
 - jak se jmenuje algoritmus pro vytváření fylgenetikého stromu, založený na star-decomposition?
 - jak fázi algoritmu Neighbor-Join označuje "branching"?
 - co je to parsimonie?
 - jaké jsou základní dva typy parsimonie?
traditional a weighted (generalized) pasimony
 - v čem se liší distance-based a parsimony-based techniky vytváření fylogenetických stromů?
 - jak se ověřuje "reliability" (důvěryhodnost) fylogenetického stromu?

Poznámky pro vylepšení prezentace:
V prezentaci 4 na slidu 13 je v třetím bulet pointu `D[i,j] -> D[i-1,j]` namísto `D[i,j] -> D[i-1,j-1]`.
V prezentaci u CATH je místo architecture napsáno hierarchy

### 11 Protein structure similarity
 - co označuje hodnota 'RMSD'?
 - co je cílem superpozičních algoritmů?
 - na jakém principu funguje algoritmus DALI a jak uplatňuje metodu Monte-Carlo?
 - v čem se CE liší od DALI a proč má stejnou nevýhodu (rozpoznává struktury v topologickém pořadí)?
 - jaký je základní princip algoritmů PROSUP a STRUCTAL?
 - co je specifické na algoritmu MAMMOTH?
 - jaký má MAMMOTH mechanismus kontroly, že vyšel správně?
 - co je to FATCAT (název ve zkratce to docela vysvětluje)?

### 12 Protein structure prediction
 - jaké jsou tři kroky (structure prediction tasks) k získání predikce 3D struktury proteinu?
 - jaké jsou tři metody pro zjištění struktury proteinu?
 - jaký je princip X-ray krystalografie
 - jaká je princip NMR spektroskopie?
 - jaký je princip 3D cryo-EM (stačí pochopit název :D )
 - co říká Anfinsenovo dogma?
 - co je to Levinthalův paradox a jak se vztahuje k predikci 3D struktury proteinů? 

# 01 Introduction and overview
[Presentation](https://cunicz-my.sharepoint.com/personal/51137390_cuni_cz/_layouts/15/onedrive.aspx?id=%2Fpersonal%2F51137390%5Fcuni%5Fcz%2FDocuments%2Fteaching%2Fbioinfo%2Flectures%2Flecture01%2Dcourse%2Doverview%2Epdf&parent=%2Fpersonal%2F51137390%5Fcuni%5Fcz%2FDocuments%2Fteaching%2Fbioinfo%2Flectures)

### Sequence
1.Introduction, data formats
2.Dynamic programming
3.Pairwise sequence similarity
4.Multiple sequence alignment
5.Efficient search in sequence databases
6.HMMs& probabilistic-based sequence alignment
7.Motif  search in sequence databases
8.Phylogenetic trees construction
### Structure
1.Protein 3D structure similarity
2.Protein tertiary structure prediction
3.(Protein secondary structure prediction)
4.(Protein interactions prediction)
5.(Protein design)
6.(RNA structure similarity algorithms)
7.(RNA structure prediction)

### Molecular actors
Bioinformatics includes:
DNA: ATGC
RNA: AUGC
Proteins: 20 AA

Chemoinformatics is about:
Next chemical agents

### Central dogma of molecular biology
DNA -> RNA -> Peptides
DNA and RNA can make a copy of itself time to time
There are also reverse flows, but very few:
RNA -> DNA (reverse transcription)
But never Peptide to DNA or RNA

### Structure (of Peptide)
Primary - string of chars
Secondary - electrostatic interactions -- O- and NH+ is charged differently
        - repetitive elements from the tertiary structure are called "secondary structure motifs"
Tertiary structure - 3D positions of every atom in macromolecule
RNA has many unexpected secondary structures
Quaternary structure means "protein with its ligands/as a whole" (proteins sometimes bi, tri and more -mers, also both homo- and hetero- mers)

### Mathematical description of molecules
Primary structure - function with alphabet
Secondary structure - Projection of "secondary structure element" (helix or so) on x,y, while x is from the protein and y is also, but x is not y
Tertiary structure - Function, which gives 3D vector to every atom in peptide

### Structure-function correlation
At first, this correlation exists. Function of macromolecules is also driven by its environment conditions.

### Similarity principle
It is proofed, that similarities in some parts of structure of peptide (and also its AA sequence) implies similar function of this peptide.
Global similarity means also similar function and similar positioning of binding sites etc.
Local similarity (e.g. binding sites) is more important than the global similarity.

### Function Example –G-Protein Coupled Receptors
[video better than text](https://youtu.be/K7WSMybZeA8)

### Course overview -existing nucleotide and protein databases and data formats
 - Databases of  DNA sequences
   - GenBank, EMBL-Bank, DDBJ
 - Databases of  protein sequences
   - SwissProt, PIR, UniProt
 - Databases of  protein structures
   - PDB
 - Classification databases
   - Pfam, SCOP, CATH, 
 - API

### Course overview - dynamic programming
Programming technique. Split bigger problem into smaller similar parts, which are easier to compute.
It is widely used in sequence alignment. Many bionformatic techniques include splitting a problem into many sequence alignments.
Also structure prediction or structure alignment techniques include sequence alignment.

### Course overview – sequence alignment
Application of  dynamic programming to DNA, RNA and protein sequence similarity

Basic algorithms:
 - Hamming distance
 - Edit distance
 - Needleman-Wunsch
 - Smith-Waterman
 - Scoring systems

### Course overview - MSA (Multiple-Sequence Alignment)
A way to find interesting, but posibly faint similarities in many proteins.
We can find conserved positions and motives (in DNA, RNA and Proteins).

### Motifs
Motifs are usually the most interesting part of polypeptide. Therefore we want know, if each peptide doesn't have this motif.
First we must find the motif, usually in a group of similar proteins by MSA.
Then we can search for the Motifs sequence pattern in other proteins.

### Phylogenetic trees
It represents evolutionary relationships between ... species.
Leaves are existing species, internal nodes are ancestors and root is the oldest ancestor.

### Protein structure similarity
We can meassure similarity of two proteins in primary, secondary and tertiary structures

### Protein structure prediction
> Protein structure prediction can be viewed as The Holy Grail of
structural bioinformatics since accurate structure prediction could
unleash the full potential hidden in the sequence databases

There are two basic types of methods:
Ab initio - very computationaly expensive
Comparative modeling - using similarity of known proteins and knowledge of their function

# 02 DATA sources and formats
[presentation](https://cunicz-my.sharepoint.com/personal/51137390_cuni_cz/_layouts/15/onedrive.aspx?id=%2Fpersonal%2F51137390%5Fcuni%5Fcz%2FDocuments%2Fteaching%2Fbioinfo%2Flectures%2Flecture02%2Ddata%2Dformats%2Epdf&parent=%2Fpersonal%2F51137390%5Fcuni%5Fcz%2FDocuments%2Fteaching%2Fbioinfo%2Flectures)

### Sequence databases and file formats
DNA:
 - GenBank/RefSeq (NCBI), ENA (EMBL-EBI), DNA Database of Japan (DDBJ)

Proteins:
 - PIR (USA), Swiss-Prot, Uni-Prot KB (Swiss-Prot + PIR + TrEMBL)

Derived databases
 - Pfam, PROSITE, SILVA

### GenBank
Contains anotated collection of nucleotide sequences (DNA, RNA...) + aditional informations about their structure, activity, what they are coding etc.

Again: three main databases - GenBank (NCBI), ENA (EBI), DDBJ (Japan)
 - RefSeq is special case -- it is also under NCBI and is curated collection of proteins, but it has far less nuber of records than GenBank and is limited only to major organisms with enough available data.

### Searching GenBank with Entrez
Its **text based** -- you can put there conditions OR, AND..., of course name of record or keywords and put constraints to the properties of the records

### Searching with FTP
Cloud-like directory system

### File Formats
##### GenBank Flat File Format
Header
- LOCUS - A short mnemonic name for the entry. The line
contains the Accession number, length of molecule, type of
molecule (DNA or RNA), a three-letter reference to possible
Taxonomy, and the date that the data was made public.
- DEFINITION - description of the sequence
- ACCESSION - accession number is a unique, unchanging code
assigned to each entry
- VERSION - primary accession number and a numeric version
number associated with the current version of the sequence data
in the record. This is followed by an integer key (a "GI") assigned
to the sequence by NCBI
- KEYWORDS - gene description
- SOURCE - common name of the organism or the name most
frequently used in the literature
- ORGANISM - formal scientific name of the organism (first
line) and taxonomic classification levels (second and subsequent
lines)
- REFERENCE - articles containing data reported in this entry
- AUTHORS - authors of the citation
- TITLE - full title of citation
- JOURNAL - journal name, volume, year, and page numbers of
the citation
- MEDLINE - Medline unique identifier for a citation
- PUBMED - PubMed unique identifier for a citation.
- REMARK - relevance of a citation to an entry
- COMMENT - cross-references to other sequence entries,
comparisons to other collections, notes of changes in LOCUS
names, and other remarks.
- Features
- SOURCE - contains information about organism, mapping,
chromosome, tissue alignment, clone identification
- CDS - instructions on how to join sequences together to make
an amino acid sequence from the given coordinates. Includes
cross references to other databases
- GENE Feature - a segment of DNA identified by a name.
- RNA Feature - used to annotate RNA on genomic sequence
(for example: mRNA, tRNA, rRNA)
- Sequence

###### Sample of GBFFF
```
LOCUS       SCU49845     5028 bp    DNA             PLN       21-JUN-1999
DEFINITION  Saccharomyces cerevisiae TCP1-beta gene, partial cds, and Axl2p
            (AXL2) and Rev7p (REV7) genes, complete cds.
ACCESSION   U49845
VERSION     U49845.1  GI:1293613
KEYWORDS    .
SOURCE      Saccharomyces cerevisiae (baker's yeast)
  ORGANISM  Saccharomyces cerevisiae
            Eukaryota; Fungi; Ascomycota; Saccharomycotina; Saccharomycetes;
            Saccharomycetales; Saccharomycetaceae; Saccharomyces.
REFERENCE   1  (bases 1 to 5028)
  AUTHORS   Torpey,L.E., Gibbs,P.E., Nelson,J. and Lawrence,C.W.
  TITLE     Cloning and sequence of REV7, a gene whose function is required for
            DNA damage-induced mutagenesis in Saccharomyces cerevisiae
  JOURNAL   Yeast 10 (11), 1503-1509 (1994)
  PUBMED    7871890
REFERENCE   2  (bases 1 to 5028)
  AUTHORS   Roemer,T., Madden,K., Chang,J. and Snyder,M.
  TITLE     Selection of axial growth sites in yeast requires Axl2p, a novel
            plasma membrane glycoprotein
  JOURNAL   Genes Dev. 10 (7), 777-793 (1996)
  PUBMED    8846915
REFERENCE   3  (bases 1 to 5028)
  AUTHORS   Roemer,T.
  TITLE     Direct Submission
  JOURNAL   Submitted (22-FEB-1996) Terry Roemer, Biology, Yale University, New
            Haven, CT, USA
FEATURES             Location/Qualifiers
     source          1..5028
                     /organism="Saccharomyces cerevisiae"
                     /db_xref="taxon:4932"
                     /chromosome="IX"
                     /map="9"
     CDS             <1..206
                     /codon_start=3
                     /product="TCP1-beta"
                     /protein_id="AAA98665.1"
                     /db_xref="GI:1293614"
                     /translation="SSIYNGISTSGLDLNNGTIADMRQLGIVESYKLKRAVVSSASEA
                     AEVLLRVDNIIRARPRTANRQHM"
     gene            687..3158
                     /gene="AXL2"
     CDS             687..3158
                     /gene="AXL2"
                     /note="plasma membrane glycoprotein"
                     /codon_start=1
                     /function="required for axial budding pattern of S.
                     cerevisiae"
                     /product="Axl2p"
                     /protein_id="AAA98666.1"
                     /db_xref="GI:1293615"
                     /translation="MTQLQISLLLTATISLLHLVVATPYEAYPIGKQYPPVARVNESF
                     TFQISNDTYKSSVDKTAQITYNCFDLPSWLSFDSSSRTFSGEPSSDLLSDANTTLYFN
                     VILEGTDSADSTSLNNTYQFVVTNRPSISLSSDFNLLALLKNYGYTNGKNALKLDPNE
                     VFNVTFDRSMFTNEESIVSYYGRSQLYNAPLPNWLFFDSGELKFTGTAPVINSAIAPE
                     TSYSFVIIATDIEGFSAVEVEFELVIGAHQLTTSIQNSLIINVTDTGNVSYDLPLNYV
                     YLDDDPISSDKLGSINLLDAPDWVALDNATISGSVPDELLGKNSNPANFSVSIYDTYG
                     DVIYFNFEVVSTTDLFAISSLPNINATRGEWFSYYFLPSQFTDYVNTNVSLEFTNSSQ
                     DHDWVKFQSSNLTLAGEVPKNFDKLSLGLKANQGSQSQELYFNIIGMDSKITHSNHSA
                     NATSTRSSHHSTSTSSYTSSTYTAKISSTSAAATSSAPAALPAANKTSSHNKKAVAIA
                     CGVAIPLGVILVALICFLIFWRRRRENPDDENLPHAISGPDLNNPANKPNQENATPLN
                     NPFDDDASSYDDTSIARRLAALNTLKLDNHSATESDISSVDEKRDSLSGMNTYNDQFQ
                     SQSKEELLAKPPVQPPESPFFDPQNRSSSVYMDSEPAVNKSWRYTGNLSPVSDIVRDS
                     YGSQKTVDTEKLFDLEAPEKEKRTSRDVTMSSLDPWNSNISPSPVRKSVTPSPYNVTK
                     HRNRHLQNIQDSQSGKNGITPTTMSTSSSDDFVPVKDGENFCWVHSMEPDRRPSKKRL
                     VDFSNKSNVNVGQVKDIHGRIPEML"
     gene            complement(3300..4037)
                     /gene="REV7"
     CDS             complement(3300..4037)
                     /gene="REV7"
                     /codon_start=1
                     /product="Rev7p"
                     /protein_id="AAA98667.1"
                     /db_xref="GI:1293616"
                     /translation="MNRWVEKWLRVYLKCYINLILFYRNVYPPQSFDYTTYQSFNLPQ
                     FVPINRHPALIDYIEELILDVLSKLTHVYRFSICIINKKNDLCIEKYVLDFSELQHVD
                     KDDQIITETEVFDEFRSSLNSLIMHLEKLPKVNDDTITFEAVINAIELELGHKLDRNR
                     RVDSLEEKAEIERDSNWVKCQEDENLPDNNGFQPPKIKLTSLVGSDVGPLIIHQFSEK
                     LISGDDKILNGVYSQYEEGESIFGSLF"
ORIGIN
        1 gatcctccat atacaacggt atctccacct caggtttaga tctcaacaac ggaaccattg
       61 ccgacatgag acagttaggt atcgtcgaga gttacaagct aaaacgagca gtagtcagct
      121 ctgcatctga agccgctgaa gttctactaa gggtggataa catcatccgt gcaagaccaa
      181 gaaccgccaa tagacaacat atgtaacata tttaggatat acctcgaaaa taataaaccg
      241 ccacactgtc attattataa ttagaaacag aacgcaaaaa ttatccacta tataattcaa
      301 agacgcgaaa aaaaaagaac aacgcgtcat agaacttttg gcaattcgcg tcacaaataa
      361 attttggcaa cttatgtttc ctcttcgagc agtactcgag ccctgtctca agaatgtaat
      421 aatacccatc gtaggtatgg ttaaagatag catctccaca acctcaaagc tccttgccga
      481 gagtcgccct cctttgtcga gtaattttca cttttcatat gagaacttat tttcttattc
      541 tttactctca catcctgtag tgattgacac tgcaacagcc accatcacta gaagaacaga
      601 acaattactt aatagaaaaa ttatatcttc ctcgaaacga tttcctgctt ccaacatcta
      661 cgtatatcaa gaagcattca cttaccatga cacagcttca gatttcatta ttgctgacag
      721 ctactatatc actactccat ctagtagtgg ccacgcccta tgaggcatat cctatcggaa
      781 aacaataccc cccagtggca agagtcaatg aatcgtttac atttcaaatt tccaatgata
      841 cctataaatc gtctgtagac aagacagctc aaataacata caattgcttc gacttaccga
      901 gctggctttc gtttgactct agttctagaa cgttctcagg tgaaccttct tctgacttac
      961 tatctgatgc gaacaccacg ttgtatttca atgtaatact cgagggtacg gactctgccg
     1021 acagcacgtc tttgaacaat acataccaat ttgttgttac aaaccgtcca tccatctcgc
     1081 tatcgtcaga tttcaatcta ttggcgttgt taaaaaacta tggttatact aacggcaaaa
     1141 acgctctgaa actagatcct aatgaagtct tcaacgtgac ttttgaccgt tcaatgttca
     1201 ctaacgaaga atccattgtg tcgtattacg gacgttctca gttgtataat gcgccgttac
     1261 ccaattggct gttcttcgat tctggcgagt tgaagtttac tgggacggca ccggtgataa
     1321 actcggcgat tgctccagaa acaagctaca gttttgtcat catcgctaca gacattgaag
     1381 gattttctgc cgttgaggta gaattcgaat tagtcatcgg ggctcaccag ttaactacct
     1441 ctattcaaaa tagtttgata atcaacgtta ctgacacagg taacgtttca tatgacttac
     1501 ctctaaacta tgtttatctc gatgacgatc ctatttcttc tgataaattg ggttctataa
     1561 acttattgga tgctccagac tgggtggcat tagataatgc taccatttcc gggtctgtcc
     1621 cagatgaatt actcggtaag aactccaatc ctgccaattt ttctgtgtcc atttatgata
     1681 cttatggtga tgtgatttat ttcaacttcg aagttgtctc cacaacggat ttgtttgcca
     1741 ttagttctct tcccaatatt aacgctacaa ggggtgaatg gttctcctac tattttttgc
     1801 cttctcagtt tacagactac gtgaatacaa acgtttcatt agagtttact aattcaagcc
     1861 aagaccatga ctgggtgaaa ttccaatcat ctaatttaac attagctgga gaagtgccca
     1921 agaatttcga caagctttca ttaggtttga aagcgaacca aggttcacaa tctcaagagc
     1981 tatattttaa catcattggc atggattcaa agataactca ctcaaaccac agtgcgaatg
     2041 caacgtccac aagaagttct caccactcca cctcaacaag ttcttacaca tcttctactt
     2101 acactgcaaa aatttcttct acctccgctg ctgctacttc ttctgctcca gcagcgctgc
     2161 cagcagccaa taaaacttca tctcacaata aaaaagcagt agcaattgcg tgcggtgttg
     2221 ctatcccatt aggcgttatc ctagtagctc tcatttgctt cctaatattc tggagacgca
     2281 gaagggaaaa tccagacgat gaaaacttac cgcatgctat tagtggacct gatttgaata
     2341 atcctgcaaa taaaccaaat caagaaaacg ctacaccttt gaacaacccc tttgatgatg
     2401 atgcttcctc gtacgatgat acttcaatag caagaagatt ggctgctttg aacactttga
     2461 aattggataa ccactctgcc actgaatctg atatttccag cgtggatgaa aagagagatt
     2521 ctctatcagg tatgaataca tacaatgatc agttccaatc ccaaagtaaa gaagaattat
     2581 tagcaaaacc cccagtacag cctccagaga gcccgttctt tgacccacag aataggtctt
     2641 cttctgtgta tatggatagt gaaccagcag taaataaatc ctggcgatat actggcaacc
     2701 tgtcaccagt ctctgatatt gtcagagaca gttacggatc acaaaaaact gttgatacag
     2761 aaaaactttt cgatttagaa gcaccagaga aggaaaaacg tacgtcaagg gatgtcacta
     2821 tgtcttcact ggacccttgg aacagcaata ttagcccttc tcccgtaaga aaatcagtaa
     2881 caccatcacc atataacgta acgaagcatc gtaaccgcca cttacaaaat attcaagact
     2941 ctcaaagcgg taaaaacgga atcactccca caacaatgtc aacttcatct tctgacgatt
     3001 ttgttccggt taaagatggt gaaaattttt gctgggtcca tagcatggaa ccagacagaa
     3061 gaccaagtaa gaaaaggtta gtagattttt caaataagag taatgtcaat gttggtcaag
     3121 ttaaggacat tcacggacgc atcccagaaa tgctgtgatt atacgcaacg atattttgct
     3181 taattttatt ttcctgtttt attttttatt agtggtttac agatacccta tattttattt
     3241 agtttttata cttagagaca tttaatttta attccattct tcaaatttca tttttgcact
     3301 taaaacaaag atccaaaaat gctctcgccc tcttcatatt gagaatacac tccattcaaa
     3361 attttgtcgt caccgctgat taatttttca ctaaactgat gaataatcaa aggccccacg
     3421 tcagaaccga ctaaagaagt gagttttatt ttaggaggtt gaaaaccatt attgtctggt
     3481 aaattttcat cttcttgaca tttaacccag tttgaatccc tttcaatttc tgctttttcc
     3541 tccaaactat cgaccctcct gtttctgtcc aacttatgtc ctagttccaa ttcgatcgca
     3601 ttaataactg cttcaaatgt tattgtgtca tcgttgactt taggtaattt ctccaaatgc
     3661 ataatcaaac tatttaagga agatcggaat tcgtcgaaca cttcagtttc cgtaatgatc
     3721 tgatcgtctt tatccacatg ttgtaattca ctaaaatcta aaacgtattt ttcaatgcat
     3781 aaatcgttct ttttattaat aatgcagatg gaaaatctgt aaacgtgcgt taatttagaa
     3841 agaacatcca gtataagttc ttctatatag tcaattaaag caggatgcct attaatggga
     3901 acgaactgcg gcaagttgaa tgactggtaa gtagtgtagt cgaatgactg aggtgggtat
     3961 acatttctat aaaataaaat caaattaatg tagcatttta agtataccct cagccacttc
     4021 tctacccatc tattcataaa gctgacgcaa cgattactat tttttttttc ttcttggatc
     4081 tcagtcgtcg caaaaacgta taccttcttt ttccgacctt ttttttagct ttctggaaaa
     4141 gtttatatta gttaaacagg gtctagtctt agtgtgaaag ctagtggttt cgattgactg
     4201 atattaagaa agtggaaatt aaattagtag tgtagacgta tatgcatatg tatttctcgc
     4261 ctgtttatgt ttctacgtac ttttgattta tagcaagggg aaaagaaata catactattt
     4321 tttggtaaag gtgaaagcat aatgtaaaag ctagaataaa atggacgaaa taaagagagg
     4381 cttagttcat cttttttcca aaaagcaccc aatgataata actaaaatga aaaggatttg
     4441 ccatctgtca gcaacatcag ttgtgtgagc aataataaaa tcatcacctc cgttgccttt
     4501 agcgcgtttg tcgtttgtat cttccgtaat tttagtctta tcaatgggaa tcataaattt
     4561 tccaatgaat tagcaatttc gtccaattct ttttgagctt cttcatattt gctttggaat
     4621 tcttcgcact tcttttccca ttcatctctt tcttcttcca aagcaacgat ccttctaccc
     4681 atttgctcag agttcaaatc ggcctctttc agtttatcca ttgcttcctt cagtttggct
     4741 tcactgtctt ctagctgttg ttctagatcc tggtttttct tggtgtagtt ctcattatta
     4801 gatctcaagt tattggagtc ttcagccaat tgctttgtat cagacaattg actctctaac
     4861 ttctccactt cactgtcgag ttgctcgttt ttagcggaca aagatttaat ctcgttttct
     4921 ttttcagtgt tagattgctc taattctttg agctgttctc tcagctcctc atatttttct
     4981 tgccatgact cagattctaa ttttaagcta ttcaatttct ctttgatc
//
```

##### FASTA
The most basic file format -- only plain sequence with header
```fasta
>seq0
FQTWEEFSRAAEKLYLADPMKVRVVLKYRHVDGNLCIKVTDDLVCLVYRTDQAQDVKKIEKF
>seq1
KYRTWEEFTRAAEKLYQADPMKVRVVLKYRHCDGNLCIKVTDDVVCLLYRTDQAQDVKKIEKFHSQLMRLME LKVTDNKECLKFKTDQAQEAKKMEKLNNIFFTLM
```

##### VCF
Variations (for storing information about subsequences and their variations)

##### FASTQ
Plain sequence with 2 more rows of annotations - quality of reads...

##### Next
SAM/BAM, BED ...

### Protein data banks
##### SwissProt
 - developed by the Swiss Institute of Bioinformatics in 1976 and later by EBI
 - it has minimal redundancy
 - it is anotated and rewieved manually

##### TrEMBL
 - Translated EMBL Sequence Data Library
 - unreviewed
 - created as a space for data, that exceeded the capacity of SwissProt

##### PIR
 - protein information resource
 - established by National Biochemical Resource Foundation in 1984
 - now maintained by Georgetown University Medical Center
 - contains protein databases and search tools, which are for free for scientists
 - Contains Protein Sequence Database (PSD), iProClass (for annotations and information about protein families), PRO (protein ontology)

##### UniProt
 - started in 2002
 - co-founders are EBI, SIB (Swiss Bioinformatics Institute) and PIR

##### ProSite
 - Currated by SIB
 - information about protein classes
 - manually curated
 - good for recognition of new protein function principles (by similarity with some known class)

##### Pfam
 - protein family database based on MSAs
 - using HMMS (hidden markov models)
 - Both manually (Pfam-A) and automatically (Pfam-B) currated

##### InterPro
 - grouping of proteins
 - integrating of member databases

### Structure databases and data formats
##### PDB (Protein DataBank)
 - established in 1971 as community driven effort
 - serves as **primary** resource of experimental structure and functional data
 - also DNA/RNA sequences and structure information can be found there

> PDB records contain (amongst
other information)
- positions of individual atoms in the
3D space
- protein sequence
- secondary structure elements (SSE)
information
- related classification (SCOP, CATH)
- meta-information such as release
date, structure determination data,
etc.

Accessible using:
 - web interface
 - FTP & API

Every record has its unique 4 letter code

###### PDB Format
```pdb
ATOM   1058  N   ARG A 141      -6.466  12.036 -10.348  7.00 19.11           N
ATOM   1059  CA  ARG A 141      -7.922  12.248 -10.253  6.00 26.80           C
ATOM   1060  C   ARG A 141      -8.119  13.499  -9.393  6.00 28.93           C
ATOM   1061  O   ARG A 141      -7.112  13.967  -8.853  8.00 28.68           O
ATOM   1062  CB  ARG A 141      -8.639  11.005  -9.687  6.00 24.11           C
ATOM   1063  CG  ARG A 141      -8.153  10.551  -8.308  6.00 19.20           C
ATOM   1064  CD  ARG A 141      -8.914   9.319  -7.796  6.00 21.53           C
ATOM   1065  NE  ARG A 141      -8.517   9.076  -6.403  7.00 20.93           N
ATOM   1066  CZ  ARG A 141      -9.142   8.234  -5.593  6.00 23.56           C
ATOM   1067  NH1 ARG A 141     -10.150   7.487  -6.019  7.00 19.04           N
ATOM   1068  NH2 ARG A 141      -8.725   8.129  -4.343  7.00 25.11           N
ATOM   1069  OXT ARG A 141      -9.233  14.024  -9.296  8.00 40.35           O
TER    1070      ARG A 141
HETATM 1071 FE   HEM A   1       8.128   7.371 -15.022 24.00 16.74          FE
HETATM 1072  CHA HEM A   1       8.617   7.879 -18.361  6.00 17.74           C
HETATM 1073  CHB HEM A   1      10.356  10.005 -14.319  6.00 18.92           C
HETATM 1074  CHC HEM A   1       8.307   6.456 -11.669  6.00 11.00           C
HETATM 1075  CHD HEM A   1       6.928   4.145 -15.725  6.00 13.25           C
```
More information on 22nd slide of the presentation.
[full pdb file link](https://files.rcsb.org/download/1AOI.pdb)

##### mmCIF
 - used for crystalographic structure of macromolecules
 - has some constraints - not good for high complexity structures

### Protein similarity classification
##### SCOP - Structural Classification of Protein Structures 
Something like taxonomy for proteins!!

> 1. Family
- proteins in the same family can have high sequence similarity (> 30%) or lower sequence similarity (> 15%) with very similar function or structure
2. Superfamily
- proteins sharing common evolutionary origin (based on structural and functional features) but differing in sequence
3. Fold
- structures sharing major secondary structures in similar topological distribution
4. Class
- structures with similar folds
- all 𝜶 - proteins containing mainly (but not exclusively) 𝛼 helices
- all 𝜷 - proteins containing mainly (but not exclusively) 𝛽 sheets
- 𝜶/𝜷 - proteins containing 𝛽 sheet surrounded by 𝛼 helices
- 𝜶 + 𝜷 - proteins containing 𝛼 helices separated by 𝛽 sheets
- small proteins, low resolution protein structures, ..

##### CATH (Class, Architecture, Topology, Homologous superfamily)
> 1. Homologous superfamily
- groups together protein domains which are thought to share a common ancestor and can
therefore be described as homologous
2. Topology
- structures grouped into fold groups at this level depending on both the overall shape and
connectivity of the secondary structures.
3. Architecture
- structures classified according to their overall shape as determined by the orientations of the
secondary structures in 3D space but ignores the connectivity between them
4. Class
- structures classified according to their secondary structure composition
- mostly 𝛼
- mostly 𝛽
- mixed 𝛼/𝛽
- few secondary structures

### Programmatic access to data
 - [UniProt API](http://www.uniprot.org/help/api)
   - retrieve individual records by ids or queries
   - mapping between different formats and databases
 - [Proteins API](https://www.ebi.ac.uk/proteins/api/doc/)
   - Mapping of data from large scale studies to UniProt
 - [PDBe API](https://www.ebi.ac.uk/pdbe/api/doc/pdb.html)
   - Access to PDB records
   - Mapping between UniProt and PDB (SIFTS)
 - [NCBI APIs](https://www.ncbi.nlm.nih.gov/home/develop/api/)
   

# 03 Dynamic programming
### Outline
 - Dynamic programming basics
   - recursion
   - approaches
 - Example problems
   - Fibonacci numbers
   - matrix product
   - longest common subsequence

### Recursion
 - useful, when problem has several subproblems of the same type, but easier to solve (smaller instances of the same problem)
 - usually, it is realized by a function, which calls itself again, but on a smaller part of data

Example:
Factorial: `n! = n*(n-1)!`
Fibonacci: `F(n) = F(n-1) + F(n-2)`
Greatest common divisor, binary search etc.

### Dynamic programming
 - similar to a recursion, but subproblems uses solution of other subproblems, so they don't have to be computed separately
 - Conditions: Optimal solution can be composed by solutions of subproblems, if there are more optimal solutions, we don't care which one we get
 - Tactiques: 
   - Top-down (retains standard recursive top-down structure but storesthe intermediate results)
   - Bottom-up (higher levels share results from the lower levels, DP solutions are often considered only those using bottom-up approach)

> Example: Fibonacci
We create a table, 0...n. The 0 and 1 is filled up. We start at 2 and going to n. For i-th element we only add i-1-th elem. with i-2-th elem. Then on the last place we've got the result of F(n).

### Dimension of DP problem
 - the DP stores a result of subproblem, so we can use it later on
 - by this we avoid remaking again and again the same operation and save comp. time
 - usually n-dimensional array is used for the storing
 - usually we talk about "DP" when n>=2, but Fibonacci from example is nice for ilustration of the technique

### Matrix Product Ordering (MPO)
 - problem of matrix parentization to decrease number of multiplications

### Longest Common Subsequence
 - it is simple example of "alignment", but it is not interesting programmatically, because Aho-Corasick algorithm is better for this

# 04 Pairwise sequence alignment
[presentation](https://cunicz-my.sharepoint.com/personal/51137390_cuni_cz/_layouts/15/onedrive.aspx?id=%2Fpersonal%2F51137390%5Fcuni%5Fcz%2FDocuments%2Fteaching%2Fbioinfo%2Flectures%2Flecture04%5Falignment%2Epdf&parent=%2Fpersonal%2F51137390%5Fcuni%5Fcz%2FDocuments%2Fteaching%2Fbioinfo%2Flectures)

### Outline
 - Motivation
 - Basic string algorithms
   - Hamming distance
   - Edit distance
 - Domain-specific algorithms
   - Needleman-Wunsch
   - Smith-Waterman
   - Scoring matrices

### Motivation
Because we know, that structure corelates with function and sequence is the main thing that affects the structure of protein, by searching for similar sequence we can find similar functionality proteins.

We can also study how evolutionary close the proteins are and so.

We can also study individual motifs by it.

Pairwise alignment serves also as a part of next more complex pipelines or is mostly the basic part for work with a protein sequence.

### Biological sequences
Can be linearly ordered. ACGT/20(21)AA as a characters.
PeptideAlphabet=`ARNDCEQGHILKMFPSTWYV`
So stringology algorithms can be employed.

### Hamming distance
Now we go straitly to the algorithms and needed terms.

For to strings `S1`,`S2` is Hamming distance `HD` defined as:
`HD(S1,S2)=SUM(from i to n)f(S1[i], S2[i])`.
```python
def f(c1, c2):
    if (c1==c2): return 0
    else: return 1
```

### Alignments
| WRI T ERS |
| V INTNER  |

### Editation distance
 - its a bit simmilar to the Hamming Distance
 - number of edits needed to change str1 to a str2
 - also called Levensthein distance
 - the algorithm for searching of the smallest Levenstein distance is the basic alignment algorithm also
 - it is quite simple - using DP (Dynamic programming) from a prewious lecture

Algorithm:
Let us have two strings `s1` and `s2`. Then make a table `D` of size `len(s1)xlen(s2)`
Then for each `i = 0...len(s1)` the values in `D` are defined as `D(i,0) = i` and simmilarly for each `j = 0...len(s2)` applies `D(0,j) = j`.
Then we can row by row (or column by column) fill the table, while for each `i`, `j` as we defined them we get:
```python
D[i,j] = min( D[i,j-1],
            D[i-1,j],
            D[i-1,j-1)] + sigma(i,j,s1,s2)
            )
```
while funktion sigma is defined:
```python
def sigma(i,j,s1,s2):
    if (s1[i]==s2[j]): return 0
    else: return 1
```
In bottom right corner we got the result.

### Backtracking
Nice -- we have got the Editation Distance of the strings (next time we will be thinking about an "alignment score". But if we want the alignment itself, we need to trace back how the score was computed. 
We can do it accordingly to our `min()` and `sigma()` functions, but in oposite direction.

The backtrack arrow leads from:
D[i,j] -> D[i-1,j-1] if D[i,j] == D[i-1,j-1] or D[i,j] -1 == D[i-1,j-1]
D[i,j] -> D[i-1,j] if D[i,j] -1 == D[i-1,j]
D[i,j] -> D[i,j-1] if D[i,j] -1 == D[i,j-1]

Now if we follow whatever path from arrows, we get right alignment. It is good to try this yourself, to understand how the final alignment looks like and where are gaps and so...

### Operation weighted ED (OWED)
Very simple -- OWED is only ED, but we score gaps and mismatches by -1, but by `d`. Every type of difference has its own score value.
To compare it with ED:
```python
D[i,j] = min( D[i,j-1] + *d*,
            D[i-1,j] + *d*,
            D[i-1,j-1)] + sigma(i,j,s1,s2)
            )
```
>while funktion sigma is defined:
```python
def sigma(i,j,s1,s2):
    if (s1[i]==s2[j]): return *e*
    else: return *r*
```
As you can see, it is almost a copy of ED, however, in ED the constants are set to:
```
d = 1
e = 0
r = 1
```
> Exercise (from presentation)
- strings: WRITERS, VINTNER
- 𝑑 = 2 𝑒 = 0, 𝑟 = 3

### Alphabet-Weight editation distance (AWED)
This is the major step from ED to alignments as we make them - you modify the `sigma()` function with matrice, so for each combination of letters you have its own score.
Excercise from the presentation (I accidentelly gave you a recipe/almost solution, sorry :D):
> - Exercise
- formalization of AWED concept

### Global Sequence Alignment (GA)
However we did smaller steps on a path from ED to GA, there are stil huge differences between AW (the last "predecessor" of GA) and GA itself.

We want the best alignment possible. In real, the scoring system is inverted. The "mistakes" are scored with negative points and the "good matches" are scored with positive points.

The second huge difference is, that we want to penalize every opened gap, because we want to prevent an alignment with many solo nucleotides (it is highly unprobable or just shows, that there is no similarity).

So we want to find an alignment with the **highest** score.

### Gap penalization in alignments
In an ideal case we want a function, which can score every type of mismatch, scores individually the length of gap, also individually scored for every type of gap surroundings etc.

The problem is, that there is no such function which works in polynomial time. Therefore we must use a simplified model.

> There are two types of models:
 - linear gap penalty model (e.g. ED)
 - affine gap penalty model (e.g. Needleman-Wunsch)

And because I mentioned a new term "Needleman-Wunsch", you can bet on which model we want to use.

### Needleman-Wunsch
Needleman-Wunsch algorithm is similar as algorithm for AWED, however more positive approach is used. So we want to find the alignment with the best score rather than score with the least mismatches.

There are also different scores for making of new gap and for a gap elongation.

The ideal alignments can be found by backtracking from the bottom right corner, similarly to ED.

Just to be said, the NW (Needleman-Wunsch) algorithm is the final algorithm for GA, which is usually used for it.

### Local Sequence Alignment (LA)
The Local Sequence Alignment (LA) is very powerful simplification of the alignment problem. Usually we don't search for the same proteins or the most similar proteins as a whole. It is not rare, that in a sequence of useful protein there is subsequence of useless AAs, which has no connection to the function of the protein. So what we want to find are the parts of proteins, that are similar. It often can be some important or at least interesting part of protein, e. g. **function site**

We can see the LA also as a GA over all substrings possible. So how can we make it?

### Smith-Waterman (SW)
Smith-Waterman (SW) is an algorithm made to search for LAs over two strings.
It is very similar to NW algorithm, but has one important modification:
***It can't go under zero.***
So in every step, where we must decide to go under zero, we fill just a zero instead, so new LA can start from that position.

Of course on practical level, we must set the scoring matrices and constants so that some two random unrelated chars have always negative value (so prevent that we will get simply a global alignment...)

### Optimizations
There are few main optimization ideas:
 - for `m = len(s1)` and `n = len(s2)`
 - for space it is possible to get somehow `O(n)` (instead of `O(mxn)` time if only score (not alignment itself) is required
    - even though the alignment is required, there is the Hirshberg's algorithm, which can compute it in `O(n+m)`
  - for time there is a "Four-Russians technique" which allows you to compute it in `O(n^2/log(n))`, which is cool.

### Some flavors of prewiously said
 - there are many types of semi-global alignments, very good for special cases as
   - repeated matches,
   - overlap matches and so.

### Evolutionary nature of sequence alignment
To be clear, we want to align only sequences, which are evolutionary related, every AA is from mutual ancestor etc. They must have a **common ancestor sequence**

**Biologically correct** alignment has to fulfill these requirements.

### Scoring systems
The algorithms itself are searching for the best alignment accordingly to given criterias. But how to set these?

##### Probabilistic model
###### Random model
It is based on an assumption, that the sequences are unrelated.
Then in scoring matrice `M` for `i,j = 0...len(s1/s2)` is:
`M[i,j] = Multip_i( f(s1[i]) ) * Multip_j( f(s2[j]) )`
where the `f(a)` is the number of `a` in sequence `s1` divided by the `len(s1)`.

###### Match model
(DANGER ZONE :D)
If we assume, that the `s1` and `s2` are independently derived from mutual predeccessor (`s0`), we can use a Match model. It is similar as the Random model, but we count in it probability, that nucleotides `a,b` are together in a sequence (`a` from `s1` and `b` from `s2`)

##### Issues on probabilistic models
We cannot easily generalize our scoring matrices to every two sequences. But we can compute the matrice on rewieved alignment and so it might be reusable for next alignments.
But the problem is that only different parts of sequences have usually different amounts of matches and nucleotides / AAs...
These two arguments are reasons to use different matrices for differently distant proteins
(the matrix made from a distant set of proteins makes false positivity in set of a less distant set)
(the matrix made from less distant set makes false negativity in alignment for more distant set of proteins)

##### PAM matrices
**PAM matrices are scoring matrices encoding expected evolutionary
change at the AA level**
These are based on principle of evolutionary distance between two sequences.
It counts with "PAM" units.
One PAM means "the amount of evolution needed to change 1% of AAs in sequence"
It is accepted only non-lethal, non-silent mutation
It is not easy to explain, but for example two sequences with 1 PAM score are different in approx. 1/100 AAs. Because the AA can be changed also again to the same AA, 200 PAM sequences has ~ 25% of AAs the same.

This all works well only with assumptions, that
 - sites also evolve independently,
 - the frequency of AAs is constant over time and
 - the proccess of mutation is constant over longer periods of time (at least during mutation of one PAM unit)

##### Computation of PAM matrices
(DANGER ZONE :D)
It is based on the Match model, so for PAM XY matrix we take set of sequences in which we assume they are in class XY PAM and then we compute
`PAM_XY[i,j] = log( f(i,j)/f(i)*f(j) )`

##### BLOSSOM matrices
The PAM matrices have a problem, because the higher XY PAM matrices have also more errors (due to non ideal conditions which doesn't match fully the assumptions)

It is quite difficult procces behind the selection of testing set of protein sequences, but the result is, that in the testing set, each pair of sequences is from XY % identical for BLOSSOM XY matrix.

# 05 Multiple Sequence Alignment
[presentation](https://cunicz-my.sharepoint.com/personal/51137390_cuni_cz/_layouts/15/onedrive.aspx?id=%2Fpersonal%2F51137390%5Fcuni%5Fcz%2FDocuments%2Fteaching%2Fbioinfo%2Flectures%2Flecture05%5Fmsa%2Epdf&parent=%2Fpersonal%2F51137390%5Fcuni%5Fcz%2FDocuments%2Fteaching%2Fbioinfo%2Flectures)
[important game for MSA understanding]
### Outline
 -  Motivation
 -  Scoring functions
 -  Algorithms
- exhaustive -> multidimensional dynamic
programming
 - heuristics
- progressive alignment
- iterative alignment/refinement
- block(local)-based alignment

### Motivation
 - Distant homologues
   - faint similarity can become apparent when present in many sequences
   - motifs might not be apparent from pairwise alignment only
 - Detection of key functional residues
   - amino acids critical for function tend to be conserved during the evolution and therefore can be revealed by inspecting sequences within given family
   -  Prediction of secondary/tertiary structure
   - Inferring evolutionary history

### Hand-made MSAs
Sometimes MSAs are made by humans. It is very expensive, but very high quality.
They are a benchmark for automatic MSAs.

### Not "computed" MSAs
 - some websites make MSAs from the secondary structure of protein

### Scoring
Usually based on:
 - minimum entropy of each column (can be expressed by the least number of bits)
 - sum of pairs - straithforward technique - sum of scores over each pair of AAs in column, over all the length of matrix
   - usually BLOSSUM 62 or similar matrix can be used

### Multidimensional dynamic programming
Generalization of GA/LA for more dimensions (3 and more dimensional array). Backtracking is analogous.

### Computational complexity of MSA
Let L be the length of sequence and N the number of sequences. Then: 
Memory complexity is (without trics): `O(L^N)` 
Time for one step is: `2^N-1`
Time complexity is: `O(2^N*L^N)

> MDP - exercise
#1
- Let’s have sequence of length 50
- Comparison of a pair of sequences using DP takes 0,1s
- What is the time needed to compare 4 sequences?
#2
> - Let’s say we have 1000 years and average sequence length is 50.
- How many sequence can afford to compare?

### Heuristic Algorithms
 - Progressive alignment methods
   - iterative building of the alignment
   - Feng & Doolittle
   - **ClustalW, Clustal Omega**
 -  Consistency-based methods
   - T-Coffee
 - Iterative refinement
   - alignment built and then refined be realigning the constituent sequences
   - Barton & Sternberg
 - Block-based alignment
   - local alignment built by identifying blocks of ungapped MSA identified and assembled
   - DIALIGN
 - Mix of approaches
  - MAFFT, MUSCLE

### Progressive alignment methods
 - Framework
- First, two sequences are aligned using standard pairwise alignment
- The remaining sequences are taken one by one and added to the pool from which
MSA emerges
- Repeated until all sequences are aligned

 - Parameters
- The order in which the sequences are be aligned
- Whether only one alignment is kept and sequences are added to it or whether also
an alignment can be aligned to another alignment (as if a tree was built)
- The process used to align and score sequences or alignments against the existing
ones

### Star alignment
It is a technique to make the best MSA by a "progressive alignment method".
Pick one starting sequence and then make pairwise alignments of this sequence with the rest.

To make it better, pick the sequence which is similar to most of the sequences.

### SA – time complexity
- Average sequence length `𝐿`
- One global alignment computation in `𝐎(𝑳^𝟐)`
- 𝑘 sequences → `O(k^2*L^2) `pairwise computations
- 𝑙 ... upper bound on the MSA length → `𝐎(l*k) `for MSA construction
`𝑂(𝑘^2*𝐿^2+𝑙*𝑘) = 𝑶(𝒌^𝟐*𝑳^𝟐)`

### Feng & Doolitle
Very serious and heavy method to find the best "guide tree" for progressive alignment.
1. make pairwise alignment for every combination of sequences
2. convert score of alignment to evolutionary distance
3. construct a guide tree using Fitch & Margoliash algorithm
4. align every childnodes, in order they were put into the guide-tree

Hack for this - gap is not put as `-` symbol and it is replaced by a neutral `x` symbol, which has score 0 for every nucleotide. It has only disadvantage, that the gaps remain conserved in a final alignment.

### Profile/MSA alignment
Highly conservated positions should be penalized more -> we divide sequences to two groups (profiles) and then we make a score also between the group alignments.

### ClustalW
 - very important and often used!!
 - similar to a Feng & Doolitle, but incorporates Profile/MSA alignment 

1. make pairwise alignment for every combination of sequences
2. convert score of alignment to evolutionary distance
3. construct a guide tree using Fitch & Magoliash algorithm
4. make alignments like ***sequence-sequence, sequence-profile and profile-profile***

Closely related sequences -> Blossum 80
Distant sequences -> Blossum 50
Position specific gap open penalties are made from structure based alignments

### Clustal Omega
Solves problem with ClustalW, which is not good form many sequences.
- Clustal Omega algorithm
  - mBed algorithm-based for guide tree construction
    - emBedding each sequence in a space of 𝑛 dimensions where n is proportional to log N
  - Each sequence replaced by an 𝑛 element vector, where each element is the distance to one of 𝑛 reference sequences
  - Clustering of the vectors by UPGMA or K-means
  -  Alignments of profiles using hidden Markov models (HHalign package)

### T-Coffee
Solves (it tries) ClustalW drawback - once error, always an error.
Makes a library of alignments, from that extended library (takes pairwise alignments), and finally if it makes sense, it makes the definite progressive alignment. During this the weights of sequences are refined accordingly to the libraries.

### Iterative refinement
To avoid problems with not optimal heuristics, this method makes more cycles of refinement to make the alignment better and goes to optimal solution by smaller steps. It removes and return sequences back.

### Barton-Stenberg
1. Find the highest scoring pair of sequences and align them using
the pairwise dynamic programming
2. Identify most similar remaining sequence with respect to the
existing profile and align it using sequence-profile alignment
3. Repeat step 2 until all sequences are aligned
4. Remove sequence 𝒔𝟏 and realign it to the profile by profile-
sequence alignment. Repeat for 𝒔𝟐, ... , 𝒔𝑵
5. Repeat step 4 for a fixed number of times or until convergence

### Block-based alignment
Both progressive and iterative methods assume that all parts of all sequences are consistent with a global alignment - not every position in the alignment must correspond to a homologous site in all sequences.
Block-based solution approach to the problem of global alignment by
- splitting sequences into blocks
- aligning the blocks
- merging block alignments

### DIALIGN
- Alignment constructed from gap-free local alignments between pairs of sequences
- based on diagonals in the dynamic programming matrix
  - Procedure
- align all possible pairs of sequences
- determine all diagonals and assign weights
- for a diagonal 𝐷 of length 𝑙, score 𝒔 is obtained from substitution matrix
- determine length-independent weight as 𝒘 𝑫 = − 𝐥𝐨𝐠 𝑷(𝒍, 𝒔), where 𝑷(𝒍, 𝒔) is the probability that diagonal of sequence of length 𝒍 will have score at least 𝒔
- build MSA by adding consistent diagonals in order of decreasing weight
(and overlap with other diagonals)
- explore unaligned regions and include them if possible

### MAFFT
 - Multiple Alignment Using Fast Fourier Transform
 - 2-cycles of progressive alignment method with low quality
 - FFT method for pairwise alignments
 - Simplification -- 20AA are reduced to 6 groups
 - computed `D_ij` (shared tuples)
 - "UPGMA" method is used for conversion `D` into distances & guide tree
 - smart work with vectors and FFT us allows to reduce computational time `O(n^2)` to `O(n*log(n))` when computing alignments
 - lately, the iterative refinement is used to optimalize the alignment (divides the alignment into two groups and realigns)

##### Version 5:
 - MAFFT got TCoffee like approach - incorporation of information from the alignments to a function
 - dropped reconstruction phase of the guide tree

##### Version 6:
 - new build-tree algorithm for larger numbers of sequences
 - multiple NC-RNA handling features, also for the structure information

### MUSCLE
 - multiple-sequence-comparizon-by-log-expectation
 - phases: draft progressive -> improved progressive -> refinement
 - k-mer distance

### BAliBase
 - standard dataset for benchmarking MSA algorithms

# 06 Speeding Up Similarity Search In Protein Databases
### Outline
- Motivation
- Standard heuristics
  - FASTA
  - BLAST
- Index-based methods
  - hashing
  - hierarchical indexing
- Parallelization

### Motivation
 - exponential growth of number of records
 - optimal algorithm for accessing sequence similarity is known, but has quadratic complexity (Needleman-Wunsch, Smith-Waterman)
 - for many users and such number of records - linear algorithm complexity at most

### Hashing
 -  technique to map query keys to record addresses
 -  In DNA/protein sequence search, hashing constructs a list capable of determining where in a sequence given query k-tuple is located

- To encode a k-tuple
  - let us set k=3
  - nucleotide sequence has 4-letter alphabet → 𝟒𝟑 = 𝟔𝟒 possible triplets
  - each letter is assigned a number (A=0, C=1, G=2, T=3) → 𝒄(𝑿) ... code for letter 𝑋

- 𝑐(𝐴𝐴𝐴) = 0, 𝑐 (𝐶𝐴𝐴) = 16, 𝑐 (𝐴𝐶𝐴) = 4, 𝑐 (𝐴𝐴𝐶) = 1
- for an amino acid sequence we need 20 letter alphabet
- Scan a sequence, take k-tuple for every position i and assign to position
𝒄𝒊 in the hash table

### Chaining
Quite an ingenious technique -- we don't have to store triplets from hashing to a long field, we can only point to the first occurence ande from that we can point to next...

### FAST(A)
**DNA and protein sequence alignment package**

- Four-step heuristics process applied to every database sequence individually
1. Location of ungapped alignments of length 𝒌 (k-tuples)
2. Identification of high-scoring alignments
3. Joining of ungapped alignments
4. Dynamic programming

Uses local alignment!

### BLAST
**Basic Local Alignment Search Tool**
More time-efficient than FASTA

1. For the query sequence, all k-mers are considered
- typically k=3 for an amino acid sequence and k=11 for a nucleotide sequence
2. Seeding - for each k-mer from step 1, all k-mers from the universe of all possible k-mers scoring above a given threshold 𝑻 are generated
- E.g. for proteins, typically BLOSSUM 62 scoring matrix and positive 𝑇 is used → since there are many negative scores in BLOSSUM 62, only very similar 3-mers score above given threshold, e.g., for 𝑻 = 𝟏𝟗 only CHH, CHY and CYH will score sufficiently against the query sequence 3-mer CHH
3. For the k-mers in step 2, a finite state automata (FSA) is built to be used for scanning the database. The FSA is then used to scan against every database sequence; the positions of the matched k-mers in the query and DB sequences are stored → alignment matrix similar to the FASTA one
4. differs in the older and newer version of BLAST.
a) In the older version, every k-mer scoring above the threshold 𝑻 is extended in both directions until the score drops by some amount 𝑋𝑈 with respect to the maximum obtained so far. The extension is called high scoring pair (HSP)
b) Later versions of BLAST (gapped BLAST) use the two hit approach. The idea is that an HSP should contain at least two sufficiently well scoring k-mers
- value of 𝑻 is decreased (compared to 4a)
- k-mers on the same diagonal within given distance are identified and joined
- extension as in 4a takes place
- HSPs not scoring above a threshold 𝑺𝒈 are removed
- 𝑆𝑔 is set so that about only 2% of the database sequence would pass
5. HSPs with scores exceeding 𝑺𝒈 are used to seed dynamic
programming
- the DP starts from the center of highest scoring k-mer of the HSP
- the matrix is filled in both directions until the score 𝑋𝑔 falls below the score of the current highest scoring alignment
- no band restrictions takes place as in FASTA
- score of the highest scoring alignment is used to determine the significance

### HSP - High Score Pair

> Distribution of random alignment scores
follows normal distribution, but we are
interested in best scores of all the
alignments and these are not normally
distributed

> Maximum of a large number of random
variables (scores) is known to have
extreme value (Gumbel) distribution

> The theory assumes that alignment can start anywhere, which is not true near
the ends of the sequences (edge effect) → effective length used instead of real
length
- Especially valid for short sequences (<200 residues)

### E-value
(DANGER ZONE :D)
𝐸 = 𝑃(𝑆 ≥ 𝑥) × 𝐷 where D...number of sequences in the database, and P(S>=x) is based on S... score is more than x (that there is such protein, that has score like our sequence)
> The number of hits one can expect to see by chance when searching a database of a particular size.

### Indexing
Need to find a sublinear solution to search for similarities in a database.
Succesful (complexity decreased to `O(log(n)` or even `O(1)` in case of hashing)

### BLAT
BLAST-like alignment tool
Procedure mostly identical to BLAST apart from the HSPs identification
- BLAST scans the database letter by letter
- BLAT builds an in-memory index (hash table) for non-overlapping DB k-mers and this index is then used for every query sequence position
- Hamming distance used as the distance/similarity measure

### SSAHA
- Sequence Search and Alignment by Hashing Algorithm [Ning et al., 2001]
- Primarily meant to be used for nucleotide sequences but the idea is generalizable to protein sequences as well
- Works over k-tuples
Simplification, because it works over hash-lists, not over sequences itself

### FT#N
(Almost DANGER ZONE :D)
Converting the sequences into vectors, which can be easily organized into "supervector" (FD#N) spaces. The filtering is based on distance meassure (FD#N) All are stored into R-tree. If some record is falsely positive, it can be again filtered by full edit distance meassurement.

### Parallelization
 - MPS - making multiple alignments in one moment
 - Hardware-based speedup

# 07 Hidden Markov Models
[presentation](https://cunicz-my.sharepoint.com/personal/51137390_cuni_cz/_layouts/15/onedrive.aspx?id=%2Fpersonal%2F51137390%5Fcuni%5Fcz%2FDocuments%2Fteaching%2Fbioinfo%2Flectures%2Flecture07%5Fhmm%2Epdf&parent=%2Fpersonal%2F51137390%5Fcuni%5Fcz%2FDocuments%2Fteaching%2Fbioinfo%2Flectures)
Outline
- Markov chains
- Hidden Markov models (HMMs)
  - Definition
  - Decoding
    - Viterbi, forward, backward algorithm
  - Parameter estimation
    - Baum-Welch algorithm

The basic idea is simple - if we know the matrix of probabilities, we can compute, from the initial state, how probable is n-th state (just by powering the matrix itself).
If we have two states of probabilities (fair/loaded dice), it is more complicated. But for given sequence we can observe, how probable is each stay. For our bioinformatical approach it is important to find how to apply this rule in macromolecules.
We have an example in the motivational introduction of the presentation. CG-islands contain more probably C and G nucleotides, but usually their presence is less than half. To find if some part of sequence is CG-island or not from only the sequence we can use Hidden-Markov models.
We want to estimate potential CG-island parts of DNA, only using the sequence of nucleotides itself.

### Viterbi algorithm
> Recursive procedure. Given probabilities `v_k(i)` of the most probable paths ending in `k` for observation `x_i`, the probabilities of the states for observations `x_i+1` can be obtained as...

You can find it on the slide 10 in the presentation.

Optimal is to generate all paths and choose the most probable. However, the Viterbi algorithm approximates the most probable path without it.

### Forward algorithm
Goes forward through the space and summarizes up probabilities of all the states.

# 08 Probabilistic alignment
[presentation](https://cunicz-my.sharepoint.com/personal/51137390_cuni_cz/_layouts/15/onedrive.aspx?id=%2Fpersonal%2F51137390%5Fcuni%5Fcz%2FDocuments%2Fteaching%2Fbioinfo%2Flectures%2Flecture08%5Fprobabilistic%5Falignment%2Epdf&parent=%2Fpersonal%2F51137390%5Fcuni%5Fcz%2FDocuments%2Fteaching%2Fbioinfo%2Flectures)

### FSA - based view of pairwise alignment
> Standard dynamic programming-based sequence alignment can be
described by finite state automata (FSA)

It is also possible to make HMM pair model of global sequence alignment by FSA.

Note: There are many ilustrational pictures and schemes in the presentation.

> Best alignment corresponds to the most probable path through the model → Viterbi algorithm for pair HMM

### Significance of matches
- With the standard DP programming solution, it is difficult to identify correct alignment when the similarity is weak
- With pair HMM we can compute the probability that a pair of sequences is related given any alignment

-- ilustration of the forward algorithm

By posterior probability we can check, if the probabilistic alignment is correct.

### Waterman & Eggert
1. Find a best-scoring alignment
2. Set cells corresponding to the chosen alignment to zero
3. Repeat alignment = obtain the next best alignment
4. Repeat from step 2 given number of times or until score drops below given
threshold

# 09 Patterns, Profiles and Motifs
[presentation](https://cunicz-my.sharepoint.com/personal/51137390_cuni_cz/_layouts/15/onedrive.aspx?id=%2Fpersonal%2F51137390%5Fcuni%5Fcz%2FDocuments%2Fteaching%2Fbioinfo%2Flectures%2Flecture09%5Fmotifs%2Epdf&parent=%2Fpersonal%2F51137390%5Fcuni%5Fcz%2FDocuments%2Fteaching%2Fbioinfo%2Flectures)
[presentation - Q&A](https://cunicz-my.sharepoint.com/personal/51137390_cuni_cz/_layouts/15/onedrive.aspx?id=%2Fpersonal%2F51137390%5Fcuni%5Fcz%2FDocuments%2Fteaching%2Fbioinfo%2Flectures%2Flecture09%5Fmotifs%5Fqa%2Epdf&parent=%2Fpersonal%2F51137390%5Fcuni%5Fcz%2FDocuments%2Fteaching%2Fbioinfo%2Flectures)

Motivation
 - MSA contains conserved regions corresponding to
   - signals (promoters, ...)
   - common structural motifs
   - chemical reactivity (active sites, ...)
 - When encountering a new sequence one is interested in comparing the new sequence to other, existing, sequences
- description of a set of sequences
- assigning new sequence to a set of
sequences
- scoring of the assignment
 - Models of conserved regions
- consensus sequence
- patterns
- position specific scoring matrix
(PSSM)
- Hidden Markov Models (HMM)

### Consensus sequence
> The simplest way to make a model from a MSA.
Principle:
- majority wins
- *but* skip too much variation

> Algorithm:
1. Count symbol distribution in each column independently
2. For each column with clear majority of one symbol, pick that symbol and assign it to the respective position in the consensus sequence
3. Fill the remaining positions with the * symbol

Pros: simple and easy to implement
Cons: highly dependent on the training set, symbol distribution not present in the resulting sequence, binary - only if matches, not how well

### Patterns
Regex for biological sequences - only different (prosite) syntax (see slide 6).

Pros: Easy to implement, Easy to understand for anyone, Ability to better express the motif than consensus sequence
Cons: Highly dependent on the training set, Small patterns generate lots of hits, possible false positives, Symbol distribution not present in the resulting sequence, Binary, only information whether a query sequence matches the input sequences, not how much

### Position specific scoring matrix for profiles
> Position Specific Scoring Matrix (PSSM) expresses the likelihood of a letter to appear at given position
> Based on counts of letters at the positions
> Resulting score for position 𝑖, 𝑗 is computed as log-likelihood ratio from the null model (each amino acid is observed with an identical frequency in a random sequence)

... during querying
> position with the highest PSSM score is reported

and the sequence is scored by the PSSM (able to paralelize)

Pros: 
- Relatively fast
- Querying is easy to implement
- Match scores are statistically interpretable
Cons:
- No insertions or deletions and
- constant-length regions

### PSSM - weighting
> Highly populated families can contain big subfamilies which can negatively influence the results
> Sequence weighting compensates the possible sampling bias

### PSI-BLAST
> Position specific iterated BLAST
- establishment of profiles
- using profiles to search sequence database

Algorithm
1. Search database using BLASTP
2. Collect high scoring results and build MSA
3. Get PSSM from the MSA
4. Use the profile from PSSM to search
against database using BLASTP
- use PSSM instead of substitution matrix
5. If new hits are identified add them to the
MSA and update the profile
6. Repeat steps 4 and 5 until stabilization

Pros:
- Capable to identify up to three times more 30% homologues than BLAST
- Fast because using BLAST heuristics
- Allows PSSMs on large databases
Cons:
- Profile drift
- high sensitivity → false positives → biased profile → incorporation in subsequent cycles

### Operating Instructions
 - Consensus sequences
- to find highly conserved signatures such as, for example, enzyme restriction sites
for DNA
 - Patterns
- to search for small signatures or active sites
- to communicate with other biologists
 - PSSM
- to model small regions with high variability but constant length

### Profile Hidden Markov Models
> - HMM can capture information present in an MSA → an alternative to PSSM → profile HMM
- Match states come from PSSM built from the input MSA and capture log-odds ratio of a residue at given position
- We should introduce position-dependent gap model, because at some positions insertions/deletions are more probable (higher ratio of gaps in the MSA)

> If we have a profile 𝑷 and align a sequence 𝒔 to it, at each step 𝑖 we can
either
- match a letter of 𝑠 to 𝑃 → 𝑴_𝒊
- add gap to 𝒔 (the corresponding letter in 𝑠 will be possibly matched with some later position in 𝑃) → 𝑫_𝒊
- add gap to the profile and align given position in 𝑠 with a gap in 𝑃 → 𝑰_𝒊
- 𝑴_𝒊, 𝑫_𝒊, 𝑰_𝒊 correspond to the states of the HMM
which emit letters of the query sequence with
given probabilities (learned from a MSA)
- Path in the HMM shows how a sequence could
be aligned to the profile and moreover gives the
score reflecting the probability with which such
an alignment could arise

### Protein Family Databases

> There exist many databases of MSAs and related
- consensus sequences
- patterns
- HMMs
- ...
- Some databases contain multiple representations of families

### Prosite
> Collection of motifs, protein domains, families and functional sites
> quality estimation under SwissProt, Prosite tool

### CDD
 - conserved domains

> Includes MSAs available as PSSMs
 - NCBI-curated domains based on 3D structure
- imported domains models (Pfam, TIGRFAM, SMART, COG, KOG ...)
 - CD-search
- search interface for scanning CDD against submitted protein or nucleotide query
- uses RPS-BLAST (variant of PSI-BLAST where profiles are precomputed and searched
by the query sequence)
- CDART
- Conserved Domain Architecture Retrieval Tool
- being used to analyze the domain architecture and retrieve proteins with similar architecture

### Pfam
> - Collection of protein domains and families and respective MSAs
- Uses HMMs (HMMER3 package)
- Versions
- Pfam-A
- manually curated
- over 12,000,000 sequences in over 13,500 families
- Pfam-B
- automatically clustered and aligned sequences not covered by Pfam-A

### InterPro
> - Combination of protein signatures from a number of member databases
into a single searchable resource
- CATH/Gene3D, PANTHER, Pfam, PRINTS, ProDom, PROSITE, SMART,
SUPERFAMILY, TIGRFAM, ....
- INTERPROSCAN
- allows scanning of sequences again InterPro’s sequences
- accessible also using web services

# 10 Phylogenetics
[prezentace](https://cunicz-my.sharepoint.com/personal/51137390_cuni_cz/_layouts/15/onedrive.aspx?id=%2Fpersonal%2F51137390%5Fcuni%5Fcz%2FDocuments%2Fteaching%2Fbioinfo%2Flectures%2Flecture10%5Fphylogenetics%2Epdf&parent=%2Fpersonal%2F51137390%5Fcuni%5Fcz%2FDocuments%2Fteaching%2Fbioinfo%2Flectures)
### Outline
> - Motivation
- Basics -> terminology
- Tree construction techniques -> molecular markers, tree building, distance-based methods, parsimony-based methods, tree reliability

### Phylogenetics
> The study of evolutionary relatedness among various groups of  entities (e.g., species, populations)
- Can be obtained from fossil records containing morphological information about ancestors of  common species
- but, e.g., for microorganisms the fossils are not available
- Genes can be viewed as molecular fossils
- accumulation of  mutations over time causes phenotypic changes
- more data available
- no sampling bias
- Assumptions
  - sequences using in phylogenetic construction are homologous
  - sequence variability is sufficiently informative
  - each sequence position evolved independently

### Trees
> Tree is:
- undirected graph without cycles
- branch
  - path in the tree
- root
  - rooted tree
    - a tree with one node being the root, forming a hierarchy
  - unrootedtree
    - a tree where all the nodes are equal
- topology
  - mutual arrangement of the nodes in the tree
  - branching pattern

### Phylogeny-related terminology
> - Taxon (taxa)
- group of (one or more) entities considered as a unit
- Clade(monophyletic group)
- a group of taxa descended from a single common ancestor
- two taxa share a unique common ancestor
- Lineage
- a branch showing ancestor-descendant relationship
- Phylogeny
- the tree-branching pattern representing the evolutionary divergence
- to obtain valid species phylogeny, multiple phylogenetic trees from variety of genes and gene families should be built
- some parts of genome evolve more rapidly than others

### Tree rooting
> - Some algorithms result in a rooted tree some do not → no assumption about direction of evolution

 - Rooting by midpoint
- Place root at the midway point between the two most distant taxa in the tree -> Assumes constant clock-like manner of  evolution
 -  Rooting using an outgroup
 - close enough to ingroup to allow inference from sequence or trait data, but far enough to be a clear outgroup
 - often determined from an independent source of information
    - bird sequence can be outgroup for mammals phylogenetic analysis (based on evidence that birds branched off prior to all mammals)

### Phylogenetic tree representation
 - Cladogram
 - branch lengths have no evolutionary meaning (do not correspond to the amount of  genetic change)
 - Phylogram
 - branch lengths represent the amount of  evolutionary divergence
 - Newick format
 - nested parentheses format
 - phylogram-based format includes branch lengths
    ***example of the Newick format***:
 - (((B:1,C:2),A:2),(D:1.5,E:3))
 - (((B,C),A),(D,E))

### Phylogenetics procedure
```
1. Choosing molecular markers
- what data to use for the analysis?
2. Performing multiple sequence alignment
- aligned positions are considered to be genealogically related
3. Choosing a model of  evolution
4. Choice of  the tree building method
- algorithm for building the tree itself
- distance-based vs. character-based
5. Assessing tree reliability
```
### Molecular markers
 - Nucleotide sequence
- evolves more rapidly → suitable for more closely related organisms
- e.g., noncoding regions of  mitochondrial DNA for individuals within population
 - Protein sequence
- slow evolving → distantly related species
- ribosomal RNA is slowly evolving as well
- more conserved than nucleotide sequences
- single-point mutation in DNA does not have to lead to protein sequences/structure change → synonymous (does not change AA type) vs. nonsynonymous (alternates AA type) mutation
- different codons are more preferred for a given AA in different species

### Sequence alignment
 - Identification of related positions in the sequences
 - More than one multiple sequence alignments tools can and should be applied
 - Manual refinement
   - alignment can contain errors which have to be corrected
   - guidelines
     - cofactor residues
     - residues with similar physico-chemical properties
     - residues sharing secondary structure

### Evolutionary distances
 - Models of  mutation and evolution built over alignments to assess evolutionary distance to a pair of  sequences
 - Evolutionary (pairwise) distance
   - Estimated number of mutations that has occurred since two sequences diverged from their common ancestor

### Fractional alignment difference (p-distance)
> p = D/L

 - L ... Length of the sequence
 - D ... number of positions where two sequence differ

##### Drawbacks
1. In longer time periods some positions can undergo multiple mutations which is not reflected in the p-distance
2. For low mutation rates or short periods of time only few mutations happen → high statistical variation between short sequences → errors in p-distance estimations
3. Notall species evolve at the same rate (different evolutionary pressures)

### Poisson corrected distance
 - The idea is to come up with a formula which would relate the actual number of mutations and observed mutations (p-distance)
 - Assumption that the probability of a mutation at a position follows Poisson distribution `P(x=k)=(l^k * e^-l)/ k!`
 - I skip there the step-by-step process and give there only the result:
 - The Poisson corrected distance id defined as `d_p:=-ln(1-p)`

### Jukes-Cantor model
 - Nucleotide sequence evolutionary model
 - Assumptions:
   - sites are independent
   - sites have identical mutation rates
   - all mutation substitutions happen at the same rate 𝜶 per unit time (probability of nucleotide change)
   - better explained on 19th slide
   - Jukes-Cantor distance is defined as `d_JC=(-3/4)ln(1-(4p/3))

### Tree building methods
 - Distance-based methods
 - based on quantitative measureslike the distanceor similarity between species (e.g., sequences)
- UPGMA (Unweighted Pair Group method Using Arithmetic Average)
- Neighbor joining
 - Character-based methods
- based on qualitative aspectslike common characters
- maximum parsimony
- maximum likelihood

### UPGMA
- Assumption
  - molecular clock
    - all taxa evolve at a constant rate and are equidistant from the root
- Based on sequential clustering:
1. Compute ***all-to-all distance matrix***
2. Group ***2 taxa with the smallest distance***
3. Place a node at the midpoint of the 2 taxa
4. Form ***a reduced distance matrix***, treating the new group as a separate taxon
  - distance between a group and a taxon T is the average of the distances of taxa in the group and T
5. Repeat steps ***2-4*** until there is only one taxa
6. Last taxa to be joined is treated as the outgroup

- why UPGMA faily?
  - assumption of "molecular clock", ***mutation speed*** has the same ***constant*** rate
  - sum of times along any branch is the same
    - if that is true, the tree will be constructed correctly
  - UPGMA does not take into account the possibility of unequal substitution rates along different branches
    - problems with ultrametrics (see slide 25)
### Neighbor joining
 - solves both problems of UPGMA
 - special case of star decomposition
 - really being used by Clustal
##### NJ – Algorithm
1. Define 𝑇(star tree) as set of  leafs (sequences) and set 𝐿=𝑇
2. Compute all-to-all distance matrix for every object in 𝐿
3. Modify distances to compensate for long edges →𝐷𝑖𝑗
4. Pick (𝐢,𝐣) ∈ 𝐿 with minimum 𝑫𝒊𝒋
5. Define a new node 𝒌 and set 𝒅(𝒌𝒎)=𝟏/𝟐(𝒅(𝒊𝒎)+𝒅(𝒋𝒎)−𝒅(𝒊𝒋)),∀𝑚∈𝐿
6. Add 𝒌 to 𝑻 with lengths 𝒅(𝒊𝒌)=𝟏/𝟐(𝒅(𝒊𝒋)+𝟏/𝟐(𝒓(𝒊)−𝒓(𝒋)),𝒅(𝒋𝒌)=𝒅(𝒊𝒋)−𝒅(𝒊𝒌)
7. **𝑳=𝑳/𝒊,𝒋⋃𝒌**
8. Repeat steps 4 – 7 until |𝑳|=𝟐
9. Connect the remaining two nodes with length 𝑑(𝑖𝑗)
10. Determine outgroupbased on the external knowledge
##### Star decomposition
 - set of algorithms for phylogeny based on a "star" - each algorithm starts with a graph of sequences connected only with a one point (in the middle of them)
### Parsimony
- Commonly used
  - Unlikedistance-based methods almost no asssumptions about the distances
  - Allows to hypothesize the ancestral sequence in addition to the point of divergence
- Finding ***a tree which can explain the observed sequences*** with ***the minimum number of  substitutions***

### Weighted (generalized) parsimony
 - Cost 𝑆(𝑎,𝑏)for each substitution in the tree 
 - 
### Traditional parsimony
 - Counting the number of  substitutions

### Boostrapping
 - a method for phylogenic tree evaluation
 - repeating the process of tree generation multiple times but with different positions in the dataset sequences (>100), build consenzus tree, meassure agreement between them
 - best on 38 slide :)

# 11 Protein structure similarity
[prezentace](https://cunicz-my.sharepoint.com/personal/51137390_cuni_cz/_layouts/15/onedrive.aspx?id=%2Fpersonal%2F51137390%5Fcuni%5Fcz%2FDocuments%2Fteaching%2Fbioinfo%2Flectures%2Flecture11%2Dprotein%2Dstructure%2Dsimilarity%2Epdf&parent=%2Fpersonal%2F51137390%5Fcuni%5Fcz%2FDocuments%2Fteaching%2Fbioinfo%2Flectures)

### Background
 - Structure-function correlation
 - Approaches
   - global similarity
     - structures are globally similar on the fold level
     - structures sharing global similarity might also share similar binding sites (protein-protein, protein-ligand, ...) or other functional motifs and therefore share similar function (at least with respect to given active site/motif)
   - local similarity
     - structures share similarity on the level of, e.g., active sites only
     - globally dissimilar proteins can still share function since their correspondence can be related to the local functional motifs only

### Pairwise protein structure similarity task
 - Input
   - A pair of protein structures (set of 3D coordinates of the constituent residues/atoms
 - Output
   - Nonalignment-basedmethods
     - output only the similarity/distance
   - Alignment/superposition-basedmethods
     - give also structural superposition (3D match)

### RMSD
 - ***root-measure-square-deviation***
 - `RMSD(S1,S2) = (1/N * SUM_i=1^N(sigma^2_i))^1/2`
   - sigma...eucleidan distance between the mapped residues

### Superpositional algorithms
 - these want to find a superposition of 2 structures, which has minimal RMSD
 - Given a mapping between atoms/amino acids of the two compared structures, superposition minimizing RMSD (based on the paired atoms) can be computed in linear time (e.g., using Kabschalgorithm or quaternions)
### Typical workflow of superposition approaches
1. Feature extraction
2. Feature-based mapping
3. Superposition
4. Scoring

### Classical Approaches
- DALI
- CE
- SSAP
- PROSUP
- STRUCTAL
- MAMMOTH
- VAST
- FATCAT

### DALI
 - ***Distance mAtrix aLIgnment*** [HolmandSander, 1993]
 - Based on matrix of intra-residual distances
   - 2D representation of a 3D structure
   - independent of the coordinate frame
 - Main idea
   - similar structures share similar intra-residual distances →similar structures share similar distance matrix

##### DALI - Algorithm
1. Intra-residual distance matrix computation 𝑀
2. Splitting 𝑀into overlapping submatrices of fixed size –contact patterns
3. Identification of similar contact patterns
4. Overlapping (pairs have a common fragment) contact patterns are merged to get seed patterns
5. Seed pattern chosen and extendedby neighboring contact patterns using either Monte Carlo algorithm or branch-and-bound approach into the overall alignment

###### DALI – Monte Carlo (step 5)
1. Compute similarity score 𝑺 for the current alignment
2. Randomly add a new (non-overlapping) pair into the alignment and compute score 𝑺′
   - (𝑺′−𝑺)>𝟎→change is accepted
   - (𝑺′−𝑺)<𝟎→change is accepted with the probability 𝑝=exp(𝛽(𝑺′−𝑺)) where 𝛽 is a parameter of the method
3. Iterate until the system converges

##### DALI - Scoring
 - additive similarity score

### CE
 - Combinatorial Extension [Shindyalov, Bourne 1998]
 - Unlike DALI does not resolve non-topological similarities (order of the structure alignment must follow the sequence order)
 - Based on the notion of Aligned Fragment Pair (AFP) - sufficiently similar constant-length portions of consecutive residues (local structure) in both sequences

##### CE - Algorithm
1. Identification of AFPs 
2. Suitable AFPs joined (path extension)
3. Optimization of the path → structure superposition
4. Iterative optimization of the superposition

### PROSUP, STRUCTAL (TN)
 - The main idea is to use dynamic programming in an iterative fashion
 - Algorithm
  1. generate one or more seed alignments
  2. superposethe structures based on the initial alignment
  3. take the inter-residual distances and use them to form a scoring matrix
  4. perform dynamic programming where the distance matrix from previous step is used as the scoring matrix
  5. the resulting path defines the new mapping of the residues which leads to a new structural superposition
  6. iterate until convergence
 - PROSUP and STRUCTAL use different ways of obtaining the initial alignment and scoring of the superposition
   - e.g., STRUCUTAL employs exposure weighting where buried amino acids score higher when aligned

### MAMMOTH
 - MAtching Molecular Models Obtained from THeory [Ortiz, Strauss, Olmea; 2002]
 - Algorithm:
   - Divide 𝐶𝛼backbone into heptapeptides
   - Convert each heptapeptide into unit vector by plotting the direction vectors between𝑖-thand 𝑖+1-th 𝐶𝛼 atom on a unit sphere
   - Compute all-to-all RMSD distances between all pairs of the heptapeptides/unit vectors in the two proteins → scoring matrix
     - Since we have vectors on a unit sphere, finding optimal superposition (for a pair of heptapeptides) requires to only find rotation which minimizes RMSD

##### MAMMOTH (cont.)
 - Use the scoring matrix from the previous step with Needleman-Wunsch algorithm with zero end gaps
 - Find the maximum subset of similar local structures that have their corresponding 𝐶𝛼 close in Cartesian space
   - variant of the heuristic MaxSub algorithm
 - Percentage of structural identity (PSI) is computed, defined as the percentage of corresponding (from previous step) residues below 4.0 Å in 3D space, measured with respect to the shorter structure
 - Calculate the probability of obtaining given proportion (from previous step) of aligned residues (with respect to the shorter model) by chance (p-value)

### FATCAT
 - **F**lexible structure **A**lignmen**T** by **C**haining **A**FPs (Aligned Fragment Pairs) with **T**wists(**FATCAT**)[Ye and Godzik; 2003]
 - Does not treat proteins as rigid bodies
 - Main idea
   - application of edit distance in 3D space
   - modify protein A using twists to match protein B
   - path minimizing number of twists (twists are penalized) determines the distance of A and B

# 12 Protein structure prediction
[Prezentation](https://cunicz-my.sharepoint.com/personal/51137390_cuni_cz/_layouts/15/onedrive.aspx?id=%2Fpersonal%2F51137390%5Fcuni%5Fcz%2FDocuments%2Fteaching%2Fbioinfo%2Flectures%2Flecture12%2Dprotein%2Dstructure%2Dprediction%2Epdf&parent=%2Fpersonal%2F51137390%5Fcuni%5Fcz%2FDocuments%2Fteaching%2Fbioinfo%2Flectures)
[Lecture recording](https://cunicz-my.sharepoint.com/personal/51137390_cuni_cz/_layouts/15/onedrive.aspx?id=%2Fpersonal%2F51137390%5Fcuni%5Fcz%2FDocuments%2Fteaching%2Fbioinfo%2Flectures%20%2D%20video%2F2022%2D01%2D03%2Dstructure%2Dprediction%2D2%2Emkv&parent=%2Fpersonal%2F51137390%5Fcuni%5Fcz%2FDocuments%2Fteaching%2Fbioinfo%2Flectures%20%2D%20video)

### Outline
- Motivation
- Protein structure determination techniques
- Protein folding
- Model scoring
- Template-less prediction
- Template-based prediction
- Evaluation
- Existing tools

### Motivation
- Sequence → structure → function
-  The number of available (protein) sequences grows much faster
than the number of available 3D structures
- Given a protein sequence we want to determine its structure
  - Inverse problem to protein structure design where, given a structure, we
want to find sequence which codes for it

### Structure → function
- Inferring function from structure
  - Detection of local structural motifs with functional roles
  - Analysis of surface clefts → catalytic sites
  - Conservation analysis
  - Quaternary structure (beware of false positives due to crystallization)
  - Buried and solvent exposed residues
- Issues
  - Moonlighting proteins
    - Multiple functions carried out by a single domain
  - Conformational change of shape upon binding
    - ligand-bound state (holo structures) vs unbound state (apo structure)
  - Intrinsically disordered proteins (IDP)
    - Natively unfolded proteins

### Protein structure prediction tasks
- Secondary structure prediction
  - Assign each amino acid one of three (or more) states (helix, sheet, loop)
- Tertiary structure prediction
  - Assign each amino acid/atom its position in 3D space
- Interaction sites prediction
  - Tertiary structure (intra-molecular) contacts
  - Protein-protein/DNA/RNA sites prediction (inter-molecular quaternary structure contacts)
  - Protein-ligand (active sites/pockets) prediction

### Protein structure determination
- X-Ray crystalography (89% of all)
- NMR Spectroscopy (8%)
- 3D (cryo) electron microscopy(2%)

#### X-ray crystallography
- Crystallized protein subjected to X-ray beams, electrons disperse the beam, interfering with each other forming a diffraction patterns which is observed
- Electron density of crystal is determined by the positions of electrons (atoms) magnitudes and phases of the X-ray diffraction waves = diffraction pattern of the crystal
  - Fourier transformation is used to estimate the
electron density for each position
- Works only for proteins which form a crystal →
suitable for rigid proteins but unsuitable for
flexible proteins

##### X-ray crystallography – quality measures
- Resolution
- 3Å → secondary structure
- 2.5Å → side chains
- <1Å → hydrogen atoms
- R-factor
  - After structure reconstruction, theoretical diffraction pattern can be computed → difference between real and theoretical pattern expressed as percentage (how well model back-predicts the data)
- Rule of thumb - good structure should have R-factor lower than resolution/10 ( ≤ 0.3 for 3Å resolution)
- R(free)-factor
- When set aside data is used for the real pattern
- B-factor (temperature factor)
- Thermal motion is present even in crystal → extent to which electron density is spread out for each atom
- 𝐵 = 8(𝜋^2)(𝑈^2)

#### NMR spectroscopy
- Purified protein in a solution is put to a strong magnetic field and probed with radio waves and observed resonances (each atom has characteristic resonance in magnetic field based on its surroundings) which are analyzed to build a model of atomic nuclei and bonded atoms
- Resonances give indication of which atoms are close to each other → list of restraints to build the model
- NMR structure commonly includes ensemble of structures which fit the constraints → diverse regions correspond to flexible parts
- Proteins in solution → works also for flexible proteins which can’t be locked in a crystal
- Works for small to medium-sized proteins

##### NMR spectroscopy – quality measures
- Completeness of resonance assignments
  - Percentage of atoms for which the resonances were measured
- Statistically unusual resonances
- Random coil index
  - How does the resonance fit usual protein conformations such as secondary structure

#### 3D cryo-EM
- A beam of electrons and a system of electron lenses is used to image
the biomolecule directly.
- Cryo-EM
  - Vitrification - protein solution is cooled so rapidly that water molecules do
not have time to crystallize → thin layer of non-crystalline ice
- Thousands of 2D projection images → 3D density map → fitting atomic
model to the map
- Chemistry Nobel prize in 2017 - Jacques Dubochet, Joachim Frank and
Richard Henderson
- Ability to analyze large, complex and flexible structure
- Works for proteins in native state
- Often breaking 3Å resolution barrier

### Protein folding
- Folding (skládání) is the process through which protein obtains its three-dimensional structure
- The protein wants to fold into most thermodynamically efficient state, i.e. state with the lowest free energy
- Information for folding is (mostly) driven by protein’s amino acid
sequence through thermodynamic process
  - Anfinsen’s dogma

### Anfinsen’s dogma
- ***All information needed to fold native structure of a protein is contained in its amino acid sequence***
- Experiment with ribonuclease A (RNaseA), a 124-long extracellular enzyme
with 4 disulfide bonds
  - Observation
    1. SS bonds reduced using mercaptoethanol → denaturation with 8M urea → inactive protein, flexible random polymer
    2. Removal of urea → oxidation of –SH groups back to SS bonds → regain of more than 90% of activity
- Control (proving that the protein was unfolded)
- Change of the order of steps in second phase → 1-2% of activity and random assortment of SS
bonds

### Levinthal’s paradox
- ***Reaching native folded state of a protein by a random search among all possible configurations can take an enormously long time***
- Unfolded polypeptide chain has many degrees of freedom
- Even a small number of allowed 𝜙 and 𝜓 combinations (torsion angles) leads to astronomically large number of structures
- Proteins fold in at most seconds which is a paradox → there must be pathway or set of pathways leading to energetically favorable conformation
  - Biased search
  - When considering some conformations as stabilizing and preferred (energy bias), the folding time becomes reasonable [Zwanzig et al. "Levinthal's paradox." PNSA 89.1 (1992): 20-22]

### Template existence dependency of tertiary structure prediction approaches
 - If we have 2 proteins, then if their sequence similarity is, we can:
   - `> 30%` ... for sure,
   - `20%-30%` ... maybe (twilight zone),
   - `< 20%` ... hardly
   - make one of them template for the 3D structure prediction of the other.

### Template-less prediction
- If there does not exist a homologue (with known structure) with
respect to the target we cannot use any structure as a template and
the model needs to be build de novo (ab initio)
- Approaches
  - Molecular dynamics
    - Model the folding process
  - Conformational space exploration
    - Sample the full conformation space
  - Fragment-based approaches
    - Restrict the conformation by considering predefined fragments


