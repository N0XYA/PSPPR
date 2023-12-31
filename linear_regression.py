import pandas as pd
import statistics as st
import math
import matplotlib.pyplot as plt


def find_square_err(coordinate):
    square_err = 0
    square_err_list = []
    for _ in coordinate:
        square_err_list.append(_**2)
        square_err += _**2
    return square_err, square_err_list

def regression(coordinates):
    print("Линейная регрессия/логистическая регрессия (0,1):")
    case = int(input())

    x = [coordinate[0] for coordinate in coordinates.values]
    x.insert(0, coordinates.columns.values.tolist()[0])
    y = [coordinate[1] for coordinate in coordinates.values]
    y.insert(0, coordinates.columns.values.tolist()[1])
    # x = [13, 20, 17, 15, 16, 12, 16, 14, 10, 11]
    # y = [1000, 600, 500, 1200, 1000, 1500, 500, 1200, 1700, 2000]
    x = [1, 2, 3, 4, 5]
    y = [2, 4, 5, 4, 5]

    x = [25, 29, 30, 31, 32, 41, 41, 42, 44, 49, 50, 59, 60, 62, 68, 72, 79, 80, 81, 84]
    y = [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 1]
    xmean = sum(x) / len(x)
    ymean = sum(y) / len(y)

    x_err = [x - xmean for x in x]
    y_err = [y - ymean for y in y]

    x_square_err, x_sq_list = find_square_err(x_err)
    y_square_err, y_sq_list = find_square_err(y_err)
    b1 = sum([x_err[i] * y_err[i] for i in range(len(x_err))]) / x_square_err
    b0 = ymean - b1 * xmean

    yt = [b0 + b1 * xc for xc in x]
    Distance_yi_ymean = sum([(y[_] - ymean) ** 2 for _ in range(len(y))])
    DistanceFromMeanSqr = sum([(yt[_] - ymean) ** 2 for _ in range(len(yt))])
    DistanceFromY = sum([(y[_] - yt[_]) ** 2 for _ in range(len(yt))])
    errSqr = ymean - DistanceFromY / ymean
    # errSqr = DistanceFromMeanSqr / y_square_err
    # print("R^2 ", errSqr)
    err_mean_sqr = DistanceFromY / (len(x) - 2)
    sqrt_err = math.sqrt(err_mean_sqr)

    # Изменчивость выходной переменной
    Q = Distance_yi_ymean
    Qr = DistanceFromMeanSqr
    Qe = DistanceFromY

    r_sqr = Qr / Q

    correlatio = math.sqrt(r_sqr)
    if b1 < 0:
        correlatio = -correlatio

    if case == 0:
        print("b1:", b1, "b0:", b0)
        print("Среднеквадратическая ошибка: = ", err_mean_sqr)
        print("Стандартная ошибка = ", sqrt_err)
        print("Изменчивость выходной переменной:")
        print("Q = ", Q, ", Qr = ", Qr, ", Qe = ", Qe)
        print("Коэфф. детерминации: ", r_sqr)
        print("Коэфф. корреляции:", correlatio)
        plt.scatter(x, y)
        plt.plot(x, yt, c="red")
        plt.scatter(x, yt, c="black")
        plt.show()

    elif case == 1:
        plt.plot(x, yt, c="red")
        plt.scatter(x, yt, c="black")
        for i in range(len(y)):
            if y[i] < ymean:
                y[i] = 0
            else:
                y[i] = 1
        plt.scatter(x, y)
        px = [math.exp(_) / 1 + math.exp(_) for _ in yt]
        plt.scatter(x, px)
        plt.show()
    else:
        print("Введите значение (1,2)")

    return
def main():
    df = pd.read_excel('lingres_xy.xlsx')
    regression(df)
    return 0

if __name__ == "__main__":
    main()