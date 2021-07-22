"""14.5. Функции  /// Различные задания"""


def linear_solve(a, b):
    if a:
        return b / a
    elif not a and not b:
        return "Бесконечное кол-во корней"
    else:
        return "Нет корней"


def discriminant(a, b, c):
    return b ** 2 - 4 * a * c


def quadratic_solve(a, b, c):
    D = discriminant(a, b, c)
    if D < 0:
        return "Нет вещественных корней"
    elif D == 0:
        return -b / (2 * a)
    else:
        return (-b - D ** 0.5) / (2 * a), \
               (-b + D ** 0.5) / (2 * a)


'''что то пошло не так'''


def min_list(L):
    if len(L) == 1:
        return L[0]
    return L[0] if L[0] < min_list(L[1:]) else min_list(L[1:])


def mirror(a, res = 0):
    return mirror(a // 10, res * 10 + a % 10) if a else res


def equal(N, S):
    if S < 0:
        return False
    if N < 10:
        return N == S
    else:
        return equal(N // 10, S - N % 10)







"""
--------------------------------------------
iter_obj = iter("Hello!")
print(next(iter_obj))
print(next(iter_obj))
print(next(iter_obj))
print(next(iter_obj))
print(next(iter_obj))
print(next(iter_obj))
print(next(iter_obj))
-------------------------------------------
def e():
    n = 1
    while True:
        yield (1 + 1 / n) ** n
        n += 1


last = 0
for a in e():
    if (a - last) < 0.00000001:
        print(a)
        break
    else:
        last = a
----------------------------------------------
print(equal(41, 5))

print(mirror(234))

print(min_list('61562166565'))

print(quadratic_solve(**{'a': 1,
                         'b': 0,
                         'c': -1}))

print(quadratic_solve(*list(map(float, input(f'Введите 3 аргумента функции через пробел: ').split()))))

print(linear_solve(0, 0))
"""
