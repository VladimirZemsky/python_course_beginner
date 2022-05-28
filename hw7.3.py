first_list = [1, 2, 3]
sec_l = [11, 22, 33]


def list_gen():
    comb_list = zip(first_list, sec_l)
    new_l = [i for sublist in comb_list for i in sublist]
    return new_l


print(list_gen())
