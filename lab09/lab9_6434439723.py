#!/usr/bin/env python3


def getPrefixFunction(p: list[str]) -> list[int]:
    print(f"getPrefixFunction has been called")
    m = len(p)
    pi = [0 for x in range(m)]
    k = 0
    for q in range(1, m):
        print(f"k: {k}, q: {q}")
        while k > 0 and p[k] != p[q]:
            print(f"p[k] != p[q]")
            k = pi[k - 1]
        if p[k] == p[q]:
            print(f"p[k] == p[q]")
            k += 1
        pi[q] = k
    print("returning pi")
    return pi


# [0,1,2,3,4,5,6,7,8,9] n-(i-m+1)+1 = n-i+m - 2


def kmp(t: list[str], p: list[str], reversed: bool) -> list[int]:
    print(f"kmp has been called")
    n = len(t)
    m = len(p)
    print(f"calling getPrefixFunction")
    pi = getPrefixFunction(p)
    q = 0
    occurs = []
    print(f"searching")
    for i in range(n):
        print(f"q: {q}, i: {i}")
        while q > 0 and p[q] != t[i]:
            print(f"p[q] != t[i]")
            q = pi[q - 1]
        if p[q] == t[i]:
            print(f"p[q] == t[i]")
            q += 1
        if q == m:
            if reversed:
                foundAt = n + m - i - 1
            else:
                foundAt = i - m + 2
            print(f"Pattern occur with shift {foundAt}")
            occurs.append(foundAt)
            q = pi[q - 1]
    return occurs


def naiveSearch(text: list[str], pattern: list[str], reversed: bool) -> list[int]:
    print(f"naiveSearch has been called")
    occurs = []
    m = len(pattern)
    n = len(text)
    print(f"searching")
    for patternStartAt in range(n - m + 1):
        charAt = 0
        print(f"patternStartAt: {patternStartAt}, charAt: {charAt}")
        while charAt < m and pattern[charAt] == text[patternStartAt + charAt]:
            print(
                f"charAt{charAt} < {m} and {pattern[charAt]} == {text[patternStartAt + charAt]}"
            )
            charAt += 1
        if charAt == m:
            if reversed:
                foundAt = n - patternStartAt
            else:
                foundAt = patternStartAt + 1
            print(f"Pattern occur with shift {foundAt}")
            occurs.append(foundAt)
    print("returning occurs")
    return occurs


# [0,1,2,3,4,5]


def toListTable(stringList: list[str]) -> str:
    size = len(stringList)
    idx = [str(x + 1) for x in range(size)]
    cellWidth = max(maxElementLength(stringList), maxElementLength(idx)) + 1
    txt = f"index: {fillList(idx, cellWidth)}\n"
    txt += f"string:{fillList(stringList, cellWidth)}"
    return txt


def fillCell(text: str, cellWidth: int) -> str:
    if len(text) < cellWidth:
        spaceLeft = cellWidth - len(text)
        text += " " * spaceLeft
    return text


def fillList(stringList: list[str], cellWidth: int) -> str:
    txt = "["
    for str in stringList:
        txt += fillCell(str, cellWidth)
    txt += "]"
    return txt


def maxElementLength(stringList: list[str]) -> int:
    maxLength = 0
    for str in stringList:
        length = len(str)
        if length > maxLength:
            maxLength = length
    return maxLength


def initData(filename: str) -> tuple[list[str], int, int, list[str], list[str]]:
    print(f"opening {filename}")
    file = open(filename, "r")

    print(f"reading data")
    sigma = file.readline().strip().split()
    line = file.readline().strip().split()
    m = int(line[0])
    n = int(line[1])
    pattern = file.readline().strip().split()
    text = file.readline().strip().split()

    print(f"closing {filename}")
    file.close()
    return sigma, m, n, pattern, text


def successor(x: int) -> int:
    return x + 1


FILE_DIRECTORY = [
    "ex.txt",  # 0
    "9.1.txt",  # 1
    "9.2.txt",  # 2
    "9.3.txt",  # 3
    "9.4.txt",  # 4
]
FILE_SELECTOR = 0
sigma, m, n, pattern, text = initData(FILE_DIRECTORY[FILE_SELECTOR])
print(f"sigma: {sigma}, m: {m}, n: {n}")
print(f"pattern: {pattern}")
print(f"text: {text}")

occursLR = kmp(text, pattern, reversed=False)
print(f"occursLR: {occursLR}")
naiveOccursLR = naiveSearch(text, pattern, reversed=False)
print(f"naive-occursLR: {naiveOccursLR}")

textReversed = text[::-1]
print(f"text-reversed: {textReversed}")

occursRL = kmp(textReversed, pattern, reversed=True)
print(f"occursRL: {occursRL}")
naiveOccursRL = naiveSearch(textReversed, pattern, reversed=True)
print(f"naive-occursRL: {naiveOccursRL}")

print("#################################")
print(f"sigma: {sigma}, m: {m}, n: {n}")
print(f"pattern: {pattern}")
print(f"{toListTable(text)}")
print(f"occursLR: {occursLR}")
print(f"occursRL: {occursRL}")
print(f"naive-occursLR: {naiveOccursLR}")
print(f"naive-occursRL: {naiveOccursRL}")
