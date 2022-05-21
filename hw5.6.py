cars = {'volvo, mustang'}
cars.add('bmw')
print(cars)

cars = {'bmw, mustang'}
cars.clear()
print(cars)

cars = {'toyota, chery, bmw'}
c = cars.copy()
print(c)

q = {'apple', 'banana', 'cherry'}
f = {'google', 'microsoft', 'apple'}

y = q.difference(f)
print(y)


g = {'tiger', 'mount', 'car', 'ball'}
f = {'car', 'foundation', 'ball', 'zoo'}

g.difference_update(f)
print(g)


fruits = {'apple', 'grape', 'pineapple'}
fruits.discard('pineapple')
print(fruits)


w = {'sword', 'gun', 'crossbow'}
i = {'medicine', 'gun', 'painkiller'}

p = w.intersection(i)
print(p)


w = {'sword', 'gun', 'crossbow'}
i = {'medicine', 'gun', 'painkiller'}

w.intersection_update(i)
print(w)


f = {'grape', 'apple', 'pineapple'}
c = {'volvo', 'bmw', 'toyota'}
b = f.isdisjoint(c)

print(b)


a = {'b', 'r', 'e'}
c = {'g', 'h', 'b', 'r', 'e'}
t = a.issubset(c)

print(t)


cars = {'volvo', 'bmw', 'mercedes'}
cars.pop()

print(cars)


company = {'blizzard', 'ubisoft', 'dice'}
company.remove('dice')

print(company)


a = {'b', 'r', 'e', 'm'}
c = {'g', 'h', 'b', 'r', 'e'}
t = a.symmetric_difference(c)

print(t)


a = {'b', 'r', 'e', 'm'}
c = {'g', 'h', 'b', 'r', 'e'}
a.symmetric_difference_update(c)

print(a)


w = {'sword', 'gun', 'crossbow'}
i = {'medicine', 'gun', 'painkiller'}

g = w.union(i)
print(g)


w = {'sword', 'gun', 'crossbow'}
i = {'medicine', 'gun', 'painkiller'}
w.update(i)

print(w)
