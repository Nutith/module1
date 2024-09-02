my_dict = {'Anton': 2001,
           'Dasha': 2002,
           'Egor': 2003,
           'Masha':2004}

print('Словарь:', my_dict)
print('Существующий ключ:', my_dict['Anton'])
print('Не существующий ключ:', my_dict.get('Andrey', 'Такого имени в словаре нет'))
my_dict.update({'Vladimir': 2005, 'Ivan': 2006})
print('Удалено из словаря:', my_dict.pop('Ivan'))
print('Словарь после добавления и удаления:', my_dict)

my_set = {1, 1, 2, 2, 3, 3, 'fox', 'fox'}

print('Множество:', my_set)
my_set.update({('apple', 'peach'), 1000})
my_set.remove(1000)
print('Множество после изменений:', my_set)