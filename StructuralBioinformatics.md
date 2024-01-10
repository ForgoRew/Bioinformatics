## Hodnocení předmětu
Šíleně dlouhé přednášky. Zvlášť ze začátku nebyly informace buďto relevantní, nebo by se výklad dal zkrátit

## 01
### Chiralita
- S- / R-
- **D- / L-**
- alpha / beta

### Souřadnicový systém/systém vzdáleností
- ortonormální (x,y,z - nm/Å)
- frakční - jde jen o jednu buňku - každou osu vydělim délkou buňky v daném rozměru
- globální ??
- chemické / interní vzdálenosti
  - vzdálenisti sousedních atomů, torzní úhly etc

### Wan der Waalsův povrch
povrch makromolekul - rozdílný pro vodu a jiné molekuly
- koulí se voda, průměr a poloměr molekuly vody
- rozdílné pro další molekuly

### Strukturní databáze
- CSD - Cambridge Structure Database
- PDB

### Krystalografie
- postup
  - získat dostatečné množství čisté látky
  - vyrůst krystaly
  - fázování
    - Fourierova cosi -> elektronové hustoty
  - Difrakce -> hustotní mapy
  - atomový model na mapu či co
  - vylepšení a validace struktury
  - interpretace struktury

- krystalizace
  - **vapor diffusion**
  - malá kapka sedí nebo visí v takový komůrce
  - je tam alá precipitant dole - odsává vodní páru z kapky s proteinem
  - kapka pomalu krystalizuje
  - jeden krystal obsahuje nějak dobře uspořádané molekuly proteinu
    - krystal = mřížka a motiv
    - mřížka ... matematický popis periodické struktury krystalu
    - motiv ... matematická abstrakce základní stavební jednotky krystalu
  - systémy krystalů
    - 7 systémů
    - 14 Bravaisovy mřížky
    - 32 tříd symetrie
    - z 14 Bravaisových mřížek a 32 tříd symetrie získáváme 240 něčeho

- X-rays mají vlnovou délku cca 1Å

- operátory symetrie
  - rotace
    - *proper rotation* ... rotace o 360˚/n
    - *screw rotation* ... rotace o 360˚/n + posun

- take home message z povídání o symetriích
  - v databázových filech máme jen informaci o jedné **asymetrické jednotce**

### Difrakce
- X-ray ... paprsky
- elektronová - pozor, není to mikroskopie
- neutronová

- jak se dělá ten experiment
  - zdroj svítí na krystal
    - stejnosměrné monochromatické rovnoměrné záření
  - detektor zachytává záření
  - difrakční obraz, takový ťupky v kružnicích
  - ty interference jsou závislý na tom, jak se sčítaj a odečítaj vlny

- pro zpětnou konstrukci makromolekuly
  - Fourierovo zobrazení
    - reflexe jdou na strukturu a naopak
    - docela náročný
    - vzniká **fázový problém**!!
      - řeší se 5 způsoby
        - mj. **molecular replacement**

## 02 Validace modelů určených pomocí krystalografie
- měření v experimentu
- konzistence s experimentálními daty
- konzistence modelu z hlediska fyziky

- všechny modely jsou aproximace

### Statistika
- přesnost a správnost
  - správnost - jak se blížíme realitě
  - přesnost - konzistence měření
  
- statistika
  - zabývá se přesností, ne správností


### Chyby
- **kde vznikají chyby** (gross and systematic errors)
  - měření
  - fázování
  - refinement elektronových hustot

- aproximace správnosti přesností můžeme provést, pouze pokud jsou naše chyby náhodné a ne systematické

- existují nástroje na odhalování chyb

- problém s normálním rozdělením
  - jen málo jevů je normálně rozdělených
  - často jsou nějak skosená

### Refinement
- 3 kroky
- postupně se vylepšuje model

- kritéria pro validaci
  - konektivita backbone a side chain atomů
    - valenční geometrie
    - distribuce torzních úhlů
      - Ramachandranův graf
  - absence stérických srážek atomů v asymetrické jednotce a napříč symetrickými operacemi
  - interpretace elektronových hustot
  - distribuce B-faktorů

- [R-factor](https://en.wikipedia.org/wiki/R-factor_(crystallography))
  - suma strukturních a pozorovaných faktorů vydělených strukturními faktory
  - počítá se v reciprokém prostoru
- [Strukturní faktor](https://en.wikipedia.org/wiki/Structure_factor#Definition_of_Fhkl)
  - souvisí nějak s fázovým prostorem, jak přesně..?

- korelační koeficient (Real Space Correlation Coeficient, **RSCC**)
  - měřím hustoty v různých bodech
  - odečtu je od sebe u různých struktur
  - počítá se buďto pro celý krystal, nebo lokálně
  - počítá se pro hotové struktury
  - někdy se používá **RSRZ** (normalizované RSCC)

### Jaké vlastnosti má dobře udělaná struktura
- přesnosti rozlišení
  - 3Å, 2Å, 1.3Å, 1Å
  - čím nižší tím lepší
  - pod 1.3Å se mluví o atomových modelech
- R factor
  - >25%, 18-22% - většina struktur, 16-18% - docela fajn, <15% výborný
- odchylky od geometrie vazeb
  - délky vazeb ne více než 0.03Å
  - úhly vazeb ne více než 3˚
- konformační kritéria, Ramachandranův graf
- RSCC - porovnání změřených a spočtených elektronových hustot

- Ramachandranův graf
  - populární - snadno se z toho něco vyčte
  - úhly peptidových vazeb
    - zpravidla jsou v trans poloze
    - pokud jsou cis - může být, ale nepravděpodobné
    - pro každou aminokyselinu jsou různé povolené možnosti

- **RMSD / RSCC** graf
  - kombinace těchto dvou ukazatelů
  - některé oblasti velmi pravděpodobné
  - některé velmi nepravděpodobné

### Validační software
- validace na PDB
  - pro přidané struktury
  - pro novou strukturu to taky jde, ale je to složitější
  - Coot modeling software - vizualizace + podmínky
  - Číselné
    - Phenix
    - Refmac

- R-faktory mají různé modifikace
  - (Fall ...) **Rall** - klasika R-faktor
  - (Fobs) (F>3sigma) - **Robs**
  - **Rfree** - zabránění přerafinování struktury - něco jako přetrénování modelu - přidání příliš tvrdých podmínek, převálcování experimentu
    - z celkového počtu reflexí vezmeme 10%
    - 90% refinujeme
    - Rfaktor zfurierovaných reflexí se nesmí lišit od nezfurierovaných o moc (o 3 třeba)
    - potom se přidá zbytek těch 10%, aby se dolepšila rafinace a pak se z toho spočítá Rall
    - často se bere míň reflexí, třeba 5%, když jich je dost
    - **Rwork** je to R-faktor z 90%

- clashscore
  - vážený počet a vážnost těsných kontaktů mezi atomy

- 3D validace
  - graficky ukázané potenciální problémy (clashe atd.)

- **RMSZ**
  - normalizovaná RMSD
    - ale asi je to blbost..?
    - beef na normalizaci

## 03 Databáze
- **CSD** & PDB
  - **CSD** je chemická databáze
  - archivní databáze
  - primární a sekundární informace
    - struktura i anotace
  - je možné v nich "snadno" vyhledávat
- rozdíly
  - formát archivovaných dat
    - CSD - topologie
    - PDB - fragmenty (monomery a ligandy zvlášť)
  - architektura databáze
    - úplně jiný
  - dostupnost
    - PDB mega dostupná
    - CSD autorizovaný přístup, registrace atd., ale pro akademické využití to jde. Ale nefunguje v prohlížeči, vlastní software

- 3D molekulární struktury

* požadavky na databázi
  * škálovatelnost
    * při velkém množství položek je potřeba strukturovanější organizace
  * flexibilita
    * možnosti rozšíření informací
    * např. při přidání NMR metody, tak jsou úplně jiné položky - ne rozlišení, ale např. více modelů naráz
  * dlouhodobá podpora jazyka
    * C++ např.
    * ne Pearl
    * S tím souvisí dobrá dokumentace
  * plní 3 základní úkoly:
    * umožňuje depozici
    * archivaci a je dlouhodobě udržovaná (sustainability)
    * distribuci

* co dalšího potřebujeme od databáze
  * dobrá znalost/kvalita dat
    * znalost obsahu
    * znalost struktury a kvalita struktury - slovník (= ontologie)
  * organizace
  * ... něco ještě

## 04 Molekulární modelování
Jiří Černý z Elixiru & Biocevu  

### Základy modelování
- Anfinsen
  - platí, že nativní struktura biomolekuly odpovídá její globálně nejnižší energii
    - do toho je třeba zahrnout rozpouštědlo (voda), membránu, ionty, ligandy, externí pole atd
- problém je, že často nevíme, jak okolí molekuly přesně vypadá
- kvantová/molekulární mechanika (mol. mechanika = mol. dynamika)
- pozice atomů jsou definované pomocí kartézských souřadnic/interních souřadnic
  - typicky `xyz` formát
  - **Z-matrix** pro interní souřadnice

- 3n-6 ... kolik má molekula stupňů volnosti

### Kvantová mechanika
- dost náročný na čas a prostor

### Molekulová dynamika
- trochu simpletonský

### Programy
- QM - kvantová mechanika
  - Gaussian, TurboMole, Molpro - komerční
  - **orca** - open-source implementace TurboMole
  - **psi4** - vysvětluje vnitřní mechaniku simulací
- MM (MD)
  - Gromacs
  - amber
- Empirical
  - FoldX
  - Modeller
  - Rosetta

## 05 Strukturní alignment
- **strukturní alignment**
  - může být užitečný, pokud chceme rozhodnout o homologii dvou a více struktur
  - pokus o co největší překryv dvou polymerních struktur

- kdy dále se nám bude strukturní alignment hodit?
  - možnost **structure based sequence alignment**
  - hledání strukturních motivů
  - anotace struktury
  - popis konformačních změn
  - benchmark pro sequence alignment
  - základ pro structure based MSA

- structure based sequence alignment
  - má zpravila více mezer, než běžný alignment
  - zpravidla o něco nižší sekvenční identita
  - pomůže odhalit funkci, ale i příbuznost v midnight zóně

- rychlosti evoluce
  - proteinová jádra se vyvíjí lineárně
  - struktura je 3-10x konzerovanější než sekvence
  - rozdíl v rychlosti evoluce u nekonzervovaných struktur je až 5 řádů
  - beta listy mají rychlejší evoluci než helixy

- **superpozice** vs. strukturní alignment
  - superpozice není alignment
  - vyžaduje mít už sekvenční alignment
  - často dvě struktury jednoho proteinu
  - optimalizace vzdáleností a úhlů
  - obvykle jen C-alpha atomy
  - program SuperPose

- **postup heuristiky**
  - najdi alignment
  - optimalizuj ho

- heuristiky
  - zjednodušení popisu struktury
    - vytvoření matici vzdáleností
    - ignorování všeho, kromě sekundárních struktur
    - předělání na komix
    - metody pro sekvenční srovnávání

### Programy
- **DALI**
  - Holm&Sander 1993
  - Distance-matrix ALIgnment tool
  - pro dvě struktury (A,B)
    - vezme strukturu A, B, změří jejich intrareziduální vzdálenosti
    - porovnává obě matice mezi sebou
    - podobné podmatice matic jsou pravděpodobně u sebe
  - pomalá metoda, pro dvě struktury asi 2minuty
  - existuje dobré mapování mezi strukturami v prostoru a reprezentované intrareziduálními vzdálenostmi
- **VAST**
  - Vector Alignment Search Tool
  - srovnávání pouze sekundárních struktur reprezentovaných vektory
- **SSM**
  - podobné, jako VAST, v PDB

- **3DBlast**
  - rozsekání řetězce na cca 6 AK

- **FATCAT**
  - flexibilní alignment
  - identifikace AFPs - aligned fragment pairs

- **TM-align**
  - používá jen CA atomy
  - získání iniciálního alignmentu - dynamické programování
  - iterativní heuristický algoritmus
  - definuje TM-score
    - template-modeling score
    - vzdálenost atomů v superpozici
    - normalizuje se na délku proteinu (nevadí dlouhý protein)
    - cca >0.5 TM-skore je dobrý

- **PhyreStorm**
  - vyhledávání podobných struktur
  - klastruje PDB proteiny
  - nejdřív se protein srovná s clustery
  - pak až jde k jednotlivým proteinům

- **SSAP**
  - velmi starý
  - pro každý atom se dívá na několik okolních atomů
    - CB atomy
  - distanční vektory z nejbližších CB atomů

- **FoldSeek**
  - přístup FoldSeeku
    - konstrukce knihovny
      - 3D podstruktury (jakoby motivy)
    - TMalign
    - běžný sekvenční alignment
  - vysoká citlivost - podobné struktury jsou určitě nalezeny

### Optimalizace alignmentu
- optimalizace superpozice atomů
- superpozice jako RMSD CA atomů
- rotuje se, minimalizují se vzdálenosti mezi atomy

### Hejt na RMSD
- globální parametr, ale citlivý na lokální změny
- **SAS skore** - normalizované RMSD na počet alignovaných aminokyselin - lépe odpovída
- **TM score** - normalizované na počet atomů v sekvenci
  - zabývá se více jádrem - je lépe konzervované

- **CASP**

- **GDT-TS**
  - kolik atomů je pod 1, 2, 4, 8Å
  - měří se, kolik jednotlivých atomů je na správném místě

### Rigidní vs. flexibilní alignment
- nesmí nebo smí být struktury trochu změněny?
  - v případě flexibilního - ve "spojích" (hinge) se proteiny smí hýbat

## 06 Strukturní alignmenty II
- **databáze** se **strukturními** alignmenty proteinů
  - BALIBASE, SABMARK, HOMSTRAD, HOMFAM
  - DASH ... využívá MAFFT a sum of pairs - zarovnané pozice, součet
  - PASS2 ... verze 5, přestože verze 6 a 7 jsou publikované

- strukturní alignmenty se hodí pro **přenos znalosti** části vlastností prozkoumaného proteinu na jemu homologní

- strukturní alignment může být **reprezentovaný jako MSA**

- **problémy**
  - proteiny často **nemají známou strukturu**
  - strukturní alignment je velmi dobrý pro **lokální struktury**, ale často **špatný pro globální alignment**
    - i pro "domény" je to náročné - často nevíme, kde začíná a končí daná doména
  - **malé změny** ve struktuře mohou udělat **velký rozdíl** v alignmentu
    - i pro různé **krystalografické struktury** jednoho proteinu mohou být alignmenty dost odlišné
  - nástroje mají velmi rychlý **"turn-over"**
    - často nástroj stojí na jednom člověku, který ho udržuje - **odejde člověk, přestane být funkční nástroj**

- **ideální nástroj**
  - často je **více možných konfigurací**, je **těžké je odladit**
  - často je ta "ideální konfigurace" na **webové verzi nástroje**
  - Marian popisuje svůj benchmarkový výzkum
  - závěr je, že je lepší **kombinovat více** služeb, dobře dopadla např. **DALI**

### Klasifikace struktur
- dělá se na **strukturním alignmentu domén**
- **pro domény**, nikoli pro proteiny
- otázky:
  - **které tvary** jsou úspěšné?
  - **proč** je úspěšný?
- problémy:
  - **rozsekat** proteiny na domény je náročné

- doména
  - jednotka evoluce
  - často kompaktní a globulární struktura
  - nezávislá při balení

- systémy klasifikace
  - FSSP
    - automatický pomocí DALI
  - SCOP
    - manuální
  - CATH
    - poloautomatický, asi nejfunkčnější v současné chvíli

- **SCOP**
  - manuální klasifikace
  - původně úplně lidsky, Alexej Durzin
  - klasifikoval proteiny, prostě je určoval
  - zahrnuje informace, které neplynou ze struktury, i četba literatury
  - po 2000 nefunkční, protože struktur bylo už moc
  - oživení v 2020, poloautomatická
  - SCOP ... 4 úrovně klasifikace (původně)
  - nyní SCOP 2, složitější ... potomek může mít více rodičů, složitější klasifikace

- **CATH**
  - nejvíc používaný
  - Class Architecture Topology Homology
  - CATH-Gene3D ... odhad struktury podle sekvence, na základě podobnosti, "mapování"
  - proteiny v úrovni **"topology"**
    - nízká sekvenční identita, ale často sdílená funkce
  - klasifikace
    - Class
      - mají stejný typ sekundárních struktur
    - Architecture
      - kolik sekundárních struktur mají
    - Topology
      - propojení sekundárních struktur dohromady
    - Homology
      - velmi podobné proteiny
      - uvnitř toho ještě **FunFams** - proteiny musí (pravděpodobně) sdílet funkci 
    - (Superfamilies)
      - proteiny, které jsou v podstatě stejné - velmi velmi podobné
  - "algoritmus"
    - jmenuje se CATHEDREL
    - automatická identifikace domén ve struktuře
    - v případě nejasnosti se struktura předá k vyřešení člověkem
  - o doménách se generuje množství užitečné statistiky

- podobnost foldů
    - jak určit, jestli jsou podobné foldy dva, nebo jen jeden variabilní?
    - určování struktury proteinů, které mají velmi nepodobnou strukturu se známými

- funfact
  - TIM barel je velmi odolný proti mutacím
  - i pro zmutované AA uprostřed alpha helixů etc mají pořád stejný fold
  - zároveň ale TIM barely mají velmi širokou škálu funkcí

- pro 90% protein coding sekvencí z DNA existuje kategorie v CATH
- nové foldy jsou vyloženě vzácné

- přes AlphaFold se nacházely nové foldy
  - některé nové byly nalezeny
  - často multidoménové proteiny + špatně definované známé kategorie (false positive určení nové struktury)
  - přesto 618 postoupilo do manuálního určování
    - vyřadili všechny nevhodné
  - našli asi reálně 25 nových foldů (cca +2% foldů, pokud by prošli všechny proteiny, cca +8% foldů)
    - často jsou to velmi velké domény (100+ AAs)

- ECOD
  - systém klasifikace, na vzestupu
  - proteinové struktury, spojení HMM, MSA a SA
  - více kategorií než CATH
  - pořád ale hierarchický systém
  - částečně manuální

### RNA struktury
- často neznámé funkce
- důležitý bude alignment
- non protein coding RNA - je jich vlastně víc, než protein coding
- jsou i velmi velké <=> výpočetně náročné

- jedna z metod pro RNA je SETTER
- webové rozhraní
- srovnávání RNA (SA)

### DNA struktury
- hledá se způsob sbalení DNA
- např. TF Compare

- US-Align
  - srovnají všechno, co se jim zadá

## 7 Predikce struktury
- Anfinsenovo dogma
- Levinthal ... predikce = simulace balení proteinu

- způsoby (od nejpříbuznějších k nejméně příbuzným)
  - homologní modelování
  - threading
  - ab initio modelování

- **homologní modelování**
  - využití
    - pro **molekulární nahrazení** pro vyřešení fázového problému u krystalografie
    - pro zaplnění prázdných míst u neurčených struktur
      - aby se o tom dalo alespoň nějak přemýšlet
  - postup
    - **výběr templatu**
      - BLAST, FASTA, i HMM (citlivější na vzdálenější sekvence)
        - pokud jsou ale sekvence moc vzdálené, je lepší použít Alpha Fold 2
      - template s lepší kvalitou udělá lepší model
      - template musí být biologicky správný
        - správná kvartérní struktura, ligandy a komplexy
    - **alignment**
      - kvalitní set ortologických sekvencí
      - můžeme zchecknout mezery v alinmentu
        - nepravděpodobná např. inzerce v alpha helixu
    - **stavba modelu**
    - snížení energie molekuly (molekulová dynamika)
    - modelování smyček - cca do 10 AK, větší už nejdou predikovat spolehlivě
    - hledání konformací postranních řetězců

  - programy
    - Modeller
      - vytváření podmínek pro model
        - probability density functions
        - hledání co nejmenšího konfliktu s templatovou strukturou
    - Swiss-Model
      - plně automatický = nemůžeme ovlivnit, co bude model
    - WhatIf
    - Rosseta
    - I-Tasser
      - někdy lepší modely, umí udělat nějaké strukturní srovnání
    - někdy je fajn zkusit víc nástrojů, zjistíme, jestli mají shodu

  - problémy
    - nemáme template/máme jich příliš mnoho
    - template je nekvalitní
      - molprobity >2 je spíš špatný


## 08 Predikce proteinové struktury
### Profilové metody
- Phyre
  - převedení sekvence do 1D
    - každá aminokyselina patří do jedné z 18 kategorií
    - podle toho, v jaké je sekundární struktuře (3 typy) a jak moc je "na povrchu či v jádru molekuly"
    - porovnává sekvenci bez struktury se známými strukturami
  - Phyre je velmi rychlý, funguje podobně jako homologní modelování
  - pro úplně neznámé proteiny bohužel nedá žádný výsledek
  - pro každou pozici dává její "důvěryhodnost"
### Threading
- X-Raptor

### Alpha Fold 2
- pLDDT score
  - skóre pro lokální strukturu
