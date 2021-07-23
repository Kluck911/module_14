data = [
   (82, 191),
   (68, 174),
   (90, 189),
   (73, 179),
   (76, 184)
]

a = ["asd", "bbd", "ddfa", "mcsa"]

print('Отсортировано по ключу:\n', sorted(data))
print('Отсортировано по значению:\n', sorted(data, key=lambda x: x[1]))
print('Отсортировано по ИМТ:\n', sorted(data, key=lambda x: x[0]/((x[1] * 100) ** 2)))
print('=================================')
print('Минимальный индекс - ', min(data, key=lambda x: x[0]/((x[1] * 100) ** 2)))
print('=================================')
print([len(i) for i in a])
print({i: len(i) for i in a})
