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


print(quadratic_solve(4, 4, 1))

"""
print(linear_solve(0, 0))
"""
