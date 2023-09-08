#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  5 20:09:33 2023

@author: tada
"""

import sys, os
currentDirectory = os.path.dirname(os.path.realpath(__file__))
parentDirectory = os.path.dirname(currentDirectory)
sys.path.append(parentDirectory)

from DatStrcInNeed import TreasureChest, Set

def concat(x, clctn) :
    for e in clctn :
        e.addItem(x)

def getChange(n, d) :
    buffer = [0 for x in range(n + 1)]
    return (helperGetChange(n, d, buffer), buffer)
                
def helperGetChange(n, d, buffer) :
    savedResult = buffer[n]
    if savedResult != 0 :
        return clneRsltSet(savedResult)
    newSet = Set()
    if n > 0 :
        for i in range(len(d)) :
            coin = d[i]
            if coin <= n :
                subResult = helperGetChange(n - coin, d, buffer)
                concat(coin, subResult)
                newSet = newSet.union(subResult)
        #print(f"get {n}")
        #print(f"give {newSet}")
        buffer[n] = newSet
        return clneRsltSet(newSet)
    newSet.addItem(TreasureChest())
    #print(f"get {n}")
    #print(f"give {newSet}")
    buffer[n] = newSet
    return clneRsltSet(newSet)

def bottomChange(n, d) :
    buffer = [0 for x in range(n + 1)]
    return helperBottomChange(n, d, buffer)

def helperBottomChange(n, d, buffer) :
    for i in range(n + 1) :
        newSet = Set()
        if i > 0:
            canChange = False
            for j in range(len(d)) :
                coin = d[j]
                if coin <= i:
                    subResult = buffer[i - coin]
                    subResult = clneRsltSet(subResult)
                    concat(coin, subResult)
                    newSet = newSet.union(subResult)
                    canChange = True
            if canChange :
                buffer[i] = clneRsltSet(newSet)
            else :
                newSet = Set()
                newSet.addItem(TreasureChest())
                buffer[i] = clneRsltSet(newSet)
        else :
            newSet.addItem(TreasureChest)
            buffer[i] = clneRsltSet(newSet)
    return buffer
        

def minimumChange(n, d) :
    buffer = [0 for x in range(n + 1)]
    return (helperMinimumChange(n, d, buffer), buffer)

def helperMinimumChange(n, d, buffer) :
    savedResult = buffer[n]
    if savedResult != 0 :
        return clneRsltSet(savedResult)
    newSet = Set()
    if n > 0 :
        best = float('inf')
        setOfBest = Set()
        for i in range(len(d)) :
            coin = d[i]
            if coin <= n :
                subResult = helperMinimumChange(n - coin, d, buffer)
                concat(coin, subResult)
                newSet = newSet.union(subResult)
        #print(f"get {n}")
        #print(f"give {newSet}")\
        for chest in newSet :
            chestSize = len(chest)
            if chestSize < best :
                best = chestSize
                setOfBest.reset()
                setOfBest.addItem(chest)
            elif chestSize == best :
                setOfBest.addItem(chest)
        #print(f"get {n}")
        buffer[n] = setOfBest
        return clneRsltSet(setOfBest)
    newSet.addItem(TreasureChest())
    #print(f"get {n}")
    #print(f"give {newSet}")
    buffer[n] = newSet
    return clneRsltSet(newSet)

def clneRsltSet(origSet) :
    newSet = Set()
    for chest in origSet :
        newSet.addItem(chest.clone())
    return newSet

def setToList(origSet) :
    newList = origSet.toList()
    for i in range(len(newList)) :
        chest = newList[i]
        newList[i] = chest.toList()
    return newList

def fileToArg(filename) :
    file = open(filename, 'r')
    n = int(file.readline().strip())
    d = [int(x) for x in file.readline().strip().split()]
    file.close()
    return (n, d)

CASE_FILE = ['4.1.txt', #0
             '4.2.txt', #1
             '4.3.txt', #2
             '4.4.txt', #3
             '4.5.txt', #4
             '4.6.txt', #5
             '4.7.txt', #6
             '4.8.txt', #7
             '4.9.txt', #8
             '4.10.txt', #9
             '4.11.txt', #10
             '4.12.txt', #11
             '4.13.txt', #12
             '4.14(Extra).txt',] #13
SELECT_FILE = 5

n, d = fileToArg(CASE_FILE[SELECT_FILE])
print(f'Amount = {n}\n' +
      f'coins [] = {d}')


print('----------------')
result, resultBuffer = getChange(n, d)
result = setToList(result)
print(f'Ways to make change = {len(result)}\n' +
      str(result) +
      f'\n\nBuffer: {resultBuffer}')



print('----------------')
minResult, minResultBuffer = minimumChange(n, d)
minResult = setToList(minResult)
minNum = len(minResult)
if minNum > 0 :
    print(f'Minimum of Coin is {len(minResult[0])}\n' +
          str(minResult) +
          f'\n\nMinBuffer: {minResultBuffer}')


'''
btmRslt,btmRsltBff = bottomChange(n, d)
'''