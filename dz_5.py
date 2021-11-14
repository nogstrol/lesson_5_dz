src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

unique = []
repeated = []
for el in src:
    if el in repeated:
        continue
    if el in unique:
        repeated.append(el)
        unique.remove(el)
        continue
    unique.append(el)

print(unique)
