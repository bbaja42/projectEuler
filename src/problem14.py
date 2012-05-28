'''
The following iterative sequence is defined for the set of positive integers:

n  n/2 (n is even)
n  3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13  40  20  10  5  16  8  4  2  1
It can be seen that this sequence (starting at 13 and finishing at 1)
 contains 10 terms.
Although it has not been proved yet (Collatz Problem),
 it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
'''

#Contains maximum chain length for each found origin number
cache_numbers = {}


def find_start_number():
    '''
    Find start number with largest chain
    Uses cache for found numbers as an optimization
    '''
    max_value = 1
    index = 0
    for i in range(2, 1000000):
        cache_numbers[i] = calc_chain(i)
        if cache_numbers[i] > max_value:
            max_value = cache_numbers[i]
            index = i
    return index


def calc_chain(n):
    if n in cache_numbers:
        return cache_numbers[n]
    if n == 1:
        return 1
    result = 1
    if (n % 2 == 0):
        result += calc_chain(n // 2)
    else:
        result += calc_chain(3 * n + 1)

    return result

print ("Chain is {}".format(find_start_number()))

import timeit
t = timeit.Timer("find_start_number", "from __main__ import find_start_number")
print ("Average running time: {} seconds".format(t.timeit(1000)))
