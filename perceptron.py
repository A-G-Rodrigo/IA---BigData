# -*- coding: utf-8 -*-
"""
Created on Tue Jan 17 19:39:42 2023

@author: agrss
"""
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

class Perceptron(object):
    """
    parámetros:
        ratio: float, rango de aprendizaje
        epocas: número de èpocas
        semilla: int, semilla para inicialización aleatoria
        w_: vector 1 dimensión, array de pesos
        errors_: lista, lista de errrores
    """
    
    def __init__(self, ratio=0.01, epocas=50, semillas=1):
        self.ratio=ratio
        self.epocas=epocas
        self.semillas=semillas
        rgen=np.random.RandomState(semillas)
        self.w_=rgen.normal(loc=0.0,scale=0.01,size=3)
        self.errors_=[]
        
    def net_input(self,X):
        return np.dot(X,self.w_[1:])+self.w_[0]#del 1 hasta el final
    
    def predict(self,X):
        return np.where(self.net_input(X)>=0.0,1,-1)
    def predict2(self,X):
        return np.where(self.net_input(X)==0,1,-1)
    def fit(self,X,y):
        """
        parametros:
            x: array de muestras shape[n_muestras,n_caracteristicas]
            
            y: clases verdades shape[n_muestras]
            
            
        returns
        
        self
        """
        # Ejercicio 7
        pintar='Valor inicial: '+str(self.w_)+'\n'
        # Ejercicio 7
        for epoca in range(self.epocas):
            errors = 0

            for xi,target in zip(X,y):
                delta=self.ratio*(target-self.predict(xi))
                self.w_[1:]+=delta*xi
                self.w_[0]+=delta

                if delta != 0:
                    errors+=1      
                    # Ejercicio 7
                    pintar +='pesos: '+str(self.w_) +'; epoca: '+str(epoca)+'; errores: '+str(errors)+ '; xi: '+str(xi)+'; y: '+str(target)+'; prediccion: '+str(self.predict(y[target])[1])+'\n'
                    # Ejercicio 7
            self.errors_.append(errors)
        # Ejercicio 7
        print(pintar)
        pintar=''
        # Ejercicio 7
        return self

# Se carga un arhivo csv 
df=pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data', header=None)

# Se seleccionan del dataframe las variedades de flor que se van a tratar

#print(df)
y=df.iloc[0:100,4]
#print(y)
y=np.where(y=='Iris-setosa',-1,1)
#print(y)
X=df.iloc[0:100,[0,2]].values
#print(X)

p=Perceptron(0.1,10,1)
print(p.fit(X,y))


# predecir si una flor con pétalo 2.1 y sépalo 5 es setosa o versicolor

petalo=2.1
sepalo=5
print(np.where(p.predict([sepalo,petalo])==1,"versicolor","setosa"))

plt.plot(range(1, len(p.errors_)+1), p.errors_, marker='o')
plt.xlabel('épocas') 
plt.ylabel('errores')
plt.show()

#################################################################
# Ejercicio 9

vec=[]
vec2=[]
y=0
for x in X:
    y = (-p.w_[0]-p.w_[1]*x)/p.w_[2]
    vec.append(y)
    vec2.append(x)
#print(len(vec))
vec = np.array(vec)
vec2 = np.array(vec2)
#print(vec2)
#print(type(vec))
#print(type(X))
#print('vec(x)_max: '+str(max(vec[:,0]))+' y vec(x)_min: '+str(min(vec[:,0])))
#print('X(x)_max: '+str(max(X[:,0]))+' y X(x)_min: '+str(min(X[:,0])))

#print('vec(y)_max: '+str(max(vec[:,1]))+' y vec(y)_min: '+str(min(vec[:,1])))
#print('X(y)_max_setosa: '+str(max(X[:50,1]))+' y X(y)_min_setosa: '+str(min(X[:50,1])))

#print('X(y)_max_versicolor: '+str(max(X[50:100,1]))+' y X(y)_min_versicolor: '+str(min(X[50:100,1])))

# Dibujar los datos

#plt.plot(vec[:100, 1]+(3.5),vec[:100, 0], color="green", marker="s", label="vector de pesos")
#plt.scatter(vec[:100, 1]+(4.3-0.59),vec[:100, 0]+(1-0.59), color="green", marker="s", label="vector de pesos y")
#plt.scatter(vec2[:100, 1]+(4.3-0.59),vec2[:100, 0]+(1-0.59), color="purple", marker="*", label="vector de pesos x")
plt.plot(vec2,vec, color="black")
plt.scatter(X[:50, 0], X[:50, 1],
            color='red', marker='o', label='setosa')
plt.scatter(X[50:100, 0], X[50:100, 1],
            color='blue', marker='x', label='versicolor')

plt.xlabel('longitud de sépalo [cm]')
plt.ylabel('longitud de pétalo length [cm]')
plt.legend(loc='upper left')

plt.savefig('limite-decision-perceptron.png', dpi=300)
plt.show()


######################################################################
# Ejercicio 10

X= df.iloc[0:150, [0,2]].values
print(X)

plt.scatter(X[:50, 0], X[:50, 1],
            color='red', marker='o', label='setosa')
plt.scatter(X[50:100, 0], X[50:100, 1],
            color='blue', marker='x', label='versicolor')
plt.scatter(X[100:, 0], X[100:, 1],
            color='black', marker='*', label='virginica')

plt.xlabel('longitud de sépalo [cm]')
plt.ylabel('longitud de pétalo length [cm]')
plt.legend(loc='upper left')

plt.savefig('clasificacion.png', dpi=100)
plt.show()

################################################
# Ejercicio 11


y=df.iloc[50:150,4]
print(y)
y=np.where(y=='Iris-virginica',-1,1)
print(y)
X=df.iloc[50:150,[0,2]].values
print(X)
p2=Perceptron(0.1,10,1)

print(p2.net_input(X))
#print(p2.fit(X,y))
prediccion1 = p2.predict([5,5.5]).item()
prediccion2 = p2.predict([6,6.5]).item()
#prediccion3 = p2.predict([5,3.5]).item()
#prediccion4 = p2.predict([7.5,6]).item()
print('Ejercicio 11\n\nPredicción 1: {}\nPredicción 2: {}'.format(prediccion1,prediccion2))
print(np.where(p2.predict([6.5,5])==-1,"virginica" ,"versicolor"))

#################################################################
# Ejercicio 12
from matplotlib.colors import ListedColormap


def plot_decision_regions(X, y, clasificador, resolution=0.02):

    # configurar el generador de markers y el mapa de color
    markers = ('s', 'x', 'o', '^', 'v')
    colors = ('red', 'blue', 'lightgreen', 'gray', 'cyan')
    cmap = ListedColormap(colors[:len(np.unique(y))])

    # mostrar la superficie de decisión
    x1_min, x1_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    x2_min, x2_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    xx1, xx2 = np.meshgrid(np.arange(x1_min, x1_max, resolution),
                           np.arange(x2_min, x2_max, resolution))
    Z = clasificador.predict(np.array([xx1.ravel(), xx2.ravel()]).T)
    Z = Z.reshape(xx1.shape)
    plt.contourf(xx1, xx2, Z, alpha=0.3, cmap=cmap)
    plt.xlim(xx1.min(), xx1.max())
    plt.ylim(xx2.min(), xx2.max())

    # mostrar los ejemplos de cada clase
    for idx, cl in enumerate(np.unique(y)):
        plt.scatter(x=X[y == cl, 0], 
                    y=X[y == cl, 1],
                    alpha=0.8, 
                    c=colors[idx],
                    marker=markers[idx], 
                    label=cl, 
                    edgecolor='black')
        
plot_decision_regions(X, y, clasificador=p2)
plt.xlabel('longitud de sépalo [cm]')
plt.ylabel('longitud de pétalo [cm]')
plt.legend(loc='upper left')


# plt.savefig('regiones.png', dpi=300)
plt.show()

###################################################################
def plot_decision_regions2(X, y, clasificador, resolution=0.008):

    # configurar el generador de markers y el mapa de color
    markers = ('s', 'x', 'o', '^', 'v')
    colors = ('red', 'blue', 'lightgreen', 'gray', 'cyan')
    cmap = ListedColormap(colors[:len(np.unique(y))])

    # mostrar la superficie de decisión
    x1_min, x1_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    x2_min, x2_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    xx1, xx2 = np.meshgrid(np.arange(x1_min, x1_max, resolution),
                           np.arange(x2_min, x2_max, resolution))
    Z = clasificador.predict(np.array([xx1.ravel(), xx2.ravel()]).T)
    Z = Z.reshape(xx1.shape)
    plt.contourf(xx1, xx2, Z, alpha=0.3, cmap=cmap)
    plt.xlim(xx1.min(), xx1.max())
    plt.ylim(xx2.min(), xx2.max())

    # mostrar los ejemplos de cada clase
    for idx, cl in enumerate(np.unique(y)):
        plt.scatter(x=X[y == cl, 0], 
                    y=X[y == cl, 1],
                    alpha=0.8, 
                    c=colors[idx],
                    marker=markers[idx], 
                    label=cl, 
                    edgecolor='black')
  
X0 = [1,0,1,0]
X1 = [1,1,0,0]
y=[]
for i in range (len(X0)):
    y.append(X0[i] ^ X1[i])
print(y)
X = np.array([X0,X1])

print(X)
y = np.where(y==1, -1, 1)
#y=np.array([X1,y])

p3 = Perceptron(0.1, 10, 1)
p3.fit(X,y)
print(p3.predict2([1,0]))
#print(p3.fit(X,y))
plot_decision_regions2(X, y, clasificador=p3,)
plt.xlabel('longitud de sépalo [cm]')
plt.ylabel('longitud de pétalo [cm]')
plt.legend(loc='upper left')


# plt.savefig('regiones.png', dpi=300)
plt.show()

