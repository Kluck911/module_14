def fib():
    a, b, = 1, 1
    yield a
    yield b

    while True:
        a, b = b, a + b
        yield b


def count(start = 1, step = 1):
    counter = start

    while True:
        yield counter
        counter += step


def repeat_list(list_):
   list_values = list_.copy()
   while True:
       value = list_values.pop(0)
       list_values.append(value)
       yield value


pos = int(input(f'Введите позицию  числа Фибоначи = '))

for num in fib():
    pos -= 1
    if pos == 0:
        print(num)
        break

""""
for i in repeat_list([1, 2, 3]):
   print(i)

for num in count(1000, 1000):
    print(num)

for num in fib():
    print(num)
"""
