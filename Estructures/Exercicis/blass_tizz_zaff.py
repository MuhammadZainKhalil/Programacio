#!/usr/bin/python3
# _*_ coding: utf-8 _*_

__author__   = "Muhammad Zain KHalil"
__email__    = "cf19zain.muhammad@iesjoandaustria.org"
__license__  = "GPL V3"

def main(range):

    for f in range(1,111):
    
        if f % 3 == 0:
            print("Blass")
            continue
        elif f % 5 == 0:
            print("Tizz")
            continue
        elif f % 7 == 0:
            print("Zaff")
            continue
        elif f % 3 == 0 and f % 5 == 0:
            print("BlassTizz")
            continue
        elif f % 3 == 0 and f % 7 == 0:
            print("BlassZaff")
            continue
        elif f % 5 == 0 and f % 7 == 0:
            print("TizzZaff")
            continue
        elif f % 3 == 0 and f % 5 == 0 and f % 7 == 0:
            print("BlassTizzZaff")
            continue
        print(f)
if __name__ == "__main__":
    print(main(range))
