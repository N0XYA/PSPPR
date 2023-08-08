import pickle
import matplotlib.pyplot as plt


with open("Coordinates.pickle", "rb") as file:
    obj = pickle.load(file)


print(len(obj))
x = [coord[0] for coord in obj]
y = [coord[1] for coord in obj]
plt.scatter(x, y)
plt.show()