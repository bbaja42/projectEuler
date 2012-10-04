'''
A permutation is an ordered arrangement of objects.
For example, 3124 is one possible permutation of the digits
 1, 2, 3 and 4. If all of the permutations are listed
  numerically or alphabetically, we call it lexicographic order.
   The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits
 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
'''

LIMIT = 1000000
NUMBERS = [0,1,2,3,4,5,6,7,8,9]
import itertools



def find_perm():
    '''
    '''
    perm =  next(itertools.islice(itertools.permutations(NUMBERS),LIMIT -1 , LIMIT))
    return "".join(map(str, perm))


print ("Permutation is ", find_perm())

import timeit
t = timeit.Timer("find_sum", "from __main__ import find_sum")
print ("Average running time in seconds", t.timeit(1000))
