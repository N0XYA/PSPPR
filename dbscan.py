import pickle
import matplotlib.pyplot as plt
import random
import math

obj = [[1, 3], [3, 3], [4, 3], [5, 3],
            [1, 2], [4, 2], [1, 1], [2, 1]]
m = 3
e = 2

# Достаем координаты из файла

# with open("Coordinates.pickle", "rb") as file:
#     obj = pickle.load(file)
# file.close()



def count_coords(coodinate, object, e):
    coords = []
    for point in object:
        if math.dist(point, coodinate) < e:
            coords.append(point)
    return len(coords)


def dbscan(object, m, e):
    clusters = 0
    noize = []
    unmarked = object
    print(type(unmarked), len(unmarked))
    while len(unmarked) != 0:
        coordinate = random.choice(unmarked)
        print(coordinate)
        points_in_e = count_coords(coordinate, unmarked, e)
        print(points_in_e)
        if points_in_e < m:
            noize.append(coordinate)
            unmarked.remove(coordinate)
        else:
            clusters += 1
            
            unmarked.remove(coordinate)
    print(noize)
    return


dbscan(obj, m, e)
'''
Вывод графика
'''
# x = [coord[0] for coord in obj]
# y = [coord[1] for coord in obj]
# plt.scatter(x, y)
# plt.show()