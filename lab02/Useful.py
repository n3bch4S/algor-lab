#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 24 20:24:28 2023

@author: tada
"""

class Counter :
    def __init__(self, count = 0) :
        self.count = count
        
    def counting(self, value = 1) :
        self.count += value
        
    def reset(self, count = 0) :
        self.count = count
        
class Boolean :
    def __init__(self, state = True) :
        self.state = state
        
    def setState(self, state = True) :
        self.state = state
        
def plotter(xDict, yDict, label, plt) :
    x = xDict["x"]
    y = yDict["y"]
    xlabel = xDict["label"]
    ylabel = yDict["label"]
    plt.plot(x, y, label = label)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.legend()
    plt.show()