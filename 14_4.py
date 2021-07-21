"""14.4. Замыкания и декораторы"""

import time


def decorator_time(fn):
    def wrapper():
       print(f"Запустилась функция {fn}")
       dt_mean = 0
       for i in range(count):
           t0 = time.time()
           result = fn()
           dt = time.time() - t0
           dt_mean += dt
       print(f"Функция выполнилась {count} раз. Среднее время: {dt_mean / count:.10f}")
       return dt
    return wrapper

@decorator_time
def pow_2():
   return 10000000000000000000000000 ** 10000

@decorator_time
def in_build_pow():
   return pow(10000000000000000000000000, 10000)


count = int(input(f'Введите кол-во выполнений = '))
if count < 1:
    print('Количество выполенний должно быть более 0')
    raise SystemExit

pow_2()
in_build_pow()