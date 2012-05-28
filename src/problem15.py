'''
Starting in the top left corner of a 2x2 grid,
 there are 6 routes (without backtracking) to the bottom right corner.

How many routes are there through a 20x20 grid?
'''
from math import factorial


def find_routes():
    '''
    Since backtracking is not allowed,
    it is only possible to go right and bottom.
    It will take 40 steps to cover whole grid.
    20 down and 20 right.
    Simple combinatorics
    '''
    size = 20
    return factorial(size * 2) // (factorial(size) * factorial(size))


print ("Number of routes is {}".format(find_routes()))

import timeit
t = timeit.Timer("find_routes", "from __main__ import find_routes")
print ("Average running time: {} seconds".format(t.timeit(1000)))
