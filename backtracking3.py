# -*- coding: utf-8 -*-
"""
Created on Wed Nov 30 16:26:49 2022

@author: agrss
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Nov 29 19:54:38 2022

@author: agrss
"""

# Tenemos una serie de bjetos: tuplas(valor,peso)
# Llenar mochila de peso max_peso de manera que no excedadmos el max_peso y 
#la llenemos con el mayor valor

def backtracking(target, soluciones, solucion_parcial,pesos,pesos_parcial, tuplas):
    exito = False
    opciones = len(tuplas)
    i=0
    while i < opciones:
        val = tuplas[i][1]
        pes=valores[i][0]
        total = val+sum(solucion_parcial)
        if total <= target and solucion_parcial.count(val) == 0: #opcion aceptable
         
            solucion_parcial.append(val)
            pesos_parcial.append(pes)
            #exito=backtracking(target, soluciones, solucion_parcial, valores)

            if total == target: #es solucion
                
                soluciones.append(solucion_parcial.copy())
                pesos.append(pesos_parcial.copy())
                suma_pesos.append(sum(pesos_parcial.copy()))

                #break;
                #exito = True
            else:
                #valores.pop(i)
                
                exito=backtracking(target, soluciones, solucion_parcial,pesos,pesos_parcial, tuplas)
    
            solucion_parcial.pop()
            pesos_parcial.pop()
        #else:

            #exito = False
            #break; #heurística  

        i+=1
    return exito

target = 15
soluciones = []
solucion_parcial = []
pesos_parcial = []
pesos=[]
suma_pesos=[]
total_pesos=[]
valores=[[12,5],[20,2],[50,15],[40,10],[8,2],[4,3]]
tuplas = [(12,5),(20,2),(50,15),(40,10),(8,2),(4,3)]#valor,peso
backtracking(target, soluciones, solucion_parcial,pesos,pesos_parcial, valores)
print(soluciones)
print(pesos)
print(suma_pesos)
print(max(suma_pesos))

print(suma_pesos.index(max(suma_pesos)))
print(soluciones[suma_pesos.index(max(suma_pesos))])