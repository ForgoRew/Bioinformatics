import numpy as np

A = np.matrix([[1950, 1960, 1970, 1980, 1990, 2000], [1, 1, 1, 1, 1, 1]]).T
b = np.matrix([2.519, 2.982, 3.692, 4.435, 5.263, 6.070]).T

print(A)
print(b)
print()

# A^TAx=A^Tb
# x = (A^T A)^-1 A^T b

x = np.linalg.inv(A.T * A) * (A.T * b)

print(x)

print()
print(A/b)

print()
print(x[0]*2020 + x[1])

print()
print(x[0]*1990 + x[1])