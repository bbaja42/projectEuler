'''
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
'''


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


def sum_of_primes():
    max_num = 2000000
    return (sum(sundaram3(max_num)))

print ("Sum of primes is  is {}".format(sum_of_primes()))


import timeit
t = timeit.Timer("sum_of_primes",
                "from __main__ import sum_of_primes")
print ("Average running time: {} seconds".format(t.timeit(1000)))
