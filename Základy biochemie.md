# ***Základy biochemie***
![](https://images.newscientist.com/wp-content/uploads/2019/10/22153920/biochemistry-shutterstock_187967735_web.jpg)

- [***Základy biochemie***](#základy-biochemie)
- [01 Prolog a prerekvizity, voda a aminokyseliny](#01-prolog-a-prerekvizity-voda-a-aminokyseliny)
- [02 A Proteiny - struktura](#02-a-proteiny---struktura)
- [02 B Proteiny - struktura a funkce](#02-b-proteiny---struktura-a-funkce)
- [03 Proteiny - enzymologie](#03-proteiny---enzymologie)
- [04 Sacharidy](#04-sacharidy)
- [05 Glykogen](#05-glykogen)
- [06 Cyklus kyseliny citronové](#06-cyklus-kyseliny-citronové)
- [07 Oxidační fosforylace](#07-oxidační-fosforylace)
- [08 Fotosyntéza a 09 Alternativní dráhy sacharidů](#08-fotosyntéza-a-09-alternativní-dráhy-sacharidů)
- [10 Lipidy a membrány](#10-lipidy-a-membrány)
- [11 Metabolismus lipidů](#11-metabolismus-lipidů)

Poznámka: U témat najdete často prokliky na prezentace. Jsou to originální prezentace z kurzů na Moodle, takže je nejspíš potřeba být zaregistrován v kurzu Základů biochemie (ze ZS 21/22) a být přihlášen do CASu. Prokliky na YouTube přednášky by ale měly fungovat i bez přihlášení.



Chyby?: Nejvíc tricky mi přišlo, jestli se něco oxiduje nebo redukuje. Při práci s materiálem prosím použijte vlastní rozum a chyby kdyžtak komentujte, nebo mi pište. To stejné i s jinými chybami. Díky moc!

Pro jistotu:
 - oxidace ... daná látka/skupina zvyšuje svoje oxidační číslo
 - redukce ... dtto snižuje svoje oxidační číslo
 - např. při 2H2 + O2 -> 2H2O se vodík oxiduje (odevzdává elektron) a kyslík redukuje (přijímá elektron)
 - NAD+ ... nikotin adenin dinukleotid, nabíjí se na NADH, někdy uvidíte i NADH+H+, což je proto, že NAD+ přijímá kromě dvou elektronů i proton (snad jsem to vysvětlil dobře, kdyžtak odkaz na [Wikiskripta](https://www.wikiskripta.eu/w/NADH,_NADPH))
 - NADP ... nikotin adenin dinukleotid fosfát - funguje trochu jinak než NAD kvůli přítomnosti fosfátové skupiny, vyrábí se v pentózofosfátové dráze a využívá se k syntéze mastných kyselin, viz odkaz výše
 - FAD ... riboflavinadenosin difosfát - nabíjí se na FADH2 a slouží v OXFOS k přenosu protonů a nabití CoQ, jeho energetická výtěžnost je ale menší než u NAD+, viz [Wiki](https://cs.wikipedia.org/wiki/Flavinadenindinukleotid) a přednáška "[07 Oxidační fosforylace](#07-oxidační-fosforylace)"

Doporučuju:
 - [zápisky od Eugleo](https://eugleo.github.io/bioinformatika/doc/zaklady-biochemie/notes.html)
 - U prezentací pak moc doporučuju shrnující slidy na konci. Jsou tam všechny důležité informace shrnuté.

Poděkování:
 - také děkuji všem autorům všech obrázků a obsahu v odkazech, děkuji takto společně, protože kdybych měl všechny citovat, tak by tyhle výpisky trvaly stejně dlouho jako dělat bakalářku a to úplně nechci

# 01 Prolog a prerekvizity, voda a aminokyseliny
1. Které vazby v biomolekulách jsou polární a proč?
 - jsou to vazby mezi ionty, molekuly, které mají náboj inukovaný díky nějakému velmi elektronegativnímu atomu a podobně.
2. Proč existuje na molekule vody dipólový moment? Co určuje tvar molekuly vody?
 - protože je v ní přítomen kyslík s vysokou a vodík s nízkou elektronegativitou. Tvar molekuly ovlivňuje především náboj vodíků a tvar orbitalů p.
3. Proč se vytvářejí vodíkové můstky mezi molekulami vody navzájem a mezi molekulami vody a polárními skupinami?
 - slabý náboj vodíků a kyslíku umožňuje vznik nevazebných interakcí jak mezi jednotlivými molekulami vody, tak i mezi jinými nabitými molekulami a vodou
4. Co určuje pH a co určuje tzv. iontový součin vody?
 - pH je -log([H+]) v roztoku. Iontový součin je určený silou, jakou je kyslík vázán k vodíkům a z toho vyplývající pravděpodobností, s jakou se vodíky mohou odštěpit. Ta je K=(10^-7*10^-7)/1=10^14
5. Které vlastnosti vody jsou důležité pro život? Proč má voda takové vlastnosti?
 - hodně důležitá je např. její hustota v kapalném a pevném skupenství. 
 - vysoká pohyblivost H_3O^+
 - vysoká hodnota dielektrické konstanty
 - vysoké měrné výparné teplo
 - vysoké povrchové napětí
 - vysoká měrná tepelná kapacita
6. Na čem je založena vysoká pohyblivost iontů H3O+ a OH- ?
 - **Grothussův mechanismus** - proton H+ přeskakuje mezi molekulami...
7. Proč se amfipatické molekuly ve vodě shlukují?
 - protože nabitá část jde směrem k vodě a nenabitá od ní
8. Co to jsou enantiomery? Liší se chemickými vlastnostmi?
 - molekuly, které se liší jen opticky
9. Kolik center asymetrie mají které AK?
 - zpravidla 2 **!**
10. Které charakteristiky AK lze odvodit z jejich struktur?
 - jsou to nabité molekuly, jejich R skupiny mohou být také nabité...
11. Které AK jsou nabité při fyziologickém pH?
 - `TODO`
12. Jak lze popsat disociaci skupin alaninu se znalostí hodnot disociačních konstant dvou disociovatelných skupin?
 - má dvě hodnoty pH, při nichž odštěpuje proton
13. Co to je prochiralita?
 - prochirální molekuly nemají rotační symetrii, tzn. mají různé enantiomery
14. Které posttranslační modifikace AK znáte?
 - fosforylace, metylace, acetylace, hydroxylace

# 02 A Proteiny - struktura
1. Jaká reakce vede ke vzniku peptidové vazby, jak se liší peptidová a isopeptidová vazba?
 - peptidová vazba je standardní vazba ak v proteinu. Isopeptidová vazba funguje na stejném principu (NH2+COOH)->(NHCO), ale vzniká u postranních řetězců ak (lysin + kys. asparagová)
2. Vlastnosti peptidové vazby.
 - trans ~ 85kJ/mol, cis ~ 77kJ/mol
3. Jak fungují peptidyl-prolyl-cis-trans-isomerasy?
 - katalýza otočení u peptidové vazby mezi nějakou ak a prolinem
4. Které sekundární strukturní motivy se vyskytují v proteinech nejčastěji a proč?
 - alpha helixy a beta listy, protože jejich struktura využívá nábojů ak a úhlů mezi vazbami ke své stabilizaci.
5. Co určuje stabilitu alfa-helixu. Jak přispívají ke stabilizaci/ detabilizaci helixu jednotlivé R-skupiny?
 - směřují ven s helixu a tak ovlivňuje strukturu helixu
6. Co určuje stabilitu beta-struktur?
 - R-skupiny aminokyselin a prostředí
7. Jaká je architektura alfa-beta soudku (TIM soudku)?
 - 8 alpha helix, 8 beta soudek
8. Jak jsou stabilní nativní konformace proteinů a jakými vlivy je lze denaturovat?
 - ss můstky, elektrostatické síly, vodíkové můstky, hydrofobní interakce
9. Jak se bude lišit struktura proteinu z hyperthermofilního organismu od téhož typu proteinu z organismu žijícího v „běžných“ podmínkách?
10. Které síly určují stabilitu proteinů?
 - `TODO`
11. Které modely skládání proteinů znáte?
12. Co to znamená, že skládání proteinů probíhá hierarchicky?
13. Jak se může lišit skládání proteinu in vitro od situace uvnitř buňky?

# 02 B Proteiny - struktura a funkce
1. Na jakém principu interagují helixy ve dvojité nadšroubovici - například v protofibrilách keratinu nebo tropomyosinu?
 - vodíkové můstky hydroxyprolinu, 
2. Na jakém principu funguje trvalá ondulace (vlasů u kadeřníka)?
 - kyselina thyokglykolová dočasně rozvolní strukturu filamentárního proteinu keratinu
3. Jsou Gly či Pro kompatibilní se strukturou alfa-helixu? Jaké AK jsou preferovány ve struktuře helixů kolagenu?
 - ano, glycin je na každé třetí pozici, hydroxyprolin pak zvyšuje sílu interakce mezi jednotlivými helixy 
4. Co je molekulární podstatou onemocnění kurdějemi a jaký je projev chronického nedostatku vitaminu C?
 - vitamín C je kofaktor pro prolin-hydroxylázu, která je esenciální pro správné skládání kolagenu.
5. Proč potřebují organismy přenašeče kyslíku v tělních tekutinách?
 - protože kyslíku by se v tekutině bez přenašečů rozpustilo jen málo.
6. Co je společnou vlastností těchto přenašečů?
 - jsou vždy kombinací polypeptidu a kovového atomu (Fe/Cu)
7. Co je to kooperativita?
 - synchronizovaná aktivita / změna konformace makromolekul
8. Co je to alosterie?
 - alosterie je mechanizmus, který umožňuje změnu funkce aktivního místa proteinu pomocí ligandu k alosterickému centru
9. Jak se liší saturační závislost myoglobinu a hemoglobinu?
 - u myoglobinu není efekt kooperativity, takže saturační závislost má u něj tvar hyperboly, zatímco u hemoglobinu je křivka sigmoidní, protože 4. kyslík se na molekulu váže se 100x větší afinitou, než první molekula
10. Jakou roli má v organismu myoglobin?
 - myoglobin slouží jako zásobárna kyslíku pro tkáně s jeho vysokou spotřebou
11. Některé druhy antarktických ryb nemají ani myoglobin ani hemoglobin. Jak mohou přežít?
 - jsou malé a voda je při nižších teplotách schopna rozpustit více O2
12. Jak se mění struktura hemu při vazbě kyslíku?
 - pyramidová struktura porfyrinu se stane planární (rozdíl cca 0.6A)
13. Jak se mění struktura Hb při vazbě kyslíku?
 - "otevřou" se i další 3 místa pro vazbu kyslíku (respektive změní strukturu tak, že získají větší afinitu ke kyslíku)
14. Co je strukturním základem kooperativního chování Hb?
 - Hb má kvartérní strukturu tetrameru, čili se skládá ze 4 podjednotek
15. Jaký je princip krátkodobé adaptace na vysokou nadmořskou výšku
 - zvýšená koncentrace 2,3-bisfosfoglycerové kyseliny (kofaktor Hb), která zvyšuje afinitu kyslíku k vazebným místům Hb.

# 03 Proteiny - enzymologie
[PDF přednášky](https://dl2.cuni.cz/pluginfile.php/327341/mod_resource/content/8/Bzaklady03-2020%20animace.pdf)
1. Které čtyři vlastnosti enzymů jsou zejména důležité pro živé organismy a proč?
 - katalyzují reakce:
   - rychlost až 10^20 rcí/s
   - umožňují reakce i v "mírných" podmínkách
   - umožňují jen některé reakce (nevznikají nechtěné produkty)
   - jsou regulovatelné (např. alosterie, kovalentní modifikace, regulační proteiny, proteolýza, změna vlastní konformace a lokalizace (enzymu?), změnou koncentrace enzymu a zastoupením isoenzymů)
2. Jakými různými způsoby může buňka regulovat enzymatické reakce svého metabolismu?
 - viz předchozí otázka, poslední podbod...
3. V roce 1926 J.B. Sumner dokázal, že protein je nositelem katalytických schopností (https://en.wikipedia.org/wiki/James_B._Sumner). Za tento svůj objev posléze obdržel Nobelovu cenu. Je proteinová struktura samotná vesměs zodpovědná za katalytické schopnosti enzymů? Jsou proteiny jedinými katalyzátory v přírodě? Znáte nějaký příklad procesu v živých systémech, který není katalyzován proteinovou strukturou?
 - struktura proteinu je určující pro jeho funkci. Kromě samotného polypeptidového vlákna s aminokyselinami různých vlastností jsou pro funkci proteinu důležité i ligandy a koenzymy, a různé modifikace
 - proteiny určitě nejsou jedinými katalyzátory. Ze složitějších látek jsou katalyzátory kromě enzymů i ribozymy (RNA)
 - myslím, že mezi katalyzátory se mohou počítat i kovové ionty, které mohou dělat přechodnou vazbu s reagující molekulou a umožní tak reakci. To se ale děje většinou přímo v enzymech...
 - a tak určitě... Třeba hexokináza dává vznik glukóza 6-fosfátu během glykolýzy. Katalyzuje (byť exergonickou) reakci ATP s glukózou na ADP a glukóza 6-fosfátu.

4. Jak byste popsali jednotlivé základní mechanismy katalýzy - 1...6 ?
 - (slide 8 a další v prezentaci)
 - acidobazická katalýza
 - kovalentní katalýza
 - katalýza kovovými ionty
 - elektrostatická katalýza
 - katalýza proximitním a orientačním efektem
 - katalýza stabilizací přechodného stavu

5. Jak měříme tzv. počáteční rychlost reakce, která figuruje v rovnici Michaelise a Mentenové?
 - rovnice -> v_0 = v_max[S]/[S]+Km
 - není to řečené přímo, ale protože se nad určitou koncentraci substrátu nemění rychlost reakce, je možné tuto "maximální" rychlost změřit ve chvíli, kdy je koncentrace substrátu mírně vyšší, než je potřeba k maximální rychlosti. Ale proč je potřeba počáteční rychlost resp. proč ne maximální? Není to nějaká záměna? A jak se to dělá ve skutečnosti? ... nevím

6. Jaká je směrnice přímky ve výnosu dle Lineweavera-Burka ?
 - tato rovnice je vlastně jen reciproká úprava (celé se to dá na -1) rovnice Michaelise a Mentenové. Směrnice je v ní daná K_M/V_max

7. Jakými parametry lze postihnout katalytickou účinnost enzymu?
 - katalytická účinnost je definovaná jako k_cat = V_max / [E]_T
 - > počet cyklů katalýzy za jednotku času za podmínky, kdy [E] je limitujcím faktorem (enzym je saturován substrátem S)

8. V čem je podstata rozdílu mezi statickými uspořádanými strukturami (=např. elektronickým přístrojem) a dynamickými uspořádanými strukturami – živými organismy?
 - eh (vracím se v čase... prvouka, 3. třída... autíčko není živé, protože... :D). Živé struktury jsou vlastně "otevřené systémy v ustáleném stavu", mj. mají schopnost seberozvoje, sebeopravy a rozmnožování (autíčko není živé, protože se nerozmnožuje :D)

9. Jaké jsou příčiny „vysokoenergetického“ charakteru ATP?
 - fosfátové skupiny kompetují o π elektrony -O- fosfoanhydridových vazeb, negativní náboje na fosfátových skupinách se odpuzují, samostatné fosfoanhydridy mají nižší solvatační energii, než hydrolytické produkty.

10. Proč je právě ATP „základním energetickým platidlem“ ? Bylo by možno jej nahradit jiným NTP?
 - ATP není jediná možnost. Existuje např. GTP a další. ATP je ale nejpoužívanější ze všech NTP. Jestli by to bylo i výhodné v prezentaci není.

# 04 Sacharidy
Můj comment: Jan Brábek, který má 04, 05, 10 a 11-tou přednášku nemá moc informací v prezentacích, ale hodně na videích.
U sacharidů jsme se na střední učili označovat místa v sacharidech pomocí číslování uhlíků, což tady dost využívám... Zapisuju to jako např. na 4C se stalo, čímž myslím, že na 4. uhlíku se stalo XY :D

> Milí přátelé,
> zasílám vám otázky pro přípravu na přespříští týden - poslechněte si prezentace k tématu Monosacharidy a glykolýza a připravte si odpovědi na uvedené otázky:

1. Podle čeho a jak dělíme monosacharidy?
 - Dělí se na aldózy (=O na začátku řetězce) a ketózy (=O na 2. uhlíku řetězce)
 - dále podle počtu uhlíků (triózy = 3C, pentózy = 5C, hexózy = 6C ...)
 - a podle optické aktivity.
2. Jak vznikají cyklické formy monosacharidů a jak jsou pojmenovávány?
 - cyklizace = přeměna na lineárních sacharidů na cyklické formy
 - názvosloví: pyranóza = šestiúhelník, furanóza = pětiúhelník,
 - alpha/beta - OH skupina na 1/2 uhlíku (viz aldóza/ketóza) směřuje dolů (alpha verze) nebo nahoru (beta verze)
 - vznikají "přepojením" vazby, kdy kyslík (aldózy na 1C, ketózy na 2C) přepojí svou vazbu na x-tý uhlík, tak, aby vznikl zmíněný pěti/šestiúhelník
3. Co je mutarotace?
 - změna poměru alpha a beta varianty cyklického sacharidu v roztoku (změna optické aktivity (kolečko se rozbalí a zase sbalí) [Hezky vysvětlené v přednášce](https://youtu.be/YEyArwRUS94?t=828)
4. Jaké sacharidy vznikají oxidací a redukcí základních monosacharidů?
 - oxidace aldóz
   - -> COOH místo -CHO na prvním uhlíku = aldonové kyseliny
   - -> COOH místo -CH2OH na posledním uhlíku = alduronové kyseliny
 - redukce aldóz
   - -> OH na prvním uhlíku = alditoly
 - laktony - vznikají "intramolekulární esterifikací" cyklických molekul
   - důležitý lakton -> kyselina L-askorbová = vitamín C 
5. Jaké znáte významné deoxy-deriváty monosacharidů?
 - deoxyribóza - důležitá složka DNA
 - fukóza, ramnóza (zásobní cukr rostlin a součást buněčné stěny nějakých bakterií)
6. Jaké znáte významné amino-deriváty monosacharidů?
 - N-acetyl-beta-D-glukosamin = stavební složka chitinu
 - N-acetyl Muramová kyselina = stavební složka peptidoglykanu z buněčné stěny bakterií
 - N-acetyl neuraminová kyselina = má funkci při změnách náboje na membránách, je důležitá u neuronů
7. Jaké je zařazení glykolýzy do energetického metabolismu, jaké jsou fáze glykolýzy?
 - probíhá v cytozolu buněk, v kompartmentech, které se jmenují glykolytické metabolony
 - z glukózy je výtěžek 2 ATP, 2 NADH+H+ a 2 pyruváty
 - hezký souhrn na  [wiki](https://cs.wikipedia.org/wiki/Glykol%C3%BDza#/media/Soubor:Glycolyse.png) a přehledná [česká wikistránka](https://cs.wikipedia.org/wiki/Glykolýza)
8. Jak probíhá hexokinázová reakce, jaký má význam pro regulaci metabolismu glukózy?
 - hexokináza fosforyluje glukózu vstupující do glykolýzy na 6C (přilípne mu fosfát H3PO4) za spotřeby 1ATP
9. Jak probíhá glukózafosfátizomerázová reakce? Probíhá stereospecificky?
 - tak zaprvé, stereospecificita znamená, že se nezmění optické vlastnosti látky ([Eh, stejně radši odkážu na Wiki :D](https://en.wikipedia.org/wiki/Stereospecificity))
 - glukózafosfátizomerázová reakce je druhá u glykolýzy. Mění glukózu-6 fosfát na fruktózu 6-fosfát
 - na to musí přepojit vazbu kyslíku za 1C na 2C (pyranóza jde na furanózu)
 - nezmění se optické vlastnosti látek, takže reakce **je stereospecifická**
10. Jak probíhá fosfofruktokinázová reakce? Jaký je její význam pro regulaci glykolýzy?
 - na fruktózu 6-fosfát se připojí další H3PO4 za spotřeby ATP a za vzniku fruktóza 1-6 bisfosfátu
 - rozhoduje o tom, že fruktóza skutečně půjde do glykolýzy (glykolýza v užším slova smyslu je )
11. Jak probíhá aldolázová reakce?
 - je potřeba rozštěpit fruktózu 1-6 bisfosfát (aldózu) na 2 3C molekuly
 - destabilizace molekuly pomocí O- na fenolové skupině
 - štěpí se na glyceronfosfát a glyceraldehyd-3-fosfát
 - glyceraldehyd-3-fosfát má na 1C =O, na 2C -OH a na 3C -OPO3
12. Jak probíhá triózafosfátizomerázová reakce? Co je dokonalý enzym? Co je alpha-beta barrel?
 - triózafosfátizomeráza usměrňuje reakci přeměny glyceronfosfátu na glyceraldehyd 3-fosfát
 - dokonalý enzym dokáže zpracovávat substrát stejně rychle, jako k němu přichází (Zdroj: [UPOL](http://pfyziolklin.upol.cz/?p=11674))
 - alpha-beta barel je struktura proteinu složená z alpha helixů a beta listů, která umožňuje uvnitř něco uzavřít. Ideální pro vytvoření aktivního místa
13. Jak probíhá glyceraldehydfosfátdehydrogenázová reakce? Kde je reoxidováno NADH?
 - oxiduje se glyceraldehyd-3 fosfát, protože se na něj předtím naváže koenzym, takže mu přebývá jeden vodík a ten se přidá a dá vznik NADH+H+
14. Jak probíhá fosfoglycerátkinázová reakce? Co je substrátová fosforylace?
 - na glyceraldehyd 3-fosfát se přidá další fosfátová skupina (jen to odštěpené H3PO4) a vznikne 1-3 bisfosfoglycerát
 - protože je v té vazbě hodně energie, může se 1-3 bisfosfoglycerátem nabít ADP na ATP (a tohle přímé nabití se jmenuje **substrátová fosforylace**), protože ATP vznikne fosforylací ze substrátu
15. Jak probíhá fosfoglycerátmutázová reakce? Co je „ping-pongový mechanismus“?
 - fosfát je přenesený z 3C na 2C. Tím vzniká 2-fosfoglycerát
 - reakce má 4 mezifáze, které mezi sebou různě přecházejí, ale jen z jedné může vzniknout produkt. To přecházení se jmenuje "ping-pongový efekt"
16. Jak probíhá enolázová reakce? Jaký typ makroergní sloučeniny při této reakci vzniká?
 - enoláza odstraňuje molekulu H2O z 2-fosfoglycerátu a vzniká 2-fosfoenolpyruvát
17. Jak probíhá pyruvátkinázová reakce? Jaký význam může mít její inhibice?
 - pyruvátkináza přenese fosfát na ATP z 2-fosfoenolpyruvátu a vzniká tím čistý pyruvát, který může dál pokračovat buď do Krebsova cyklu, nebo za anoxických podmínek může jít do alkoholového nebo mléčného kvašení
18. Co je hlavním důvodem pro fermentaci?
 - fermentace umožňuje nabití NADH+ pro plynulý běh glykolýzy
 - vzniká tím laktát, který způsobuje bolest svalů - v případech vysoké zátěže je ale tento proces energeticky nutný, aby se nabilo rychle co nejvíc ATP i bez kyslíku
19. Jak probíhá laktátová fermentace? Jaký význam může mít reakce v „opačném“ směru?
 - laktát dehydrogenáza oxiduje pyruvát za vzniku laktátu a nabití NADH+
 - v opačném směru reakce probíhá, když se organismus dostane do stavu nižší zátěže a dostatku kyslíku
20. Jak probíhá alkoholová fermentace? Jak souvisí s metanolovou aférou?
 - alkoholová fermentace má 2 fáze - pyruvátdekarboxyláza z pyruvátu odštěpí CO2 a následně vzniklý acetaldehyd je redukován na ethanol
 - v prezentaci není zmíněné, jak může vzniknout v této fázi methanol na molekulární úrovni, ale methanol je prostě jednouhlíkatý alkohol (CH3OH), zatímco ethanol je dvouuhlíkatý (CH3-CH2-OH)
 - ethanol je jen mírně toxický :D
 - ale methanol se mění v metabolismu na formaldehyd a kyselinu mravenčí a to fakt nechceš :(
21. Jak je glykolýza regulována? Co jsou substrátové cykly?
 - hexokináza a fosfofruktokináza jsou ty hlavní regulační místa
 - hexokináza nemá aktivátory, ale je inhibována vyšší koncentrací glukóza-6-fosfátem
 - fosfofruktokináza je inhibována vysokou koncentrací ATP a aktivována ADP, cAMP, AMP a dalšími "vybitými" energetickými látkami a vysokou koncentrací fruktóza 1-6 bisfosfátu
 - substrátové cykly jsou další způsob, jak regulovat glykolýzu
   - všechny reakce jsou v glykolýze vratné, tím, jak nastavíme poměr rychlostí dopředu a dozadu se ovlivňuje rychlost glykolýzy jako takové
   - stojí i nějakou energii, může ale tím pádem sloužit k netřesové endogenezi (např. hmyz díky tomu může létat) [vysvětlené tady](https://youtu.be/YEyArwRUS94?t=4112)

> S pozdravem,
> Jan Brábek

# 05 Glykogen
[prezentace](https://dl2.cuni.cz/pluginfile.php/198122/mod_resource/content/2/BZ10a_Polysacharidy%20a%20glykogen.pdf)
[online přednáška](https://youtu.be/faV6qNY3_sg)

> Milí přátelé,
> zasílám vám otázky pro přípravu na příští týden - poslechněte si prezentace k tématu Polysacharidy a glykogen a připravte si odpovědi na uvedené otázky:

1. Jak vznikají glykosidy, jaké znáte příklady skupin glykosidů?
 - [Wiki](https://cs.wikipedia.org/wiki/Glykosidy)
 - Glykosidy jsou deriváty sacharidů, které vznikají reakcí na hydroxylové skupině sacharidu s jiným cukerným nebo necukerným radikálem. Vznikají odštěpením vody u dvou -OH skupin. Tzn. dvě molekuly jsou výsledně propojené přes kyslík (-O-).
 - Organické glykosidy (mluví se o nich v prezentaci) - flavinové, saponinové a kardiogenní glykosidy (na Wiki je pojmenovávájí trochu jinak).
2. Jaké znáte významné disacharidy, které z nich jsou redukující?
 - cukróza (nebo také sacharóza) (D-glukóza a D-ribóza spojené 1-4 glykosid. vazbou),
 - laktóza (beta-D-galaktóza a beta-D-glukóza spojené 1-4 glykosid. vazbou), v mléce :)
 - celobioza (2 **beta**-D-glukózy spojené 1-4 glykosid. vazbou), prekurzor celulózy
 - maltóza (2 D-glukózy spojené 1-4 glykosid. vazbou), vzniká štěpením škrobu (amylázou) a z glykogenu
 - izomaltóza (jako maltóza, jen 1-6 glykosid. vazba)
 - z výše zmíněných je neredukující pouze cukróza, protože ne 1C u fruktózy nemá volnou -OH skupinu (jde o to, jestli ta "pravá" podjednotka disacharidu má na 1C volnou -OH skupinu, nebo ne), ostatní jsou redukující (a díky tomu mohou vytvářet polysacharidy, řetězit se, viz dále)
 - *trehalóza* - funfact disacharid, propojené 2 D-glukózy 1-1 glykosid. vazbou, chrání organizmy před vysoušením a mrazem (želvušky), někteří členovci ji mohou mít místo glukózy jako přenašeč energie v hemolymfě, používá se při léčbě neurodegenerativních onemocnění
3. Jaké znáte významné homopolysacharidy, jaká je jejich struktura a funkce?
 - celulóza (opakující se podjednotky celobiózy, pořád 1-4 glykosid. vazba),
 - chitin (prakticky stejný jako celulóza, jen na 2C mají podjednotky -acetylamin (NH(OCCH3)), takže podjednotky se jmenují N-acetylglukosamin
 - škrob (amylóza + amylopektin) (amylopektin se od amylózy liší tím, že jednou za cca 20 podjednotek se vytvoří propojení u 6C a základní řetězec se rozvětví do dalšího řetězce)
4. Jaké funkce mají glykosaminoglykany, jaké znáte důležité zástupce?
 - jsou důležitou složkou mezibuněčné hmoty, dobře váží vodu a ionty, jejich fyzikální vlastnosti je předurčují pro tvorbu chrupavek a dalších tkání podobnécho charakteru
 - skládají se z alduronové kyseliny a glukosaminu + sirné skupiny
 - nejčastější je **hyaluronát** - prekurzor pro ty ostatní
 - chondritin-4 sulfát a chondritin-6 sulfát - v chrupavkách
 - dermatan sulfát v pokožce,
 - keratan sulfát v rohovitých strukturách,
 - ***heparin*** je hodně odlišný, protože má velmi velké množství záporných nábojů a omezuje srážlivost krve interakcí s antitrombinem a vyskytuje se v granulích bílých krvinek
5. Jak vypadá kartáčová struktura proteoglykanu?
 - jako kartáč :D
 - často slouží jako výplň v mezibuněčných prostorech
 - na sacharidové (kys. hyaluronová) vlákno jsou navázané proteiny, ze kterých mohou být navázané další vlákna sacharidů
6. Na jakých sekvencích dochází k N-glykosylaci, jaké jsou její funkce?
 - proteiny mohou mít navázané mono- i oligo- sacharidy
 - často komplexní struktury sacharidů na proteinech
 - v mnoha případech se ještě neví, co je funkce sacharidů, ale může mít strukturní funkci (mění strukturu glykoproteinu), může mít stabilizační funkci nebo i třeba signální funkci
7. Na jakých aminokyselinách dochází k O-glykosylaci, jaké jsou její funkce?
 - serin, threonin (, tyrosin)
 - O-glykosilované glykoproteiny jsou součástí ochranných struktur na povrchu buněk
8. Jaká je struktura a funkce peptidoglykanu?
 - složka buněčné stěny gram pozitivních i gram negativních bakterií
 - vlákna jsou tvořena (střídavě) N-acetylglukosaminem a kyselinou muramovou, které jsou propojeny 5-glycinovým řetízkem a peptidovým řetězcem, který často obsahuje *D-aminokyseliny* -> rezistence proti savčím proteázám
9. Jak vypadá struktura glykogenu?
 - podobná jako škrob, 1-4 glykosydické vazby, někdy přidaný řetězec s 1-6 vazbou, (*opravte mě kdyžtak, ale zdá se, že oproti amylopektinu se liší jen častějším rozvětvováním díky 1-6 glykosydickým vazbám*)
 - optimalizované pro rychlé štěpení a uvolňování energie
 - oproti tuku má výhody: 1) rychlé získávání energie, 2) může probíhat za anaerobních podmínek, 3) odbourává se na prekurzory glukózy, čímž může sloužit jako její zásoba
 - skladuje se v glykogenových granulích, oproti čisté glukóze má výhodu, že nezvyšuje tolik osmotický tlak
10. Jaké důležité domény obsahuje glykogenfosforyláza? Jak probíhá glykogenfosforylázová reakce?
 - glykogenfosforyláza odbourává glykogen s využitím kyseliny fosforečné
 - má kofaktor - derivát vitamínu B6 (také jako PLP) - pyridoxal-5fosfát
 - má dvě podjednotky, má vazebné místo pro pyridoxal-5fosfát a v aktivním místě může navázat i 5 glukózových podjednotek
 - štěpí vazbu mezi dvěma glukózovými podjednotkami s využitím kyseliny fosforečné
 - výstupem je glukóza 1-fosfát
11. Jak probíhá fosfoglukomutázová reakce? Které reakci z glykolýzy se podobá?
 - přenáší fosfát z glukóza 1-fosfát na glukózu 6-fosfát
 - reakce probíhá přes meziprodukt - glukózu 1-6 fosfát
 - záleží čím by se měla reakce přesně podobat, ale pokud jde o produkt, podobá se 1. reakci z glykolýzy, kdy se alpha-D-glukóza mění na alpha-D-glukózu 6-fosfát, za katalýzy glukokinázou
12. Jaké aktivity má linearizační enzym?
 - odštěpuje postranní řetězce glykogenu až na jednu glukózu a přenese na konec hlavního řetězce glykogenu - 1-4 glykosilázová aktivita
 - hydrolyzace postranního zbytku na hlavním řetězci - 1-6 glykosidázová aktivita
13. Jaký enzym syntetizuje UDP-glukózu a z jakých prekurzorů?
 - UDP-glukózadifosforyláza
 - z UTP (jako ATP, jen je tam uracyl místo adeninu) a glukózy 1-fosfátu
 - z UTP odštěpí 2P -> vznik UMP
 - UMP přidá ke glukóze 1-fosfátu na fosfátovou skupinu -> vznik UDP-glukóza
14. Jak probíhá glykogensyntázová reakce?
 - "inicializace" řetězce začíná na -OH skupině Tyr u proteinu glykogeninu, kam se nejprve přidá několik glukózových zbytků, pak začne "řetězící" fáze syntézy
 - glykogensyntáza samotná pak řetězí za sebou glukózy s alpha 1-4 glykosidickou vazbou
15. Jaké aktivity má větvící enzym?
 - větvící enzym odštěpuje volné delší konce glykogenového řetězce a přidává je na C6 glukóz v řetězci
16. Jakými způsoby je přímo regulována glykogenfosforyláza?
 - glykogenfosforyláza slouží k rozkladu glykogenu, viz 10. otázka
 - má místo pro alosterickou regulaci
 - fosforyláza má 2 formy - "a" a "b" - rozdíl je fosforylace na serinovém zbytku
 - fosforyláza b je citlivá na alosterickou regulaci
   - pokud je hodně ATP nebo Glukóz 6-fosfátu, fosforyláza b je inaktivní
 - fosforyláza a je necitlivá na regulaci
   - reguluje ji pouze vysoké množství glukózy
 - mezi *a* a *b* formou přechází fosforyláza pomocí fosforyláza-kinázou (b->a) a fosforyláza-fosfatázou (a->b)
17. Jak se liší závislost aktivity hexokinázy a glukokinázy na koncentraci glukózy?
 - hexokináza je enzym zajišťující první krok glykolýzy - G6 na G6P
 - glukokináza slouží v procesu vzniku glykogenu v játrech a ve svalových tkáních
 - hexokináza má velmi rychlý nárůst, ale pak při vysokých koncentracích je inhibována
 - glukokináza naproti tomu má pozvolný nárůst aktivity, není glukózou inhibována
18. Co to je Coriho cyklus? Po kom je pojmenován?
 - v Coriho cyklu figurují játra, svalová tkáň a krevní řečiště jako přenašeč látek mezi nimi
 - ve svalech za anaerobních podmínek vzniká laktát
 - ten je přenesen do jater, kde je v procesu glukoneogeneze přeměněn na glukózu
 - ta opět krví dojde do svalové tkáně, kde je využita k výrobě glykogenu, nebo rovnou spotřebována při svalové činnosti (kdy potenciálně může opět vzniknout laktát)
 - manželé Coriovi vystudovali medicínu v Praze (v roce 1920) a získali (už v USA) Nobelovu cenu za svojí práci
19. Jak je metabolismus glykogenu regulován pomocí glukagonu a adrenalínu?
 - regulace probíhá přímo přes druhé posly (typicky cAMP)
 - adrenalin - stresová reakce
 - glukagon - nízká hladina glukózy v krvi
 - u obou se získává glukóza z jaterního glykogenu (glykogen fosforylázová aktivita)
20. Jak je metabolismus glykogenu regulován pomocí inzulínu?
 - když je glukózy nadbytek, buňky přijímají více glukózy
21. Co je inzulínová rezistence?
 - inzulinová signalizace je přetěžována např. dlouhodobě zvýšenou hladinou glukózy v krvi
 - normální hladiny inzulinu vyvolávají malou odpověď organizmu (často v těhotenství, pubertě, při obezitě a při cukrovce 2. typu)
 - může způsobovat zdánlivě nečekané problémy (vznik nádorů)
22. Co jsou glykogenózy?
 - choroby spojené s poruchou metabolismu glykogenu
 - Mc Ardle's disease -> pomalý nástup vzniku glukózy z glykogenu - disfunkční svalová glykogenfosforyláza

# 06 Cyklus kyseliny citronové
[prezentace](https://dl2.cuni.cz/pluginfile.php/333456/mod_resource/content/2/KC-z20.pdf)
[přednáška](https://youtu.be/WkyhKlNwAA0)

>Milí přátelé,
Přikládám otázky pro přípravu na přednášku v příštím týdnu – 15. 11. 2021. Otázky se týkají tématu Z06 – Cyklus kyseliny citronové. Poslechněte si prezentace k tomuto tématu a připravte si odpovědi na následující otázky:

1. Proč se buněčný katabolismus označuje za konvergentní?
 - katabolismus ... degradace složitějších sloučenin na jednodušší
 - konvergentní ... směřující k něčemu
 - katabolismus v buňce směřuje k získání Acetyl-CoA
2. Jaké jsou jednotlivé úrovně odbourávání molekul sloužících jako zdroj energie pro buňku?
 - substrátová fosforylace - ATP
 - uvolňování elektronů - NADH, FADH2
 - redukce redukovaných koenzymů NADH a FADH2 - elektrotransportní řetězec -> O na H2O, ATP syntáza (oxidační fosforylace)
3. Které enzymy tvoří komplex pyruvát dehydrogenázy (PDH)?
 - jsou to 3 druhy enzymů (E1, E2 a E3)
 - E1 ... pyruvát dehydrogenáza
 - E2 ... dyhydrolipyl transacetyláza
 - E3 ... dyhydrolipyl transkarboxyláza
 - u e. coli je 24x E1, 12x E2 a 24x E3
4. Které koenzymy jsou nezbytné pro funkci PDH?
 - lipoamid
 - thiamin difosfát
 - NAD+
 - FAD+
 - koenzym A
5. Jakou strukturu má pyruvát dehydrogenázový komplex?
 - Pravidelnou a vrstevnatou - E1 jsou uvnitř, E2 a E3 na povrchu
6. Jaký enzymatický mechanismus katalyzuje oxidační dekarboxylaci pyruvátu v PDH?
 - E1 ... dekarboxylace (- CO2, napojení na TPP (thyamin difosfát)
 - E2 ... odpojení z TPP, navázání na lypoyllyzin - dehydrogenace přepojení na acetyl koenzym A - odchod Acetyl-CoA z komplexu
 - E3 ... lypoyllyzin má stále v E2 dva nevyužité elektrony - předání na FAD (vznik FADH2, které jde k elektortransportnímu řetězci)
7. Jak je regulována aktivita PDH?
 - fosforylace E1 - pyruvát dehydrogenázy (pyruvát dehydrogenáza kináza deaktivuje, pyruvát dehydrogenáza fosforyláza aktivuje)
 - pyruvát dehydrogenáza kináza je
   - aktivována NADH a acetylem-CoA
   - inhibována ADP a pyruvátem
 - pyruvát dehydrogenáza fosforyláza
   - aktivátory Ca2+ a Mg2+ (ionty mají často signalizační funkci)
8. Jaký je význam jednotlivých reakcí cyklu kyseliny citronové?
 - [přednáška v čase 49:34](https://youtu.be/WkyhKlNwAA0?t=2974)
![citrátový cyklus jako obrázek](https://www.sigmaaldrich.com/deepweb/assets/sigmaaldrich/marketing/global/images/technical-documents/articles/research-and-disease-areas/metabolism-research/TCA-krebs-cycle1/TCA-krebs-cycle1.png)

    a) citrát syntáza
    - acetyl-CoA se spojí s oxaloacetátem za spotřeby vody a odštěpením CO2
    - vznik citrátu

    b) akonitáza
    - z citrátu na cis-akonitát
    - z cis-akonitátu na isocitrát, který má oproti citrátu přesunutou skupinu -OH z 2. uhlíku na 3.
    - ve výše zmíněných reakcích je odštěpena a přidána molekula vody

    c) isocitrát dehydrogenáza
    - dekarboxylace na alpha-ketoglutarát (odštěpené CO2 a nabitý jeden NADH+H+)

    d) a-ketoglutarát dehydrogenáza
    - opět dekarboxylace a nabití NADH+H+
    - přidaný -CoA
    - vznik Succinyl-CoA

    e) sukcinyl CoA syntetáza
    - odštěpený CoA
    - substrátová fosforylace GTP
    - -> Sukcinát

    f) sukcinát dehydrogenáza
    - nabití FADH2
    - vznik dvojné vazby na uhlících -> Fumarát

    g) fumaráza
    - hydratace
    - přidání -OH skupiny
    - nasycení dvojné vazby

    h) malát dehydrogenáza
    - nabije NADH+H+
    - vznik oxaloacetátu

9. Jak je cyklus regulován?
 - citrátsynthasa,
 - isocitrátdehydrogenasa a
 - α-ketoglutarátdehydrogenásový komplex
 - jsou inhibovány vysokou koncentrací ATP
 - některé enzymy jsou inhibovány redukovanými koenzymy (např. při nedostatku kyslíku)
10. Co jsou to anaplerotické reakce a které znáte?
 - doplňující reakce, umožňují doplnit meziprodukty Krebsova cyklu
 - pyruvát -> malát
 - fosfoenolpyruvát -> oxaloacetát
11. Co je to glyoxalátový cyklus a jaký je jeho význam?
 - odvozený od Krebsova cyklu, mají ho některé rostliny
 - vznik glyoxalátu a succinátu pro vznik cukrů

>Těším se na shledanou,
Martin Kalous

# 07 Oxidační fosforylace
[prezentace](https://dl2.cuni.cz/pluginfile.php/198124/mod_resource/content/2/oxfos-z20.pdf)
[přednáška](https://www.youtube.com/watch?v=ioHTdGxBoMo)

> Milí přátelé,
> Přikládám otázky pro přípravu na přednášku v příštím týdnu – 22. 11. 2021. Otázky se týkají tématu Z07 – Oxidační fosforylace. Poslechněte si prezentace k tomuto tématu a připravte si odpovědi na následující otázky:

1. Kde je lokalizován systém oxidační fosforylace (OXFOS)? Rozdíl mezi pro- a eukaryoty.
    -  eukaryota mají celý systém na vnitřní membráně mitochondrií
    -  prokaryota jej mají na plazmatické membráně

2. Jaká je struktura mitochondrií a jaké jsou vlastnosti nezbytné pro fungování OXFOS
    - vnější membrána (volně propustná pro menší molekuly)
    - vnitřní membrána (neprostupná) - obsahuje ADP-ATP transportázy, ATP syntázy a různé membránové přenašeče, elektronové přenašeče 1-4
    - krysty (vchlípení vnitřní membrány dovnitř mitochondrie)
    - matrix (vnitromembránový a mezimembránový) - obsahuje pyruvát dehydrogenázový komplex, enzymy citrátového cyklu, enzymy pro beta-oxidaci mastných kyselin, enzymy pro oxidaci aminokyselin, různé metabolické intermediáty (meziprodukty), ATP, ADP, Ca2+, Na+ etc.
    - ribozomy - mitochondrie si menší část proteinu vyrábí sama a větší část je do ní transportována

3. Ze kterých komplexů se skládá elektrontransportní řetězec?
   - I. NADH-CoQ reduktáza: redukuje NADH+H+ a nabíjí CoQ
   - II. Succinát-CoQ reduktáza: oxiduje Succinát na Fumarát a nabíjí (redukuje) CoQ
   - III. CoQH2 cytochrom c oxido-reduktáza: redukuje CoQ
   - IV. Cytochrom c oxidáza

4. Proč v tomto řetězci putují elektrony tak, jak putují?
 - protože musí využít co nejvíc svoji energii
 - přenašeče zároveň pumpují protony z jedné strany membrány na druhou
 - - v gradientu protonů je "uchována" energie z těchto přenosů
5. Co jsou to redoxní pumpy a jak a co pumpují?
 - [souhrnný článek o proteinových pumpách na wiki](https://cs.wikipedia.org/wiki/Protonov%C3%A1_pumpa)
 - pumpují protony (H+ ionty),
 - využívají k tomu elektronový redox potenciál

6. Jaké typy redoxních center naleznete v elektrontransportním řetězci?

7. Jaká je struktura a funkce jednotlivých komplexů elektrontransportního řetězce?

 a) Komplex I
  - obsahuje více Fe-s center, které přenášejí elektrony z NADH+H+
  - má 2 podjednotky
  - ve 2. podjednotce se přenese elektron na CoQ a přepumpují 4H+ do mezimembránové matrix

 b) Komplex II
  - jediný ne-transmembránový komplex elektrotransportního řetězce
  - má jen jeden segment
  - přijme succinát, dehydrogenuje ho na fumarát
  - nabije CoQ

 c) Komplex III
  - poměrně složitý, vícepodjednotkový komplex
  - obsahuje hemy B, přenáší elektrony na cyt-c
  - probíhá na něm "Q" cyklus, který umožní vypustit 2x 2H+ na jeden svůj běh

 d) Komplex IV
  - má 4 podjednotky
  - získá 4 e- ze 4Cyt-c
  - transportovány přes 4 redoxní centra a 2 hemové skupiny -> 4 H+ na 4 Cyt-c
  - výsledek -> 10H+ z 1 NADH+H+, z 1 FADH2 jen 6H+

8. Jaký je podíl mtDNA na kódování podjednotek komplexů OXFOS?
 - "OXFOS" znamená "oxidativní fosforylace", v otázce jde tedy o proteiny kompexů I-V (vč. FoF1 ATP syntázy)
 - [prezentace, v místě, kde se to vysvětluje](https://youtu.be/ioHTdGxBoMo?t=3594)
 - 13/83 podjednotek je kódováno v mtDNA 

9.  V čem spočívá chemiosmotický princip mitochondriální syntézy ATP?
 - vysoká koncentrace protonů H+ v mezimembránové matrix vytváří velký chemiosmotický gradient
 - to je využito k rozběhnutí FoF1 ATP syntézy, která propouští proteiny zpět na vnitřní stranu membrány a syntetizuje ATP

10. Jaká je základní struktura FoF1 ATP syntázy?
 - má alpha až epsilon podjednotky, které vytvářejí dohromady strukturu jako lízátko na špejli

11. Jaký je mechanismus syntézy ATP tímto komplexem (rotační model)?
 - ve třech krocích je navázáno ADP, spojeno s fosfátem za vzniku ATP a odchází
 - to je dáno díky rotaci alpha, beta a gama podjednotek (v Fo části syntázy)
 - postranní kanál - podjednotka _a_
 - postranní stonek - podjednotka _b_
 - rotor propojený s gama částí - _c_
 - _a_+_b_ + alpha,beta hexamer -> stator

12. Jaké jsou možné způsoby reoxidace glykolytického NADH v mitochondriích?
 - za redukce malátu na oxaloacetát (malát-aspartátový člunek)

13. Jaký je celkový energetický zisk (v molekulách ATP) při oxidaci jedené molekulu glukózy?
 - 1 glukóza = 2ATP substrátovou fosforylací, 2GTP (stejná energie jako ATP), 24e-
   - 10 NADH, 2 FADH2
   - transport 2e- přes I-IV vede k translokaci 10H+
   - transport 2e- přes II-IV vede k translokaci 6H+
   - -> 
   - syntéza a export 1 ATP stojí 3+1 H+
   - 1 NADH -> 2.5 ATP
   - 1 FADH2 -> 1.5 ATP
   - celkem 32 ATP pro malát - aspartátové kyvadlo
   - nebo 32 - 2 = 30 ATP pro glycerolfosfátové kyvadlo

>Těším se opět na shledanou,
>Martin Kalous

# 08 Fotosyntéza a 09 Alternativní dráhy sacharidů

Pozn.: 1.-8. otázka je z #08 a 9.-14 otázka je z #09

[prezentace - fotosyntéza](https://dl2.cuni.cz/pluginfile.php/198125/mod_resource/content/1/Fotosyn-z19.pdf)
[prezentace - alternativní dráhy sacharidů](https://dl2.cuni.cz/pluginfile.php/198126/mod_resource/content/1/OtherSach-z19.pdf)
[přednáška - spojená i s dalším tématem](https://youtu.be/bDs5On5ux20)


> Milí přátelé,

> Přikládám otázky pro přípravu na přednášku v příštím týdnu – 29. 11. 2021. Otázky se týkají tématu Z08/09 – Fotosyntéza/Alternativní dráhy sacharidů. Poslechněte si prezentace k tomuto tématu a připravte si odpovědi na následující otázky:

1. Jaká je struktura chloroplastů, kolik kompartmentů zde rozlišujeme?
 - podobně jako mitochondrie má i chloroplast vnitřní a vnější membránu,
 - stroma ... ve vnitřním prostoru chloroplastu je ne "matrix" jako u mitochondrie, ale "stroma",
 - thylakoidy ... struktury uvnitř chloroplastu, kde probíhá fotosyntéza
 - grana ... thylakoidy, vytvářející "palačinkové" struktury
 - granula škrobu ... škrob, uložený přímo v chloroplastu
 - dále chloroplast obsahuje vlastní DNA a ribozomy

2. Jaký je rozsah vlnové délky světla využitelného pro fotosyntézu?
 - chlorofyl *a* a *b* pokrývají téměř celé spektrum viditelného světla
 - 380-700nm (viditelné světlo má ~380-750nm)

3. Jaké fotosyntetické pigmenty znáte, které jsou základní a které pomocné?
 - chlorofyl *a* a chlorofyl *b* jsou základní pigmenty (dále např. phycoerythrin je v červených řasách)
 - dále je využíván např. ß-karoten

4. Jaká jsou absorpční maxima jednotlivých pigmentů a proč jsou rostliny většinou zelené?
 - chlorofyly *a*, *b* i ß-karoten mají svá maxima u nižších vlnových délek - 400-500 nm
 - chlorofyly *a*, *b* pak zachycují s menší účinností světlo mezi 500-600 nm
 - poté zase nabývají vyšší účinnosti při 600-700 nm

 - rostliny jsou zelené, protože zelené světlo je právě mezi 500-560nm, kde chlorofyly zachytávají jen menší množství světla

5. Jaké typy fotosystémů známe u prokaryot a jak jsou uspořádány u eukaryot?
 - fotosystém purpurových bakterií
 - fotosystém zelených sirných bakterií (bakterií chlorobi)
 - reakční centrum zachytí kvantum světelné energie
 - excituje se
 - vyhodí elektron na přenašeč - u purp. bakteriích Pheophytin -> CoQ, u chlorobi rovnou CoQ
 - protonová pumpa (Cytc complex) -> přenesení H+ přes membránu, elektron se s Cytc vrací na reakční centrum
 - u zelenosirných bakterií (chlorobi) se může excitovaný elektron rovnou (acyklicky) použít přes feredoxin na oxidaci NADH+H+

 - u eukaryot jsou tyto systémy spojené do systému *Z*
   - fotosystém II a fotosystém I (v tomto pořadí jsou řetězené)
   - ve dvou fázích se excituje elektron
   - ve fotosystému II se vytváří protonový gradient
   - ve fotosystému I se oxiduje NADPH

6. Kde jsou tyto fotosystémy v chloroplastech lokalizovány?
 - v membráně tylakoidu (většinou v granech)

7. Co je hlavními produkty světelné fáze fotosyntézy?
 - ATP

8. Jaká jsou hlavní stádia fixace CO2 u fotosyntetizujících organismů?
 - jsou známy 3 možnosti fixace CO2 - Calvinův cyklus, Hatch-Slackův cyklus a CAM cyklus
 - v přednášce je zmíněn Calvinův cyklus, protože je relativně nejběžnější

 a. K čemu dochází v první fázi?
 - fixace CO2 - na Ribulóza 1,5-fosfát (enzymem Rubisco), rozdělení 6C na 2x 3C molekuly (fosfoglycerát)
 b. K čemu dochází ve druhé fázi?
 - redukce - využívá se NADPH+H, vzniká glyceraldehyd 3-fosfát - ten může odejít k syntéze dalších molekul, nebo jít do 3. fáze
 c. K čemu dochází ve třetí fázi?
 - regenerace - vzniká Ribulóza 1,5-fosfát (z 5 trióz vzniknou 3 pentózy)

9. V čem se liší glukoneogeneze od glykolýzy?
 - jde o to nějakým způsobem získat 3-fosfoglycerát
 - ten může vznikat přímo z fotosyntézy
 - nebo jako meziprodukt citrátového cyklu (ten může využívat ke svému chodu i aminokyseliny)
   - živočichové mohou získávat pyruvát z laktátu (pokud předtím měli anaerobní glykolýzu)
 - z 3-fosfoglycerátu je pak syntetizována glukóza 6-fosfát
   - syntéza probíhá vpodstatě zrcadlově, ale jsou tu 3 vysoce makroergní reakce glukoneogeneze, které se musí řešit jinak
   - pyruvátkinázová reakce -> stojí ATP a GTP
   - hexokinázová reakce a ribózafosfát kinázová reakce -> fosfatázy prostě odštěpí fosfát

10. Kde je v buňce glukoneogeneze lokalizována?
 - mitochondrie a cytosol

11. Mohou být z tuků syntetizovány cukry?
 - ano - z glycerolu (jde na dihydroxyaceton-fosfát) + acetyl-CoA je palivo citrátového cyklu

12. Jaké jsou hlavní produkty pentózofosfátové dráhy?
 - ribóza-5-fosfát, redukční ekvivalenty (NADPH)

13. Jak souvisí pentózofosfátová dráha se zametáním volných kyslíkových radikálů?
 - glutathion je molekula, která umí vychytávat volné kyslíkové radikály, ale potřebuje spotřebovávat NADPH aby se sama redukovala

14. Co je to Cori cyklus?
 - Coriho cyklus slouží k odbourávání laktátu, viz přednáška #5 Glykogen

> Těším se opět na shledanou,
> Martin Kalous

# 10 Lipidy a membrány

[prezentace](https://dl2.cuni.cz/pluginfile.php/198127/mod_resource/content/1/BZ12_Lipidy.pdf)
[přednáška](https://www.youtube.com/watch?v=O5PNZnhcvZ4)

> Milí přátelé,
> Přikládám otázky pro přípravu na přednášku o lipidech 6.12.  Poslechněte si prezentace k tomuto tématu a připravte si odpovědi na následující otázky:

1. Jakou strukturu mají živočišné tuky?
 - tuky se skládají z glycerolu (3 uhlíky, -OH skupina na každém z nich) a tří uhlíkatých zbytků na esterové vazbě (tuky = triacylglyceroly)
 - mohou být jednoduché a smíšené triacylglyceridy
   - jednoduché mají třikrát stejný "acyl"
   - smíšené mají různé tři "acyly"
 - (k téhle otázce doporučuji nastudovat prezentaci na slidu 2, je tam přehled základních struktur mono-di-tri acyl glycerolů a slide 6 o mastných kyselinách (což zpravidla jsou uhlíkaté zbytky, o kterých jsem psal nahoře))

2. Co jsou vosky, jaké znáte zástupce?
 - [Wiki](https://cs.wikipedia.org/wiki/Vosk)
 - vosky jsou sloučeniny mastné kyseliny (MK) a vyššího jednosytného alkoholu
 - MK a alkohol jsou spojené esterovou vazbou

 - včelí vosk: kyselina palmitová (16C) a 1-triakontanol (30 C)
 - velrybí vosk: cetylpalmitát - kys. palmitová (16C) a ?palmitol? (16C)

3. Jaké znáte zástupce terpenů?
 - isopren ... základní stavební jednotka terpenů, struktura se dá zapsat jako 1-methyl but-1,3dien
 - limonen
 - citronen
 - mentol
 - kyselina diberelová ... základ pro fytohormony
 - phytol ... prekurzor pro vitamin E a K1

4. Jak dělíme membránové lipidy?
 - klasické lipidy ... glycerol + skupiny
   - fosfolipidy ... 2 acyl skupiny, 1 PO4 + alkohol nebo choline
 - sphingolipidy ... základ lipidu je sphingosine, dále jedna -acyl skupina a poté
   - glycerolfosfolipidy ... přes PO4 skupinu mají navázaný glycerol
   - glykolipidy ... navázán mono/oligo sacharid

5. Co víte o složení a stavbě biomembrán?
 - obsahuje z většiny fosfolipidy s nasycenými i nenasycenými acylovými skupinami (např. kys. oleová)
   - nenasycená skupina vytváří zalomení a dělá membránu více pohyblivou
 - obsahuje i sfingolipidy a cholesterol
 - důležitou složkou membrán jsou i membránové proteiny (u E. coli až 75%)

 - membrána se skládá ze dvou vrstev lipidů, kdy polární část je orientovaná ven a nepolární je orientovaná dovnitř

6. Co víte o vlivu lipidů na vlastnosti biomembrán?
 - teplota a stabilita:
   - zastoupení jednotlivých lipidů / dalších látek výrazně ovlivňuje především fluiditu membrán
   - čím vyšší teplota, tím víc se má membrána tendenci chovat jako běžná kapalina (nefunkční)
   - to se dá spravit např. vyšším zastoupením cholesterolu, který ji stabilizuje
   - při nižších teplotách má naopak tendenci tuhnout - je potřeba vyšší zastoupení běžných fosfolipidů, aby byla membrána pohyblivá
 - dále mají různé typy látek vliv na zakřivení membrán

 - tloušťka membrány:
   - např. fosfatidylcholine (PC) tvoří "tenší" membránu, když je sám, než když je v kombinaci s cholesterolem - PC má totiž pohyblivé acylové skupiny, které mají tendenci se kroutit
   - oproti tomu sfingomyelin (SM) je stabilní sám o sobě a přítomnost cholesterolu jeho vlastnosti nemění

7. Co víte o difúzi lipidů v biomembránách?
 - laterální pohyb (pohyb po povrchu membrány) je **velmi rychlý (1ɳm/s)**
 - "transbilayer - flip-flop" pohyb (z jedné strany dvouvrstvy na druhou) je **velmi pomalý** (pro daný lipid se poločas počítá v řádu **dní**) 
 - také enzymy katalizují přesun lipidů z jedné strany membrány na druhou (***translokázy***)
   - flipáza ... přesouvá fosfatidylserin a "PE" (nějaký další lipid) z vnější strany buněčné membrány na vnitřní
   - flopáza ... přesouvá fosfolipidy z vnitřní straný membrány na vnější
   - skrambláza ... náhodně přehazuje lipidy oběma směry (spoiler alert: *funguje například při apoptóze*)

8. Jaká je struktura a funkce fosfolipidů?
![obrázek mluví za vše](https://www.creative-biolabs.com/lipid-based-delivery/static/img/Phosphatidylcholine-2.png)

 - mají na glycerolu dva hydrofobní ocásky, fosfátovou skupinu a na ní ještě alkohol  
 - na fosfát ale mohou být přidané ještě úplně různé další struktury - aminoskupiny, fosfatidil glycerol, inositol bifosfát etc.

9.  Jak jsou fosfolipidy odbourávány?
 - fosfolipázy (A1, A2, C) odštěpí od glycerolu navázané skupiny
 - acyly (odštěpené A1, A2 fosfolipázami) jdou do ß-oxidace MK

10. Jak jsou fosfolipidy syntetizovány?
 - fosfatidylcholin (PC)
   - přes ethanolamine-cholin
   - přes CDP-ethanolamin a CDP-cholin
   - cholin se získává především ve stravě
   - vzniká fosfatidylethanolamin nebo fosfatidyl cholin
 - fosfatidylserin (PS)
   - syntetizuje se z fosfatidylethanolaminu
   - odštěpí se ethanol a místo něj se dá serin
   - funfact o PS - když je na vnější straně buněčné membrány, signalizuje apoptózu
   - skrambláza slouží hlavně k tomu, aby PS dala právě na vnější stranu membrány
 - fosfatidyl-glycerol (PG) a fosfatidyl-inositol
   - vznikají ze "základního" fosfolipidu - jen glycerol, 2 acyl skupiny a fosfo skupina
   - na fosfát se přidá glycerol, nebo inositol

 - kardiolipin je speciální lipid, který vzniká ze dvou PG, které se spojí svými glyceroly (slide 55)

11. Jaká je struktura a funkce sfingolipidů?
 - doporučuju prezentaci, slide 58
 - sfingolipidy jsou zajímavé tím, že je tvoří sfingosin - vypadá jako glycerol, jen na 1C má ještě 15C řetězec (bez esterové vazby, jen s dvojnou vazbou)
 - dále mají jednu acyl-skupinu a nějakou další skupinu na 3C
 - cerebrosidy, gangliosidy, sulfatidy, globosidy ... nervová soustava

12. Co se děje při poruchách odbourávání glykosfingolipidů?
 - např. Tay-Sachsova choroba ... hromadění gangliosidů na povrchu nervových buněk, demence

> S pozdravem,
> Jan Brábek

# 11 Metabolismus lipidů

[prezentace](https://dl2.cuni.cz/pluginfile.php/198128/mod_resource/content/1/BZ12_Metabolismus%20lipidu.pdf)
[přednáška](https://youtu.be/mCYZuWs8P5Y)

> Milí přátelé,
> Přikládám otázky pro přípravu na přednášku o metabolismu lipidů 13.12.  Poslechněte si prezentace k tomuto tématu a připravte si odpovědi na následující otázky:

1. Jak probíhá trávení a odbourávání tuků?
 - tuky se tráví za pomoci pankreatické lipázy - ta štěpí triacylglyceroly na mono/diacyl glyceroly a na volné mastné kyseliny
 - zbylé triacylglyceroly jsou uloženy do **chylomikronů**
 - chylomikron ... váček z cholesterolu, fosfolipidů a alipoproteinů obsahující triacylglyceroly
 - volné mastné kyseliny vstupují přímo přes stěnu tenkého střeva do lymfatického systému a krevního řečiště, odkud jsou vstřebávány do buněk
 - lipoprotein lipáza umí štěpit triacylglyceroly v tkáních na glycerol a mastné kyseliny

2. Jak probíhá aktivace mastných kyselin a jejich transport do mitochondrií?
 - u člověka jsou tuky uskladněné v tukové tkáni, v adipocytech
 - adipocyt ... buňka tukové tkáně
 - na základě hormonového signálu se aktivuje signální dráha, která uvolní cAMP
 - cAMP aktivuje hormon-senzitivní lipázu, která se přidá do membrány "lipid droplet"
 - dále lipáza začne rozkládat triacylglyceroly na mastné kyseliny a glycerol
 - mastné kyseliny se přes membránu adipocytu vloží do serum albuminu v krevním řečišti, odkud je využíván dalšími buňkami
 - serum albumin ... protein v krevním řečišti produkovaný játry, má více funkcí, ale mj. se nespecificky váže k mastným kyselinám, což je využíváno pro jejich transport. Více na [Wiki](https://en.wikipedia.org/wiki/Serum_albumin)

 - uvolněný glycerol vstupuje do glykolýzy (fosforyluje se a redukuje na glyceraldehyd 3-fosfát)
 - např. myocyt (svalová buňka) má na svém povrchu transportéry mastných kyselin, které přijímají mastné kyseliny z krve
 - dále jsou mastné kyseliny transportovány do mitochondrií, kde nastupuje proces beta oxidace

 - přenos přes membránu mitochondrie probíhá přes *karnitin* - je to trochu složitější proces, takže ho radši rozepíšu:
   - MK s už navázaným -CoA přijde k membráně mitochondrie, kde se místo -CoA naváže karnitin a MK přejde pomocí *karnitinacyltransferázy* přes vnější membránu mitochondrie
   - tam v antiportu s nenavázaným karnitinem projde přes vnitřní membránu skrz transportér
   - uvnitř se pak karnitin z MK odštěpí a na jeho místo se naváže opět CoA a MK jde do beta oxidace
   - zpět se karnitin dostane opět antiportem přes transportér do mezimembránového prostoru
   - díky své malé velikosti projde karnitin samovolně přes vnější membránu mitochondrie, čímž se jeho cyklus uzavírá
   - na následujícím obrázku od 1. lékařské fakulty se proces částečně liší od toho, co má doc. Brábek v prezentaci... Asi je jedno z toho zastaralé. Njn. :D
![obrázek karnitin-transferu MK](http://fblt.cz/wp-content/uploads/2013/12/karnitinovy-prenasec-011.jpg)

3. Jak probíhá beta oxidace mastných kyselin?
 - nejprve je potřeba aktivovat mastnou kyselinu (navázat CoA)
   - to se dělá tak, že na -COO- konec mastné kyseliny se naváže AMP (za spotřeby ATP a vzniku P2 ... pyrofosfátu)
   - místo AMP se pak naváže -CoA
   - energetická bilance tohoto je silně záporná (-33.6kJ/mol)

![obrázek mluví za vše](https://eluc.kr-olomoucky.cz/uploads/images/20307/content_beta_oxidace.jpg)

 - beta oxidace samotná probíhá ve 3 krocích
   - nejprve se vytvoří dvojná vazba na předposledním uhlíku, čímž se nabije FADH2
   - pak se dvojná vazba hydratuje a nabije se NADH
   - následně se odštěpí acetyl-CoA a na volné místo se naváže další -CoA

4. Jak jsou odbourávány MK s lichým počtem uhlíků a nenasycené MK?
 - oxidace MK s lichým počtem uhlíků vytváří kromě acetyl-CoA i jeden propionyl-CoA, který se převádí na sukcinil-CoA, což je intermediát Krebsova cyklu. [Více viz Wikiskripta.](https://www.wikiskripta.eu/w/Oxidace_mastn%C3%BDch_kyselin_s_lich%C3%BDm_po%C4%8Dtem_uhl%C3%ADk%C5%AF)

 - nenasycené MK se betaoxidují dokud se nedojde k nenasycené (dvojné) vazbě
 - ta ještě není problém, pokud je v *trans* konformaci
   - pokud je ale v *cis* konformaci, je přeměněna na *trans* konformaci enoyl-CoA isomerázou
   - ta je následně použita už v beta oxidaci
 - podobně se řeší i ostatní problémy s dvojnou vazbou - dvě dvojné vazby za sebou etc.
 - mch. energetická bilance odbourání palmitátu je +108 ATP, což je 3.5x víc než u glukózy (~30-32 ATP)

5. Jaké znáte ketolátky? Jak se tvoří a odbourávají?
   
![aceton, acetoacetát, hydroxobutyrát](https://vydavatelstvi-old.vscht.cz/knihy/uid_es-002_v1/figures/ketogenese.schema.01.gif)
 - keto látka ... kyslík je na dvojné vazbě
 - aceton ... 3C s kyslíkem na dvojné vazbě na prostředním uhlíku
 - acetoacetát ... 4C, karboxylová skupina na 4. uhlíku, kyslík dvojné vazbě na 2. uhlíku
 - hydroxybutyrát ... jako acetoacetát, keto skupina na druhém uhlíku zaměněna za hydroxyskupinu
 - tvorba výše zmíněných (slide 39):
   - 2x acetyl-CoA -> acetoacetyl-CoA
   - acetoacetyl-CoA + acetyl CoA -> hydroxymethylglutaryl-CoA
   - hydroxymethylglutaryl-CoA -> acetoacetát + acetyl-CoA
   - acetoacetát -> acetol + -COOH
   - acetoacetát -> hydroxybutyrát
 - odbourávání:
   - opět přes acetoacetát
   - acetoacetát + succinyl-CoA -> acetoacetyl-CoA a sukcinát
   - acetoacetyl-CoA + CoA-SH -> 2x acetyl-CoA

6. Jaké jsou rozdíly mezi syntézou a beta-oxidací mastných kyselin?
 - doslova z prezentace:
> Biosyntéza mastných kyselin se od jejich oxidace liší v několika ohledech. Zatímco oxidace
mastných kyselin probíhá v mitochondriích a využívá estery acyl-CoA, biosyntéza
mastných kyselin probíhá v cytosolu, přičemž rostoucí acylový zbytek je připojen esterovou
vazbou k proteinu přenášejícímu acylové skupiny (ACP).

 - jednoduše:
| beta-oxidace | syntéza |
|---|---|
| mitochondrie | cytosol |
| -CoA | ACP |
 - ACP ... protein, který tam prostě je

1. Jak probíhá reakce acetyl-CoA-karboxylázy? Jaký má enzym kofaktor?


2. Jak je acetyl-CoA-karboxyláza regulována?
3.  Jak probíhá syntéza mastných kyselin? Jak vypadá syntáza mastných kyselin?
4.  Jak se dostává acetyl-CoA z mitochondrií do cytoplazmy?
5.  Kde a jak probíhá elongace mastných kyselin?
6.  Kde a jak probíhá desaturace mastných kyselin?
7.  Jak probíhá syntéza triacylglycerolů?
8.  Jak je regulován metabolismus živočišných tuků?
9.  Jaké jsou důležité „vedlejší produkty“ syntézy cholesterolu?
10. Jak je regulována syntéza cholesterolu?
11. Jak probíhá syntéza skvalenu?
12. Jak probíhá syntéza a transport cholesterolu v hepatocytu?
13. Syntéza kterých zásadně důležitých látek vychází z cholesterolu?

> S pozdravem,
> Jan Brábek


