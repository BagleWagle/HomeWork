
def  test_function():

    def inner_function():
       print("Я в области видимости функции test_function")
    inner_function()
    return

test_function()
print(globals())
# inner_function() # выдет ошибку, потому что находиться внутри функции, и не попадает в глобальное простанство имен.

"""
Домашнее задание по уроку "Пространство имен"

Создайте новый проект в PyCharm
Запустите созданный проект
Ваша задача:
Создайте новую функцию test_function
Создайте внутри test_function другую функцию - inner_function, Эта функция должна печатать значение "Я в области видимости функции test_function"
Вызовите функцию inner_function внутри функции test_function
Попробуйте вызывать inner_function вне функции test_function и посмотрите на результат выполнения программы
"""