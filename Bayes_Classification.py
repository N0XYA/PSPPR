import random

import pandas as pd
import statistics as st
import math
import matplotlib.pyplot as plt

# DataFrame = pd.read_excel('baes.xlsx')
DataFrame = pd.read_csv('500_Person_Gender_Height_Weight_Index.csv')

# print(DataFrame.head())
list_of_people = DataFrame.values.tolist()

def getHeightWeight(list):
    height = []
    weight = []
    for row in list:
        height.append(row[1])
        weight.append((row[2]))
    return height, weight


def dividePeople(list_of_people):
    men = []
    women = []
    for line in list_of_people:
        if line[0] == "Male":
            men.append(line)
        else:
            women.append(line)
    return men, women


def getExpected(height, weight):
    mH = st.mean(height)
    mW = st.mean(weight)
    return mH, mW


def getStandartDeviation(height, weight, mH, mW):
    height_dispersion = 0
    weight_dispersion = 0
    for i in range(len(height)):
        height_dispersion += (height[i] - mH)**2
        weight_dispersion += (weight[i] - mW)**2
    height_dispersion = math.sqrt(height_dispersion / len(height))
    weight_dispersion = math.sqrt(weight_dispersion / len(weight))
    return height_dispersion, weight_dispersion


def Bayes():
    men, women = dividePeople(list_of_people)
    men_probability = len(men) / len(list_of_people)
    women_probability = 1 - men_probability
    men_height, men_weight = getHeightWeight(men)
    women_height, women_weight = getHeightWeight(women)
    men_height_M, men_weight_M = getExpected(men_height, men_weight)
    women_height_M, women_weight_M = getExpected(women_height, women_weight)

    men_height_StDeviation, men_weight_StDeviation = getStandartDeviation(men_height, men_weight, men_height_M,
                                                                          men_weight_M)
    women_height_StDeviation, women_weight_StDeviation = getStandartDeviation(women_height, women_weight,
                                                                              women_height_M, women_weight_M)
    print(women_height_StDeviation)

    print(random.uniform(0, 1))
    guess = ""
    return guess


def main():
    unidentified = ['Someone', 186, 73, 2]
    Bayes()

    return


if __name__ == "__main__":
    main()

# def findExpectedValues(list):
#     sumH = 0
#     sumW = 0
#     for line in list:
#         sumH += line[1]
#         sumW += line[2]
#     mH = sumH / len(list)
#     mW = sumW / len(list)
#     return mH, mW
#
#
# def finDispersions(list, mH, mW):
#     numerator_h = 0
#     numerator_w = 0
#     for line in list:
#         numerator_h += (line[1] - mH)**2
#         numerator_w += (line[2] - mW)**2
#     dispersionH = math.sqrt(numerator_h / len(list))
#     dispersionW = math.sqrt(numerator_w / len(list))
#     return dispersionH, dispersionW
#

# list_of_men, list_of_women = dividePeople(list_of_people)
#
# men_prob = len(list_of_men)/len(list_of_people)
# women_prob = 1 - men_prob
#
#
# print(len(list_of_men), len(list_of_women))
# print(men_prob, women_prob)
#
# male_m_height, male_m_weight = findExpectedValues(list_of_men)
# female_m_height, female_m_weight = findExpectedValues(list_of_women)
#
# male_dispersion_height, male_dispersion_weight = finDispersions(list_of_men, male_m_height, male_m_weight)
# female_dispersion_height, female_dispersion_weight = finDispersions(list_of_women, female_m_height, female_m_weight)
# print(male_m_height)
# print(female_m_height)
# print('male d height ->', male_dispersion_height)
# print('female d height ->', female_dispersion_height)
# print(female_m_weight, male_m_weight)
#
# male_height_list = []
# for row in list_of_men:
#     male_height_list.append(row[1])
# print(male_height_list)
#
# plt.plot (male_height_list, norm. pdf (x, 0, 1))