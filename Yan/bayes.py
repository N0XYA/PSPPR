import math

data = [
    [1, 1, 0, 1],[0, 0, 1, 1],[1, 0, 1, 0],[1, 1, 0, 1],[0, 1, 1, 1],
    [1, 1, 0, 0],[0, 0, 1, 0],[1, 0, 1, 1],[1, 1, 0, 0],[0, 0, 1, 0]
]
x1 = [1, 1, 1]
x2 = [0, 1, 0]
x3 = [1, 0, 1]
def go(x, data):
    C1, C2 = 0, 0
    for item in data:
        if item[-1] == 1: C1 += 1
        else: C2 += 1
    PC1 = C1/(C1+C2)
    PC2 = C2/(C1+C2)
    print("PC1", PC1)
    print("PC2", PC2)
    xC1 = list()
    xC2 = list()
    for i in range (len(x)):
        countC1 = 0
        countC2 = 0
        for item in data:
            if item[i] == x[i] and item[-1] == 1: countC1 +=1
            if item[i] == x[i] and item[-1] == 0: countC2 +=1
        xC1.append(countC1/C1)
        xC2.append(countC2/C2)

    print('Р(Х|Выплатит=Да)', math.prod(xC1))
    print('Р(Х|Выплатит=Нет)', math.prod(xC2))
    print('Р(Х|Выплатит=Да)×Р(Выплатит=Да)', math.prod(xC1) * PC1)
    print('Р(Х|Выплатит=Нет)×Р(Выплатит=Нет)', math.prod(xC2) * PC2)
    print(math.prod(xC1) * PC1 / (math.prod(xC1) * PC1 + math.prod(xC2) * PC2) * 100 )
    print(math.prod(xC2) * PC2 / (math.prod(xC2) * PC2 + math.prod(xC1) * PC1) * 100 )

go(x1, data)
print("====================================")
go(x2, data)
print("====================================")
go(x3, data)

