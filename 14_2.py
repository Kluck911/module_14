def adder(*nums):
    print(f'аргумент функции', *nums)
    sum_ = 1
    for n in nums:
        print(f'значение n= {n}')
        sum_ *= n

    return sum_


def fact(n):
    if n == 1:
        return 1
    else:
        return n * fact(n - 1)


def rec_fibb(n):
    if n == 1:
        return 1
    if n == 2:
        return 1
    return rec_fibb(n - 1) + rec_fibb(n - 2)

def rec_sum_14_2_3 (n):
    if n == 1:
        return 1
    return n + rec_sum_14_2_3(n - 1)


def rec_reverse14_2_4(string):
    if len(string) == 0:
        return ''
    return string[-1] + rec_reverse14_2_4(string[:-1])


def rec_sum_N_14_2_5(n):
    if n < 10:
        return n
    return n % 10 + rec_sum_N_14_2_5(n // 10)



'''
print(rec_sum_N_14_2_5(152))
print(rec_reverse14_2_4('test'))
print(rec_sum_14_2_3(5))
print(rec_fibb(100))  # 55
print(fact(4))
print(adder(1, 2, 3))
'''
