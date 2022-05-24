some_data = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": "S005"}, {"V": "S009"},
             {"VIII": "S007"}]

smth = []
for d in some_data:
    for i in d.values():
        if i not in smth:
            smth.append(i)

print(smth)
