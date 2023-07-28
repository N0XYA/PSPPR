import random
import matplotlib.pyplot as plt
import math


xrange = 10
yrange = 10
test_obj = [[1, 3], [3, 3], [4, 3], [5, 3],
            [1, 2], [4, 2], [1, 1], [2, 1]]

num_of_clusters = 4


def create_obj(xrange, yrange):
    object = []
    len = 0
    while len < 4:
        len = random.randint(0, 10)
    print(len)
    for i in range(0, len):
        coord = [random.randint(-xrange, xrange), random.randint(-yrange, yrange)]
        object.append(coord)
    return object

# obj = create_obj(xrange, yrange)


def choose_centers(obj):
    centers = []
    for i in range(0, num_of_clusters):
        centers.append(random.choice(obj))
    return centers

#
# for coord in test_obj:
#     print(coord)


def what_cluster(centers, obj):
    clusters_sorted = {}
    for coords in obj:
        minuclus = {}
        # print(coords)
        dist = []
        for cn in centers:
            dist.append(round(math.dist(cn, coords), 2))
        dist.sort()
        print(dist)
    print(clusters_sorted)
        # if dist[0] <= dist[1]:
        #     first_c.append(coords)
        # else:
        #     second_c.append(coords)
    # return first_c, second_c


def get_key(dict, value):
    for k , v in dict.items():
        if v == value:
            return k


def choose_cluster(centers, object):
    clusters = {}
    for item in centers:
        item = tuple(item)
        clusters[item] = []
    for coordinates in object:
        # print('coords are:', coordinates)
        distance = {}
        for item in centers:
            item = tuple(item)
            crd = tuple(coordinates)
            distance[item] = round(math.dist(item, coordinates), 2)
        # print(distance, coordinates)
        min_distance = min(distance.values())
        key = get_key(distance, min_distance)
        # print('min', min_distance)
        # print('точка', coordinates, 'принадлежит кластеру с центром в ', key)
        # print(type(key))
        clusters[key].append(coordinates)
    return clusters

def offset():

    pass


# centers = choose_centers(test_obj)
centers = [[1, 1],[2,1]]
print('centers are', centers)
clusters = choose_cluster(centers, test_obj)
# what_cluster(centers, test_obj)

for items in clusters:
    print(items, clusters[items])

# for i in f:
#     print(i)
# x = [coord[0] for coord in test_obj]
# y = [coord[1] for coord in test_obj]
# k1 = random.choice(test_obj)
# k2 = random.choice(test_obj)
# print(type(k1))
# plt.scatter(x, y)
# plt.scatter(k1[0], k1[1])
# plt.scatter(k2[0], k2[1])
# plt.show()