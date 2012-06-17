'''
Let d(n) be defined as the sum of proper divisors of n
    (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a  b, then a and b are
 an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are
 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110;
  therefore d(220) = 284.
   The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
'''

import math


def sumDiv(number):
    '''Returns the sum of divisors of a given number.'''
    div = 1
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            div += i
            if number / i != i:
                div += number / i
    return div


def digits_sum():
    summ = 0
    for n in range(2, 10000):
        if sumDiv(sumDiv(n)) == n and sumDiv(n) != n:
            summ += n
    return summ


print ("Sum is {}".format(digits_sum()))

import timeit
t = timeit.Timer("digits_sum", "from __main__ import digits_sum")
print ("Average running time: {} seconds".format(t.timeit(1000)))
