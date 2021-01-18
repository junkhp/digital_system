# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.collections as mc


def get_coordinates(city_num):
    return np.random.rand(city_num, 2)

def get_closest_tour(p):
    city_num = len(p)
    min_dist = float('inf')
    for i in range(city_num - 1):
        for j in range(i + 1, city_num):
            dist = np.linalg.norm(p[i] - p[j])
            if min_dist > dist:
                min_dist = dist
                closest_pair = (i, j)
    return closest_pair


def nearest_addition(cities):
    city_num = len(cities)
    S = list(range(city_num))
    i, j = get_closest_tour(cities)
    print(S)
    print(i)
    print(j)
    del S[i]
    del S[j - 1]
    print(S)
    tour = [i, j, i]

    while len(S) > 0:
        min_dist = float('inf')
        for city_index in range(len(S)):
            for toured_index in range(len(tour) - 1):
                dist = np.linalg.norm(cities[city_index] - cities[toured_index])
                if min_dist > dist:
                    min_dist = dist
                    min_city_index = city_index
                    correspond_city = toured_index
        tour.insert(correspond_city + 1, S[min_city_index])
        del S[min_city_index]
    print(tour)
    return tour


def draw_tour(P):
    plt.gca().scatter(P[:, 0], P[:, 1], color='r')
    tour = nearest_addition(P)
    lines = [[P[u], P[v]] for u, v in zip(tour[:-1], tour[1:])]
    plt.gca().add_collection(mc.LineCollection(lines, colors='g',
                                               linewidth=3, zorder=-1))


def main():
    city_num = 6
    coodinates = get_coordinates(city_num)
    print(coodinates)
    tour = nearest_addition(coodinates)
    # print(tour)
    draw_tour(coodinates)
    plt.savefig('tsp_nearest_addtion_result.png')

if __name__ == "__main__":
    main()
