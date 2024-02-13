# -*- coding: utf-8 -*-
"""
Created on Wed Nov 30 15:53:38 2022

@author: agrss
"""


def valida_peso(mochila,objeto,max_peso):
    peso_total=0
    for item in mochila:
        peso_total+=item[1]
        
    return not peso_total+objeto[1]>max_peso

def suma_valor(mochila):
    valor_total=0
    for item in mochila:
        valor_total+=item[0]
    return valor_total

def copia_mochila(mochila_optim,mochila):
    mochila_optim.clear()
    for x,y in mochila:
        mochila_optim.append((x,y))

def optimiza_mochila(mochila,max_peso,lista_objetos,mochila_optim,paso):
    print("{} mochila={},lista_objetos={},mochila_optim={}".format(" "*paso+":"+str(paso),mochila, lista_objetos, mochila_optim))
    for i in range(len(lista_objetos)):
        objeto=lista_objetos[i]
        if valida_peso(mochila,objeto,max_peso):
            mochila.append(objeto)              #anotar
            lista_objetos.pop(i)
            
            nuevo_valor=suma_valor(mochila)
            if suma_valor(mochila_optim)<nuevo_valor:
                copia_mochila(mochila_optim,mochila)
                
            optimiza_mochila(mochila, max_peso, lista_objetos, mochila_optim,paso+1)
            
            mochila.pop()                   #desanotar = backtrack
            lista_objetos.insert(i,objeto)
            

mochila=[]
mochila_optim=[]
max_peso=12
lista_objetos=[(12,5),(20,2),(50,15),(40,10),(8,2),(4,3)]

optimiza_mochila(mochila, max_peso, lista_objetos, mochila_optim,0)
print(mochila_optim)