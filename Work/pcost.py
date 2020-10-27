# pcost.py

import sys
import csv
from report import read_portfolio


def portfolio_cost(filename):
    '''
    Computes the total cost (shares*price) of a portfolio file
    '''

    portfolio: List[tuple] = read_portfolio(filename)
    return sum([x['shares'] * x['price'] for x in portfolio])


def main(argv):
    if len(argv) == 2:
        filename = sys.argv[1]
    else:
        filename = input('Enter a filename:')
    cost = portfolio_cost(filename)
    print('Total cost:', cost)


if __name__ == '__main__':
    main(sys.argv)


"""
import sys

"""
