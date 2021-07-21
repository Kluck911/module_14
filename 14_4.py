import time


def decorator_time(fn):
   def wrapper():
       print(f"Запустилась функция {fn}")
       dt_total = 0
       for i in range(count) :
           t0 = time.time()
           result = fn()
           dt = time.time() - t0
           print(f"Функция выполнилась {i + 1} раз. Время: {dt:.10f}")
           dt_total += dt_total + dt
       print(f"Функция выполнилась {count} раз. Среднее время: {dt_total / count:.10f}")
       return dt  # задекорированная функция будет возвращать время работы
   return wrapper


def pow_2():
   return 10000000000000000000000000 ** 100000


def in_build_pow():
   return pow(10000000000000000000000000, 100000)

count = int(input(f'Введите кол-во выполнений = '))
pow_2 = decorator_time(pow_2)
in_build_pow = decorator_time(in_build_pow)
pow_2()
in_build_pow()
