# Pokračování v Javě

# 01
### Podmínky:
- zápočťák -> netriviální použití technologie z kurzu
- zkouška
- úkoly -> alespoň 75%

### Osnova předmětu
 - hlubší pohled do jazyka Java
    - přehled a historie platformy Java
    - reflection API
    - generické typy, anotace
    - class loaders, security 
- GUI
- distribuované technologie: RMI,...
- komponentový model JavaBeans
- JEE: Servlety, EJB, Spring,...
- JME: CLDC, MIDP, MEEP
- RTSJ
- další technologie založené na platformě Java: Java APIs for XML, JDBC, JMX,...
- další jazyky kompilované do Java byte
- code
- Android

### O Javě
 - silně typový jazyk (všechno je objekt nějaké třídy nebo primitivního typu) 
 - neexistují globální proměnné -> statické proměnné
 - viditelnost je možné ovlivnit pomocí `public` a `private`
 - změny typů jsou možné, ale pozor!
   - covariantní změna ... ze specifické na obecnější
   - contravariantní změna ... naopak

### Reflection API
 - Reflection: Mění strukturu a stav objektů
 - Introspection: Zkoumá strukturu objektů
 - Umožňuje
   - zjišťovat informace o třídách, atributech, metodách
   - vytvářet objekty
   - volání metod
   - ...
 - java.lang.reflect
 - java.lang.Class

### java.lang.Class<T>
 - generický typ
 - primitivní typy jsou reprezentovány jako instance třídy Class<T>
 - získání instance třídy Class
   - getClass() na třídě objekt
   - literál class (int.class)
 - Class.forName(String className)
 - Má spoustu dalších metod 
   - is... -> array, primitivní typ etc.
   - pro arraye další metody etc.
   - pro získání konstruktorů, získání polí etc.
   - vrací pole konstant enumu a typ objektů v poli
   - získávání modifikátorů etc

### Java.lang.reflect
 - .Field: getName, getType ...
 - .Method - získávání metody a volání metody
 - Constructor
 - Executable
 - .Array: dynamická práce s polema

### Reflexe vs. generické typy
 - úplně jsem nechytil ... :(

### Anotace
 - můžeme anotovat na úrovni bytecodu -> řekneme si příští týden!

### Reflexe a moduly
 - řekneme si také příště

### Použití
 - je to hodně praktické, přímý přístup dovnitř našeho kódu

### .Proxy
![](Screenshot_4.png)

### Pluginy
 - samostatně fungující segment kódu

# 02

### Java platform
 - JSE ... java standard edition
 - JEE ... java enterprice edition

### Výkon
 - spuštění vždy virtual - machine
   - má Just-in-time compilation
   - má optimalizaci za běhu
 - srovnatelný s normálními aplikacemi
 - velká spotřeba paměti

### Implementace Javy
 - Oracle: Oficiální implementace
 - Windows, Linux, macOS
 - OpenJDK: podporovaná Oraclem
   - z ní vychází oficiální implementace
 - existují i jiné implementace, ale nejsou příliš použité

### Androidové aplikace
 - Android compiluje do Java bytecodu,
 - má jinou virtual-machine

### Generické typy
 - opakování a nové informace
 - obdoba šablon z C#
 - parametry pro typy
 - cíl: přehlednější kód a typová bezpečnost.
   - `List<Integer>`
 - nejde dávat primitivní typy, interně se to mění na `Object`

 - není možné typy měnit
 - otazník (wildcard) je libovolný typ
   - `List<?>`
 - omezený `?` dáme extends
   - povolujeme kovariantní změnu (`List<? extends Shape>`)
   - děláme kontravariantní změnu (`List<? super T>`)
 - max() -> porovnatelné prvky -> implementují Comparable<Object>

### Anotace
 - dřív (Java 5) nebyly snadno přidávatelné.
 - nyní lze přidat ke každému elementu
 - i na dalších místech
 - lze omezit, na co půjde použít

@ a identifikátor
 - mega cool věc...


