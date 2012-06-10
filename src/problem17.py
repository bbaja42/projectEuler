'''
If the numbers 1 to 5 are written out in words: one, two, three, four, five,
 then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in
 words, how many letters would be used?


NOTE: Do not count spaces or hyphens. For example, 342
 (three hundred and forty-two)
 contains 23 letters and 115 (one hundred and fifteen) contains 20 letters.
 The use of "and" when writing out numbers is in compliance with British usage.
'''


def find_sum():
    units = ["", "one", "two", "three", "four", "five",
              "six", "seven", "eight", "nine", "ten", "eleven",
               "twelve", "thirteen", "fourteen", "fifteen",
                "sixteen", "seventeen", "eighteen", "nineteen", ]
    tens = ["", "", "twenty", "thirty", "forty", "fifty",
             "sixty", "seventy", "eighty", "ninety"]
    scales = ["hundred"]
    result = 11  # one thousand length
    for i in range(1, 1000):
        if i < 20:
            result += len(units[i])
        elif i > 19 and i < 100:
            pri = int(str(i)[0])
            seg = int(str(i)[1])
            result += len(tens[pri])
            result += len(units[seg])
        elif i > 99:
            pri = int(str(i)[0])
            seg = int(str(i)[1])
            ter = int(str(i)[2])
            result += len(scales[0]) + len(units[pri]) + 3  # X hundred + AND
            if seg == 1:
                result += len(units[int(str(1) + str(ter))])
            else:
                result += len(tens[seg])
                result += len(units[ter])
            if seg == 0 and ter == 0:
                result += -3  # no AND in 100, 200...
    return result

print ("Sum of digits is {}".format(find_sum()))

import timeit
t = timeit.Timer("find_sum", "from __main__ import find_sum")
print ("Average running time: {} seconds".format(t.timeit(1000)))
