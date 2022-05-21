numbers = [12, 22, 66, 44, 76, 534]
has_odd = False
i = 0
while not i >= len(numbers):
    if numbers[i] % 2 == 1:
        print('no')
        has_odd = True
        break
    i += 1
if not has_odd:
    print('all numbers are even')
