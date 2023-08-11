import matplotlib.pyplot as plt
import numpy as np

x = [0.90, 4.11, 4.82, 8.53, 8.90]
y = [1.91, 1.84, 4.47, 6.38, 3.92]

def go(x, y):
    m,b = 1,1
    nu = 0.1

    for i in range (10):
        y_pred = [x * m + b for x in x]

        err = [ abs(y[i] - y_pred[i]) for i in range(0, len(y)) ]
        err_mean = sum(err) / len(err)     
        print("Средняя ошибка: ", err_mean)

        b_change = [ x[i] * np.sign(y[i] - y_pred[i]) for i in range (0, len(y)) ]
        b_mean = sum(b_change) / len(b_change)

        m_change = [ np.sign(y[i] - y_pred[i]) for i in range (0, len(y))]
        m_mean = sum(m_change) / len(m_change)

        m = m + nu * m_mean
        b = b + nu * b_mean
    
    plt.scatter(x, y)
    plt.plot(x, y_pred)
    plt.grid()
    plt.show()

# f(x) = mx + b 
go(x, y)
