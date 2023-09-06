#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 24 20:21:41 2023

@author: tada
"""
'''import sys
import os

currentDirectory = os.path.dirname(os.path.realpath(__file__))
parentDirectory = os.path.dirname(currentDirectory)
sys.path.append(parentDirectory)'''

import matplotlib.pyplot as plt
import numpy as np
from Useful import Counter, Boolean, plotter
a = []
possible_ham_path=[]
possible_ham_cycleformpath=[]
def pemu(runningNums, templateNums, posibilities, whichPos, isNewPos, counter) :
    counter.counting()
    remain = len(runningNums)
    if remain > 1 :
        counter.counting()
        for i in range(remain) :
            counter.counting()
            if isNewPos.state :
                counter.counting()
                posibilities[whichPos.count] = [x for x in templateNums]
                isNewPos.setState(False)
            selectNum = runningNums.pop(i)
            posibilities[whichPos.count].append(selectNum)
            templateNums.append(selectNum)
            pemu(runningNums, templateNums, posibilities, whichPos, isNewPos, counter)
            runningNums.insert(i, selectNum)
            templateNums.pop()
    elif remain == 1 :
        counter.counting()
        selectNum = runningNums[0]
        posibilities[whichPos.count].append(selectNum)
        posibilities.append([])
        isNewPos.setState(True)
        whichPos.counting()
        
def combi(nums, tempNums, n, posibilities, whichPos, isNewPos, counter) :
    counter.counting()
    remain = len(nums)
    if n > 0 :
        counter.counting()
        for i in range(remain) :
            counter.counting()
            if isNewPos.state :
                counter.counting()
                posibilities[whichPos.count] = [x for x in tempNums]
                isNewPos.setState(False)
            selectNum = nums.pop(i)
            posibilities[whichPos.count].append(selectNum)
            tempNums.append(selectNum)
            combi(nums, tempNums, n - 1, posibilities, whichPos, isNewPos, counter)
            nums.insert(i, selectNum)
            tempNums.pop()
    else :
        counter.counting()
        posibilities.append([])
        isNewPos.setState(True)
        whichPos.counting()
        
def findPath(u, v, matrix, counter) :
    counter.counting()
    n = len(matrix)
    nums = [x for x in range(n) if x != u and x != v]
    tempNums = []
    posibilities = [[]]
    betweenPath = [[]]
    whichPos = Counter()
    isNewPos = Boolean(False)
    
    for i in range(n - 2) :
        counter.counting()
        combi(nums, tempNums, i, betweenPath, whichPos, isNewPos, counter)
    
    whichPos = Counter()
    isNewPos = Boolean(False)
    for middlePath in betweenPath :
        counter.counting()
        pemu(middlePath, tempNums, posibilities, whichPos, isNewPos, counter)
        
    dataframe = {"posible": [],
                 "imposible": [],
                 "betweenPath": [x for x in betweenPath],
                 "posibilities": [x for x in posibilities]}
    for middlePath in posibilities :
        counter.counting()
        middlePath.insert(0, u)
        middlePath.append(v)
        posible = isPathRight(middlePath, matrix, counter)
        if posible :
            counter.counting()
            dataframe["posible"].append(middlePath)
        else :
            counter.counting()
            dataframe["imposible"].append(middlePath)
    return dataframe

def findHamPath(matrix, counter) :
    counter.counting()
    n = len(matrix)
    nums = [x for x in range(n)]
    tempNums = []
    posibilities = [[]]
    whichPos = Counter()
    isNewPos = Boolean(False)
    
    pemu(nums, tempNums, posibilities, whichPos, isNewPos, counter)
    posibilities.pop()
        
    dataframe = {"posible": [],
                 "imposible": [],
                 "posibilities": [x for x in posibilities]}
    for path in posibilities :
        counter.counting()
        posible = isPathRight(path, matrix, counter)
        if posible :
            counter.counting()
            dataframe["posible"].append(path)
        else :
            counter.counting()
            dataframe["imposible"].append(path)
    
    return dataframe

def findHamCycle(matrix, counter) :
    frame = findHamPath(matrix, counter)
    posiblePath = frame["posible"]
    frame["imposibleToBeCycle"] = []
    posible = []
    
    for path in posiblePath :
        start = path[0]
        end = path[-1]
        tempPath = [end, start]
        if not isPathRight(tempPath, matrix, counter) :
            frame["imposibleToBeCycle"].append(path)
        else :
            posible.append(path)
    frame["posible"] = [x for x in posible]
    return frame
    
def isPathRight(path, matrix, counter) :
    #global possible_ham_path
    counter.counting()
    for i in range(len(path) - 1) :
        counter.counting()
        currentNode = path[i]
        nextNode = path[i + 1]
        if matrix[currentNode][nextNode] == 0 :
            counter.counting()
            if len(path)-2 == i:
                a.append(path)
                possible_ham_path.append([path[:-1],[path[-2],path[-1]]])
                possible_ham_cycleformpath.append([path[:-1],[path[-2],path[-1]],[path[-1],path[0]]])
            return False
    return True

def toMatrix(file, sep, counter) :
    counter.counting()
    matrix = []
    for line in file :
        counter.counting()
        adjSet = line.split(sep)
        adjSet = [int(x) for x in adjSet]
        matrix.append(adjSet)
    return matrix

def printMatrix(matrix) :
    for i in matrix :
        print(i)

FILE_NAME = ["Example_LAB2.txt", #0
             "2.1.1.txt", #1
             "2.1.2.txt", #2
             "2.1.3.txt", #3
             "2.1.4.txt", #4
             "2.1.5.txt", #5
             "2.1.6.txt", #6
             "2.1.7.txt", #7
             "2.2.1.txt", #8
             "2.2.2.txt", #9
             "2.2.3.txt", #10
             "2.2.5.txt", #11
             "2.2.6.txt", #12
             "2.2.7.txt"] #13
FILE_SELECTOR = 11
MAX_FILE = 0
SEP = " "
U = 0
V = 2
COUNTER = Counter()
COUNTER_PATH = Counter()
COUNTER_HAM_PATH = Counter()
COUNTER_HAM_CYCLE = Counter()
file = open(FILE_NAME[FILE_SELECTOR], 'r')
matrix = toMatrix(file, SEP, COUNTER)
file.close()
printMatrix(matrix)
data = {}

for i in range(MAX_FILE) :
    COUNTER = Counter()
    COUNTER_PATH = Counter()
    COUNTER_HAM_PATH = Counter()
    COUNTER_HAM_CYCLE = Counter()
    file = open(FILE_NAME[FILE_SELECTOR], 'r')
    matrix = toMatrix(file, SEP, COUNTER)
    file.close()
    printMatrix(matrix)
    
    framePath = findPath(U, V, matrix, COUNTER_PATH)
    frameHamPath = findHamPath(matrix, COUNTER_HAM_PATH)
    frameHamCycle = findHamCycle(matrix, COUNTER_HAM_CYCLE)
    print(COUNTER.count)
    print(COUNTER_PATH.count)
    print(COUNTER_HAM_PATH.count)
    print(COUNTER_HAM_CYCLE.count)
    
framePath = findPath(U, V, matrix, COUNTER_PATH)
frameHamPath = findHamPath(matrix, COUNTER_HAM_PATH)
frameHamCycle = findHamCycle(matrix, COUNTER_HAM_CYCLE)
print(COUNTER.count)
print(COUNTER_PATH.count)
print(COUNTER_HAM_PATH.count)
print(COUNTER_HAM_CYCLE.count)