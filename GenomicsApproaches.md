## Sylabus
Microarrays
Sequencing technologies
QC
Resources - databases & large projects
Mapping
Assembly
Variant calling
CNV calling
Phasing/Imputation
RNA-seq, single-cell analyses
ChIP-seq
Structural variation
Metagenomics
Data integration, visualization

## 01 Next Generation Sequencing
Martin Převorovský  

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

