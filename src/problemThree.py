'''
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
'''
from math import sqrt, floor


def sundaram3(max_n):
    '''
    Returns list of primes up to a max value
    :param max_n:
    '''
    numbers = list(range(3, max_n + 1, 2))
    half = (max_n) // 2
    initial = 4

    for step in range(3, max_n + 1, 2):
        for i in range(initial, half, step):
            numbers[i - 1] = 0
        initial += 2 * (step + 1)

        if initial > half:
            return [2] + list(filter(None, numbers))


def find_prime_factor():
    target = 600851475143
    primes = sundaram3(floor(sqrt(target)))
    result = 1
    for prime in reversed(primes):
        if(target % prime == 0):
            result = prime
            break
    return result


print ("Largest prime is {}".format(find_prime_factor()))

import timeit
t = timeit.Timer("find_prime_factor()",
                  "from __main__ import find_prime_factor, sundaram3")
print ("Average running time: {} seconds".format(t.timeit(10)))
