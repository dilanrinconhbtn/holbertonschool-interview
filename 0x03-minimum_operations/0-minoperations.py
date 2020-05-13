#!/usr/bin/python3
"""
Operations file for logic
"""


def minOperations(n):
    copy = 0
    count = 0
    h = 1

    if type(n) is not int or n <= 1:
        return 0
    else:
        while n != count:
            if h == n:
                return count
            elif (n % h) == 0:
                copy = h
                h = h + copy
                count = count + 2
            else:
                h = h + copy
                count = count + 1
