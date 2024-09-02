immutable_var = (1, True, 'fox')
print(immutable_var)

# следующая строка приведет к ошибке т.к. кортеж является неизменяемой последовательностью
# immutable_var[0] = 5

mutable_list = [10, 'tree', False]
mutable_list[2] = True
print(mutable_list)