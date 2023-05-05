#!/usr/bin/python3
"""
In a text file, there is a single character H.
Your text editor can execute only two operations in this file:
Copy All and Paste. Given a number n, write
a method that calculates the fewest number of
operations needed to result in exactly n
H characters in the file.
"""


def minOperations(n):
    num_opr = 0
    min_opr = 2
    while n > 1:
        while n % min_opr == 0:

            num_opr += min_opr
            n /= min_opr
        min_opr += 1
    return num_opr