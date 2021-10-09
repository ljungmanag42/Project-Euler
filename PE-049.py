# ProjectEuler 49

''''
The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases 
by 3330, is unusual in two ways: 
    (i) each of the three terms are prime, and, 
    (ii) each of the 4-digit numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, 
exhibiting this property, but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this 
sequence?
'''

from itertools import permutations
import numpy as np

def is_prime(x):
    if x >= 2:
        for n in range(2, x ):
            if (x % n) == 0:
                return False
        #after the complete for n loop
        return True
    else:
        return False

primes = []
N=1000
while N<=9999:
    if is_prime(N):
        print(N)
        primes.append(N)
    N+=1

potential_sequences = []
for n in primes:
    print(n)
    seq = [n]
    charset = [c for c in str(n)]
    pSet = [int(''.join(x)) for x in list(permutations(charset))] 
    for d in range(1,5000):
        if n+d in primes and n+d in pSet:
            seq.append(n+d)
            break
    if n+d+d in primes and n+d+d in pSet:
        seq.append(n+d+d)
        potential_sequences.append(seq)

if len(potential_sequences)==1:
    seq = potential_sequences[0]
    print(seq)
