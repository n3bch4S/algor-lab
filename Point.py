#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 13 16:02:46 2023

@author: tada
"""

class Point :
    def __init__(self, *axsVal) :
        self.axsVal = [val for val in axsVal]
        self.dimension = len(self.axsVal)
        
    def __str__(self) :
        txt ='('
        for val in self.axsVal :
            txt += str(val) + ','
        txt = txt.strip(',')
        txt += ')'
        return txt
   
    def __repr__(self) :
        return self.__str__()
    
    def __len__(self) :
        return self.dimension
    
class Line :
    def __init__(self, p1, p2) :
        delX = 
        self.m = 
    
    
a = Point(3, 4)
print(a)