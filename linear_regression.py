import pandas as pd
from decimal import Decimal
import math
import matplotlib.pyplot as plt


def regression(coordinates):
    x = [coordinate[0] for coordinate in coordinates.values]
    x.insert(0, coordinates.columns.values.tolist()[0])
    y = [coordinate[1] for coordinate in coordinates.values]
    y.insert(0, coordinates.columns.values.tolist()[1])
    LENGTH = len(x)
    xmean = sum(x) / LENGTH
    ymean = sum(y) / LENGTH
    xmean = round(xmean, 1)
    xerr = []
    for i in range(len(x)):
        xi = float(x[i])
        value = xi - xmean
        value = round(value, 1)
        print(value)
        xerr.append(value)
    sum_x_err = 0
    for value in xerr:
        sum_x_err+=value
    
    print(sum_x_err)



    return
def main():

    df = pd.read_excel('lingres_xy.xlsx')
    regression(df)

    # plot
    #
    # plt.scatter(x, y)
    # plt.show()
    return 0

if __name__ == "__main__":
    main()