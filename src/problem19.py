'''
You are given the following information,
    but you may prefer to do some research for yourself.

1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4,
    but not on a century unless it is divisible by 400.
How many Sundays fell on the first of the month
    during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
'''

import datetime


def find_sundays():
    '''
    find each first of the month Sunday
    '''
    result = len([1
                  for year in range(1901, 2001)
                  for month in range(1, 13)
                  if datetime.date(year, month, 1).isoweekday() == 7])
    return result


print ("Number of Sundays is {}".format(find_sundays()))

import timeit
t = timeit.Timer("find_sundays", "from __main__ import find_sundays")
print ("Average running time: {} seconds".format(t.timeit(1000)))
