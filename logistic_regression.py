import math

import matplotlib.pyplot as plt
import numpy as np

x = [25, 29, 30, 31, 32, 41, 41, 42, 44, 49, 50, 59, 60, 62, 68, 72, 79, 80, 81, 84]
y = [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 1]


def log_loss(y_true, y_pred):
    ans = 0
    for i in range(len(y_true)):
        ans+= (-1 * y_true[i] * np.log(abs(y_pred[i]))) - ((1 - y_true[i]) * np.log(abs(1 - y_pred[i])))
    return ans
def sigmoid(val):
    return 1 / (1 + math.exp(-val))


class Logistic_regression:
    def __init__(self):
        self.w = []
        for i in range(len(x)):
            self.w.append(np.random.randn() * 0.001)
        self.b = np.random.randn() * 0.001
        self.losses_train = []

    def train(self, x, y, learning_rate = 0.005, epochs = 500):
        for epoch in range(epochs):
            dw = [0 for _ in range(len(x))]
            db = 0

            for i in range(len(x)):
                z = x[i] * self.w[i] + self.b
                a = sigmoid(z)

                dw[i] = (a - y[i]) * x[i]
                db += (a - y[i])

            dw = sum(dw) / len(x)
            db = db / len(x)

            for i in range(len(x)):
                self.w[i] = self.w[i] - learning_rate * dw
            self.b = self.b - learning_rate * db
            self.losses_train = log_loss(y, self.predict(x))

    def predict(self, x):
        ans = [x[i] * self.w[i] + self.b for i in range(len(x))]
        return ans

    def get_weight(self):
        return self.w, self.b

def main():
    logres = Logistic_regression()
    logres.train(x, y, epochs=50000, learning_rate= 0.005)
    plt.scatter(x, y)
    w, b = logres.get_weight()
    px = [x[_] * w[_] + b for _ in range(len(x))]
    plotp = [1 / (1 + math.exp(-_)) for _ in px]
    plt.plot(x, plotp)
    plt.show()
    return 0


if __name__ == "__main__":
    main()