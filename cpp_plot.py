import matplotlib.pyplot as plt

file = open("cpp_lin_regression.txt", 'r')

coordinates = []
for line in file:
    line = line.replace('\n', '')
    coordinates.append(line.split(','))

b0, b1 = float(coordinates[-1][0]), float(coordinates[-1][1])
coordinates.pop(-1)
x = [float(_[0]) for _ in coordinates]
y = [float(_[1]) for _ in coordinates]
reg = [b0 + b1 *_ for _ in x]
plt.scatter(x, y)
plt.plot(x, reg)
plt.show()