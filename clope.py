transactions = [('a','b'), ('a', 'b', 'c'),
                ('a', 'c', 'd'), ('d', 'e'),
                ('d', 'e', 'f')]

first_cluster = [[('a','b'), ('a', 'b', 'c'), ('a', 'c', 'd')],
                [('d', 'e'), ('d', 'e', 'f')]]

second_cluster = [[('a','b'), ('a', 'b', 'c')],
                [('a', 'c', 'd'), ('d', 'e'), ('d', 'e', 'f')]]



def find_unique_items(transactions):
    # uniques = {}
    uniques = []
    for elements in transactions:
        for item in elements:
            if item not in uniques:
                # uniques[item] = 0
                uniques.append(item)
    return(uniques)


def count_items(cluster, unique_items):
    for transactions in cluster:
        uniques = []
        count = 0
        for elements in transactions:
            print(elements)
            for unique in unique_items:
                if unique in elements:
                    count += 1
                    if unique not in uniques:
                        uniques.append(unique)
        print(count, len(uniques))
        uniques.clear
    return

unique_items = find_unique_items(transactions)
count_items(first_cluster, unique_items)

# value = count_entries(first_cluster)
# print(value)