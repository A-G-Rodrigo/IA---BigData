#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 12 20:19:59 2022

@author: ivan
"""


import csv
import numpy as np

def carga(archivo):
    matriz=np.empty((9,9))
    with open(archivo,"r") as f:
        reader=csv.reader(f, delimiter=";")
        i=0
        for row in reader:
            matriz[i]=row
            i+=1
    return matriz.astype(int)

def comprobar_fila(x,y,matriz,opcion):
    fila = []
    for i in range(9):
        fila.append(matriz[x][i])
    print("fila"+str(fila))
    if fila.count(opcion)==1:
        return True
    else:
        return False, fila
    
def comprobar_columna(x,y,matriz,opcion):
    columna = []
    for i in range(9):
        columna.append(matriz[i][y])
    print("columna"+str(columna))

    if columna.count(opcion)==1:
        return True
    else:
        return False, columna
        
def comprobar_subMatriz(x,y,matriz,opcion):
    #print(x)
    #print(y)
    sub_matriz = []
    array_sub_matriz = []
    subx=int(x/3)
    suby=int(y/3)
    print(subx*3)
    print(suby*3)
    print(type(matriz))

    sub_matriz.append(matriz[subx*3:(subx*3)+3,suby*3:(suby*3)+3])
    array_sub_matriz.append(sub_matriz[0].reshape(-1).tolist())
  
    #submatriz.append(matriz[(subx*3):((subx*3)+3),submy*3):((int(submy)*3)+3)].reshape(-1).tolist())
    #submatriz.append(matriz[x:x+3,y:y+3].reshape(-1)).tolist()
    
    print(array_sub_matriz[0])
    
    for i in range(9):
       
        if array_sub_matriz[0].count(opcion) == 1:
            return True
        else:
            return False
    
def sudoku(matriz, paso):
    
    exito=False
    x=int(paso/9)
    y=int(paso%9)

    #heurística
    if matriz[x,y]!=0:
        return sudoku(matriz, paso+1)
    
    opcion=1
    while opcion<10 and not exito:
        matriz[x,y]=opcion  #anotar siguiente opción
        print(paso)
        print(matriz)
        print(opcion)
        print(comprobar_columna(x,y,matriz,opcion))
        print(comprobar_fila(x,y,matriz,opcion))
        print(comprobar_subMatriz(x,y,matriz,opcion))
        if comprobar_fila(x,y,matriz,opcion) and comprobar_columna(x,y,matriz,opcion) and comprobar_subMatriz(x,y,matriz,opcion):

            if paso==80:
                #matriz[x,y]=opcion  #anotar siguiente opción
                exito=True
            else:
                #opcion=1
                #matriz[x,y]=opcion  #anotar siguiente opción

                exito=sudoku(matriz,paso+1)
                if not exito:
                    matriz[x,y]=0
        else:
            matriz[x,y]=0
        opcion+=1

    return exito

#sub_matriz = []
#array_sub_matriz = []
paso = 0
sudoku(carga('sudoku.txt'), paso)