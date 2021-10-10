# ProjectEuler 41

''''
We shall say that an n-digit number is pandigital if it makes use of all the 
digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is 
also prime.

What is the largest n-digit pandigital prime that exists?
'''

def is_prime(x):
    if x >= 2:
        for n in range(2, x ):
            if (x % n) == 0:
                return False
        #after the complete for n loop
        return True
    else:
        return False

def is_pandigital(x):
    x_str = str(x)
    xSet = set(x_str)
    charSet = set([str(c) for c in range(1,len(x_str)+1)])
    intersectionSet = charSet.intersection(xSet)
    if len(intersectionSet)==len(xSet) and len(xSet)==len(x_str):
        return True
    else:
        return False

primes_short = []
n=0
while n<=20:
    n+=1
    if is_prime(n):
        primes_short.append(n)

pandigital_primes = []
while n<1e9:
   n+=1
   if is_pandigital(n):
       print(n)
       if is_prime(n):
           pandigital_primes.append(n)
print(pandigital_primes)          