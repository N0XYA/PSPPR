import random
import matplotlib.pyplot as plt
import math


xrange = 10
yrange = 10
test_obj = [[1, 3], [3, 3], [4, 3], [5, 3],
            [1, 2], [4, 2], [1, 1], [2, 1]]

num_of_clusters = 2


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

# centers = choose_centers(test_obj)

def offset():

    pass

centers = [[1, 1],[2,1]]
print('centers are', centers)
clusters = {}
what_cluster(centers, test_obj)

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