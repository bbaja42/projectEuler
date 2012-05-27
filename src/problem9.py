'''
A Pythagorean triplet is a set of three natural numbers, a  b  c, for which,

a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
'''

from math import sqrt, floor


def find_triplet():
    top = 1000
    for a in range(1, top):
        for b in range(1, top):
            c = a * a + b * b
            # check is c square of normal number
            if (floor(sqrt(c)) == sqrt(c)
                # check is sum correct
                and a + b + sqrt(c) == top):
                    return int(a * b * sqrt(c))

print ("Found triplet is {}".format(find_triplet()))

print (floor(sqrt(81)) == sqrt(81))

import timeit
t = timeit.Timer("find_triplet",
                "from __main__ import find_triplet")
print ("Average running time: {} seconds".format(t.timeit(10)))
