# 01
NPFL129

- učení
  - zkušenost
  - úloha
  - výsledek/měření

- úloha
  - klasifikace
  - regrese
  - predikce s určitou strukturou

- měření
  - přesnost, míra chyby, F-score

- zkušenost
  - supervised (učící data, víme výstup)
  - unsupervised (učící data, nevíme výstup, jen úlohu)
  - reinforcement learning (opakované upravování strategie)

- základní úlohy ... pro vstup $x \in \Reals^D$
  - regrese ... zobrazení $x \rightarrow t, t \in \reals$
  - klasifikace ... máme $K$ skupin, cílem je pro každé $x$ dát správnou skupinu

- tréningový set - množina dvojic $(x,t)$
- optimalizace ... co nejlepší fitnutí tréningových dat
- generalizace ... zobecnění modelu, aby fungoval i na neznámá data
  - abychom příliš nenaoptimalizovali model, vydělíme si část tréningových dat jako testovací data

- notace
  - *a* ... skalár
  - ***a*** ... vektor
  - ***A*** ... matice
  - A ... tensor
  - ||***a***||$_2$ je Euklidovská norma
  - derivace vs parciální derivace !!

- vstup
  - trénovací data můžeme předělat do matice |x1|x2|x3|...|xn| = X
  - trénovací výstupy ***t*** - vektor
  - zpravidla se do vstupního vektoru nakonec přidává 1, do vah nakonec pak o kolik má být přímka/nadrovina posunuta

- error function
  - MSE nebo sum of squares

- underfitting vs. overfitting

# 02 Lineární regrese II
- kapacita modelu
  - to, jak moc je model natrénovaný
  - má hodně nebo málo vah

- reprezentační vs. efektivní kapacita

- jak "oslabit" model
  - třeba ... *přidáme data*
  - ale spoustu jiných možností
  - -> **regularizace** - snižování chyby na testovacích datech
  - *limitace kapacity modelu*
  - *l2 regularizace*
    - vezmeme si ten nejjednodušší model
    - jednodušší modely mají malé váhy
    - zajišťuje se tak, že přidáme další člen do minimalizační funkce
      - $\frac{\lambda}{2}||w||^2$
      - ve výsledku udělám
        - $w = (X^TX+\lambda I_n)^{-1}X^Tt$
- hyperparametry
  - věci, co určujeme my před učením jako takovým
  - abychom si jen neoptimalizovali naše hyperparametry na naše trénovací data, je nejlepší si udělat ještě třetí zvláštní množinu dat, tzv. validační data
- co, když $X^TX$ není regulární matice?

- gradient descent
  - hledá se minimum funkce
  - poskakuje se po funkci o malé kroky ($\alpha$)
    - $\alpha$ se jmenuje "learning rate"
    - použijí se všechna data
- stochastický gradient descent
  - použijeme náhodné jedno dato
- minibatch SGD
  - vezmeme jen určitý počet příkladů z dat a na nich spočítáme GD
  - střední pozice mezi SGD a GD
- gradient descent funguje, pokud je funkce konvexní a spojitá (můžeme dojet na dno misky)

- příklady konvexních funkcí
  - $x^2$, exp(x), -log(x), suma čtverců 

- trénuje se přes "batche" b dat (výběry z dat)
- když projdeme všechna data, řekneme, že jsme dokončili "epochu"
  - většinou se totiž už "použité" příklady v dané epoše znovu nepoužívají

- ztrátová funkce

- learning curves

- one-hot features
  - zakódování kategorických znaků do jedniček a nul
  - `OneHotEncoder`

- feature normalization
  - znamená normalizaci i standardizaci
    - normalizace
      - posunutí minima na nulu a maxima na jedničku
      - `MinMaxScaler`
    - standardizace
      - odečtení střední hodnoty a vydělení rozptylem
      - `StandardScaler`

# 03 Perceptron & logistická regrese

### Binární klasifikace & perceptron
- vstup buďto je, nebo není v dané kategorii
- $x^Tw+b<0$ nebo $x^Tw+b>0$
  - 0 nebo 1
  - syntaktický hacky
    - ale používá se target $t \in (-1, 1)$
    - b je zase přidané k x a w jako poslední hodnota
  - pokud můžeme hodnoty rozdělit přímkou - jedním perceptronem - nazveme je **lineárně separabilní**

- **perceptronový algoritmus**
  - input - lineárně separabilní dataset (X,t)
  - output - váhy
  - postup
    1. w <- o (nulový vektor)
    2. y <- $x_i^Tw$ (predikujeme hodnotu výsledku pro x_i)
    3. pokud $t_iy<=0$
      - w <- w + tixi
- na tomhle algoritmu je blbý, že
  - najde prostě nějakou nadrovinu - je zpravidla nekonečně mnoho možných nadrovin
  - pokud není (X,t) lineárně separabilní, nikdy neskončí
  - nezískáme pravděpodobnosti predikcí, jen jedničky a nuly (minus jedničky)

### Common probability distributions
- Bernoulliho distribuce
  - hezká rovnice
    - $P(x) = \phi^x × (1-\phi)^{1-x}$

- categorial distribution
  - mnoho výsledků - nejen 1/0, každý má vlastní pravděpodobnost

### Information theory
- **self information** (*I(x)*)
  - záporný logaritmus pravděpodobnosti náhodné proměnné
- **entropie** (*H(P)*)
  - "self information" přes celé rozdělení *P*
  - střední hodnota "self information" v pravděpodobnosti veličiny, dá se spočítat jako $-E_{x~P}(log(P(x)))$
  - stejná rovnice jako fyzikální entropie
  - oficiálně se jmenuje *diferenciální*
  - logaritmus je zpravidla *přirozený*
    - z toho vychází, že potřebujeme pro poslání zprávy průměrně *$e*H(P)$* informace, říká se H(P) **natů** (pro binární logaritmy je to v *bitech*)
- **Cross-Entropy**
  - pro dvě distribuce - *P*, *Q*
  - očekávám, že zprávy se řídí distribucí *Q*
  - ale posílám s pravděpodobností *P*
  - počítá se $-E_{x~P}(log(Q(x)))$
  - funguje pro ní **Gibbsova nerovnost**
    - $H(P, Q) \geq H(P)$
    - $H(P, Q) = H(P)$ jen když $H=P$
    - **Důkaz** (vysvětlený ve videu, 1:01:00)
  - **KL-Divergence**
    - Kullback-Leiber
    - rozdíl cross-entropie a entropie
    - $D_{K||L}H(P,Q)-H(P)$
- proč chceme **normální rozdělení**
  - centrální limitní věta
  - pro danou střední hodnotu a rozptyl má **nejvyšší entropii**

- **empirická datová distribuce**
  - distribuce, která přesně popisuje *náš* dataset
    - $p_{data}=\frac{|i:x_i=x|}{N}$

- **maximal likelihood estimation**
  - nová hezká ztrátová funkce
  - rovná se
    - **negative log likelihood**
    - ***cross-entropy***
- **logistická regrese**
  - jakože nevim co přesně - perceptrony..?

# 04
- **zobecněné lineární modely**
  - nejdřív proženeme *x*ka **aktivační funkcí**

- **softmax**
  - zobecnění sigmoidu

- **poissonovská regrese**
  - jiná aktivace než logistická regrese (`exp()`)

- **multilayer perceptron**

- **hiddem layer**
  - aktivační funkce
    - sigmoid(x)?
    - 2*sigmoid(2x) - 1
      - = **hyperbolický tangens (tanh(x))**
    - ReLU
      - pod nulu nula, pak identita pro kladné hodnoty

# 05
- **skrytá vrstva** nám z **lineárního modelu** udělá **generalizovaný lineární model**
- **univerzální aproximační teorém**
  - složitý polynom můžeme aproximovat pomocí **ReLU**
  - **ReLU**(x) = max(0,x)

- **constrained optimization**
  - **Lagrangeovy multiplikátory**

- **F1-skore**
  - pro binární klasifikaci
    - **precision**=sensitivita=počet falešně pozitivní/všichni označení za pozitivní
    - **specificita**=počet falešných/všema idk asi **blbě!** 
    - **recall**=falešně negativní/všichni pozitivní
    - $F_{beta} = \frac{1 + \beta^2}{precision^{-1}+\beta^2*recall^{-1}}$

