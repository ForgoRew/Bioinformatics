## 01
Martin Lepšík
Vaclav Veverka

4 fields of medical chamistry:  
1. Structural biology
2. Organic Chemistry
3. Computational Chamistry
4. Chemical Biology

### Disease Etiology
- external
  - pathogens
  - environment
    - UV & chemical induced mutations
- internal
  - genetic
    - hereditary - mutations inherited from parents
  - aging+cancer

- Viry pro 21. století - možná stojí za to se do ní podívat

- history
  - antiquity, Galen, plants, shapes of plants
  - middle ages, Paracelsus, plants, disease and drugs, toxicology, dosing
  - 1803, Sertürner, opium poppy, morphine (pain killer)
  - 1860-1880, L. Pasteur & R. Koch - germ theory of disease
  - 1909, Ehrlich, chemical, salvarsan - syfilis
  - 1928, A. Fleming, fungi, penicilin - antibiotics
  - after 1950 - molecular era - drugs&targets

- targets&drucs
  - HIV reverse transcriptase, tenofovir, A. Holy IOCB
  - DNA, Cisplatin, anticancer
  - Bcr-abl kinase, Glivec, anticancer
  - bacterial ribozome, chloramphenicol, tetraclins, resistance
  - COX-2, aspirin, covalent

- drug targets
  - mostly proteins
  - types of drugs
    - signaling proteins
    - kinases
    - proteases

- how drugs can be applied
  - oral
  - transdermal
  - intravenous injection

- interactions of drugs and body
  - pharmacodynamics
    - what drugs do to the system
  - pharmacokinetics
    - what system does to the drugs
- pharmacodynamics (PD)
  - biochemical/physiologic effects on body
  - dose,
  - therapeutic window - dose which is effective, but not toxic
  - mechanisms of action
    - enzymes (inhibition/activation)
    - ion channel (block/open)
    - receptor (agonist (activates)/antagonist(blocks))
    - direct effect - destroy cell wall by penicilin
  - mode of action (MoA)
  
- Pharmacokinetics (PK)
  - actions of body on the drug
  - depends on the route
    - liberation, bioavailability, distribution, metabolism, elimination/expression (P450)

### Process of delivering the drug
- preclinical and clinical trials
- Food Drug Agency (USA)
- European Medicin Agency (EU)

## 02 Struktura a dynamika biomolekul

...

### Covalent structure
- both nucleic acids
  - covalent modifications of the nucleotides
    - methylation - A,G,C
    - pseudouridine
    - inosine

### Non-covalent interactions
- non-covalent interactions
  - electrostatic
    - hydrogen bonds
    - ion interactions
    - stacking interactions - phenylalanine
  - van der Waals dispersion forces

### Conformational (chemical ) space

- solvation & desolvation

### Secondary structure
- helices, beta sheets, loops

- prolines - seeding helices
- glycine - breaking secondary structure elements (very free in conformation)

- helices
  - alpha
  - straight

- beta sheets
  - paralel, anti-parallel

### Quaternary structure
- also antibodies
- oligomerization/multimerization
  - often huge biological benefit (avidity etc.)

### Intrinsically disordered proteins
- proteins/regions

### Nucleic acids
- canonical/non-canonical
- structure of DNA
  - single/double stranded
  - minor/major groove

- variability - different canonical pairing has different structure properties

- RNA - more variability in structure
  - pseudoknots
- DNA
  - G-quadruplexes
  - triple-helix
  - I-motifs
  - DNA aptamers

### Molecular complexes
- biomolecules are always in context
- made for cooperation

- molecular complexes
  - (even in UniProt there is section about protein's interactions)

- lysine & glutamine make interaction

### Dynamics
- order/disorder

- Targeting dynamic proteins
  - KRAS oncoprotein

## 03 Už drug design
- chemical library screening

- binding pose of compound onto the protein
  - **native pose** - good pose
  - **decoy pose** - bad pose
- binding affinity (**score**)
  - binding free energy (jakoby pravděpodobnost, že by se takhle chytl protein s kompoundem, sortuje se pomocí toho)

- scoring of protein-ligand binding
  - several steps (when analysing the scoring process)
    - protein in water & ligand in water
    - change the binding conformation
    - imagine protein & compound in vacuum
    - resolvation process - puting it back to water
  - počítá se několik energií
    - změna konformace, entropická, solvatační atd
  - afinita = interakce + solvatace + entropie
  - covalent drugs are often toxic (may attack some proteins and cause inreversible changes)

- afinity - vzorce
  - termodynamika
    - reverzibilní reakce
      - $K_i=e^{-\Delta G/RT}$
        - $K_i$ je jakoby disociační konstanta pro *inhibitory*
        - čím menší disociační konstanta, tím lépe se váže molekula na protein
      - $\Delta G = \Delta H- T\Delta S$
  - kinetika
    - $K_i = k_{off}/k_{on}$

- nekovalentní vazby
  - Hydrogen bonds
    - slabé (C-H ... 0, C-H ... $\pi$)
    - klasické (H2O ... H2O asi)
    - solné můstky
  - další nepolární
    - $\pi$ ... $pi$ interakce (benzenové kruhy)
    - **$\sigma$ holes** - **halogen bonds**
      - na vazbách halogenů s organickými sloučeninami
      - zjištěno, že i Cl atom má kousek nabitý kladně!
    - **chalcogen bonds** - i síra má takovou **sigma-hole**

- covalent drugs
  - aspirin
  - penicilin
  - warfarin
  - bortezomib ... reverzible covalent bond, used for cancer

### Practical aspects
- protein preparation
  - broblems with missing atoms
    - often lysin with missing some atoms
    - by modeling program - adding the atoms
  - pH - what is protonated and what is not
  - tautomerie (**tautomerism**)
- ligand
  - conformation of the ligand
    - many different angles etc., choose only the most probable

- docking
  - ligand - we have ensamble of ligand conformations for docking
  - **Anchor-Grow algorithm**

- alchemical simulations
  - jde o to zjistit energie přechodů mezi stavy
    - navázaný/nenavázaný stav
    - během simulace se postupně přechází mezi stavy (malé změny)

- QM methods, MM methods (?? quantum mechanics, molecular mechanics = forcefield)

- require supercomputers, many calcs&huge amount of data
- long molecular dynamics often require also days/weeks

## 05

1. chemoinformatics
2. structure-activity relationship
3. pharmacophore
4. pharmacokinetics


* Databases of chemical compounds
  * "physical" - you can do reactions in lab with them
    * pharma companies have their own physical ones
    * Enamine, Sigma
    * academy
    * libraries are ment for different purposes/properties
      * diverse, focused, fragment, covalent, FDA approved
        * **FDA** ... food&drug agency
  * virtual
    * ZINC db, ChEMBL, ChEBI, PubChem
    * in nice formats
      * 1D: SMILES, IUPAC
      * 2D: SDF
      * 3D: XYZ, PDB etc., **MOL2** file - has partial charges

* structure-activity relationship (SAR)
  * 

## 08 Biologics
* Vaccines
* Cell therapies
* Gene therapies, RNA-based therapies
* recombinant proteins
* monoclonal antibodies

### Vaccines
* viry mají variabilní glykosilaci na povrchu
  * je těžké zacílit vakcíny, na každý kmen influenzy je potřeba jiný typ vakcíny
    * i ta glykosylace evolvuje

### Cell Therapies
* CAR-T cell therapy - léčba rakoviny
* Stem Cells - pro opravu a obnovu poškozených tkání

### Gene Therapy
* vložení nového genetického materiálu
* replacement, editing, addition, silencing
* oncolytic virotherapy

### RNA-based therapies
* mRNA vaccines !?
* RNAi therapies
  * silencing of virus RNA
  * využívá přirozeného procesu likvidace a silencování dsRNA virů

* výzvy
  * stabilizace dsRNA, aby se nedegradovalo tak rychle
    * ((glykosilace?))
    * změna části nukleotidů na DNA formu
  * doprava dsRNA do jádra
    * ((lipid nanoparticles))
  * 

### Gene Therapies
* především CRISPR
  * je možný zavést pro člověka?? možná, FDA ještě neaproovla ani jednu terapii pomocí CRISPRu
  * v procesu je něco ohledně hemoglobinu, nějaký fetální hemoglobin pro dospělého člověka či cooo

* možná se najde nějaký lepší enzym (existuje kandidát), který nestříhá divně DNA, takže bude bezpečnější pro použití v genové terapii

### Recombinant proteins
* proteiny produkované pomocí geneticky modifikovaných organismů
* produkce inzulinu, růstového hormonu a clotting factors (srážení krve)

* inzulin je možné seskládat jinak, aby měl jinou křivku nástupu po injekci
  * kovalentní modifikace lysinu na jednom místě
  * inzulin má schopnost tvořit zásobní tělíska, které mají nějaký poločas rozpadu a buňky je mohou vázat postupně
  * ((inzulinový receptor je tyrosin kináza))

### Monoclonal antibodies (mAbs)
* extracelulární cíle
* rychlejší approval (cca 60% doby pro uznání malé molekuly) - má míň "neznámých" vlastností

* značení zumab, umab, ximab, momab

* je potřeba vytvořit Ab tak, aby byla kompatibilní s organizmen
  * humanized/human antibodies
  * využívány humanized myši, které mají lidské protilátky

* často stačí malá část Ab - třeba jen tu binding site (Fab fragment)

* jde to používat i na nošení radionukleotidů
  * ničení target cells pomocí radiace
* linkování nějakých léčiv na Ab - nosiče
* linkování na immunoliposome
* použití přes T-Cell

* příklad jak působí
  * TNF - trimer, tumor necrosis receptor

### Targeted degradation of proteins
* je možné vytvořit molekulu, která se naváže na protein a indukuje ubiquitinaci. to vede k degradaci proteinu
  * PROTAC

* molekuly vedoucí k degradaci proteinu mohou být
  * rationally designed - vážou se kovalentně (PROTAC)
  * oportunistické - nenavážou se, ale indukují degradaci jen tak

