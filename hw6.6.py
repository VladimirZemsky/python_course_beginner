shedule = {'monday': ['clean house', 'drive car', 'meet with freands'], 'thuesday': None, 'wednesday': ['manicure', 'hammam', 'beer']}

count = (0)

for i in shedule.values():
    if i:
        for k in i:
            count+=1

print(count)
