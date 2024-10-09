def call_count():
    global calls
    calls = calls + 1

def string_info(string):
    call_count()
    info_ = []
    info_.append(len(string))
    info_.append(string.lower())
    info_.append(string.upper())
    return tuple(info_)

def is_contains(string, list_to_search):
    call_count()
    is_true = True
    for i in range(len(list_to_search)):
        if string.lower() == list_to_search[i].lower():
            is_true = True
            break
        else:
            is_true = False
    return is_true

calls = 0

print(string_info('Hello'))
print(string_info('Я помню чудное мнгновенье'))
print(is_contains('klauS', ['hahaHA', 'KLAus', 'Braun']))
print(is_contains('Дорога', ['ночь', 'улица', 'фонарь', 'АПТЕКА']))
print(calls)