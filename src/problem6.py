'''
The sum of the squares of the first ten natural numbers is,

12 + 22 + ... + 102 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)2 = 552 = 3025
Hence the difference between the sum of the squares
 of the first ten natural numbers and
 the square of the sum is 3025 385 = 2640.

Find the difference between
the sum of the squares of
 the first one hundred natural numbers
 and the square of the sum.
'''

import math


def difference():
    """Return greatest common divisor using Euclid's Algorithm."""
    size = 100 + 1
    sum_of_squares = sum(x * x for x in range(size))
    square_of_sums = int(math.pow((size * (size - 1) // 2), 2))
    return square_of_sums - sum_of_squares


print ("Difference is {}".format(difference()))


import timeit
t = timeit.Timer("difference",
                "from __main__ import difference")
print ("Average running time: {} seconds".format(t.timeit(1000)))
