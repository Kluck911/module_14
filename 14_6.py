def even(x):
    return x % 2 == 0


some_list = [i - 10 for i in range(20)]


def pow2(x): return x ** 2
def positive(x): return x > 0


print(list(map(pow2, filter(positive, some_list))))
print([i**2 for i in some_list if i > 0])
'''
--------------------------------------------
def pow2(x): return x ** 2
def positive(x): return x > 0


print(some_list)
print(list(map(pow2, filter(positive, some_list))))
print([i**2 for i in some_list if i > 0])
---------------------------------------------
def even(x):
    return x % 2 == 0


result = filter(even, [-2, -1, 0, 1, -3, 2, -3])
print(list(result))
----------------------------------------------
L = ['THIS', 'IS', 'LOWER', 'STRING']

print(list(map(str.lower, L)))
-----------------------------------------------
'''