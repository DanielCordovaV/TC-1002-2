import numpy as np
import numpy.linalg as la
import matplotlib.pyplot as plt
from random import randrange as rr
import random
import math

def genData(n,seed=1,m=False): #Genera data linearmente separable por una pendiente (m)
    np.random.seed()
    if(m==False):
        m= (rr(20)+1)/10
        X = np.random.random((n, 2))
        y = ((X[:,1]/X[:,0])>m)*1
        X = (X-0.5)*2
    return [X,y]

def ordenamientoBurbuja(unaLista):
    for numPasada in range(unaLista.shape[0]-1,0,-1):
        for i in range(numPasada):
            if unaLista[i][0]>unaLista[i+1][0]:
                temp = unaLista[i][0]
                aux = unaLista[i][1]
                unaLista[i][0] = unaLista[i+1][0]
                unaLista[i][1] = unaLista[i+1][1]
                unaLista[i+1][0] = temp
                unaLista[i+1][1] = aux

def genPoint():
    np.random.seed()
    X = np.random.random((1, 2))
    X = (X-0.5)*2
    return X
    
def graphPoint(x):
    p = x[0,0:2]
    plt.plot(p[0],p[1],color="green",marker="X")

def near(t,X,y,n):
    vecino = np.zeros((n,2))
    r = t[0,0:2]
    for i in range(0,X.shape[0]):
        p = X[i,0:2]
        res = math.sqrt((r[0] - p[0])**2+(r[1] - p[1])**2)
        if i < n:
            vecino[i][1] = i
            vecino[i][0] = res
        else:
            if i == 3:
                ordenamientoBurbuja(vecino)
            flag = False
            aux = np.zeros(2)
            for j in range(0,n):
                if flag == True:
                    temp = np.zeros(2)
                    temp[0] = vecino[j][0]
                    temp[1] = vecino[j][1]
                    vecino[j][0] = aux[0]
                    vecino[j][1] = aux[1]
                    aux[0] = temp[0]
                    aux[1] = temp[1]
                if (vecino[j][0] > res and flag == False):
                    flag = True
                    aux[0] = vecino[j][0]
                    aux[1] = vecino[j][1]
                    vecino[j][0] = res
                    vecino[j][1] = i
    rojo = 0
    azul = 0
    for i in range(0,n):
        index = vecino[i][1]
        if(y[int(index)]):
            rojo += 1
        else:
            azul += 1
    if(rojo >= azul):
        print("El punto debe ser rojo")
        plt.scatter(r[0],r[1],color="red", s=4)
    else:
        print("El punto debe ser azul")
        plt.scatter(r[0],r[1],color="black", s=4)
    
def graphPoints(X,y): #Grafica los puntos y los puntos proyectados
    for i in range(0,X.shape[0]):
        p = X[i,0:2]
        #p2 = Xp[i,0:2]            
        if(y[i]):
            plt.scatter(p[0],p[1],color="red", s=4)
        else:
            plt.scatter(p[0],p[1],color="black", s=4)

[X,y] = genData(100)
punto = genPoint()
graphPoints(X,y)
graphPoint(punto)
plt.show()
graphPoints(X,y)
near(punto,X,y,3)
plt.show()