# Project Euler 10
#
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#
# Find the sum of all the primes below two million.

'''Answer = 142913828922'''

def is_prime(x):  
    if x==1 or x==2:
        return True
    for f in xrange(2,int(round(x**0.5))+1):
        if x%f==0:
            return False
    return True 

total = 0
for n in xrange(2,int(2e6)):
    if is_prime(n):
        total += n
        
print total