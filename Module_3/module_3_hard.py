# Задание "Раз, два, три, четыре, пять .... Это не всё?"

def calculate_structure_sum(data):
    sum_ = 0
    for i in data:
        if isinstance(i, dict):
           i = [element for pair in i.items() for element in pair]
        if isinstance(i, str):
            sum_ = sum_ + len(i)
        elif isinstance(i, int):
            sum_ = sum_ + i
        elif isinstance(i, list) or isinstance(i, tuple) or isinstance(i, set):
            sum_ = sum_ + calculate_structure_sum(i)
        else:
            print('wrong type of data:', i)
            # здесь можно бы поставить break и прервать вычисления, но я предпочел пропустить
            # такие данные (например, float) и подсчитать все остальное
    return sum_


data_structure = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)