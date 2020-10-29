import numpy as np
import matplotlib.pyplot as plt
from random import randrange as rr
import math


def gen_data(n, m=False):  # Generates linear separable data by a slope (m).
    np.random.seed()
    if not m:
        m = (rr(20)+1)/10
    x = np.random.random((n, 2))
    y = ((x[:, 1]/x[:, 0]) > m)*1
    x = (x-0.5)*2
    return [x, y]


def bubble_sort(matrix):
    for past_num in range(matrix.shape[0] - 1, 0, -1):
        for i in range(past_num):
            if matrix[i][0] > matrix[i + 1][0]:
                temp = matrix[i][0]
                aux = matrix[i][1]
                matrix[i][0] = matrix[i + 1][0]
                matrix[i][1] = matrix[i + 1][1]
                matrix[i + 1][0] = temp
                matrix[i + 1][1] = aux


def gen_point():
    np.random.seed()
    x = np.random.random((1, 2))
    x = (x-0.5)*2
    return x


def graph_point(x):
    p = x[0, 0:2]
    plt.plot(p[0], p[1], color="green", marker="x")


def near(t, x, y, n):
    neighbor = np.zeros((n, 2))
    r = t[0, 0:2]
    for i in range(0, x.shape[0]):
        p = x[i, 0:2]
        res = math.sqrt((r[0] - p[0])**2+(r[1] - p[1])**2)
        if i < n:
            neighbor[i][1] = i
            neighbor[i][0] = res
        else:
            if i == 3:
                bubble_sort(neighbor)
            flag = False
            aux = np.zeros(2)
            for j in range(0, n):
                if flag:
                    temp = np.zeros(2)
                    temp[0] = neighbor[j][0]
                    temp[1] = neighbor[j][1]
                    neighbor[j][0] = aux[0]
                    neighbor[j][1] = aux[1]
                    aux[0] = temp[0]
                    aux[1] = temp[1]
                if neighbor[j][0] > res and not flag:
                    flag = True
                    aux[0] = neighbor[j][0]
                    aux[1] = neighbor[j][1]
                    neighbor[j][0] = res
                    neighbor[j][1] = i
    red = 0
    blue = 0
    for i in range(0, n):
        index = neighbor[i][1]
        if y[int(index)]:
            red += 1
        else:
            blue += 1
    if red >= blue:
        print("Point must be red")
        plt.scatter(r[0], r[1], color="red", s=4)
    else:
        print("Point must be red")
        plt.scatter(r[0], r[1], color="black", s=4)


def graph_points(x, y):  # Graphs the points and the projected points.
    for i in range(0, x.shape[0]):
        p = x[i, 0:2]
        if y[i]:
            plt.scatter(p[0], p[1], color="red", s=4)
        else:
            plt.scatter(p[0], p[1], color="black", s=4)


def main():
    [x, y] = gen_data(100)
    point = gen_point()
    graph_points(x, y)
    graph_point(point)
    plt.show()
    graph_points(x, y)
    near(point, x, y, 3)
    plt.show()


main()
