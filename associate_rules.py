import pandas as pd


transactions_table = pd.read_excel('transactions.xlsx')

def get_col_sum(table):
    for name in table:
        if table[name].sum() < 4:
            table = table.drop(columns=[name], axis= 1)
    return table


def merge(table):
    all_pairs = {}
    for i in range(len(table.columns)):  # index of a column
        column = table.columns[i]
        while i < len(table.columns) - 1:
            next_column = table.columns[i+1]
            new_column = pd.concat([
                table[column],
                table[next_column]],
                axis=1)
            summ = new_column.sum(axis=1)

            count = 0 # Считаем количество попаданий в один чек
            for rows in summ:
                if rows == 2:
                    count += 1

            all_pairs[column + ' ' + next_column] = count
            i += 1
    return all_pairs


def print_dict(table):
    print("LENGTH: ", len(table))
    for rows in table:
        print(rows, table[rows])


def make_f2(dict):
    f2 = {}
    for name in dict:
        if dict[name] >= 4:
            f2[name] = dict[name]
    return f2


def make_f3(dict):
    f3 = {}
    names_list = []
    for name in dict:
        names_list.append(name)

    for i in range(len(names_list)):
        first_key = names_list[i]
        first_word = first_key.split(" ")[0]
        while i < len(names_list) - 1:
            second_key = names_list[i + 1]
            second_word = second_key.split(" ")[0]
            if first_word == second_word:
                new_index = first_key +  ' ' + second_key.split(" ")[-1]
            f3[new_index] = 1
            i += 1

    return f3


def find_third(index, first, second):
    third = ''
    for name in index:
        if name != first and name != second:
            third = name
    return third


def support(len):
    sup = round(len / num_of_trans * 100, 1)
    return sup


def reliability(len, f, s):
    key = f + ' ' + s
    for words in all_pairs:
        if key == words:
            value = all_pairs[words]

    rel = round(len / value * 100, 1)
    return rel



def rules_generation(dict):
    sets = []
    for index in dict:
        sets.append(index.split(" "))

    for index in sets:
        for num in range(len(index)):
            first = index[num]
            while num < len(index) - 1:
                second = index[num + 1]
                third = find_third(index, first, second)
                associate = transactions_table.loc[(transactions_table[first] == 1) & (transactions_table[second] == 1)
                & (transactions_table[third] == 1)]
                lengh = len(associate)
                supp = support(lengh)
                rel = reliability(lengh, first, second)
                sc = round(supp * rel, 3)
                print(first, second, '->', third, '|', 'Поддержка - ',  supp, 'Достоверность - ', rel, 'SC - ', sc)
                num += 1
    return



def associate(f, s):
    result = transactions_table.loc[(transactions_table[f] == 1) & (transactions_table[s] == 1)]
    return len(result)


def rel_f2(assos, s):
    all = len(transactions_table.loc[(transactions_table[s] == 1)])
    result = round(assos / all * 100, 1)
    return result

def rules_f2(dict):
    sets = []
    for index in dict:
        sets.append(index.split(" "))

    for pair in sets:
        first = pair[0]
        second = pair[1]
        assoc = associate(first, second)
        sup = support(assoc)
        rel = rel_f2(assoc, first)
        sc = round(sup * rel, 3)
        print(first, second, '|',  'Поддержка - ', sup, 'Достоверность - ',  rel, 'SC - ', sc)

        first = pair[1]
        second = pair[0]
        assoc = associate(first, second)
        sup = support(assoc)
        rel = rel_f2(assoc, first)
        sc = round(sup * rel, 3)
        print(first, second, '|', 'Поддержка - ', sup, 'Достоверность - ',  rel, 'SC - ', sc)
    return


f1 = get_col_sum(transactions_table)
num_of_trans = len(f1.index)
all_pairs = merge(f1)
# print_dict(all_pairs)
f2 = make_f2(all_pairs)
# print_dict(f2)
f3 = make_f3(f2)
# print_dict(f3)
rules_generation(f3)
# rules_f2(f2)
