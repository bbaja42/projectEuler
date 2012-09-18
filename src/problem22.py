'''
Using names.txt (right click and 'Save Link/Target As...'),
 a 46K text file containing over five-thousand first names,
  begin by sorting it into alphabetical order. 
  Then working out the alphabetical value for each name,
   multiply this value by its alphabetical position in the list to obtain a
    name score.

For example, when the list is sorted into alphabetical order,
 COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53,
  is the 938th name in the list. 
  So, COLIN would obtain a score of 938  53 = 49714.

What is the total of all the name scores in the file?
'''

import math


def sumDiv(number):
    '''Returns the sum of divisors of a given number.'''
    div = 1
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            div += i
            if number / i != i:
                div += number / i
    return div


def digits_sum():
    result = 0
    names = open('../names.txt','r').readline()
    index = 0
    for name in sorted(names.replace('"',"").split(",")):
        index += 1;
        name_value = 0
        for letter in name:
            name_value += ord(letter) - ord('A') + 1
        result += index * name_value
    return result


print ("Sum is",digits_sum())

import timeit
t = timeit.Timer("digits_sum", "from __main__ import digits_sum")
print ("Average running time in seconds", t.timeit(1000))
