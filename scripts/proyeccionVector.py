#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 09:31:17 2020

@author: jesuspalomino
"""

import numpy as np
import numpy.linalg as la
import matplotlib.pyplot as plt
from random import randrange as rr
import random


def genData(n, seed=1, m=False):  # Genera data linearmente separable por una pendiente (m)
    np.random.seed(seed)
    if (m == False):
        m = (rr(20) + 1) / 10
    X = np.random.random((n, 2))
    y = ((X[:, 1] / X[:, 0]) > m) * 1
    X = (X - 0.5) * 2
    return [X, y]


def graphPoints(X, y):  # Grafica los puntos y los puntos proyectados
    for i in range(0, X.shape[0]):
        p = X[i, 0:2]
        # p2 = Xp[i,0:2]
        if (y[i]):
            plt.scatter(p[0], p[1], color="red", s=4)
        else:
            plt.scatter(p[0], p[1], color="black", s=4)
    plt.xlim(-1, 1)
    plt.ylim(-1, 1)
    plt.show()


def randomVector():
    vec = (np.array([random.randint(-5, 5), random.randint(-5, 5)]))
    plt.quiver(0, 0, vec[0], vec[1], color="black", angles='xy', scale_units='xy', scale=5)
    plt.xlim(-1, 1)
    plt.ylim(-1, 1)
    plt.show()
    return vec


def proyectPoints(x, y, vec):
    proyeccion = []
    for i in x:
        p = np.dot(vec, i) / (la.norm(vec) ** 2) * vec
        proyeccion.append(p)
    proyeccion = np.array(proyeccion)
    graphPoints(proyeccion, y)


[x, y] = genData(30)
graphPoints(x, y)
proyectPoints(x, y, randomVector())