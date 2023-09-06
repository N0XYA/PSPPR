import pandas as pd
from decimal import Decimal
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
    x = [coordinate[0] for coordinate in coordinates.values]
    x.insert(0, coordinates.columns.values.tolist()[0])
    y = [coordinate[1] for coordinate in coordinates.values]
    y.insert(0, coordinates.columns.values.tolist()[1])
    # x = [13, 20, 17, 15, 16, 12, 16, 14, 10, 11]
    # y = [1000, 600, 500, 1200, 1000, 1500, 500, 1200, 1700, 2000]
    # x = [1, 2, 3, 4, 5]
    # y = [2, 4, 5, 4, 5]
    plt.scatter(x, y)

    xmean = sum(x) / len(x)
    ymean = sum(y) / len(y)

    x_err = [x - xmean for x in x]
    y_err = [y - ymean for y in y]

    x_square_err, x_sq_list = find_square_err(x_err)
    y_square_err, y_sq_list = find_square_err(y_err)
    b1 = sum([x_err[i] * y_err[i] for i in range(len(x_err))]) / x_square_err
    b0 = ymean - b1 * xmean

    yt = [b0 + b1 * xc for xc in x]
    DistanceFromMeanSqr = sum([(yt[_] - ymean)**2 for _ in range(len(yt))])
    DistanceFromY = sum([(y[_] - yt[_])**2 for _ in range(len(yt))])
    errSqr = ymean - DistanceFromY / ymean
    # errSqr = DistanceFromMeanSqr / y_square_err
    print("b1:",b1, "b0:", b0)
    # print("R^2 ", errSqr)
    err_mean_sqr = DistanceFromY / (len(x) - 2)
    print("Среднеквадратическая ошибка: = ", err_mean_sqr)
    sqrt_err = math.sqrt(err_mean_sqr)
    print("Стандартная ошибка = ", sqrt_err)

    #TODO:
    #   Изменчивость выходной переменной
    #   Коэф. детерминации
    #   Коэф. корреляции



    plt.plot(x, yt, c="red")
    plt.scatter(x, yt, c="black")
    # plt.show()
    return
def main():
    df = pd.read_excel('lingres_xy.xlsx')
    regression(df)
    return 0

if __name__ == "__main__":
    main()