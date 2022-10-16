x = {1: 2, 2: 3, 3: 0, 4: -1}

s = dict(sorted(x.items(), key= lambda item: item[1]))

print(s)