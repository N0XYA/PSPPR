import pickle
import matplotlib.pyplot as plt
import random
import math

min_samples = 2
eps = 2.05

# Достаем координаты из файла

with open("Coordinates.pickle", "rb") as file:
    obj = pickle.load(file)
file.close()


def howManyNeighbours(point):
    neighbours_count = 0
    for neighbours in obj:
        if neighbours == point:
            continue
        if math.dist(point, neighbours) <= eps:
            neighbours_count += 1
    return neighbours_count


def findCorePoints(unmarked):
    core_points = []
    for point in unmarked:
        num_of_neighbours = howManyNeighbours(point)
        if num_of_neighbours >= min_samples:
            core_points.append(point)
        # print(item, core_points[item])
    return core_points


def findBlackPoints(unmarked, core_points):
    blacks = []
    for point in unmarked:
        if point not in core_points:
            blacks.append(point)
    return blacks


def findClusters(core_points, black_points):
    cluster = []
    start_cluster = random.choice(core_points)
    cluster.append(start_cluster)
    core_points.remove(start_cluster)
    for cluster_point in cluster:
        for point in core_points:
            if math.dist(cluster_point, point) <= eps:
                cluster.append(point)
                core_points.remove(point)

        for black_point in black_points:
            if math.dist(cluster_point, black_point) <= eps:
                cluster.append(black_point)
                black_points.remove(black_point)
    return cluster


def main():
    core_points = findCorePoints(obj)
    black_points = findBlackPoints(obj, core_points)
    print(len(core_points))

    clusters = []
    while len(core_points) > 0:
        clusters.append(findClusters(core_points, black_points))
    print(len(core_points))

    x = [coord[0] for coord in obj]
    y = [coord[1] for coord in obj]
    plt.scatter(x, y, c='black', marker= '+')

    for clust in clusters:
        x = [coordinate[0] for coordinate in clust]
        y = [coordinate[1] for coordinate in clust]
        plt.scatter(x, y)

    plt.show()


if __name__ == '__main__':
    main()


'''
HISTORY
'''

# def if_core(coord):
#     count = 0
#     samples_around_core = []
#     for point in obj:
#         if point == coord:
#             continue
#         if math.dist(coord, point) <= eps:
#             count += 1
#             samples_around_core.append(point)
#
#     return count, samples_around_core
#
#
# def find_centers():
#     core_points = []
#     clusters = {}
#     for coord in obj:
#         coord = tuple(coord)
#         num_of_neighbours, neighbours = if_core(coord)
#         if num_of_neighbours >= min_samples:
#             clusters[coord] = neighbours
#             core_points.append(coord)
#
#     return clusters
#
#
# # core_points = find_centers()
#
# # print(core_points)
#
# clusters = find_centers()
# print(clusters)
#
# for samples in clusters.values():
#     for coordinate in samples:
#         if coordinate in obj:
#             obj.remove(coordinate)
# for clust in clusters:
#     center = clust
#     centerx = center[0]
#     centery = center[1]
#     x = [cord[0] for cord in clusters[center]]
#     y = [cord[1] for cord in clusters[center]]
#     plt.scatter(x, y)
#     plt.scatter(centerx, centery, c='red',marker= '+')
#
# x = [coord[0] for coord in obj]
# y = [coord[1] for coord in obj]
#
# plt.scatter(x, y, c='black', marker='+')
# plt.show()
# # corex = [coord[0] for coord in core_points]
# # corey = [coord[1] for coord in core_points]
# # plt.scatter(x, y)
# # plt.show()