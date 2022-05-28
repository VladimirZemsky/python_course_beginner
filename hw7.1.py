def sides(u):
    p = 4 * u
    d = (u ** 2) / 2
    d = d ** 0.5
    s = u * u

    x = (p, s, d)

    return x


print(sides(10))
