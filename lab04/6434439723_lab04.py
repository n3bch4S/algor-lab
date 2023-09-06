#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  5 20:09:33 2023

@author: tada
"""

def getChange(n, d) :
    if n <= 0 :
        print(f"get {n}")
        print("no need to change")
    else :
        for c in d :
            if c <= n :
                print(f"get {n}")
                print(f"give {c}")
                remain = n - c
                getChange(remain, d)
                
n = 
d = [1,2,3]
getChange(n, d)