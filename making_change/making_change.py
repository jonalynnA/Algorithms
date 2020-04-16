#!/usr/bin/python

import sys
import random


def making_change(amount, denominations):
  pass


if __name__ == "__main__":
    # Test our your implementation from the command line
    # with `python making_change.py [amount]` with different amounts
    amount = random.randrange(300)
    if amount > 1:
        denominations = [1, 5, 10, 25, 50]
        amount = amount
        ways = making_change(amount, denominations)
        print("\nThere are \033[92m{:,d}\033[37m ways to make \033[92m{amount}\033[37m cents.\n".format(
            ways, amount=amount))
    else:
        print("Usage: making_change.py [amount]")
