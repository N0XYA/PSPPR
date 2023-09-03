import matplotlib.pyplot as plt
import random
import math

colors = ["red", "blue", "green"]

def go(k, x, y, m):
    
    klist = [ [] for i in range (k) ]
    e = 0

    for k in range (len(x)):
        count = 0
        minDist = math.dist(m[0], [x[k], y[k]])
        for i in range (len(m)):
            if math.dist(m[i], [x[k], y[k]]) < minDist:
                minDist = math.dist(m[i], [x[k], y[k]])
                count = i
        klist[count].append([x[k], y[k]])
        e += minDist ** 2
    print(e)

    for item in klist:
        print(item)
    for i in range(len(klist)):
        for dot in klist[i]:
            plt.scatter(dot[0], dot[1], c=colors[i])
            plt.scatter(m[i][0], m[i][1], c="black", marker="*", s = 100)
            plt.xlabel("SepalLength")
            plt.ylabel("PetalLength")
    plt.show()

    newM = list()
    for cluster in klist:
        x, y = 0, 0
        for dot in cluster:
            x += dot[0]
            y += dot[1]
        if len(cluster) != 0:
            newM.append([x/len(cluster), y/len(cluster)])
    return newM, e
    
    

SepalLength = [2.1, 1.9, 2.7, 1.6, 3.0, 7.9, 9.2, 6.3, 8.9, 7.3]
PetalLength = [1.0, 1.4, 1.3, 1.5, 6.1, 4.9, 7.0, 7.5, 6.9, 7.4]

m = [[random.randint(0, 9), random.randint(0, 9)] for i in range(2)]



oldE = 999
while(True):
    m, e = go(2, SepalLength, PetalLength, m)

    if oldE == e: break
    else: oldE = e
