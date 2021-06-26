#!/bin/env python3.9
from typing import Any, List, Optional


def make_table(rows: List[List[Any]], labels: Optional[List[Any]] = None, centered: bool = False) -> str:
    """
    :param rows: 2D list containing objects that have a single-line representation (via `str`).
    All rows must be of the same length.
    :param labels: List containing the column labels. If present, the length must equal to that of each row.
    :param centered: If the items should be aligned to the center, else they are left aligned.
    :return: A table representing the rows passed in.
    """
    ...
    def width_of_column(n:int):
        from operator import itemgetter
        if labels is not None:
            rows.insert(0,labels)
        column = list( map( itemgetter(n), rows ) )
        return len(max(column, key=len))
