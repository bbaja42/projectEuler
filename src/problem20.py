'''
n! means n  (n  1)  ...  3  2  1

For example, 10! = 10  9  ...  3  2  1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
'''

from math import factorial


def digits_sum():
    large_num = factorial(100)
    result = sum(map(int, str(large_num)))
    return result


print ("Number of Sundays is {}".format(digits_sum()))

import timeit
t = timeit.Timer("digits_sum", "from __main__ import digits_sum")
print ("Average running time: {} seconds".format(t.timeit(1000)))
