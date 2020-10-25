# fileparse.py
#
# Exercise 3.3
# fileparse.py
from typing import List
import csv

def parse_csv(filename: str, select: List['str'] = None, types: list = None, has_headers = True, delimiter: str = ',', silence_errors=False):
    '''
    Parse a CSV file into a list of records
    '''
    with open(filename) as f:
        rows = csv.reader(f, delimiter=delimiter)

        # Read the file headers
        if has_headers:
            headers = next(rows)

        if not has_headers and select:
            raise RuntimeError("select argument requires column headers")

        # If a column selector was given, find indices of the specified columns.
        # Also narrow the set of headers used for resulting dictionaries
        if select:
            indices = [headers.index(colname) for colname in select]
            headers = select
        else:
            indices = []


        records = []
        for idx, row in enumerate(rows):
            if not row:    # Skip rows with no data
                continue
            if types:
                try:
                    row = [func(val) for func, val in zip(types, row)]
                except ValueError as e:
                    if not silence_errors:
                        print("Row %i: Couldn't convert %s" % (idx + 1, row))
                        print("Row %i: Reason invalid literal for int() with base 10: ''" % (idx + 1))
            if has_headers:
                record = dict(zip(headers, row))
            else:
                record = tuple(row)
            records.append(record)

    return records


shares_held = parse_csv('Data/portfolio.csv', select=['name','shares'], types=[str, int])
portfolio = parse_csv('Data/portfolio.dat', types=[str, int, float], delimiter=' ')
portfolio = parse_csv('Data/missing.csv', types=[str, int, float], silence_errors=True)
# prices = parse_csv('Data/prices.csv', types=[str,float], has_headers=False)
# parse_csv('Data/prices.csv', select=['name','price'], has_headers=False)
print(portfolio)

# print(prices)