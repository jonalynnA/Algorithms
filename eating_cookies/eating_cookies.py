#!/usr/bin/python

import sys
import random

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive
# recursive solution


def eating_cookies(n, cache={}):
    if n < 0:
        return 0
    if n <= 1:
        return 1

    if n not in cache:
        cache[n] = eating_cookies(
            n - 1) + eating_cookies(n - 2) + eating_cookies(n - 3)
    return cache[n]


if __name__ == "__main__":
    num_cookies = random.randrange(21)
    if num_cookies > 1:
        #num_cookies = int(sys.argv[1])
        ways = eating_cookies(num_cookies)
        n = num_cookies
        print("\033[97m\nThere are \033[96m{:,d}\033[37m ways for Cookie Monster to eat \033[96m{:,d} cookies\n".format(
            ways, n))
    else:
        print('Usage: eating_cookies.py [num_cookies]')
