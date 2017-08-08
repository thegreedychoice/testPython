#!/bin/python

import sys


def reverse(A, start, end):
    while start < end:
        temp = A[end]
        A[end] = A[start]
        A[start] = temp
        start = start + 1
        end = end - 1


def rotate_left(A, n, k):
    if n < 1 or k < 1:
        return
    else:
        reverse(A, 0, k - 1)
        reverse(A, k, n - 1)
        reverse(A, 0, n - 1)


def rotate_right(A, n, k):
    if n < 1 or k < 1:
        return
    else:
        reverse(A, 0, n - k - 1)
        reverse(A, n - k, n - 1)
        reverse(A, 0, n - 1)


n, k, q = raw_input().strip().split(' ')
n, k, q = [int(n), int(k), int(q)]
a = map(int, raw_input().strip().split(' '))
direction = "right"

if direction == "right":
    rotate_right(a, n, k)
if direction == "left":
    rotate_left(a, n, k)




