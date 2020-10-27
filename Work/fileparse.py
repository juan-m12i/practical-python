# fileparse.py
import csv
from typing import List, Union, Iterable

DictTuple = Union[List, tuple]


def parse_csv(lines: Iterable, select=None, types=None, has_headers=True, delimiter=',', silence_errors=False) -> List[DictTuple]:
    """
    Parse a CSV file into a list of records with type conversion.
    """

    if select and not has_headers:
        raise RuntimeError('select requires column headers')

    rows = csv.reader(lines, delimiter=delimiter)
    headers = next(rows) if has_headers else []

    # If specific columns have been selected, make indices for filtering and set output columns
    if select:
        indices = [headers.index(colname) for colname in select]
        headers = select

    records = []
    for rowno, row in enumerate(rows, 1):
        if not row:     # Skip rows with no data
            continue

        # If specific column indices are selected, pick them out
        if select:
            row = [row[index] for index in indices]

        # Apply type conversion to the row
        if types:
            try:
                row = [func(val) for func, val in zip(types, row)]
            except ValueError as e:
                if not silence_errors:
                    print(f"Row {rowno}: Couldn't convert {row}")
                    print(f"Row {rowno}: Reason {e}")
                continue

        # Make a dictionary or a tuple
        if headers:
            record = dict(zip(headers, row))
        else:
            record = tuple(row)
        records.append(record)

    return records

import gzip
with gzip.open('Data/portfolio.csv.gz', 'rt') as file:
    port = parse_csv(file, types=[str, int, float])

print(port)

lines = ['name,shares,price', 'AA,100,34.23', 'IBM,50,91.1', 'HPE,75,45.1']
port = parse_csv(lines, types=[str, int, float], has_headers=True)

print(port)
