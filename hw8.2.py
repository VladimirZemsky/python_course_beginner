def max_f(one, two):
    if one > two:
        return one
    elif two > one:
        return two


f_num = int(input('enter first num'))
s_num = int(input('enter second num'))
t_num = int(input('third second num'))


def sec_f(one, two, three):
    return max_f(three, max_f(one, two))


all_num = sec_f(f_num, s_num, t_num)
print(all_num)
