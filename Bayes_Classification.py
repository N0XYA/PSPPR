import pandas as pd
import math
import matplotlib.pyplot as plt

# DataFrame = pd.read_excel('baes.xlsx')
DataFrame = pd.read_csv('500_Person_Gender_Height_Weight_Index.csv')

print(DataFrame.head())


def dividePeople(list_of_people):
    men = []
    women = []
    for line in list_of_people:
        if line[0] == "Male":
            men.append(line)
        else:
            women.append(line)
    return men, women


def findExpectedValues(list):
    sumH = 0
    sumW = 0
    for line in list:
        sumH += line[1]
        sumW += line[2]
    mH = sumH / len(list)
    mW = sumW / len(list)
    return mH, mW


def finDispersions(list, mH, mW):
    numerator_h = 0
    numerator_w = 0
    for line in list:
        numerator_h += (line[1] - mH)**2
        numerator_w += (line[2] - mW)**2
    dispersionH = math.sqrt(numerator_h / len(list))
    dispersionW = math.sqrt(numerator_w / len(list))
    return dispersionH, dispersionW

list_of_people = DataFrame.values.tolist()
list_of_men, list_of_women = dividePeople(list_of_people)

men_prob = len(list_of_men)/len(list_of_people)
women_prob = 1 - men_prob


print(len(list_of_men), len(list_of_women))
print(men_prob, women_prob)

male_m_height, male_m_weight = findExpectedValues(list_of_men)
female_m_height, female_m_weight = findExpectedValues(list_of_women)

male_dispersion_height, male_dispersion_weight = finDispersions(list_of_men, male_m_height, male_m_weight)
female_dispersion_height, female_dispersion_weight = finDispersions(list_of_women, female_m_height, female_m_weight)
print(male_m_height)
print(female_m_height)
print('male d height ->', male_dispersion_height)
print('female d height ->', female_dispersion_height)
print(female_m_weight, male_m_weight)

male_height_list = []
for row in list_of_men:
    male_height_list.append(row[1])
print(male_height_list)

plt.plot (male_height_list, norm. pdf (x, 0, 1))