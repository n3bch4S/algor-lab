#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 22:41:17 2023

@author: tada
"""

from typing import Type, NewType, List

class Vertex :
    pass
class SGraph :
    pass

''' Vertex Section '''
class Vertex :
    
    def __init__(self, name: str) -> None :
        self.name = name
        self.neighbor = {}
        self.color = ""
        self.pi = None
        self.d = -1
        self.f = -1
        
    def addNeighbor(self, name: str) -> Vertex :
        if name not in self.neighbor :
            self.neighbor[name] = Vertex(name)
        return self
    
    def __str__(self) -> str :
        txt = self.name + " -> " + str([self.neighbor[key].name for key in self.neighbor]) + "{\n"
        txt += "  color: " + str(self.color) + ",\n"
        if self.pi is not None :
            txt += "  pi: " + str(self.pi.name) + ",\n"
        else :
            txt += "  pi: None" + ",\n"
        txt += "  discovered: " + str(self.d) + ",\n"
        txt += "  finished: " + str(self.f) + "\n"
        txt += "}\n"
        return txt
    
    def __repr__(self) -> str :
        return self.__str__()
''' End of Vertex Section '''
        
''' Sparse Graph section '''
class SGraph :
    
    def __init__(self) -> None :
        self.vertices = {}
        
    def addV(self, a: str) -> Vertex :
        if a in self.vertices :
            return self.vertices[a]
        v = Vertex(a)
        self.vertices[a] = v
        return v
    
    def addE(self, a: str, b: str, c: int) -> List[List[Vertex]] :
        if c < 0 or c > 2 :
            raise ValueError("c less than 0 or greater than 2")
        u = self.addV(a)
        v = self.addV(b)
        edges = []
        if c > 0 :
            u.addNeighbor(b)
            edges = [[u, v]]
            c -= 1
        if c > 0 :
            v.addNeighbor(a)
            edges.append([v, u])
        return edges
    
    def DFS(self, vertices: List[Vertex]) -> List[List[Vertex]] :
        
        for u in vertices :
            u = self.vertices[u.name]
            u.color = "white"
            u.pi = None
            
        self.time = 0
        self.DFT = []
        
        for u in vertices :
            u = self.vertices[u.name]
            if u.color == "white" :
                self.DFT.append([])
                self.DFS_visit(u.name)
        
        return self.DFT
                
    def DFS_visit(self, name: str) -> None :
        if name not in self.vertices :
            raise ValueError("node name not found in this graph")
        u = self.vertices[name]
        if u.color == "grey" or u.color == "black" :
            return None
        
        self.DFT[len(self.DFT) - 1].append(u)
        self.time += 1
        u.d = self.time
        u.color = "grey"
        
        for neighborKey in u.neighbor :
            neighbor = self.vertices[neighborKey]
            if neighbor.color == "white" :
                neighbor.pi = u
                self.DFS_visit(neighbor.name)
        
        self.time += 1
        u.f = self.time
        u.color = "black"
        
    def SCC(self) -> List[List[Vertex]] :
        self.DFS(self.getVertexList())
        revVtx = sortDecrese(self.getVertexList())
        
        self.transpost()
        treeL = self.DFS(revVtx)
        self.transpost()
        return treeL
        
    def transpost(self) -> None :
        newVertices = {}
        for u in self.vertices :
            if u not in newVertices :
                newVertices[u] = Vertex(u)
            u = self.vertices[u]
            for v in u.neighbor :
                if v not in newVertices :
                    newVertices[v] = Vertex(v)
                newVertices[v].addNeighbor(u.name)
        self.vertices = newVertices
                
        
    def getVertexList(self) -> List[Vertex] :
        return [self.vertices[key] for key in self.vertices]
    
    def __str__(self) -> str :
        txt = ""
        for key in self.vertices :
            txt += self.vertices[key].__str__() + "\n"
        return txt
    
    def __repr__(self) -> str :
        return self.__str__()
''' End of Sparse Graph section '''    
    
def getFinished(v: Vertex) -> int :
    return v.f

def sortDecrese(treeL: List[Vertex]) -> List[Vertex] :
    newTreeL = [vertex for vertex in treeL]
    newTreeL.sort(key=getFinished, reverse=True)
    return newTreeL

def fileToGraphs(filename: str) -> List[SGraph] :
    file = open(filename, 'r')
    graphs = []
    
    line = file.readline().strip()
    while line != "0 0" :
        line = [int(x) for x in line.split()]
        n = line[0]
        m = line[1]
        graph = SGraph()
        for i in range(m) :
            line = file.readline().strip()
            line = [x for x in line.split()]
            a = line[0]
            b = line[1]
            c = int(line[2])
            graph.addE(a, b, c)
        graphs.append(graph)
        print(str(graph) + "############################\n")
        line = file.readline().strip()
        
    file.close()
    return graphs

FILE_DIR = ["ex.txt", #0
            "6.1.txt", #1
            "6.2.txt", #2
            "6.3.txt", #3
            "6.4.txt", #4
            "Extra6.5.txt", #5
            "EXtra6.6.txt", #6
            "Extra6.7.txt", #7
            "lab 6 input Demo.txt", #8
            "test.txt"] #9
FILE_SELECTOR = 4

graphs = fileToGraphs(FILE_DIR[FILE_SELECTOR])
sccs = []
for graph in graphs :
    treeL = graph.SCC()
    sccs.append(treeL)
    print(1 if len(treeL) == 1 else 0)

''' test vertex 
v = Vertex('v')
v.addNeighbor('a')
v.addNeighbor('b')
v.color = "white"
print(v.name + str(v.neighbor) + v.color)
''' 

''' test graph 
g = SGraph()
g.addE('1', '2', 2)
g.addE('1', '3', 1)

g.DFS(g.getVertexList())
revVtx = sortDecrese(g.getVertexList())

g.transpost()
treeL = g.DFS(revVtx)
print(treeL)

''' 