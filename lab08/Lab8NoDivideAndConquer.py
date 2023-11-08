#!/usr/bin/env python3
import random


def toint(lst):
    for i in range(len(lst)):
        lst[i] = int(lst[i])


def check(lst):
    for i in range(1, len(lst) - 1):
        x = lst[i]
        dx = 2 * x
        for j in range(0, i):
            if lst[j] < dx and dx - lst[j] < len(lst):
                n = dx - lst[j]

                found = False
                for k in range(0, i):
                    if lst[k] == n:
                        found = True
                if not found:
                    return False
        for j in range(i + 1, len(lst)):
            if lst[j] < dx and dx - lst[j] < len(lst):
                n = dx - lst[j]

                found = False
                for k in range(i + 1, len(lst)):
                    if lst[k] == n:
                        found = True
                if not found:
                    return False
    return True


def solve(lst):
    while check(lst) != True:
        random.shuffle(lst)

    print(lst)


def isSeq(numList: list[int]) -> bool:  # O(n^2)
    n = len(numList)
    if n < 3:
        return True
    for i in range(1, n - 1):
        limit = min(i, n - i - 1)
        for j in range(1, limit + 1):
            left = numList[i - j]
            right = numList[i + j]
            middle = numList[i] * 2
            if left + right == middle:
                print(f"left: {left}, middle: {middle}, right: {right}")
                return False
    return True


x = list(range(16))
solve(x)
print(isSeq(x))
