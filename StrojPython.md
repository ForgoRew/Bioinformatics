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

