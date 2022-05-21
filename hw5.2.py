products = ['bear', 'milk', 'eg', 'eg', 'eg', 'eg']
i = 0
while True:
    if i == len(products):
        break
    if products[i] == 'eg':
        del (products[i])
    else:
        i += 1
print(products)
