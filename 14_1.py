# объявили функцию для подсчета количества символов в тексте
def char_frequency(text):
    text = text.lower()
    text = text.replace(" ", "")
    text = text.replace("\n", "")

    count = {}  # для подсчета символов и их количества
    for char in text:
        if char in count:  # если символ уже встречался, то увеличиваем его количество на 1
            count[char] += 1
        else:
            count[char] = 1

    for char, cnt in count.items():
        print(f"Символ {char} встречается {cnt} раз")


# Задание 14.1.1 Напишите функцию print_2_add_2, которая будет складывать 2 и 2

def print_2_add_2():
    print(2 + 2)


def hello_world():
    print('Hello World')


# вызвали функцию в любом месте программы

def pow_func(base, n=2):
    inside_result = base ** n
    return inside_result


def is_divisor(a, n):
    if a % n:
        print(f'число {n} не является делитедем числа {a}')
    else:
        print(f'число {n} является делителем числа {a}')


def rev_ladder(n):
    for i in range(n, 0, -1):
        print("*"*i)


def get_multipliers(a):
    count = 0
    for i in range(1, a + 1):
        if not a % i:
            count += 1
    return count


def check_palindrome(str_):
    str_ = str_.lower()
    str_ = str_.replace(" ", "")

    if str_ == str_[::-1]:
        return True
    else:
        return False


temp_text = """
   У лукоморья дуб зелёный;
   Златая цепь на дубе том:
   И днём и ночью кот учёный
   Всё ходит по цепи кругом;
   Идёт направо -- песнь заводит,
   Налево -- сказку говорит.
   Там чудеса: там леший бродит,
   Русалка на ветвях сидит;
   Там на неведомых дорожках
   Следы невиданных зверей;
   Избушка там на курьих ножках
   Стоит без окон, без дверей;
   Там лес и дол видений полны;
   Там о заре прихлынут волны
   На брег песчаный и пустой,
   И тридцать витязей прекрасных
   Чредой из вод выходят ясных,
   И с ними дядька их морской;
   Там королевич мимоходом
   Пленяет грозного царя;
   Там в облаках перед народом
   Через леса, через моря
   Колдун несёт богатыря;
   В темнице там царевна тужит,
   А бурый волк ей верно служит;
   Там ступа с Бабою Ягой
   Идёт, бредёт сама собой,
   Там царь Кащей над златом чахнет;
   Там русский дух... там Русью пахнет!
   И там я был, и мёд я пил;
   У моря видел дуб зелёный;
   Под ним сидел, и кот учёный
   Свои мне сказки говорил.
   """
char_frequency(temp_text)
print_2_add_2()
hello_world()
pow_func(3)
pow_func(4, 2)
is_divisor(5, 2)
rev_ladder(10)
print(pow_func(3))
outside_result = pow_func(3)
print(outside_result)
print(get_multipliers(4))
print(check_palindrome("test"))
print(check_palindrome("Кит на море не романтик"))