#!/usr/bin/env python3
from abc import ABC
from itertools import combinations


def findAllCover(matrix: list[list[int]], k: int) -> list[list[int]]:
    allCover = []
    nodes = list(range(len(matrix)))
    posibleCover = map(list, combinations(nodes, k))
    posibleCover = list(posibleCover)
    for nodes in posibleCover:
        if isCover(matrix, nodes):
            allCover.append(nodes)
    return allCover


def quickFindCover(matrix: list[list[int]]) -> list[int]:
    nodeNum = len(matrix)
    nodes = list(range(nodeNum))
    subNodes = list(range(nodeNum))
    forbidNodes = []
    for i in nodes:
        if i in forbidNodes:
            continue
        isRowClear = True
        for j in range(i + 1, nodeNum):
            base = matrix[i][j]
            mirror = matrix[j][i]
            if base != 0 and mirror != 0 and j not in forbidNodes:
                forbidNodes.append(j)
            elif base != 0 and mirror == 0:
                isRowClear = False
        if isRowClear:
            subNodes.remove(i)
    return subNodes


def coverFrom(clauseList: list[list[int]]) -> tuple[int, int, list[list[int]]]:
    clauseNum = len(clauseList)
    variableNum, variableList = variableFrom(clauseList)
    nodeNum = 2 * variableNum + 3 * clauseNum
    coverNum = variableNum + 2 * clauseNum

    matrix = initMatrix(nodeNum, nodeNum)
    symRelate(matrix, variableNum)
    trigRelate(matrix, variableNum, clauseNum)
    clauseRelate(
        matrix,
        clauseList,
        variableNum,
        variableList,
    )
    return nodeNum, coverNum, matrix


def variableFrom(matrix: list[list[int]]) -> tuple[int, list[int]]:
    variableList = []
    for row in matrix:
        for num in row:
            if num < 0:
                num *= -1
            if num not in variableList:
                variableList.append(num)
    variableList.sort()
    return len(variableList), variableList


def initMatrix(rowNum: int, colNum: int) -> list[list[int]]:
    matrix = []
    for i in range(rowNum):
        row = []
        for j in range(colNum):
            row.append(0)
        matrix.append(row)
    return matrix


def symRelate(matrix: list[list[int]], variableNum: int) -> None:
    for i in range(variableNum):
        i *= 2
        matrix[i][i + 1] = 1
        matrix[i + 1][i] = 1


def trigRelate(matrix: list[list[int]], variableNum: int, clauseNum: int) -> None:
    startIdx = variableNum * 2
    for i in range(clauseNum):
        i = startIdx + i * 3
        matrix[i][i + 1] = 1
        matrix[i][i + 2] = 1

        matrix[i + 1][i] = 1
        matrix[i + 1][i + 2] = 1

        matrix[i + 2][i] = 1
        matrix[i + 2][i + 1] = 1


def clauseRelate(
    matrix: list[list[int]],
    clauseList: list[list[int]],
    variableNum: int,
    variableList: list[int],
) -> None:
    clauseStartAt = variableNum * 2
    for clauseAt in range(len(clauseList)):
        clause = clauseList[clauseAt]
        for literalAt in range(len(clause)):
            literal = clause[literalAt]
            neg = 1 if literal < 0 else 0
            varAt = variableList.index(literal * -1 if literal < 0 else literal)
            symIdx = varAt * 2 + neg
            clauseIdx = clauseAt * 3 + literalAt + clauseStartAt

            matrix[symIdx][clauseIdx] = 1
            matrix[clauseIdx][symIdx] = 1


def isCover(matrix: list[list[int]], nodes: list[int]) -> bool:
    nodeNum = len(matrix)
    for i in range(nodeNum):
        for j in range(nodeNum):
            if matrix[i][j] != 0 and (i not in nodes and j not in nodes):
                return False
    return True


def inputFromFile1(filename: str) -> tuple[int, list[list[int]]]:
    file = open(filename, "r")
    k = int(file.readline())
    matrix = []
    for line in file:
        row = map(int, line.split())
        matrix.append(list(row))
    file.close()
    return k, matrix


def inputFromFile2(filename: str) -> list[list[int]]:
    file = open(filename, "r")
    matrix = []
    for line in file:
        row = map(int, line.split())
        matrix.append(list(row))
    file.close()
    return matrix


def inputFromFile3(filename: str) -> tuple[int, list[list[int]]]:
    file = open(filename, "r")
    clauseNum = int(file.readline().strip())
    matrix = []
    for line in file:
        clauseList = map(int, line.split())
        clauseList = list(clauseList)
        matrix.append(clauseList)
    file.close()
    return clauseNum, matrix


def matrixToText(matrix: list[list[int]]) -> str:
    txt = ""
    for row in matrix:
        txt += str(row) + "\n"
    return txt


def humanize(
    matrix: list[list[int]],
) -> list[list[int]]:  # human don't count starting from 0
    newMatrix = []
    for row in matrix:
        row = map(lambda x: x + 1, row)
        newMatrix.append(list(row))
    return newMatrix


"""
k, matrix = inputFromFile1("1.ex.txt")
print(f"{k}\n{matrixToText(matrix)}")
allCover = findAllCover(matrix, k)
print(humanize(allCover))
"""
