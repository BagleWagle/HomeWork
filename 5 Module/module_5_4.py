class House:

    houses_history = []

    def __new__(cls, name, number_of_floor):
        cls.houses_history.append(name)
        return super().__new__(cls)

    def __init__(self, name, number_of_floor):
        self.name = name
        self.number_of_floors = int(number_of_floor)

    def __del__(self):
        print(f'{self.name} снесён, но он останется в истории.')
        del self


    def go_to(self, new_floor):
        if self.number_of_floors >= new_floor >= 1:
            for i in range(0, new_floor):
                    print(i + 1)
        else:
            print('Такого этажа не существует!')

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f'Название: {self.name}, кол-во этажей: {self.number_of_floors}'

    def __eq__(self, other):
        if isinstance(other.number_of_floors, int):
            return self.number_of_floors == other.number_of_floors

    def __lt__(self, other):
        if isinstance(other.number_of_floors, int):
             return self.number_of_floors < other.number_of_floors

    def __le__(self, other):
        if isinstance(other.number_of_floors, int):
            return self.number_of_floors <= other.number_of_floors

    def __gt__(self, other):
        if isinstance(other.number_of_floors, int):
            return self.number_of_floors > other.number_of_floors

    def __ge__(self, other):
        if isinstance(other.number_of_floors, int):
            return self.number_of_floors >= other.number_of_floors

    def __ne__(self, other):
        if isinstance(other.number_of_floors, int):
            return self.number_of_floors != other.number_of_floors

    def __add__(self, value):
        if isinstance(value, int) == True:
            self.number_of_floors += value
            return self

    def __radd__(self, value):
        if isinstance(value, int):
            self.number_of_floors = value + self.number_of_floors
            return self

    def __iadd__(self, value):
        if isinstance(value, int):
            self.number_of_floors += value
            return self



h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)
# Удаление объектов
del h2
del h3
print(House.houses_history)


"""
Задача "История строительства":
Для решения этой задачи будем пользоваться решением к предыдущей задаче "Перегрузка операторов".
В классе House создайте атрибут houses_history = [], который будет хранить названия созданных объектов.
Правильней вписывать здание в историю сразу при создании объекта, тем более можно удобно обращаться к атрибутам класса используя ссылку на сам класс - cls.
Дополните метод __new__ так, чтобы:
Название объекта добавлялось в список cls.houses_history.
Название строения можно взять из args по индексу.
Также переопределите метод __del__(self) в котором будет выводиться строка:
"<название> снесён, но он останется в истории"
Создайте несколько объектов класса House и проверьте работу методов __del__ и __new__, а также значение атрибута houses_history.

Пример выполнения программы:
h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)
# Удаление объектов
del h2
del h3
print(House.houses_history)
"""