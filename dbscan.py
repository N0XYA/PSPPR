import pickle
import matplotlib.pyplot as plt
import random
import math

obj = [(1, 3), (3, 3), (4, 3), (5, 3),
            (1, 2), (4, 2), (1, 1), (2, 1)]
m = 2
e = 2

# Достаем координаты из файла

# with open("Coordinates.pickle", "rb") as file:
#     obj = pickle.load(file)
# file.close()



def findNeighbours(coodinate, object):
    coords = []
    for point in object:
        if point == coodinate:
            continue
        if math.dist(point, coodinate) < e:
            coords.append(point)
    return coords


def clusterization(neighbours, unmarked, center):
    cluster = {'center': center, 'objects': [], 'border': []}
    print(neighbours)
    for coordinate in neighbours:
        points_in_range = findNeighbours(coordinate, unmarked)
        points_in_range.remove(center)
        print(coordinate, 'points what are in range',points_in_range)
        if len(points_in_range) <= m:
            cluster['border'] = coordinate
        else:
            cluster.append(clusterization(points_in_range, unmarked, center))
            print("end of clusterization")
            print(cluster)
    return cluster


def clust(center, neighbours, unmarked):
    border_points = []
    core_points = []
    print('cluster center', center)
    print('cluster points', neighbours)
    for coordinate in neighbours:
        print('checking', coordinate)
        new_neighbours = findNeighbours(coordinate, unmarked)
        print(new_neighbours)
        for new_neigh in new_neighbours:
            if len(new_neighbours) >= m:
                print(len(new_neighbours), '=> making new clust')
                if new_neigh not in core_points:
                    core_points.append(new_neigh)
                    unmarked.remove(new_neigh)
            else:
                border_points.append(new_neigh)
                unmarked.remove(new_neigh)
    print('border points', border_points)
    print('core points', core_points)

    return


def dbscan(object):
    clusters = {}
    noize = []
    unmarked = object
    while len(unmarked) != 0:
        coordinate = random.choice(unmarked)
        neighbours = findNeighbours(coordinate, unmarked)
        if len(neighbours) < m:
            noize.append(coordinate)

        else:
            cluster = clust(coordinate, neighbours, unmarked)
            clusters[coordinate] = neighbours
            unmarked.remove(coordinate)
    return


dbscan(obj)
'''
Вывод графика
'''
# x = [coord[0] for coord in obj]
# y = [coord[1] for coord in obj]
# plt.scatter(x, y)
# plt.show()