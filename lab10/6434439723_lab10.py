#!/usr/bin/env python3
from helper import *


def solution1(allCover: list[list[int]]) -> None:
    if len(allCover) > 0:
        print("Yes")
        hmnzCover = humanize(allCover)
        print(matrixToText(hmnzCover))
    else:
        print("No")


def solution2(subNodes: list[int]) -> None:
    subNodes = map(lambda x: x + 1, subNodes)
    subNodes = list(subNodes)
    print(f"{subNodes}\n{len(subNodes)}")


def solution3(nodeNum: int, coverNum: int, matrix: list[list[int]]) -> None:
    print(f"{nodeNum}\n{coverNum}\n{matrixToText(matrix)}")


""" 
FILE_DIR1 = [
    "1.ex1.txt",  # 0
    "1.ex2.txt",  # 1
    "1.1.txt",  # 2
    "1.2.txt",  # 3
    "1.3.txt",  # 4
    "1.4.txt",  # 5
    "1.5.txt",  # 6
]
FILE_SELECTOR1 = 0
k, matrix = inputFromFile1(FILE_DIR1[FILE_SELECTOR1])
print(f"{k}\n{matrixToText(matrix)}")

allCover = findAllCover(matrix, k)
solution1(allCover)
"""

""" 
FILE_DIR2 = [
    "2.ex.txt",  # 0
    "2.1.txt",  # 1
    "2.2.txt",  # 2
    "2.3.txt",  # 3
    "2.4.txt",  # 4
]
FILE_SELECTOR2 = 0
matrix = inputFromFile2(FILE_DIR2[FILE_SELECTOR2])
print(matrixToText(matrix))

subNodes = quickFindCover(matrix)
solution2(subNodes)

allCover = findAllCover(matrix, len(subNodes))
solution1(allCover)
"""

""" 
FILE_DIR3 = [
    "3.ex.txt",  # 0
    "3.1.txt",  # 1
    "3.2.txt",  # 2
    "3.3.txt",  # 3
]
FILE_SELECTOR3 = 0
clauseNum, clauseList = inputFromFile3(FILE_DIR3[FILE_SELECTOR3])
print(f"{clauseNum}\n{matrixToText(clauseList)}")

nodeNum, coverNum, matrix = coverFrom(clauseList)
solution3(nodeNum, coverNum, matrix)

allCover = findAllCover(matrix, coverNum)
solution1(allCover)

subNodes = quickFindCover(matrix)
solution2(subNodes)
"""
