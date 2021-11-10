#!/usr/bin/python3
# -*- coding: utf-8 -*-


import sys
"""
salt_de_granota.py
"""

__author__ = "Zain"

def main(inici, final, salt):
    """
    >>> main(10, 18, 2)
    10, 12, 14, 16, 18
    >>> main(10, 17, 2)
    10, 12, 14, 16
    >>> main(18, 10, -2)
    18, 16, 14, 12, 10
    """
    resultat = ''
    for index in range(inici, final, salt):
        resultat =resultat +  ", " + str(index)
    return resultat


if __name__ == "__main__":
    print(main(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])))
