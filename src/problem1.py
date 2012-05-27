'''
If we list all the natural numbers below 10 that are multiples of 3 or 5,
we get 3, 5, 6 and 9.
The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
'''


def find_sum():
    result = sum([x for x in range(1000) if x % 3 == 0 or x % 5 == 0])
    return result

print ("Sum is {}".format(find_sum()))

import timeit
t = timeit.Timer("find_sum()", "from __main__ import find_sum")
print ("Average running time: {} seconds".format(t.timeit(1000)))
