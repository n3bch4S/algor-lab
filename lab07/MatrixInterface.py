from abc import ABC, abstractmethod
from Asserter import assertPosInt
from Interface import NodeInterface


class MatrixInterface(ABC):
    def __init__(self, m: int, n: int) -> None:
        assertPosInt(m)
        assertPosInt(n)

        self.row = m
        self.column = n
        self.matrix: list[list] = []
        for i in range(m):
            self.matrix.append([])
            for j in range(n):
                self.matrix[i].append(0.0)

    def matrixToStr(self) -> str:
        if self.row == 0 or self.column == 0:
            return "No Matrix"

        txt = ""
        nodeList = [x + 1 for x in self.row]
        maxLenNode = Graph.maxLenNode(nodeList)
        maxLenWeigth = Graph.maxLenWeigth(matrix)

        txt = ""
        if maxLenNode == 0:
            return txt
        txt += f" {Graph.fillInCell(' ', maxLenNode)} |{Graph.fillInRow(nodeList, maxLenWeigth)}\n"
        txt += f"-{'-' * maxLenNode}-+{'-' * (maxLenWeigth + 1) * len(nodeList)}\n"
        for node in nodeList:
            rowIdx = nodeList.index(node)
            nodeName = node.name
            txt += f" {Graph.fillInCell(nodeName, maxLenNode)} |{Graph.fillAnyInRow(matrix[rowIdx], maxLenWeigth)}\n"
        return txt

    @staticmethod
    def fillInCell(txt: str, cellSize: int) -> str:
        assertString(txt)
        assertInt(cellSize)

        lenTxt = len(txt)
        if lenTxt > cellSize:
            raise ValueError("Text size is larger than cell")
        diff = cellSize - lenTxt
        return " " * diff + txt

    @staticmethod
    def fillInRow(nodeList: list, cellSize: int) -> str:
        assertList(nodeList)
        assertInt(cellSize)

        txt = ""
        for node in nodeList:
            nodeName = node.name
            txt += f" {Graph.fillInCell(nodeName, cellSize)}"
        return txt

    @staticmethod
    def fillAnyInRow(valueList: list, cellSize: int) -> str:
        assertList(valueList)
        assertInt(cellSize)

        txt = ""
        for value in valueList:
            value = str(value)
            txt += f" {Graph.fillInCell(value, cellSize)}"
        return txt

    @staticmethod
    def maxLenNode(nodeList: list) -> int:
        maxLen = 0
        for node in nodeList:
            name = node.name
            if len(name) > maxLen:
                maxLen = len(name)
        return maxLen

    @staticmethod
    def maxLenWeigth(wMatrix: list) -> int:
        assertList(wMatrix)

        maxLen = 0
        for row in wMatrix:
            for ele in row:
                value = str(ele)
                if len(value) > maxLen:
                    maxLen = len(value)
        return maxLen

    def __str__(self) -> str:
        if self.row == 0 or self.column == 0:
            return "No matrix"

        txt = ""
        for tRow in self.matrix:
            for ele in tRow:
                txt += f"{ele} "
            txt += "\n"
        return txt

    def __repr__(self) -> str:
        return self.__str__()
