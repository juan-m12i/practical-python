# pcost.py

import report
from typing import List
from stock import Stock


def portfolio_cost(filename):
    '''
    Computes the total cost (shares*price) of a portfolio file
    '''
    portfolio: List[Stock] = report.read_portfolio(filename)
    return sum([s.shares * s.price for s in portfolio])


def main(args):
    if len(args) != 2:
        raise SystemExit('Usage: %s portfoliofile' % args[0])
    filename = args[1]
    print('Total cost:', portfolio_cost(filename))


if __name__ == '__main__':
    import sys
    main(sys.argv)
