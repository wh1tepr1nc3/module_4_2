def test_function():
    # print('Я в области видимости функции test_function')
    def inner_function():
        print('Я в области видимости функции test_function')
        inner_function()


# inner_function() ---> выдает ошибку
test_function()
