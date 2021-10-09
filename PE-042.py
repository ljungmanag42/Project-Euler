# ProjectEuler 42

'''
The nth term of the sequence of triangle numbers is given by, t_n = 1/2*n(n+1); 
so the first ten triangle numbers are:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to its 
alphabetical position and adding these values we form a word value. 
For example, the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word 
value is a triangle number then we shall call the word a triangle word.

Using words.txt (right click and 'Save Link/Target As...'), a 16K text 
file containing nearly two-thousand common English words, how many are 
triangle words?
'''

import math
import string

file = 'p042_words.txt'


letterValue = dict()
alphabet = list(string.ascii_lowercase)
for lNum in range(len(alphabet)):
    letterValue[alphabet[lNum]] = lNum+1 

triangle_numbers = dict()
triangle_numbers[1] = int((1/2)*1*(1+1))
def update_triangle_numbers(triangle_numbers,limit):
    max_val = max(triangle_numbers.values())
    C = max_val<limit
    while C:
        N = max(triangle_numbers.keys())+1
        tN = int((1/2)*N*(N+1))
        triangle_numbers[N]=tN
        max_val = max(triangle_numbers.values())
        C = max_val<limit
    return triangle_numbers    

def calc_word_value(word):
    total = 0
    for letter in word:
        total+=letterValue[letter]
    return total

with open(file,'r') as f:
    txt = f.readline()
    
triangle_words = []
for word in txt.split(',') :
    word = word.replace('"','')
    word_value = calc_word_value(word.lower())
    triangle_numbers = update_triangle_numbers(triangle_numbers,word_value)
    if word_value in triangle_numbers.values():
        triangle_words.append(word)

print(len(triangle_words))
