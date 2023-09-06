#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 30 14:36:05 2023

@author: tada
"""

from Useful import Counter, Boolean

GRAB = "G"
PASSENGER = "P"

class Pair :
    def __init__(self, u, v) :
        self.u = u
        self.v = v
        
    def clone(self) :
        return Pair(self.u, self.v)
    
    def toTuple(self) :
        return (self.u, self.v)

def genPair(arr, k) :
    n = len(arr)
    pairList = []
    for i in range(n) :
        for j in range(i, n) :
            pair = Pair(i, j)
            if canPair(arr, pair) and not tooFar(pair, k) :
                pairList.append(Pair(i, j))
    return pairList

def c(arr, r) :
    cArr = [[]]
    cI = Counter(0)
    newLine = Boolean(True)
    helperC(arr, r, cArr, cI=cI, newLine=newLine)
    cArr.pop()
    return cArr

def helperC(arr, r, cArr, srtIdx = 0, tArr = [], cI = Counter(), newLine = Boolean()) :
    if r > 0 :
        n = len(arr) - r + 1
        for i in range(srtIdx, n) :
            if newLine.state :
                cArr[cI.count] = [x for x in tArr]
                newLine.setState(False)
            e = arr[i]
            cArr[cI.count].append(e)
            tArr.append(e)
            r -= 1
            helperC(arr, r, cArr, i + 1, tArr, cI, newLine)
            e = tArr.pop()
            #arr.insert(i, e)
            r += 1
    else :
        cI.counting()
        cArr.append([])
        newLine.setState(True)
        
def canPair(grabMap, pair) :
    u = grabMap[pair.u].lower()
    v = grabMap[pair.v].lower()
    case1 = u == GRAB.lower() and v == PASSENGER.lower()
    case2 = u == PASSENGER.lower() and v == GRAB.lower()
    return case1 or case2

def tooFar(pair, k) :
    u = pair.u
    v = pair.v
    distance = u - v if u >= v else v - u
    return distance > k
        
def canGrab(grabMap, k, pairArr) :
    pairNum = len(pairArr)
    if pairNum < 1 :
        return False
    counted = []
    for i in range(pairNum) :
        pair = pairArr[i]
        u = pair.u
        v = pair.v
        if u in counted or v in counted :
            return False
        counted += [u, v]
    return True

def timeStoneGrab(arr, k) :
    n = len(arr) // 2
    allPairs = genPair(arr, k)
    
    grabable = {}
    for maxPair in range(n, 0, -1) :
        cPairs = c(allPairs, maxPair)
        cNum = len(cPairs)
        dictPointer = f"{maxPair} pairs"
        grabable[dictPointer] = []
        for i in range(cNum) :
            pairArr = cPairs[i]
            if canGrab(arr, k, pairArr) :
                x = [x.toTuple() for x in pairArr]
                #print(x)
                grabable[dictPointer] += [x]
    return grabable

def hungryGrab(arr, k, howtoFind) :
    grab = GRAB.lower()
    pairList = []
    selectedPassenger = []
    n = len(arr)
    for i in range(n) :
        e = arr[i]
        if e.lower() == grab :
            j = howtoFind(arr, i, k, selectedPassenger)
            if i != j :
                pairList.append((i, j))
                selectedPassenger.append(j)
                
    return pairList

def hungryGrab2(arr, k, howtoFind) :
    grab = GRAB.lower()
    pairList = []
    selectedPassenger = []
    n = len(arr)
    drcs = [-1, 1]
    for grbIdx in range(n // 2 + 1) :
        for drc in drcs :
            i = grbIdx if drc == -1 else n - grbIdx - 1
            e = arr[i]
            if e.lower() == grab :
                j = howtoFind(arr, i, k, selectedPassenger)
                if i != j :
                    pairList.append((i, j))
                    selectedPassenger.append(j)
                
    return pairList
        
def spnCirLeft(arr, grb, k, selectedPassenger) :
    n = len(arr)
    drcts = [-1, 1]
    for step in range(1, k):
        for drct in drcts :
            pnt = grb + step * drct
            if pnt >= n or pnt < 0:
                continue
            pick = arr[pnt].lower()
            if pick == PASSENGER.lower() and pnt not in selectedPassenger :
                return pnt
    return grb

def spnCirRight(arr, grb, k, selectedPassenger) :
    n = len(arr)
    drcts = [1, -1]
    for step in range(1, k):
        for drct in drcts :
            pnt = grb + step * drct
            if pnt >= n or pnt < 0:
                continue
            pick = arr[pnt].lower()
            if pick == PASSENGER.lower() and pnt not in selectedPassenger :
                return pnt
    return grb

def spnRadLeft(arr, grb, k, selectedPassenger) :
    n = len(arr)
    drcts = [-1, 1]
    for drct in drcts:
        for step in range(1, k) :
            pnt = grb + step * drct
            if pnt >= n or pnt < 0:
                continue
            pick = arr[pnt].lower()
            if pick == PASSENGER.lower() and pnt not in selectedPassenger :
                return pnt
    return grb

def spnRadRight(arr, grb, k, selectedPassenger) :
    n = len(arr)
    drcts = [1, -1]
    for drct in drcts:
        for step in range(1, k) :
            pnt = grb + step * drct
            if pnt >= n or pnt < 0:
                continue
            pick = arr[pnt].lower()
            if pick == PASSENGER.lower() and pnt not in selectedPassenger :
                return pnt
    return grb

def impCirLeft(arr, grb, k, selectedPassenger) :
    n = len(arr)
    drcts = [-1, 1]
    for step in range(k, 0, -1) :
        for drct in drcts :
            pnt = grb + step * drct
            if pnt >= n or pnt < 0:
                continue
            pick = arr[pnt].lower()
            if pick == PASSENGER.lower() and pnt not in selectedPassenger :
                return pnt
    return grb

def impCirRight(arr, grb, k, selectedPassenger) :
    n = len(arr)
    drcts = [1, -1]
    for step in range(k, 0, -1) :
        for drct in drcts :
            pnt = grb + step * drct
            if pnt >= n or pnt < 0:
                continue
            pick = arr[pnt].lower()
            if pick == PASSENGER.lower() and pnt not in selectedPassenger :
                return pnt
    return grb

def impRadLeft(arr, grb, k, selectedPassenger) :
    n = len(arr)
    drcts = [-1, 1]
    for drct in drcts :
        for step in range(k, 0, -1) :
            pnt = grb + step * drct
            if pnt >= n or pnt < 0:
                continue
            pick = arr[pnt].lower()
            if pick == PASSENGER.lower() and pnt not in selectedPassenger :
                return pnt
    return grb

def impRadRight(arr, grb, k, selectedPassenger) :
    n = len(arr)
    drcts = [1, -1]
    for drct in drcts :
        for step in range(k, 0, -1) :
            pnt = grb + step * drct
            if pnt >= n or pnt < 0:
                continue
            pick = arr[pnt].lower()
            if pick == PASSENGER.lower() and pnt not in selectedPassenger :
                return pnt
    return grb

def fileToCase(fileName) :
    file = open(fileName, 'r')
    grabMap = [x for x in file.readline().strip()]
    print(grabMap)
    k = int(file.readline().strip())
    print(k)
    file.close()
    return Pair(grabMap, k)
        
fileCase = ["3.1.1.txt", #0
            "3.1.2.txt", #1
            "3.1.3.txt", #2
            "3.2.1.txt", #3
            "3.2.2.txt", #4
            "3.2.3.txt", #5
            "3.3.1.txt", #6
            "3.3.2.txt", #7
            "3.3.3.txt", #8
            "3.4.1.txt", #9
            "3.4.2.txt", #10
            "3.4.3.txt", #11
            "3.4.4.txt", #12
            "3.4.5.txt", #13
            "3.5.1.txt", #14
            "3.5.2.txt", #15
            "3.5.3.txt",] #16

testCase = [Pair(["G", "P", "P", "G", "P"], 1),
    Pair(["P", "P", "G", "G", "P", "G"], 2),
    Pair(["G", "P", "G", "P", "P", "G", "G", "G", "G", "G", "G", "G", "G", "G"], 3),
    Pair(["G", "P"], 1)]

SELECT_CASE = 12
#pair = testCase[SELECT_CASE]
pair = fileToCase(fileCase[SELECT_CASE])

#solBF = timeStoneGrab(pair.u, pair.v)

solscl = hungryGrab(pair.u, pair.v, spnCirLeft)
solscr = hungryGrab(pair.u, pair.v, spnCirRight)
solsrl = hungryGrab(pair.u, pair.v, spnRadLeft)
solsrr = hungryGrab(pair.u, pair.v, spnRadRight)
solicl = hungryGrab(pair.u, pair.v, impCirLeft)
solicr = hungryGrab(pair.u, pair.v, impCirRight)
solirl = hungryGrab(pair.u, pair.v, impRadLeft)
solirr = hungryGrab(pair.u, pair.v, impRadRight)

solscl2 = hungryGrab2(pair.u, pair.v, spnCirLeft)
solscr2 = hungryGrab2(pair.u, pair.v, spnCirRight)
solsrl2 = hungryGrab2(pair.u, pair.v, spnRadLeft)
solsrr2 = hungryGrab2(pair.u, pair.v, spnRadRight)
solicl2 = hungryGrab2(pair.u, pair.v, impCirLeft)
solicr2 = hungryGrab2(pair.u, pair.v, impCirRight)
solirl2 = hungryGrab2(pair.u, pair.v, impRadLeft)
solirr2 = hungryGrab2(pair.u, pair.v, impRadRight)