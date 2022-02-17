# Pravděpodobnost a statistika I

### Practices - conditions
Homework 20%

Midterm tutorial test 40-45%

Endterm tutorial test 40-45%


## 01 P
### Independent events
Events A,B are independent, if:
 - P[A^B]=P[A]*P[B]
 - P[A|B]=P[A], P[B|A]=P[B]
 - P[AvB]=P[A]+P[B]-P[A]*P[B]

We can sum up these in the formula P[A|B]=P[A^B]/P[B]

### Practice
Events A,B,C are mutually independent if:
 - P[A^B^C] = P[A].P[B].P[C]
 - A, B, C are pairwise independent

Events E are mutually independent if:
 - product of probabilities of events are equal to probability of intersect of the events
 - all the k events, k = |E|-1 are mutually independent
 - all the events are pairwise independent

Dies - O1={1,2,3,4,5,6}
For two throws:
O2={(1,1),(1,2),...,(6,6)}

Event A: You roll a total of 9 on two times.
A={(4,5),(5,4),(3,6),(6,3)}
|A|=4
P[A]=4/36=1/9

Event B: You roll even number both times.
Are A and B independent?
P[A^B]=0
P[A].P[B]=1/18
No.

O3 ... prob. space o 3times tossing of a coin
O3 = {(0,0,0), (0,0,1), ..., (1,1,1)}
X ... number of heads obtained = {0,1,2,3} ... 1/8,3/8,3/8,1/8
E[X]=SUM_a(a.P[X=a])=3/8+2*3/8+3*1/8=12/8=3/2



