# ProjectEuler 22

''''
Using names.txt (right click and 'Save Link/Target As...'), a 46K text file 
containing over five-thousand first names, begin by sorting it into 
alphabetical order. Then working out the alphabetical value for each name, 
multiply this value by its alphabetical position in the list to obtain a name 
score.

For example, when the list is sorted into alphabetical order, COLIN, which is 
worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN 
would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?
'''

import string

fpath = 'p022_names.txt'


letterValue = dict()
alphabet = list(string.ascii_lowercase)
for lNum in range(len(alphabet)):
    letterValue[alphabet[lNum]] = lNum+1 
    
def calc_word_value(word):
    total = 0
    for letter in word:
        total+=letterValue[letter]
    return total

with open(fpath,'r') as f:
    txt = f.readline()
    
name_str = txt.split(',')
names = []
for s in name_str:
    names.append(s.replace('"',''))
names = sorted(names)

total = 0
for n in range(len(names)):
    total += (n+1)*calc_word_value(names[n].lower())
print(total)
