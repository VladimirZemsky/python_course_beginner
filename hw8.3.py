def sort_tuples(some_tup):
    lst = len(some_tup)
    for i in range(0, lst):
        for u in range(0, lst - i - 1):
            if some_tup[u][1] > some_tup[u + 1][1]:
                temp = some_tup[u]
                some_tup[u] = some_tup[u + 1]
                some_tup[u + 1] = temp
    return some_tup


random_tup = [('Arsenal', 13), ('Man_City', 8), ('Man_United', 13), ('Chelsea', 6)]

print(sort_tuples(random_tup))
