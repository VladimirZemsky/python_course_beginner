def random_dec(func):
    def construction(*args, **kwargs):
        returned_value = func(*args, **kwargs)

        return returned_value

    return construction


@random_dec
def sum_numb(f_element, s_element):
    return f_element + s_element


a, b = 3, 7
print('sum =', sum_numb(a, b))
