# Project Euler 5

# 2520 is the smallest number that can be divided by each of the 
# numbers from 1 to 10 without any remainder.

# What is the smallest positive number that is evenly divisible 
# by all of the numbers from 1 to 20?

##############################
# Correct Answer = 232792560 #
##############################
import numpy as np

num = np.product([11,12,13,14,15,16,17,18,19,20])+1 
max_divisor = 20

def check_divisibility(num_check, num_max):
    if num_check%2 !=0:
        return False
    else:
        for n in range(1, num_max+1):
            if num_check%n != 0:
                return False
    return True

while True:
    num -= 1
    #print num
    if check_divisibility(num, max_divisor):
        print(num)        
        break 
