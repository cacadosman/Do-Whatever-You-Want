# Cats and a Mouse

## Problem

Two cats and a mouse are at various positions on a line. You will be given their starting positions. Your task is to determine which cat will reach the mouse first, assuming the mouse does not move and the cats travel at equal speed. If the cats arrive at the same time, the mouse will be allowed to move and it will escape while they fight.

## Input Format

The first line contains a single integer, `q`, denoting the number of queries.
Each of the `q` subsequent lines contains three space-separated integers describing the respective values of `x` (cat `A`'s location), `y` (cat `B`'s location), and `z` (mouse `C`'s location).

## Output format

string: Either 'Cat A', 'Cat B', or 'Mouse C'