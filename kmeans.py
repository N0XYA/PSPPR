import random
import matplotlib.pyplot as plt
import math


xrange = 1000
yrange = 1000
test_obj = [[1, 3], [3, 3], [4, 3], [5, 3],
            [1, 2], [4, 2], [1, 1], [2, 1]]

num_of_clusters = 3


def create_obj(xrange, yrange):
    object = []
    num_of_objects = 30
    print('obj len = ', num_of_objects)
    for i in range(0, num_of_objects):
        coord = [random.uniform(-xrange, xrange), random.uniform(-yrange, yrange)]
        object.append(coord)
    return object


def choose_centers(obj):
    centers = []
    i = 0

    while i < num_of_clusters:
        item = random.choice(obj)
        if item not in centers:
            centers.append(item)
            i += 1
    # for i in range(0, num_of_clusters):
    #     centers.append(random.choice(obj))
    return centers


def get_key(dict, value):
    for k , v in dict.items():
        if v == value:
            return k


def choose_cluster(centers, object):
    clusters = {}
    err_square = 0.0
    for item in centers:
        item = tuple(item)
        clusters[item] = []

    for coordinates in object:
        # print('coords are:', coordinates)
        distance = {}
        for item in centers:
            item = tuple(item)
            distance[item] = round(math.dist(item, coordinates), 2)
        # print(distance, coordinates)
        min_distance = min(distance.values())
        key = get_key(distance, min_distance)
        # print('min', min_distance)
        # print('точка', coordinates, 'принадлежит кластеру с центром в ', key)
        # print(type(key))
        clusters[key].append(coordinates)
        err_square += min_distance ** 2

    return clusters, err_square


def new_centers(clusters):
    centers_arr = []
    for items in clusters:
        center = []
        x_arr = []
        y_arr = []
        for coordinates in clusters[items]:
            x_arr.append(coordinates[0])
            y_arr.append(coordinates[1])

        centroid_x = sum(x_arr) / len(x_arr)
        centroid_y = sum(y_arr) / len(y_arr)

        center.append(centroid_x)
        center.append(centroid_y)

        centers_arr.append(center)
    return centers_arr


def main():
    test_obj = create_obj(xrange, yrange)
    centers = choose_centers(test_obj)
    # centers = [[1, 1],[2, 1]]
    clusters, old_err = choose_cluster(centers, test_obj)
    centers = new_centers(clusters)

    delta = 30
    centers_dots = []
    iteration = 1
    while delta >= 2:
        print('iter', iteration)
        print('old err', old_err)
        clusters, err = choose_cluster(centers, test_obj)
        print('err', err)
        centers = new_centers(clusters)
        delta = old_err - err
        old_err = err
        iteration += 1
        centers_dots.append(centers)
    print('centers are', centers)

    for clust in clusters.values():
        x = [coord[0] for coord in clust]
        y = [coord[1] for coord in clust]
        kx = [coord[0] for coord in clusters]
        ky = [coord[1] for coord in clusters]
        plt.scatter(x, y)
        plt.scatter(kx, ky, color = 'black', marker= 'x')

    plt.show()


if __name__ == "__main__":
    main()