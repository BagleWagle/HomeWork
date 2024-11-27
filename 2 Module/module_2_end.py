digit = 0
while True:
    try:
        digit = int(input("Введите число от 3 до 20 что бы узнать пароль: "))
    except:
        print("Это явно не число!!!")
        continue
    if digit >= 3 and digit <= 20:
        break
numbers = list(range(1, digit + 1))
result = []
for i in numbers:
    for j in numbers:
        for g in numbers:
            if digit == i and i % (j + g) == 0 and j < g and g < i and j < i and i >= 3:
                result.append(j)
                result.append(g)
            elif digit == i and j < g and g < i and j < i and i >= 3 and (j + g) % i == 0:
                result.append(j)
                result.append(g)
print("Пароль от числа", digit, "=", ''.join(map(str, result)))

"""
Дополнительное практическое задание по модулю: "Основные операторы"
Цель: Применить знания полученные в модуле, решив задачу повышенного уровня сложности
Задание "Слишком древний шифр":
Вы отправились в путешествие на необитаемый остров и конечно же в очередной вылазке в джунгли вы попали в ловушку местному племени (да-да, классика "Индиана Джонса").
К вашему удивлению, в племени были неплохие математики и по совместительству фантазёры.
Вы поняли это, когда после долгих блужданий перед вами появились ворота (выход из ловушки) с двумя каменными вставками для чисел.
В первом поле камни с числом менялись постоянно (от 3 до 20) случайным образом, а второе было всегда пустым.
К вашему счастью рядом с менее успешными и уже неговорящими путешественниками находился папирус, где были написаны правила для решения этого "ребуса". (Как жаль, что они поняли это так поздно :( ).
Во вторую вставку нужно было написать те пары чисел друг за другом, чтобы число из первой вставки было кратно(делилось без остатка) сумме их значений.
Пример кратности(деления без остатка):
1 + 2 = 3 (сумма пары)
9 / 3 = 3 (ровно 3 без остатка)
9 кратно 3 (9 делится на 3 без остатка)

Пример 1:
9 - число из первой вставки
1218273645 - нужный пароль (1 и 2, 1 и 8, 2 и 7, 3 и 6, 4 и 5 - пары; число 9 кратно сумме каждой пары)

Пример 2:
11 - число из первой вставки
11029384756 - нужный пароль (1 и 10, 2 и 9, 3 и 8, 4 и 7, 5 и 6 - пары; число 11 кратно сумме каждой пары)
К сожалению, у вас не так много времени, чтобы подбирать пароль вручную, шипы сверху уже движутся на вас (обожаю клише), тем более числа в первой вставке будут попадаться случайно.
Составьте алгоритм, используя циклы, чтобы в независимости от введённого числа n (от 3 до 20) программа выдавала нужный пароль result, для одного введённого числа.
Что является парой?:
Пары являются уникальными на примере следующего:
7 3 3 5 8
В этой последовательности уникальными парами являются:
Для первой 7: 73 73 75 78
Для второй 3: 33 35 38 (с первой 7 у этой 3 уже есть пара, поэтому её не берём).
"""