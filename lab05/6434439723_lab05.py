#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 13 20:11:14 2023

@author: tada
"""

from sympy import Point, Line, Triangle, Polygon

#determin all 3 points can construct triangle.
def isTrig(p1: Point, p2: Point, p3: Point) -> bool :
    line = Line(p1, p2)
    return p3 not in line

#return perimeter of triangle (Be caution, all 3 point must be trianglabel!)
def allLength(p1: Point, p2: Point, p3: Point, costBuffer: dict) :
    trig = Triangle(p1, p2, p3)
    if trig in costBuffer :
        return costBuffer[trig]
    
    length = trig.perimeter
    costBuffer[trig] = length
    return length

#return value, point, and polygon of best sub-Polygon.
def bestSubPoly(*pLst: Point, costBuffer: dict, subBuffer: dict) -> dict :
    pLst = list(pLst)
    pNum = len(pLst)
    bestSub = {'length': float('inf'),
               'point': None,
               'poly': None}
    for i in range(pNum) :
        temp = pLst.pop(i)
        subPoly = Polygon(*pLst)
        if subPoly in costBuffer :
            challengeMin = costBuffer[subPoly]
        else :
            challengeMin = minCostTrig(*pLst, costBuffer=costBuffer, subBuffer=subBuffer)
        pLst.insert(i, temp)
        
        if challengeMin is not None and challengeMin < bestSub['length'] :
            bestSub['length'] = challengeMin
            bestSub['point'] = temp
            bestSub['poly'] = subPoly
    return bestSub
            
#return sub-triangle of newly connected polygon with a new point.
def joinPoint(p: Point, *pLst: Point) -> Triangle :
    pLst = list(pLst)
    poly = Polygon(*pLst)
    sides = poly.sides
    sideDis = {}
    for side in sides :
        sideDis[side] = side.distance(p)
        
    minSeg = None
    minDis = float('inf')
    for segment in sideDis :
        if sideDis[segment] < minDis :
            minDis = sideDis[segment]
            minSeg = segment
    pLst = list(minSeg.points)
    pLst.append(p)
    return Triangle(*pLst)
    
#return minimum cost of Triangular in convex point (not support for point, where convex line not pass).
def minCostTrig(*pLst: Point, costBuffer: dict, subBuffer: dict) :
    polygon = Polygon(*pLst)
    if polygon in costBuffer :
        return costBuffer[polygon]
    
    pNum = len(pLst)
    if pNum > 3 :
        bestSub = bestSubPoly(*pLst, costBuffer=costBuffer, subBuffer=subBuffer)
        if bestSub['poly'] == None :
            return None
        bestPoint = bestSub['point']
        bestPoly = bestSub['poly'].vertices
        newTrig = joinPoint(bestPoint, *bestPoly)
        if newTrig == None :
            return None
        
        result = newTrig.perimeter + bestSub['length']
        costBuffer[polygon] = result
        subBuffer[polygon] = bestPoint
        return result
    elif pNum == 3 and isTrig(*pLst) :
        return allLength(*pLst, costBuffer)
    #costBuffer[tuple(pLst)] = float('inf')
    return None

def testResult(pLst: list) -> (int, dict, dict) :
    costBuffer = {}
    subBuffer = {}
    result = minCostTrig(*pLst, costBuffer=costBuffer, subBuffer=subBuffer)
    return (result,costBuffer,subBuffer)

def fileToPoints(filename: str) -> list :
    pLst = []
    file = open(filename, 'r')
    pNum = int(file.readline())
    for i in range(pNum) :
        line = file.readline()
        point = [float(x) for x in line.split()]
        pLst.append(Point(*point))
    return pLst

def simplifyBuffer(buffer: dict) -> None :
    for poly in buffer :
        buffer[poly] = str(buffer[poly])
        
def evalBuffer(buffer: dict) -> None :
    for poly in buffer :
        buffer[poly] = float(buffer[poly].evalf())


CASE_FILE = ['0.0.txt', #0
             '1.1.txt', #1
             '1.2.txt', #2
             '2.1.txt', #3
             '2.2.txt', #4
             '3.txt',   #5
             '4.txt',   #6
             '5 Extra.txt', #7
             '6 Extra.txt'] #8
SELECT_CASE = 3
pLst = fileToPoints(CASE_FILE[SELECT_CASE])
print(str(pLst) + '\n')

result, cost, sub = testResult(pLst)
evalBuffer(cost)
simplifyBuffer(sub)
print('Result: ' + str(result) + ' = ' + str(result.evalf()))