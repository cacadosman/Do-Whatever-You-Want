
import math
import os
import random
import re
import sys

def pickingNumbers(a):
    a.sort()
    maxLenght = 0

    for elmA in a:
        tmpMaxLenght = 0
        for elmA2 in a:
            absDif = abs(elmA-elmA2)
            dif = elmA-elmA2
            if(dif <= 0):
                if absDif <=1 :
                    tmpMaxLenght += 1

        if tmpMaxLenght > maxLenght:
            maxLenght = tmpMaxLenght

    return maxLenght

if __name__ == '__main__':

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    print(str(result) + '\n')

