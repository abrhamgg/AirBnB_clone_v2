x = {1: 'A', 2: 'B', 3: 'C', 4: 'A'}

s = dict(sorted(x.items(), key= lambda item: item[1]))

print(s)