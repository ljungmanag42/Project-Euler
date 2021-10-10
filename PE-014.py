# ProjectEuler 14

''''
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 
10 terms. Although it has not been proved yet (Collatz Problem), it is thought 
that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
'''

#max_start = 20000
max_start = 1000000

def is_even(x):
    if x % 2 == 0:
        return True
    else:
        return False

sequence_dict = dict()
n0 = 0
while n0<max_start:
    n0 += 1
    
    n = n0
    seq = [n]
    while n>1:    
        if is_even(n):
            n = n/2
        else:
            n = 3*n+1
        seq.append(n)    
    sequence_dict[n0]=len(seq)        
print(max(sequence_dict.values()))