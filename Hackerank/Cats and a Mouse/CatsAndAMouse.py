
import os
import sys


def catAndMouse(x, y, z):
    distanceA = abs(x-z)
    distanceB = abs(y-z)
    winner = min(distanceA,distanceB)

    if distanceA == distanceB:
        return "Mouse C"

    if winner == distanceA:
        return "Cat A"
    else:
        return "Cat B"

if __name__ == '__main__':
    
    q = int(input())

    for q_itr in range(q):
        xyz = input().split()

        x = int(xyz[0])

        y = int(xyz[1])

        z = int(xyz[2])

        result = catAndMouse(x, y, z)

        print(result + '\n')
