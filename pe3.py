# ProjectEuler 3
#
# The prime factors of 13195 are 5, 7, 13 and 29.
#
# What is the largest prime factor of the number 600851475143 ?

import math
number = 600851475143
#number = 13195

def is_prime(x):  
    if x==1 or x==2:
        return True
    for f in xrange(2,int(round(x**0.5))+1):
        if x%f==0:
            return False
    return True       

prime_factors = []
i = 0
while i<=math.sqrt(number):
    i+=1
    if number%i==0 and is_prime(i):
        prime_factors.append(i)
        
print "Largest prime factor of %d is %d" % (number, max(prime_factors))
