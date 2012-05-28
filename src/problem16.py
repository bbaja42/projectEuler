'''
2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?
'''


def find_sum():
    big_number = 2 ** 1000
    return sum(map(int, str(big_number)))

print ("Sum of digits is {}".format(find_sum()))

import timeit
t = timeit.Timer("find_sum", "from __main__ import find_sum")
print ("Average running time: {} seconds".format(t.timeit(1000)))
