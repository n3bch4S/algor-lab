#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  7 18:22:44 2023

@author: tada
"""

#just contain somthing unorder
class TreasureChest :
    def __init__(self) :
        self.cntnr = []
        self.n = 0
        self.index = 0
        
    def __str__(self) :
        text = "{"
        for e in self.cntnr :
            text += f"{e}, "
        if self.n > 0 :
            text = text.rstrip(', ')
        text += "}"
        return text
    
    def __repr__(self) :
        return self.__str__()
    
    def __len__(self) :
        return self.n
    
    def __eq__(self, o) :
        if not isinstance(o, type(self)) :
            return False
        
        thisCntnr = self.cntnr
        oCntnr = [x for x in o.cntnr]
        
        for i in range(self.n) :
            e = thisCntnr[i]
            if e in oCntnr :
                atOther = oCntnr.index(e)
                oCntnr.pop(atOther)
        if len(oCntnr) > 0 :
            return False
        return True
    
    def __iter__(self) :
        return self
    
    def __next__(self) :
        idxNow = self.index
        sizeNow = self.n
        thisCntnr = self.cntnr
        if idxNow < sizeNow :
            e = thisCntnr[idxNow]
            self.index += 1
            return e
        
        self.index = 0
        raise StopIteration
    
    def addItem(self, itm) :
        self.cntnr.append(itm)
        self.n += 1
    
    def setItem(self, oldItm, newItm) :
        for i in range(self.n) :
            e = self.cntnr[i]
            if e == oldItm :
                self.cntnr[i] = newItm
                break
            
    def setAllItem(self, oldItm, newItm) :
        for i in range(self.n) :
            e = self.cntnr[i]
            if e == oldItm :
                self.cntnr[i] = newItm
            
    def delItem(self, itm) :
        if itm in self.cntnr :
            self.cntnr.remove(itm)
            self.n -= 1
            
    def delAllItem(self, itm) :
        while itm in self.cntnr :
            self.cntnr.remove(itm)
            self.n -= 1
            
    def having(self, itm) :
        return itm in self.cntnr
    
    def toList(self) :
        return [x for x in self.cntnr]
    
    def clone(self) :
        newChest = TreasureChest()
        for e in self.cntnr :
            newChest.addItem(e)
        return newChest
    
    def reset(self) :
        self.cntnr = []
        self.n = 0
        self.index = 0
        
            
class Set(TreasureChest) :
    def addItem(self, itm) :
        if not self.having(itm) :
            super().addItem(itm)
            
    def union(self, other) :
        newSet = Set()
        if not isinstance(other, type(self)) :
            return newSet
        
        thisCntnr = self.cntnr
        otherCntnr = other.cntnr
        for i in range(self.n) :
            e = thisCntnr[i]
            newSet.addItem(e)
            
        for i in range(other.n) :
            e = otherCntnr[i]
            newSet.addItem(e)
        
        return newSet
                
    def intersect(self, other) :
        newSet = Set()
        if not isinstance(other, type(self)) :
            return newSet
        
        thisCntnr = self.cntnr
        for i in range(self.n) :
            e = thisCntnr[i]
            if other.having(e) :
                newSet.addItem(e)
        
        return newSet
    
    def difference(self, other) :
        newSet = Set()
        if not isinstance(other, type(self)) :
            return newSet
        
        thisCntnr = self.cntnr
        for i in range(self.n) :
            e = thisCntnr[i]
            if not other.having(e) :
                newSet.addItem(e)
                
        return newSet
    
    def clone(self) :
        newSet = Set()
        for e in self.cntnr :
            newSet.addItem(e)
        return newSet