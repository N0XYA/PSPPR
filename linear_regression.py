import pandas as pd
import matplotlib.pyplot as plt


def regression(coordinates):
    x = [coordinate[0] for coordinate in coordinates.values]
    x.insert(0, coordinates.columns.values.tolist()[0])
    y = [coordinate[1] for coordinate in coordinates.values]
    y.insert(0, coordinates.columns.values.tolist()[1])
    print(x)
    xmean = sum(x)
    ymean = sum(y)
    print(xmean, ymean)
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