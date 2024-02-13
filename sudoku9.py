# -*- coding: utf-8 -*-
"""
Created on Mon Dec 12 20:03:50 2022

@author: agrss
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

def comprobar_fila(x,matriz,valor):
    for i in range(9):
        fila.append(matriz[x][i]) 
    if fila.count(valor) == 0:
        return False, fila
    else:
        return True, fila

def comprobar_columna(y,matriz,valor):
    for j in range(9):
        columna.append(matriz[j][y])
    if columna.count(valor) == 0:
        return False, columna
    else:
        return True, columna

def comprobar_subMatriz(x,y,matriz,valor):
    sub_matriz.append(matriz[x:x+3,y:y+3])
    array_sub_matriz.append(sub_matriz[0].reshape(-1).tolist())
    if array_sub_matriz[0].count(valor) == 0:
        return False, array_sub_matriz[0]
    else:
        return True, sub_matriz[0], array_sub_matriz[0]
   

def pos_ceros(x,y,matriz):
    ceros_fil = []
    ceros_col = []
    ceros_fil.append(np.where(matriz[x:x+3,y:y+3]==0)[0].tolist())
    ceros_col.append(np.where(matriz[x:x+3,y:y+3]==0)[1].tolist())
    return ceros_fil, ceros_col

def pos_actual(matriz,stepY,stepX):
    valor = 0
    valor = matriz[x+stepX][y+stepY]
    return valor


def sudoku(matriz, stepY, stepX):
    lista_ceros = pos_ceros(stepY,stepX,matriz)
    valor = pos_actual(matriz,stepY,stepX)
    
    print(lista_ceros[0][0])
    i=0

    while i < len(lista_ceros[0][0])-1:
        for j in range(1,10):
            
            if comprobar_fila(x,matriz,valor)[1].count(j) == 0 and comprobar_columna(y,matriz,valor)[1].count(j) == 0 and comprobar_subMatriz(x,y,matriz,valor)[2].count(j) == 0: #opcion aceptable
                matriz[lista_ceros[0][0][i]+stepX][lista_ceros[0][1][i]+stepY] = j
                #i+=1
                """
                solucion_parcial.append(i)
    
                if len(solucion_parcial) == len(lista_ceros[0]): #es solucion
                    matriz[lista_ceros[0][i]+stepX][lista_ceros[1][i]+stepY] = j
                    soluciones.append(solucion_parcial.copy())
                    #pesos.append(pesos_parcial.copy())
                    #suma_pesos.append(sum(pesos_parcial.copy()))
    
                else:
                    
                    exito=sudoku(matriz, stepY, stepX)
        
                solucion_parcial.pop()
                #pesos_parcial.pop()
    
            i+=1
            """
            else:
                print("El número "+str(j)+" no es solucion")
        i+=1
    #return soluciones, solucion_parcial
    #print(pos_ceros(x,y,matriz))
    print(comprobar_subMatriz(x,y,matriz,valor)[0])
    print(comprobar_subMatriz(x,y,matriz,valor)[1])
    print(comprobar_subMatriz(x,y,matriz,valor)[2])
    print(comprobar_fila(x,matriz,valor))
    print(comprobar_columna(y,matriz,valor))
    print(matriz)
    print(lista_ceros)
x=0
y=0   
stepY = 0
stepX = 0
soluciones = []
solucion_parcial = []
sub_matriz = []
array_sub_matriz = []
fila = []
columna = []
x = 0
y = 0
print(sudoku(carga('sudoku.txt'),stepY,stepX))




