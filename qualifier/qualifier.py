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
    def width_of_column(column_index:int) -> int:
        from operator import itemgetter
        column = list( map( itemgetter(column_index), rows ) )
        column = list( map( str, column ) )
        column_width = len(max(column, key=len))
        if labels is not None:
            column_width = max(column_width, len(str(labels[column_index])))
        return column_width
    
    column_widths = [width_of_column(column_index) for column_index in range(len(rows[0]))]
    
    def spaces_in_row(row:list) -> list:
        _spaces = []
        for column_index in range(len(row)):
            column_width = column_widths[column_index]
            cell_content_width = len(str(row[column_index]))
            if centered:
                left_space = ( ( column_width - cell_content_width ) // 2 ) + 1
            else:
                left_space = 1
            right_space = ( column_width - ( cell_content_width + left_space - 1 ) ) + 1
            _spaces.append((left_space, right_space))
        return _spaces
    
    def tablify_row(row:list) -> str:
        table_row = '│'
        for (left_space,right_space),cell in zip(spaces_in_row(row), row):
            table_cell = ' '*left_space + str(cell) + ' '*right_space + '│'
            table_row += table_cell
        table_row += '\n'
        return table_row

    def make_border(first_piece:str, middle_piece:str, last_piece:str):
        _border = ''
        for dash_line in border_dashes:
            _border += dash_line + middle_piece
        _border = first_piece + _border[:-1] + last_piece
        return _border

    border_dashes = ['─'*( width + 2 ) for width in column_widths]
    top_border    = make_border('┌','┬','┐\n')
    bottom_border = make_border('└','┴','┘')

    table = ''+top_border

    if labels is not None:
        label_border = make_border('├','┼','┤\n')
        table += tablify_row(labels) + label_border

    for row in rows:
        table += tablify_row(row)
    
    table += bottom_border

    return table



