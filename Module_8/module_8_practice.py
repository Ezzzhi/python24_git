def calc(line_):
    num_1, operation, num_2 = line_.split(' ')
    num_1 = int(num_1)
    num_2 = int(num_2)
    if operation == '+':
        return num_1 + num_2
    if operation == '-':
        return num_1 -num_2
    if operation == '*':
        return num_1 * num_2
    if operation == '//':
        return num_1 // num_2
    if operation == '/':
        return num_1 / num_2
    if operation == '%':
        return num_1 % num_2

with open(r'D:\_Python24\Module_8\Модуль_8_допмат\python_snippets\calc.txt', 'r') as file:
    sum_ = 0
    cnt = 0
    errors = 0
    for line in file:
        cnt += 1
        try:
            res = calc(line)
            if isinstance(res, int) or isinstance(res, float):
                sum_ += 1
            else:
                print(res)
        except ValueError as exc:
            errors += 1
            if 'unpack' in exc.args[0]:
                print(f'{cnt}: "{line.strip("\n")}" - Not enough data in line')
            elif 'int' in exc.args[0]:
                print(f'{cnt}: "{line.strip("\n")}" - Wrong order in line')
            else:
                print(f'{exc.args}')

    print()
    print(f'Сумма: {sum_}, Ошибок: {errors}')
