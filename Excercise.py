def FindRoots(n):
    roots = []
    for div in range(2, n//2+1):
        if n % div == 0:
            roots.append(div)
    return roots

print(FindRoots(64))

def PrimeFactors(n):
    factors = []
    div = 2
    while div <= n:
        while n % div == 0:
            factors.append(div)
            n /= div
        div += 1
    return factors

print(PrimeFactors(64))
print(PrimeFactors(51))

import re
def IsPalindrome(string):
    return string == string[::-1]

print(IsPalindrome("kajakartaA"))

print("PokemonLOL")