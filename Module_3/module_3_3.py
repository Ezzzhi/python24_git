# Задача "Распаковка"
# 1. Функция с параметрами по умолчанию:
def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

print_params()
print_params(False, 2, 3.5)
print_params(b = 25)
print_params(c = [1,2,3])

# 2. Распаковка параметров:
value_list = ['example', (5, 6, 'go'), {"i": 'zero', "j": 'one', "k": 2}]
value_dict = {"a": 'zero', "b": True, "c": 2.66}
print_params(*value_list)
print_params(**value_dict)

# 3. Распаковка + отдельные параметры:
values_list_2 = ['true', False]
print_params(*values_list_2, 42)
