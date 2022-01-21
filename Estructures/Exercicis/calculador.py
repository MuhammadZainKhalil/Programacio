#!/usr/bin/python3
# -*- coding: utf-8 -*-


import sys
"""
calculadora.py
"""

__author__ = "Zain"

def main(number_1, operation, number_2):
    """
    >>> main(3, '+', 8)
    11
    >>> main(8, '-', 3)
    5
    >>> main(3, '*', 3)
    9
    >>> main(81, '/',9)
    9.0
    """

    if operation == '+':
        return number_1 + number_2

    elif operation == '-':
        return number_1 - number_2

    elif operation == '*':
        return number_1 * number_2

    elif operation == '/':
        return number_1 / number_2

    else:
        print(' Not Valid')


if __name__ == "__main__":
    print (main(int(sys.argv[1]), sys.argv[2], int(sys.argv[3])))