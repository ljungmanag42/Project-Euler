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