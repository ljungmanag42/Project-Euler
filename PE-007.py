# Project Euler 7
#
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see 
# that the 6th prime is 13.
#
# What is the 10 001st prime number?

###################
# Answer = 104743 
###################

def is_prime(x):  
    if x==1 or x==2:
        return True
    for f in xrange(2,int(round(x**0.5))+1):
        if x%f==0:
            return False
    return True  

num = 1
primes = []
while len(primes)<=10000:
    num += 1
    if is_prime(num):
        primes.append(num)

print max(primes)        