import matplotlib.pyplot as plt


x = [242, 290, 340, 363, 430, 450, 500, 390, 450, 500]
y = [23.2, 24, 23.9, 26.3, 26.5, 26.8, 27.6, 27.6, 28.5, 28.4]
# x = [1, 2, 3, 4, 5]
# y = [2, 4, 5, 4, 5]

def go(x, y):
    plt.scatter(x, y)
    
    x_mean = sum(x)/len(x)
    y_mean = sum(y)/len(y)
    
    x_pred = [ x - x_mean for x in x]
    y_pred = [ y - y_mean for y in y]

    print('x - *x', x_pred)
    print('y - *y', y_pred)

    b1 = sum([x_pred[i] * y_pred[i] for i in range(len(x_pred))]) / sum([x ** 2 for x in x_pred])
    b0 = y_mean -  b1 * x_mean 
    print('b1', b1)
    print('b0', b0)


    y_func = [b0 + b1 * x for x in x]
    plt.plot(x, y_func, c="pink")
    plt.show()


    Q = sum([y_pred**2 for y_pred in y_pred])
    QR = sum([ (y_func[i] - y_mean) ** 2 for i in range(len(y_func))])
    QE = sum([ (y[i] - y_func[i]) ** 2 for i in range(len(y))])
    ESKO =  QE/ (len(x) - 2)
    EST = ESKO ** 0.5
    r2 = QR/Q   #Детерминация
    r = r2 ** 0.5 if b1 > 0 else (r ** 0.5 ) * -1   #Корреляция


    print("ESKO = ", ESKO)
    print("EST = ", EST)
    print("Q = ", Q)
    print("QR = ", QR)
    print("QE = ", QE)
    print("r2 = ", r2)
    print("r = ", r)
    return b1, b0


b1, b0 = go(x, y)
xtest = 700
#print(b0 + b1 * xtest)