## Sylabus
1. Microarrays
2. Sequencing technologies
3. QC
4. Resources - databases & large projects
5. Mapping
6. Assembly
7. Variant calling
8. CNV calling
9. Phasing/Imputation
10. RNA-seq, single-cell analyses
11. ChIP-seq
12. Structural variation
13. Metagenomics
14. Data integration, visualization

## 01 Next Generation Sequencing
Martin Převorovský  
Petr Daněček  

- cvičení
  - samostatná práce
  - zápočet -> zkouška

- NGS
  - clonal DNA populations
  - single molecule sequencing

- ABi Solid??
- BGI-SEQ

- NGS
  - cca 100-150nt
  - postup
    - (převedení RNA do DNA)
    - vytvoření sekvenační knihovny (přidání primerů atd.)
    - klonální amplifikace DNA
    - sequencing + basecalling (převedení signálu na báze)
    - datová analýza

- Illumina
  - ssDNA fragmenty jdou na *flow cell*/*lane*
    - *flow cell* je sklíčko s kanálkama (*lanes*)
  - klonální amplifikace
    - ssDNA se připojí na kotvy (*adaptérová* sekvence) (komplementarita bazí)
    - replikuje se
    - jde o to mít toho "hodně"
    - máme jen jednu polaritu - druhou vymyjeme
  - pošlou se reverzibilní terminální dNTPs - dNTP, který ukončí polymeraci, ale jde odblokovat - odmyje se
  - s každým dalším cyklem se snižuje intenzita signálu a zvyšuje se šum - kvůli odmývání a občasné neúspěšné polymeraci
  - vytvoří jeden read
    - ready mají fixní délku
  - datová analýza
  - stroje
    - HiSeq series
      - 2x 150nt reads, až 2x 250nt za použití některých komponent
      - ~1.8Tb/run
      - cca 6 miliard readů
      - cca 3 dny to běží
      - human genome <1000$
    - NextSeq
    - MiSeq
      - ready 2x 300nt
- limitace pro Illuminu
  - krátké ready, tzn. nedokáže zpětně seskládat
    - repetice
    - často alternative splicing
    - haplotype determination

- single molecule sequencing
  - sekvenuje se jedna dlouhá molekula
  - stovky kb
  - vyvažuje nevýhody Illuminy
  - bohužel vysoká chybovost
  - Oxford Nanopore

- Oxford Nanopore
  - malinkaté rozměry (ala flashka)
  - membrána, pór a motorový protein
  - změny elektrického proudu
    - z toho se odvozuje, jaké nk prochází - vždycky k-mery
    - v póru je několik nk naráz

- PacBio (Pacific Biosciences)
  - fluorescence - fluorescenčně značené nukleotidy
  - cca 20kb
  - 3nk/sek

- typical NGS workflow
  - design of experiment
  - obtaining DNA/RNA & quality control (=QC)
  - sequencing
  - QC of sequencing data
  - read mapping (+QC)
  - analysis
- většinou není možné použít nějaké řešení, které ošetři všechny požadavky experimentu

- design of experiment
  - which animals/tissues
  - size of sample - with respect to the statistics of the experiment
  - blinded/double blinded tests
    - control sample
  - replicates
  - read lengths
    - usually Illumina, very short reads
      - the shorter, the faster
        - the cheaper
        - sometimes - better quality
  - sequencing depth
    - how many reads you need
    - Illumina's maximum is 150milion reads
  - coverage
    - while mapping the short reads to whole genome, it is how many short reads "cover" the long read
  - single-end/paired-end
  - strandedness
    - is it in sense/antisense strand?
  - multiplexing

- MINSEQE guidelines
  - Minimum INformation about high-troughput SEQuencing
  - by Functional Genomics Data Society
- primers
  - functions
    - catching the sequence
    - "barcodes" - we know what starting sequence is on one size

- single end/paired end sequences
  - víme, jak vypadá začátek readu vs víme, začátek i konec readu

- library preparation
  - DNA fragmentation
  - PCR amplification - need to meassure the concentration

## 04 HTC-QC
[prezentace](https://dl2.cuni.cz/pluginfile.php/76101/mod_resource/content/1/hts-qc.pdf)  

- SAM/BAM
  - mapovací formáty
  - reference genome, pak namapované kratší sekvence
- CRAM
  - reference based compression of SAM/BAM - shows only differences from the reference sequence
- VCF
  - variant calling format - v principu může mít každá pozice v reference genomu vlastní řádek s variantami a popisem

## 05 Pokračování předchozí (04)
- **De novo sequencing** vs. **resequencing**
  - sequence variation
    - not de novo, we can see SNPs, indels & structural variation (**SV**)

- mapování readů
  - suffix tree -> suffix field -> **Burrow-Wheeler** transformation
    - upravené suffixové pole, seřadit lexikograficky, pak se vezme poslední sloupec
    - dvě pole - první výskyt daného znaku

## 6 RNA-seq II
- RNAs
  - splicing in eukaryots
  - reverse transcription to DNA
  - single stranded - it has it's polarity to remember from which strand of DNA it came from
  - not so stable

### getting RNA
- typy RNA
  - nejvíc ribozomální (>90%)
  - translační RNA
  - mRNA

- snaha **zbavit se rRNA** - je hodně konzervované a tím pádem nezajímavé
  - jen pár genů, pořád se opakují
- příklad s koronavirem
  - chceme jen koronavir, ne lidské RNA
  - musíme vytvořit specifické primery - vytvoříme amplikony - získáme jen to, co chceme

- kontrola kvality amplifikované RNA
  - na elektroforéze se podíváme, kolik čeho je
  - získáme nějakou hodnotu kvality

- rRNA problém
  - můžeme ho **biotinovat** - biotin je na nějaké specifické sekvenci
  - na biotin pak použijeme třeba **streptavidin**,, který se na něj naváže
    - na **streptavidin** je navázaný nějaký magnetek
    - magnetem ho dostaneme z roztoku
  - můžeme to udělat i **naopak pro mRNA** - dáme biotin na sekvenci TTTTTTT, která je komplementární s polyA ocáskem mRNA
    - pak naopak magnetem přitáhneme mRNA a zbytek vylejeme

- někdy chceme ale získat úplně specifická RNA, takže pak to je **složitější**

- **cDNA priming**
  - musíme vzít náhodné hexamery jako primery
    - hexamery nejsou úplně náhodné
    - dělá to na začátku zvláštní šum
    - pak už to je ale náhodný
  - vhodné, pokud chceme mít obecný přehled o "všem"
  - pokud chceme získat jen něco specifického, musíme zvolit jinou techniku, např. amplikony

- vrámci přípravy RNA library se zachová informace o tom, který strand byl původní

- kontaminace **jadernou RNA**
  - použijeme DNázu, která to od něj pročistí

### RNA-seq for quantification
- we map the sequences on the reference molecule
- has 2 rounds
  - 1. we map as many reads as possible
  - 2. we map the reads, which should have some gap inside - have some kind of exon etc.

- metriky
  - RPKM (SE)
    - reads per kilobase per million reads mapped
  - FPKM (PE)
    - fragments per kilobase per million reads mapped
  - TPM
    - transcripts per milion

## 07 Variant calling
- naivní variant calling
  - postup
    - počítáme, kolik namapovaných sekvencí má stejnou/alternativní alelu jako reference sekvence
    - vyhodíme namapovaný read, který se hodně liší od referenční sekvence
  - problémy
    - i read s malou kvalitu 
- Bayesův teorém

- mpileup
  - pileup - máme mapované sekvence
  - děláme z nich vcf

- filtrování
  - snaha odstranit chyby
    - kontaminace
    - PCR errors
    - mapping errors
    - etc.

- **Fisher's test**
  - kontingenční tabulka

|   | >  | < |
|---|----|---|
| R | 1  | 4 |
| A | 12 | 0 |

Je to pravděpodobný? Asi ne.




`Hardy-Weinberg & natural selection?`

## 10 ChIP-seq
((Chromosome Imuno-Percipitation))

- chromatin
  - histones
  - regulators
  - chromatin remodeling enzymes
  - proteins for modification of histones
  - ...
- 

- pomocí ChIP sequ můžeme zjistit, na jaká místa v genomu se navázal (např. transkripční faktor)
- můžeme zjistit, jaké geny reguluje
- můžeme shromáždit informace o tom genu

- postup
  - fixace chromatinu buňky pomocí formaldehydu
  - rozbití genomu na kousky
  - pomocí IgG označení fragmentů s targetovaným proteinem
  - vytáhnutí (fish-out) IgA označených částí
  - odpoutání DNA od proteinů
  - sekvenace DNA -> získáme znalosti o daných úsecích DNA, které byly navázány na náš protein

- postup podrobně
  - fixace chromatinu buňky
    - pomocí
      - formaldehydu
      - nemusí tam být i nic, pokud se jedná o histony
    - problémy
      - nedostatek kroslinkingu - nevytáhneme všechny kousky s naším proteinem (odpadne)
      - příliš kroslinkingu - vytáhneme i to, co nechceme, noise
  - rozbití genomu na kousky
    - musíme rozbít na dobře definované kousky
    - způsoby
      - ultrazvuk (sonication)
      - microcoal nuclease
        - dokáže sníst všechno DNA, které není chráněné nukleozomem
        - více diskrétní - 1 nukleozom chrání cca 146 bp
  - pomocí IgG označení fragmentů s targetovaným proteinem
    - antibodies musí být validované na ChIP-seq - ne každá to umí
    - na IgG se naváže A/G protein z bakterie (A/G dobře vážou protilátky)
      - mají ještě na sobě malý magnetek
      - pomocí magnetu se vytáhnou z kapaliny
    - 
  - vytáhnutí (fish-out) IgA označených částí
    - magnetek, někdy stačí centrifugace
  - odpoutání DNA od proteinů
    - zahřátí na cca 65˚C
  - sekvenace DNA -> získáme znalosti o daných úsecích DNA, které byly navázány na náš protein
    - vrámci toho bude i faakt hodně noisu
  - uděláme statistickou analýzu toho, z jakých pozic na DNA jsme získali kolik readů -> víme, které frekvence byli enhancnuté pomocí těch prvních kroků ChIPu

- kontrola ChIP sequ
  - kontrolované kroky
    - input DNA
    - irrelevantní protilátky
    - KO
  - můžeme udělat negativní kontrolu
  - typické artifakty
    - "phantom" peaks
      - hodně transkribované geny se nějakým způsobem objevují jako více sekvenované
      - hodně aktivní promotory - dobře vážou cokoliv, takže mohou být snadno fishovány ven


## 11

