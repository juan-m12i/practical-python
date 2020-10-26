# pcost.py

import csv
from report import read_portfolio


def portfolio_cost(filename):
    '''
    Computes the total cost (shares*price) of a portfolio file
    '''

    portfolio: List[tuple] = read_portfolio(filename)
    return sum([x['shares'] * x['price'] for x in portfolio])

import sys
if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = input('Enter a filename:')

cost = portfolio_cost(filename)
print('Total cost:', cost)
