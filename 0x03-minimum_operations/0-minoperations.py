#!/usr/bin/python3
"""
Operations file for logic
"""

def minOperations(n):
    result = 0
    count = 1
    while n != count:
        if (n % (count + 1)) == 0:
            count = count * 2
        else:
            count = count + 1
        result = result + 1
    return result