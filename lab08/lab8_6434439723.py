#!/usr/bin/env python3
import itertools

# permutations = list(itertools.permutations(elements))


def getSeq(n: int) -> list[int]:
    numList = [x for x in range(n + 1)]
    seq = []
    fillSeq(seq, numList)
    return seq


def fillSeq(
    target: list[int], numList: list[int]
) -> None:  # T(n) = 2T(n/2) + n -> O(n * log n)
    n = len(numList)
    if n > 1:
        even = []
        odd = []
        for i in range(n):
            if i % 2 == 0:
                even.append(numList[i])
            else:
                odd.append(numList[i])
        fillSeq(target, even)
        fillSeq(target, odd)
    elif n == 1:
        target.append(numList[0])


def getSeqSlide(n: int) -> list[int]:
    numList = [x for x in range(n + 1)]
    slide(numList, n)
    return numList


def slide(numList: list[int], n: int) -> None:
    print(numList)
    for i in range(n):
        for j in range(i + 1, n + 1):
            a = numList[i]
            b = numList[j]
            # print(f"n[{i}]: {a}, n[{j}]: {b}")
            if goodPair(a, b):
                compairAndSlide(numList, i, j)


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


def goodPair(n: int, m: int) -> bool:
    return (n + m) % 2 == 0


def compairAndSlide(numlist: list[int], i: int, j: int) -> None:
    a = numlist[i]
    b = numlist[j]
    avg = (a + b) // 2
    k = numlist.index(avg)
    if k >= 0 and i < k < j:
        b = numlist.pop(j)
        numlist.insert(k, b)


n = 18
print(n)
seq = getSeq(n)
print(f"{seq}, {min(seq)}-{max(seq)}, {isSeq(seq)}\n")

seq = getSeqSlide(n)
while not isSeq(seq):
    slide(seq, n)
print(f"{seq}, {min(seq)}-{max(seq)}, {isSeq(seq)}\n")
