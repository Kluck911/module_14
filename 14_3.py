def fib():
    a, b, = 0, 1
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
   list_
   while True:
       value = list_.pop(0)
       list_.append(value)
       yield value

for num in count(1000, 1000):
    print(num)

""""
for i in repeat_list([1, 2, 3]):
   print(i)

for num in count(1000, 1000):
    print(num)

for num in fib():
    print(num)
"""
