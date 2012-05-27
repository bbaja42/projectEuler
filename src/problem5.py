'''
2520 is the smallest number that can be divided by
 each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that
 is evenly divisible by all of the numbers from 1 to 20?
'''
from functools import reduce


def gcd(a, b):
    """Return greatest common divisor using Euclid's Algorithm."""
    while b:
        a, b = b, a % b
    return a


def lcm(a, b):
    """Return lowest common multiple."""
    return a * b // gcd(a, b)


def lcmm(*args):
    """Return lcm of args."""
    return reduce(lcm, args)


def find_smallest_disible():
    '''
    Find all functors for range of numbers, and multiply for result
    '''
    return lcmm(*range(1, 21))

print ("Smallest divisible is {}".format(find_smallest_disible()))

import timeit
t = timeit.Timer("find_smallest_disible",
                "from __main__ import find_smallest_disible, lcm, gcd, lcmm")
print ("Average running time: {} seconds".format(t.timeit(1000)))
