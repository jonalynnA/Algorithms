#!/usr/bin/python

import argparse


def find_max_profit(prices):
    bought_price = 0
    sold_price = 0
    max_profit = 0

    for i in range(len(prices)-1):

        if bought_price == 0 and prices[i] < prices[i+1]:
            bought_price = prices[i]

        elif bought_price != 0 and prices[i] > prices[i+1]:
            if sold_price < prices[i]:
                sold_price = prices[i]

    if bought_price == 0:
        bought_price = prices[-1]
    max_profit = sold_price - bought_price
    global buy
    buy = prices.index(bought_price)
    global sell
    sell = prices.index(sold_price)
    return max_profit


prices = ([10, 7, 5, 8, 11, 9])
profit = find_max_profit(prices)

print(
    f"\nA profit of \033[92m${profit}\033[37m can be made from the stock prices {prices}.\n\033[94mBuy on day: {buy}\033[37m. \n\033[94mSell on day {sell}\033[37m\n")


""" if __name__ == '__main__':
    # This is just some code to accept inputs from the command line
    parser = argparse.ArgumentParser(
        description='Find max profit from prices.')
    parser.add_argument('integers', metavar='N', type=int,
                        nargs='+', help='an integer price')
    args = parser.parse_args()

    print("A profit of ${profit} can be made from the stock prices {prices}.".format(
        profit=find_max_profit(args.integers), prices=args.integers)) """
