import pandas as pd


transactions = pd.read_excel('transactions.xlsx')
f2 = {}
f2_form = {}
f3 = []


for i in range(len(transactions.columns)):
    col = transactions.columns[i]
    while i < len(transactions.columns) - 1:
        next_col = transactions.columns[i+1]

        two_cols = pd.concat([
            transactions[col],
            transactions[next_col]
        ], axis=1)

        sum = two_cols.sum(axis = 1)
        count = 0
        for rows in sum:
            if rows == 2:
                count += 1

        f2[col + ' ' + next_col] = count
        # print(col, next_col, count)
        # print("--------")
        i += 1


print("МНОЖЕСТВО f2\n")
for keys in f2:

    print(keys, f2[keys])
    if f2[keys] >= 4:
        f2_form[keys] = f2[keys]


print("=====")


def check(index):
    count = 0
    for i in range(len(index) - 1):
        check_index = [index[i]]
        for k in range(1, len(index)):
            if check_index[0] == index[k]:
                continue
            check_index.append(index[k])
            if len(check_index) == 3:
                check_index.pop(1)
            string = ''
            for elem in check_index:
                string += elem + ' '
            string = string[:-1]
            if f2[string] >= 4:
                count += 1

        if count == 3:
            f3.append(index)
    return


f2_df = pd.DataFrame([f2_form])


print("\nМНОЖЕСТВО f3\n")
for i in range(len(f2_df.columns)):
    key = f2_df.columns[i]
    key_f = key.split(" ")[0]
    while i < len(f2_df.columns) - 1:
        next_key = f2_df.columns[i + 1]
        next_key_f = next_key.split(" ")[0]
        if key_f == next_key_f:

            new_index = key_f, key.split(" ")[1],  next_key.split(" ")[1]

            print(new_index)
            check(new_index)

        i += 1


# temp = []
# for x in f3:
#     if x not in temp:
#         temp.append(x)
# f3 = temp


print("\nНЕСВЯЗЫВАЕМЫЕ НАБОРЫ\n")
for row in f3:
    print(row)


def associate_rules(list):
    for row in list:
        for item in range(len(row)):
            pass
    return


associate_rules(f3)