transactions = [('a','b'), ('a', 'b', 'c'),
                ('a', 'c', 'd'), ('d', 'e'),
                ('d', 'e', 'f')]

first_cluster = [[('a','b'), ('a', 'b', 'c'), ('a', 'c', 'd')],
                [('d', 'e', 'f')]]

second_cluster = [[('a','b'), ('a', 'b', 'c')],
                [('a', 'c', 'd'), ('d', 'e'), ('d', 'e', 'f')]]



def count_e(transactions):
    a = 0
    b = 0
    c = 0
    d = 0
    print(transactions)
    for elements in transactions:
        # print(elements)
        pass
        # a += transactions.count('a')
        # b += transactions.count('b')
        # c += transactions.count('c')
        # d += transactions.count('d')

    return([a, b, c, d])


def count_entries(cluster):
    value = []
    for elements in cluster:
        for transactions in elements:
            value.append(count_e(transactions))
    return(value)

value = count_entries(first_cluster)
print(value)