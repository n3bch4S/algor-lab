#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 22 14:47:02 2023

@author: tada

in asymtotic notation, |C| mean number of connected node
"""
from typing import Any, Type
from Interface import NodeInterface, GraphInterface


class Node(NodeInterface):
    def __init__(self, num: int) -> None:  # O(1)
        assertInt(num)

        super().__init__(num)

    def leadTo(self, other: NodeInterface) -> bool:  # O(C^3)
        Node.assertNode(other)

        if other not in self.toThe and self not in other.fromThe:
            self.toThe.append(other)
            self.toThe.sort()
            other.fromThe.append(self)
            other.fromThe.sort()

            self.outDeg += 1
            other.inDeg += 1

            self.noteCanTo(other)
            other.noteCanFrom(self)
            return True
        return False

    def unLeadTo(self, other: NodeInterface) -> bool:  # O(C^3)
        Node.assertNode(other)

        if other in self.toThe and self in other.fromThe:
            self.toThe.remove(other)
            other.fromThe.remove(self)

            self.outDeg -= 1
            other.inDeg -= 1

            self.noteCantTo(other)
            other.noteCantFrom(self)
            return True
        return False

    def comeFrom(self, other: NodeInterface) -> bool:  # O(C^3)
        Node.assertNode(other)

        if other not in self.fromThe and self not in other.toThe:
            self.fromThe.append(other)
            self.fromThe.sort()
            other.toThe.append(self)
            other.toThe.sort()

            self.inDeg += 1
            other.outDeg += 1

            self.noteCanFrom(other)
            other.noteCanTo(self)
            return True
        return False

    def unComeFrom(self, other: NodeInterface) -> bool:  # O(C^3)
        Node.assertNode(other)

        if other in self.fromThe and self in other.toThe:
            self.fromThe.remove(other)
            other.toThe.remove(self)

            self.inDeg -= 1
            other.outDeg -= 1

            self.noteCantFrom(other)
            other.noteCantTo(self)
            return True
        return False

    def noteCanTo(self, other: NodeInterface) -> bool:  # O(C^3)
        Node.assertNode(other)

        if other not in self.canTo:
            self.canTo.append(other)

            for canTo in other.canTo:
                if canTo not in self.canTo:
                    self.canTo.append(canTo)
            self.canTo.sort()

            for follower in self.fromThe:
                follower.noteCanTo(other)

            self.buildHomie()
            return True
        return False

    def noteCantTo(self, other: NodeInterface) -> bool:  # O(C^3)
        Node.assertNode(other)

        for candidate in self.toThe:
            if candidate == other or other in candidate.canTo:
                return False

        if other in self.canTo:
            self.canTo.remove(other)

            for candidate in other.canTo:
                self.noteCantTo(candidate)

            for follower in self.fromThe:
                follower.noteCantTo(other)

            self.buildHomie()
            return True
        return False

    def noteCanFrom(self, other: NodeInterface) -> bool:  # O(C^3)
        Node.assertNode(other)

        if other not in self.canFrom:
            self.canFrom.append(other)

            for canFrom in other.canFrom:
                if canFrom not in self.canFrom:
                    self.canFrom.append(canFrom)

            self.canFrom.sort()

            for leader in self.toThe:
                leader.noteCanFrom(other)

            self.buildHomie()
            return True
        return False

    def noteCantFrom(self, other: NodeInterface) -> bool:  # O(C^3)
        Node.assertNode(other)

        for candidate in self.fromThe:
            if candidate == other or other in candidate.canFrom:
                return False

        if other in self.canFrom:
            self.canFrom.remove(other)

            for candidate in other.canFrom:
                self.noteCantFrom(candidate)

            for leader in self.toThe:
                leader.noteCantFrom(other)

            self.buildHomie()
            return True
        return False

    def buildHomie(self) -> None:  # O(C^2)
        self.allHomie = []
        self.homieName = ""
        for canFrom in self.canFrom:
            if canFrom in self.canTo:
                self.allHomie.append(canFrom)

        if self not in self.allHomie:
            self.allHomie.append(self)
            self.allHomie.sort()

        for node in self.allHomie:
            self.homieName += node.name

    def __str__(self) -> str:  # O(C)
        txt = ""
        txt += f"{[x.name for x in self.fromThe]} -> {self.name} -> {[x.name for x in self.toThe]}\n"
        txt += f"{[x.name for x in self.canFrom]} ->> {self.name} ->> {[x.name for x in self.canTo]}\n"
        txt += f"num: {self.num}, in: {self.inDeg}, out: {self.outDeg}, homie: {self.homieName}{[x.name for x in self.allHomie]}\n"
        txt += f"color: {self.color}, discovered: {self.d}, finished: {self.f}, pi: {self.pi}\n"
        return txt

    def __repr__(self) -> str:  # O(C)
        return self.__str__()

    def __hash__(self) -> int:  # O(1)
        return self.num

    def __lt__(self, other: NodeInterface) -> bool:  # O(1)
        Node.assertNode(other)

        return self.num < other.num

    def __le__(self, other: NodeInterface) -> bool:  # O(1)
        Node.assertNode(other)

        return self.num <= other.num

    def __eq__(self, other: NodeInterface) -> bool:  # O(1)
        Node.assertNode(other)

        return self.num == other.num

    def __ne__(self, other: NodeInterface) -> bool:  # O(1)
        Node.assertNode(other)

        return self.num != other.num

    def __gt__(self, other: NodeInterface) -> bool:  # O(1)
        Node.assertNode(other)

        return self.num > other.num

    def __ge__(self, other: NodeInterface) -> bool:  # O(1)
        Node.assertNode(other)

        return self.num >= other.num

    @staticmethod
    def assertNode(x: Any) -> None:  # O(1)
        if type(x) != Node:
            raise TypeError("This parameter is not Node")

    @staticmethod
    def assertEmptyNode(node: NodeInterface) -> None:
        Node.assertNode(node)

        if node.inDeg > 0 or node.outDeg > 0:
            raise ValueError("This node is not empty (has connection)")


""" """


class Graph(GraphInterface):
    def __init__(self, name: str) -> None:  # O(1)
        assertString(name)

        super().__init__(name)

    def addNode(self, node: NodeInterface) -> bool:
        Node.assertNode(node)
        Node.assertEmptyNode(node)

        if node not in self.nodes:
            self.nodes.append(node)
            self.nodes.sort()
            self.nodeNum += 1

            i = self.nodes.index(node)
            for row in self.wMatrix:
                row.insert(i, float("inf"))
            newRow = [float("inf") for x in self.nodes]
            self.wMatrix.insert(i, newRow)
            return True
        return False

    def addEdge(
        self, u: NodeInterface, v: NodeInterface, distance: float, twoSide: bool
    ) -> bool:
        Node.assertNode(u)
        Node.assertNode(v)
        assertFloat(distance)
        assertBoolean(twoSide)

        if u not in self.nodes:
            self.addNode(u)
        if v not in self.nodes:
            self.addNode(v)

        i = self.nodes.index(u)
        u = self.nodes[i]
        j = self.nodes.index(v)
        v = self.nodes[j]
        oldValue = self.wMatrix[i][j]
        if distance < oldValue:
            u.leadTo(v)
            self.wMatrix[i][j] = distance
            self.edgeNum += 1
            if twoSide:
                v.leadTo(u)
                self.wMatrix[j][i] = distance
                self.edgeNum += 1
            return True
        return False

    def buildComponent(self) -> bool:
        for node in self.nodes:
            allHomie = node.allHomie
            homieNode = Node(int(node.homieName))
            if homieNode not in self.components:
                self.components.append(homieNode)
                self.compNum += 1
            else:
                i = self.components.index(homieNode)
                homieNode = self.components[i]

            for memberNode in allHomie:
                for suspect in memberNode.toThe:
                    if suspect not in allHomie:
                        outerHomieNode = Node(int(suspect.homieName))
                        if outerHomieNode not in self.components:
                            self.components.append(outerHomieNode)
                            self.compNum += 1
                        else:
                            i = self.components.index(outerHomieNode)
                            outerHomieNode = self.components[i]
                        homieNode.leadTo(outerHomieNode)

    def FWAllPair(self):
        pass

    def __invert__(self) -> None:
        pass

    def __str__(self) -> str:
        txt = f"___Graph {self.name}___\n\n"

        txt += "---Node detail---\n"
        txt += f"{self.nodes}\n\n"

        txt += "---Adjacency Matrix---\n"
        txt += f"{Graph.matrixToText(self.wMatrix, self.nodes)}\n\n"
        # txt += f"{Graph.matrixToText(self.minWeightMatrix, self.nodes)}\n\n"
        # txt += f"{Graph.matrixToText(self.piMatrix, self.nodes)}\n\n"

        txt += "---Graph components---\n"
        txt += f"{self.components}\n\n"

        txt += "---Property of graph---\n"
        txt += (
            f"nodeNum: {self.nodeNum}, edgeNum: {self.edgeNum}, compNum: {self.compNum}"
        )
        return txt

    def __repr__(self) -> str:
        return self.__str__()

    def __eq__(self, other):
        pass

    def __ne__(self, other):
        pass

    def __hash__(self):
        pass

    @staticmethod
    def matrixToText(matrix: list, nodeList: list) -> str:
        assertList(matrix)
        assertList(nodeList)

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
        assertList(nodeList)

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


"""
   | 1   2   3   4   5 ---> ele-width = 1 + max-len-value
---+-------------------
 1 | 32.3  13.4  23  32  32 ---> cell-width = 1 + max-len-value
 2 |
 3 |
 4 |
 5 |
 ele-width = 1 + max-len-ele + 1
"""


""" """


def assertString(x: Any) -> None:  # O(1)
    if type(x) != str:
        raise TypeError("This parameter is not string")


def assertInt(x: Any) -> None:
    if type(x) != int:
        raise TypeError("This parameter is not integer")


def assertFloat(x: Any) -> None:  # O(1)
    if type(x) != float:
        raise TypeError("This parameter is not float")


def assertBoolean(x: Any) -> None:
    if type(x) != bool:
        raise TypeError("This parameter is not boolean")


def assertList(x: Any) -> None:
    if type(x) != list:
        raise TypeError("This parameter is not list")


a = Graph("a")
a.addEdge(Node(1), Node(2), 3.0, False)
a.addEdge(Node(2), Node(3), 4.0, False)
a.addEdge(Node(3), Node(4), 5.0, False)
a.addEdge(Node(4), Node(5), 6.0, False)
a.addEdge(Node(5), Node(3), 8.0, False)

a.buildComponent()
print(a)
