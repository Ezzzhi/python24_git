#1
immutable_var = (1, 2.6, 'cat', False, [2, 5, 7])
print(immutable_var)

#2
# immutable_var[0] = 5
# print(immutable_var)
# код выдаст ошибку, т.к. класс tuple является
# неизменяемым и нельзя заменить конкретный элемент,
# но можно заменить элементы изменяемого объекта внутри этого списка

#3
mutable_list = ['work', 5, 123.5, (1, 5, 'dog')]
mutable_list[3] = 'Modified'
print(mutable_list)