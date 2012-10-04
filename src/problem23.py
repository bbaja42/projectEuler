'''
A perfect number is a number for which the sum of its proper divisors is exactly equal
 to the number. For example, the sum of the proper divisors of
 28 would be 1 + 2 + 4 + 7 + 14 = 28,
  which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors
 is less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16,
 the smallest number that can be written as
 the sum of two abundant numbers is 24. 
 By mathematical analysis, it can be shown that all integers greater 
 than 28123 can be written as the sum of two abundant numbers.
  However, this upper limit cannot be reduced any further by 
  analysis even though it is known that the greatest number 
  that cannot be expressed as the sum of two abundant numbers 
  is less than this limit.

Find the sum of all the positive integers which cannot
 be written as the sum of two abundant numbers.
'''


MAX_SUM_TWO_AMBUNDANT = 28123

def divisors_sum(n):
    '''
    Return sum of divisors for given number
    '''
    # Number is always divisible by itself
    # but it should be counted
    sumDivisor = -n
    div = 1
    while div * div <= n:
        if n % div == 0:
            sumDivisor += div
            if n / div != div: sumDivisor += n / div 
        div += 1
    return sumDivisor


def ambundant_numbers(max_num):
    '''
    Returns list of all ambundant number less than max_num
    '''
    ambundant_nums = []
    for i in xrange(max_num):
        if(divisors_sum(i) > i):
            ambundant_nums.append(i)
    return ambundant_nums

def find_sum():
    '''
    Find the sum of all the positive integers which cannot
    be written as the sum of two abundant numbers.
    '''
    input_nums = ambundant_numbers(MAX_SUM_TWO_AMBUNDANT)
    result = 0
    sum_ambundant_nums = {0}
    for i in input_nums:
        for j in input_nums:
            sum_ambundant_nums.add(i + j)
    
    for target in range(MAX_SUM_TWO_AMBUNDANT):
        if target not in sum_ambundant_nums:
            result += target            
 
    return result



print ("Sum is", find_sum())

import timeit
t = timeit.Timer("find_sum", "from __main__ import find_sum")
print ("Average running time in seconds", t.timeit(10))
