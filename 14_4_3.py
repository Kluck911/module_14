import time


def decoration_cache(func):
    cache_dict = {}
    def wrapper(num):
        nonlocal cache_dict
        if num not in cache_dict:
            cache_dict[num] = func(num)
            print(f'Добавление результата в кэш: {cache_dict[num]}')
        else:
            print(f'Возвращене результата из кэша: {cache_dict[num]}')
        print(f'Кэш {cache_dict}')
        return cache_dict[num]
    return wrapper

@decoration_cache
def f(num):
   return num ** 100


while True:
    num = int(input('Введите умножаемое число: '))
    t0 = time.time()
    f(num)
    dt = time.time() - t0
    print(f'время выполнения функции = {dt:.1000f}')
    t0 = time.time()
    num ** 100
    dt = time.time() - t0
    print(f'время выполнение умножен = {dt:.1000f}')