def my_decorator(fn):
    print("Этот код будет выведен один раз в момент декорирования функции")

    def wrapper(*args, **kwargs):
        print('Этот код будет выполняться перед каждым вызовом функции')
        result = fn(*args, **kwargs)
        print('Этот код будет выполняться после каждого вызова функции')
        return result

    return wrapper


def do_it_twice(func):
    count = 0

    def wrapper(*args, **kwargs):
        nonlocal count
        func(*args, **kwargs)
        count += 1
        print(f"Функция {func} была вызвана {count} раз")

    return wrapper


@do_it_twice
def say_word(word):
    print(word)


say_word("Oo!!!")
say_word("Oo!!!")
say_word("Oo!!!")
