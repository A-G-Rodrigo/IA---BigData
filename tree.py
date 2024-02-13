#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Tree:
    def __init__(self, data):
        self.children = []
        self.data = data

a = Tree("A")
b = Tree("B")
c = Tree("C")
root = Tree("root")
root.children.append(a)
root.children.append(b)
root.children.append(c)


a1=Tree("A1")
a2=Tree("A2")
root.children[0].children.append(a1)
root.children[0].children.append(a2)


b1=Tree("B1")
b2=Tree("B2")
root.children[1].children.append(b1)
root.children[1].children.append(b2)

c1=Tree("C1")
c2=Tree("C2")
root.children[2].children.append(c1)
root.children[2].children.append(c2)

c21=Tree("C21")
c2.children.append(c21)
"""
print(root.data)

for i in root.children:
    print(i.data)
    for j in i .children:
        print(j.data)
        for k in j.children:
            print(k.data)
"""        
def recorrerP(arbol):
    for i in arbol.children:
        recorrerP(i)
    print(arbol.data)
    
recorrerP(root)

def recorrerA(arbol):
    for i in arbol.children:
        print(i.data)
    for i in arbol.children:
        recorrerA(i)
print(root.data)#procesar el nodo raiz
recorrerA(root)