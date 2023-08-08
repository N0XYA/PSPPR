import random
import matplotlib.pyplot as plt
import math
import pickle

xrange = 10
yrange = 10


def create_obj(xrange, yrange):
    object = []
    num_of_objects = 100
    print('obj len = ', num_of_objects)
    for i in range(0, num_of_objects):
        coord = [random.uniform(-xrange, xrange), random.uniform(-yrange, yrange)]
        object.append(coord)
    return object


obj = create_obj(xrange, yrange)

with open ("Coordinates.pickle", "wb") as file:
    pickle.dump(obj, file)

x = [coord[0] for coord in obj]
y = [coord[1] for coord in obj]
plt.scatter(x, y, c = "black")
plt.show()
