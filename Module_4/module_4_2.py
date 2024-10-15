def test_fuction():
    def inner_function():
        print('Я в области видимости функции test_function')
    inner_function()

test_fuction()
# inner_function() запуск этой функции все test_function() выдаст ошибку, т.к. она находится
# в локальной области видимости этой функции и из глобальной недоступна
