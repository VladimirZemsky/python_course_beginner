def max_num(first_num, sec_num, third_num):
    if first_num > sec_num and first_num > third_num:

        return first_num

    elif sec_num > third_num:

        return sec_num

    else:

        return third_num


a = int(input('enter first num:'))

b = int(input('enter second num:'))

c = int(input('enter third num:'))

ans = max(a, b, c)

print('largest of three numbers=', ans)
