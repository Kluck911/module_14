def even(x):
    return x % 2 == 0


d = {2: "c", 1: "d", 4: "a", 3: "b"}


result = filter(even, [-2, -1, 0, 1, -3, 2, -3])
print(list(result))
print('-----------------------')
print(list(map(lambda x: x ** 2, range(1, 11))))
print('-----------------------')
print(dict(sorted(d.items())))
print('-----------------------')
print(dict(sorted(d.items(), key=lambda x: x[1])))

