# Picking Numbers

## Problem

Given an array of integers, find the longest subarray where the absolute difference between any two elements is less than or equal to `1`.

## Input

The first line contains a single integer `n`, the size of the array `a`.
The second line contains `n` space-separated integers, each an `a[i]`.

## Output

int: the length of the longest subarray that meets the criterion

## Example
`a=[1,1,2,2,4,4,5,5,5]`
There are two subarrays meeting the criterion: `[1,1,2,2]` and `[4,4,5,5,5]`. The maximum length subarray has `5` elements.