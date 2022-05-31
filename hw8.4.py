import datetime

right_now = datetime.datetime.now()
print(right_now)

year = lambda x: x.year
month = lambda x: x.month
t = lambda x: x.time()

print(year(right_now))

day = lambda x: x.day

print(month(right_now))
print(day(right_now))
print(t(right_now))
