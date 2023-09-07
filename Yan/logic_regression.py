import matplotlib.pyplot as plt
import numpy as np


x = [-3.1, -1.3, 2, 2.9, 3.6, 5.1, 5.3, 1.4, 1.9, -5]
y = [0, 0, 1, 0, 1, 1, 1, 0, 0, 0]
nu = 5
m,b = 1,10
plt.grid()
plt.scatter(x,y, c="black")

# Логическая функция до обучения
test = np.linspace(-10,10 , num=1000)
a = [1/(1+np.exp(-(m*test[i]+b))) for i in range(len(test))]
plt.plot(test, a, c="red")


for i in range(10):
    pred = [1/(1+np.exp(-(m*x[i]+b))) for i in range(len(x))]
    err = [y[i] - pred[i] for i in range(len(y))]
    print(np.sum(err)/len(err))

    m = nu * np.sum([x[i] * np.sign(err[i]) for i in range(len(x))])/len(x)
    b = nu * np.sum([np.sign(err[i]) for i in range(len(x))])/len(x)


# Логическая функция после обучения
test = np.linspace(-10,10 , num=1000)
a = [1/(1+np.exp(-(m*test[i]+b))) for i in range(len(test))]
plt.plot(test, a, c="green")
plt.show()


y_mean = sum([(1/(1+np.exp(-(m*x[i]+b)))) for i in range(len(x))])/len(y)
Q = sum([(y[i] - y_mean)**2 for i in range(len(y))])
QR = sum([(1/(1+np.exp(-(m*x[i]+b))) - sum(y)/len(y))**2 for i in range(len(x))])
r2 = QR/Q
r = r2 ** 0.5 if m > 0 else (r2 ** 0.5) * -1
print("r2 = ", r2)
print("r = ", r)

