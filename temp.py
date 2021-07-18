# установим аргумент name_arg пустым а внутри функции будем проверять его
def correct_func(name_arg=None):
   if name_arg is None:
       name_arg = []
   print("Аргумент до изменения", name_arg)
   name_arg.append(1)
   print("Аргумент после изменения", name_arg)

def fact(n):
    if n==1:
        return 1
    else:
        return n * fact(n - 1)
