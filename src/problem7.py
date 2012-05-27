'''
By listing the first six prime numbers:
2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
'''

import math


def is_prime(n):
    if n == 2:
        return True
    elif n % 2 == 0:
        return False
    i = 3
    max_value = int(math.sqrt(n))
    while(i <= max_value):
        if(n % i == 0):
            return False
        i += 2
    return True


def find_triplet():
    prime_counter = 1
    counter = 2
    while(prime_counter <= 10001):
        counter += 1
        if(is_prime(counter)):
            prime_counter += 1
    return counter

print ("Found prime is {}".format(find_triplet()))


import timeit
t = timeit.Timer("find_triplet",
                "from __main__ import find_triplet")
print ("Average running time: {} seconds".format(t.timeit(10)))
