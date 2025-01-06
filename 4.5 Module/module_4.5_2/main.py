from sortfunc import *

data_1 = list(map(int, input("Введите числа для пузырьковой через пробел! ").split())) # 1 2 3 4 5 6
data_2 = list(map(int, input("Введите числа для выборочной через пробел! ").split())) # 1 2 3 4 5 6
data_3 = list(map(int, input("Введите для вставочной через пробел! ").split())) # 1 2 3 4 5 6

bubble_sort(data_1)
selection_sort(data_2)
insertion_sort(data_3)

print("Пузырек ", data_1)
print("Выбор", data_2)
print("Вставоч", data_3)

print(globals())



