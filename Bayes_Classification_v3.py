import pandas as pd
import statistics as st
import math
import matplotlib.pyplot as plt


#ОБУЧЕНИЕ МОДЕЛИ


def dividePeople(list_of_people):
    men = []
    women = []
    for line in list_of_people:
        if line[0] == "Male":
            men.append(line)
        else:
            women.append(line)
    return men, women


def getHeight(people):
    height = []
    for row in people:
        height.append(row[1])
    return height


def getWeight(people):
    weight = []
    for row in people:
        weight.append(row[2])
    return weight


def GaussDist(param, mu, sigma):
    distibution = []
    for value in param:
        degree = -1 * (((value - mu) ** 2) / (2 * sigma ** 2))
        distibution.append(math.exp(degree) / (math.sqrt(2 * math.pi * sigma)))
    return distibution


def makeDict(param, normal):
    dict = {}
    for i in range(len(param)):
        dict[param[i]] = normal[i]
    return dict


def toFloat(list):
    float = list[0]
    return float
DataFrame = pd.read_csv('gender_height_weight.csv')
list_of_people = DataFrame.values.tolist()
men_l, women_l = dividePeople(list_of_people)
#Вероятность кластеров
men_probability = len(men_l) / len(list_of_people)
women_probability = 1 - men_probability

menHeight, menWeight = getHeight(men_l), getWeight(men_l)
womenHeight, womenWeight = getHeight(women_l), getWeight(women_l)
#Мат. ожидание
mHeightMean, mWeightMean = st.mean(menHeight), st.mean(menWeight)
wHeightMean, wWeightMean = st.mean(womenHeight), st.mean(womenWeight)
#Среднеквадратическое отклонение
mHeightStD, mWeightStD = st.stdev(menHeight), st.stdev(menWeight)
wHeightStD, wWeightStD = st.stdev(womenHeight), st.stdev(womenWeight)
#Значения функции нормального распределения (Вероятность)
mHeightNormal, mWeightNormal = GaussDist(menHeight, mHeightMean, mHeightStD), GaussDist(menWeight, mWeightMean,
                                                                                          mWeightStD)
wHeightNormal, wWeightNormal = GaussDist(womenHeight, wHeightMean, wHeightStD), GaussDist(womenWeight, wWeightMean,
                                                                                          wWeightStD)

mHeightDict, mWeightDict = makeDict(menHeight, mHeightNormal), makeDict(menWeight, mWeightNormal)
wHeightDict, wWeightDict = makeDict(womenHeight, wHeightNormal), makeDict(womenWeight, wWeightNormal)
#ОБУЧЕНИЕ ЗАВЕРШЕНО!

#ОПРЕДЕЛЯЕМ ОБЪЕКТ
unknown = [['Unknown', 186, 74, "doesn't matter"]]
#См в дюймы и кг в фунты
unknown[0][1] = unknown[0][1] * 0.393701
unknown[0][2] = unknown[0][2] * 2.20462
uHeight = getHeight(unknown)
uWeight = getWeight(unknown)
# uHGauss = GaussDist(uHeight, uHeight, 0)
# uWGauss = GaussDist(uWeight, uWeight, 0)


#Нахождение вероятностей принадлежности к кластерам
PmHeightNormal, PmWeightNormal = GaussDist(uHeight, mHeightMean, mHeightStD), GaussDist(uWeight, mWeightMean,
                                                                                        mWeightStD)
PwHeightNormal, PwWeightNormal = GaussDist(uHeight, wHeightMean, wHeightStD), GaussDist(uWeight, wWeightMean,
                                                                                        wWeightStD)
#Конвертация list to float (3:12 ночи)
PmHeightNormal = toFloat(PmHeightNormal)
PmWeightNormal = toFloat(PmWeightNormal)
PwHeightNormal = toFloat(PwHeightNormal)
PwWeightNormal = toFloat(PwWeightNormal)

if PmHeightNormal > PwHeightNormal:
    yH = PmHeightNormal
else:
    yH = PwHeightNormal

if PmWeightNormal > PwWeightNormal:
    yW = PmWeightNormal
else:
    yW = PwWeightNormal

# uHeight = toFloat(uHeight)
ManProbability = men_probability * PmHeightNormal * PmWeightNormal
WomanProbability = women_probability * PwHeightNormal * PwWeightNormal

print("Man prob ->", ManProbability)
print("woman prob ->", WomanProbability)

if ManProbability > WomanProbability:
    guess = "Man"
else:
    guess = "Woman"

print("Guess ->", guess)
#Вывод графика
fig, axs = plt.subplots(nrows=1, ncols=2)
axs[0].scatter(mHeightDict.keys(), mHeightDict.values())
axs[0].scatter(wHeightDict.keys(), wHeightDict.values())
axs[0].axvline(uHeight, ymin=0, ymax=1, c='black')
axs[0].scatter(uHeight, yH, marker= "x", c='red')
axs[1].scatter(mWeightDict.keys(), mWeightDict.values())
axs[1].scatter(wWeightDict.keys(), wWeightDict.values())
axs[1].axvline(uWeight, ymin=0, ymax=1, c='black')
axs[1].scatter(uWeight, yW, marker= "x", c='red')
plt.show()