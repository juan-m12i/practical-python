# report.py
#
# Exercise 2.4

import sys
from typing import List, Tuple, Dict, Any, Sequence
import csv
from pprint import pprint

Holding_2 = Tuple[str, int, float]
Holding = Dict[str, Any]



def read_portfolio_dict(filename: str) -> List[Holding]:
    portfolio: List[Holding] = []
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for rowno, row in enumerate(rows, start=1):
            holding: Holding = dict(zip(headers, row))
            portfolio.append(holding)
    return portfolio




def read_prices(filename: str) -> dict:
    prices: dict = {}
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(f)
        for row in rows:
            try:
                prices[row[0]] = float(row[1])
            except Exception as e:
                print("wrong line")
    return prices

def compute_value(portfolio: List[Holding_2], prices: dict) -> float:
    current_value = 0
    for holding in portfolio:
        try:
            current_value += int(holding["shares"]) * prices[holding["name"]]
        except Exception as e:
            print("Missing price for stock %s" % holding["name"])

    return current_value


def make_report(portfolio, prices) -> List[tuple]:
    report: List[tuple] = []
    for holding in portfolio:
        try:
            current_price: float = prices[holding["name"]]
            original_price: float = float(holding["price"])
            price_change: float = (current_price - original_price)
            report.append((holding["name"], int(holding["shares"]), current_price, price_change))
        except Exception as e:
            print("Missing price for stock %s" % holding["name"])
    return report


def portfolio_cost(portfolio: List[Holding]) -> float:
    holding_costs = [int(holding["shares"]) * float(holding["price"]) for holding in portfolio]
    return sum(holding_costs)


def print_report(report: List[tuple]):
    """
    for r in report:
        print('%10s %10d %10.2f %10.2f' % r)
    """
    headers = ('Name', 'Shares', 'Price', 'Change')
    print('%10s %10s %10s %10s' % headers)
    separator = "---------- ---------- ---------- -----------"
    print(separator)
    for name, shares, price, change in report:
        adj_price: str = f'${price:.2f}'
        print(f'{name:>10s} {shares:>10d} {adj_price:>10s} {change:>10.2f}')


if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'
    filename = 'Data/portfoliodate.csv'


prices = read_prices("Data/prices.csv")
# pprint(prices)
portfolio: List[Holding] = read_portfolio_dict(filename)

cost = portfolio_cost(portfolio)
print('Total cost:', cost)

# pprint(portfolio)
portfolio_value = compute_value(portfolio, prices)
print('Portfolio value:', portfolio_value)
report = make_report(portfolio, prices)
print_report(report)







"""



class Position:
    def __init__(self, ticker_name: str, number_of_stocks: int, price_per_stock: float):
        self.ticker_name: str = ticker_name
        self.number_of_stocks: int = number_of_stocks
        self.price_per_stock: float = price_per_stock

    def total_price(self) -> float:
        return self.number_of_stocks * self.price_per_stock


def portfolio_cost(filename: str) -> float:
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(f)
        positions: List[Position] = [get_position_from_line(x) for x in f]
        prices: List[float] = [x.total_price() for x in positions]
        return sum(prices)



def get_position_from_line(line: str) -> Position:
    row = line.rstrip().split(',')
    try:
        return Position(row[0], int(row[1]), float(row[2]))
    except ValueError:
        print("Warning with input: %s" % line, end="")
        return Position(row[0], 0, 0)


def read_portfolio_tuple(filename: str) -> List[Holding_2]:
    portfolio: List[Holding_2] = []
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            holding: Holding_2 = (row[0], int(row[1]), float(row[2]))
            portfolio.append(holding)
    return portfolio


#cost = portfolio_cost(filename)
#print('Total cost:', cost)

"""
