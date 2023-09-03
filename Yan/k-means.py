import matplotlib.pyplot as plt
import random
import math

colors = ["red", "blue", "green"]

def go(k, data, m):
    
    klist = [ [] for i in range (k) ]
    e = 0
    for dot in data:
        count = 0
        minDist = math.dist(m[0], dot)
        for i in range (len(m)):
            if math.dist(m[i], dot) < minDist:
                minDist = math.dist(m[i], dot)
                count = i
        klist[count].append(dot)
        e += minDist ** 2
    print(e)

    for i in range(len(klist)):
        for dot in klist[i]:
            plt.scatter(dot[0], dot[1], c=colors[i])
            plt.scatter(m[i][0], m[i][1], c=colors[i], marker="*")
    plt.show()

    newM = list()
    for cluster in klist:
        x, y = 0, 0
        for dot in cluster:
            x += dot[0]
            y += dot[1]
        newM.append([x/len(cluster), y/len(cluster)])
    return newM, e
    
    

data = [[1, 3], [3, 3], [4, 3], [5, 3], [1, 2], [4, 2],
        [1, 1], [2, 1]]
m = [[random.randint(0, 9), random.randint(0, 9)] for i in range(2)]



oldE = 999
while(True):
    m, e = go(2, data, m)

    if oldE == e: break
    else: oldE = e
