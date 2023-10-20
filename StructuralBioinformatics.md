# Hodnocení předmětu
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

