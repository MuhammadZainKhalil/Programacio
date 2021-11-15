#!/usr/bin/python3
# -*- coding: utf-8 -*-


import sys
"""
lloro.py
"""

__author__ = "Zain"

def main():

    """
    >>> main Hola lloro
    El lloro repeteix: Hola lloro
    L'usuari diu:
    
    """
    entrada = input("L'usuari diu: ")

    while entrada != "":
        print("El lloro repeteix: " + entrada)
        
        entrada = input("L'usuari diu:" )
    print("fins")


if __name__ == "__main__":
    main()