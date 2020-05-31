# pcost.py
#
# Exercise 1.27
import sys
from typing import List
import csv

class Position:
    def __init__(self, ticker_name: str, number_of_stocks: int, price_per_stock: float):
        self.ticker_name: str = ticker_name
        self.number_of_stocks: int = number_of_stocks
        self.price_per_stock: float = price_per_stock

    def total_price(self) -> float:
        return self.number_of_stocks * self.price_per_stock


def get_position_from_line(line: str) -> Position:
    row = line.rstrip().split(',')
    try:
        return Position(row[0], int(row[1]), float(row[2]))
    except ValueError:
        print("Warning with input: %s" % line, end="")
        return Position(row[0], 0, 0)


def portfolio_cost(filename):
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(f)
        positions: List[Position] = [get_position_from_line(x) for x in f]
        prices: List[float] = [x.total_price() for x in positions]
        return sum(prices)

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

cost = portfolio_cost(filename)
print('Total cost:', cost)


