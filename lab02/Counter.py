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