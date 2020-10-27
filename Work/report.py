# report.py
import csv
from typing import List, Union
import fileparse

DictTuple = Union[dict, tuple]


def read_portfolio(filename: str) -> List[tuple]:
    """
    Read a stock portfolio file into a list of dictionaries with keys
    name, shares, and price.
    """

    with open(filename) as file:
        return fileparse.parse_csv(file, select=['name', 'shares', 'price'], types=[str, int, float])


def read_prices(filename: str) -> dict:
    """
    Read a CSV file of price data into a dict mapping names to prices.
    """
    with open(filename) as file:
        return dict(fileparse.parse_csv(filename, types=[str, float], has_headers=False))


def make_report_data(portfolio: List[DictTuple], prices: dict) -> List[tuple]:
    """
    Make a list of (name, shares, price, change) tuples given a portfolio list
    and prices dictionary.
    """
    rows = []
    for stock in portfolio:
        current_price: float = prices[stock['name']]
        change: float = current_price - stock['price']
        summary = (stock['name'], stock['shares'], current_price, change)
        rows.append(summary)
    return rows


def print_report(reportdata):
    '''
    Print a nicely formated table from a list of (name, shares, price, change) tuples.
    '''
    headers = ('Name', 'Shares', 'Price', 'Change')
    print('%10s %10s %10s %10s' % headers)
    print(('-'*10 + ' ')*len(headers))
    for row in reportdata:
        print('%10s %10d %10.2f %10.2f' % row)


def portfolio_report(portfoliofile: str, pricefile: str):
    '''
    Make a stock report given portfolio and price data files.
    '''
    # Read data files
    portfolio: List[tuple] = read_portfolio(portfoliofile)
    prices: dict = read_prices(pricefile)

    # Create the report data
    report: List[tuple] = make_report_data(portfolio, prices)

    # Print it out
    print_report(report)


def main(args):
    portfolio_report(args[1],
                     args[2])


if __name__ == '__main__':
    import sys
    main(sys.argv)
