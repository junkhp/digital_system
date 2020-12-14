# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
from pathlib import PosixPath
import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt

import numpy as np
import math
import os
import csv
import random



def radius(points, S):
    return max(min(np.linalg.norm(points[i] - points[s]) for s in S) for i in range(len(points)))

def make_random_points(point_num):
    return np.random.randint(0, 100, (point_num, 2))

def distace(a, b):
    return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)

def main():
    point_num = 50
    k = int(math.sqrt(point_num))
    # 点を初期化
    points = make_random_points(point_num)
    # 点をプロット
    for p in points:
        plt.plot(p[0], p[1], marker='.', color='red')
    i = np.random.randint(0, point_num)
    S = [i]
    while(len(S) < k):
        max_dist = 0
        for j in range(point_num):
            min_dist = float('inf')
            for i in S:
                dist = distace(points[j], points[i])
                if min_dist > dist:
                    min_dist = dist
            if max_dist < min_dist:
                max_dist = min_dist
                next = j
        S.append(next)

    r = radius(points, S)
    for s in S:
        plt.plot(points[s][0], points[s][1], marker='.', color='blue')
        c = plt.Circle(points[s], r, alpha=0.2, color='green')
        plt.gca().add_artist(c)
    plt.gca().scatter(points[S, 0], points[S, 1], color='r', s=10)
    plt.axes().set_aspect('equal', 'datalim')
    plt.savefig('out.png')

if __name__ == "__main__":
    main()
    