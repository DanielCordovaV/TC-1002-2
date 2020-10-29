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


def gen_data(n, m=False):  # Genera data linearmente separable por una pendiente (m)
    np.random.seed()
    if not m:
        m = (rr(20) + 1) / 10
    x = np.random.random((n, 2))
    y = ((x[:, 1] / x[:, 0]) > m) * 1
    x = (x - 0.5) * 2
    return [x, y]


def graph_points(x, y):  # Grafica los puntos y los puntos proyectados
    for i in range(0, x.shape[0]):
        p = x[i, 0:2]
        if y[i]:
            plt.scatter(p[0], p[1], color="red", s=4)
        else:
            plt.scatter(p[0], p[1], color="black", s=4)
    plt.xlim(-1, 1)
    plt.ylim(-1, 1)
    plt.show()


def random_vector():
    vec = (np.array([random.randint(-5, 5), random.randint(-5, 5)]))
    plt.quiver(0, 0, vec[0], vec[1], color="black", angles='xy', scale_units='xy', scale=5)
    plt.xlim(-1, 1)
    plt.ylim(-1, 1)
    plt.show()
    return vec


def project_points(x, y, vec):
    projection = []
    for i in x:
        p = np.dot(vec, i) / (la.norm(vec) ** 2) * vec
        projection.append(p)
    projection = np.array(projection)
    graph_points(projection, y)


def main():
    [x, y] = gen_data(30)
    graph_points(x, y)
    project_points(x, y, random_vector())


main()
