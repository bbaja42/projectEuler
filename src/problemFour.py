'''
A palindromic number reads the same both ways.
The largest palindrome made from the product
 of two 2-digit numbers is 9009 = 91  99.

Find the largest palindrome made from the product of two 3-digit numbers.
'''


def find_palindrome():
    start = 100
    end = 1000
    return max([x * y for x in range(start, end) for y in range(x, end)
                if str(x * y) == str(x * y)[::-1]])

print ("Largest palindrome is {}".format(find_palindrome()))

import timeit
t = timeit.Timer("find_palindrome()", "from __main__ import find_palindrome")
print ("Average running time: {} seconds".format(t.timeit(10)))
