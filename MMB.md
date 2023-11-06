# 03 Lineární procesy v diskrétním čase (lingebra)
- breberky
```py
import numpy as np

# [r1, r2, r3]
stav = np.array([1., 0.5, 0.5/3])

prechod = np.array([
    # 6 nových brouků z jednoho starého
    [0, 0, 6],
    # půl jednoročního brouka přežije do druhého roku
    [0.5, 0, 0],
    # třetina dvouletého brouka přežije do třetího roku
    [0, 1/3, 0]
    ])

# Vymíraj?! Jedině kvůli aritmetice procesoru - pokud se 1/3 zaokrouhlí na 0.333...
print('rok', 0, stav)
for i in range(100):
    stav = prechod@stav
    print('rok', i, stav)
```
- hezká věc - můžeme převádět matice na lineární zobrazení na soustavy rovnic na matice
