"""
Большой подвиг 6. (Для закрепления предыдущего материала). Вводится таблица целых чисел (см. пример ниже)
размером N x N элементов (N определяется по входным данным). Эта таблица содержит нули, но кое-где - единицы.
С помощью функции с именем verify, на вход которой передается двумерный список чисел, необходимо проверить,
являются ли единицы изолированными друг от друга, то есть, вокруг каждой единицы должны быть нули.

Рекомендуется следующий алгоритм. В функции verify производить перебор двумерного списка.
Для каждого элемента (списка) со значением 1 вызывать еще одну вспомогательную функцию verify
для проверки изолированности единицы. То есть, функция verify должна возвращать True,
если единица изолирована и False - в противном случае.

Как только встречается не изолированная единица, функция verify должна возвращать False.
Если успешно доходим (по элементам списка) до конца, то возвращается значение True.

Функцию выполнять не нужно, только определить.

P. S. При реализации функции verify не следует прописывать восемь операторов if. Подумайте,
как это можно сделать красивее (с точки зрения реализации алгоритма). 

Sample Input:
1 0 0 0 0
0 0 1 0 0
0 0 0 0 0
0 1 0 1 0
0 0 0 0 0

Sample Output:
True

"""


def verify(lst):
    flag = True
    for i in range(len(lst) - 1):
        for j in range(len(lst[i]) - 1):
            if lst[i][j] + lst[i][j+1] + lst[i+1][j] + lst[i+1][j+1] > 1:
                flag = False
                break
    return flag


# ----- test № 1 -----
if verify([[1, 0, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 0, 0], [0, 1, 0, 1, 0], [0, 0, 0, 0, 0]]) == True:
    print('test №1 was successful')
else:
    print('test №1 failed')

# ----- test № 2 -----
if verify([[1, 0, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 0, 0], [0, 1, 0, 1, 0], [0, 1, 0, 0, 0]]) == False:
    print('test №2 was successful')
else:
    print('test №2 failed')

# ----- test № 3 -----
if verify([[1, 0, 0], [0, 0, 1], [0, 0, 0], [0, 1, 0], [0, 1, 0]]) == False:
    print('test №3 was successful')
else:
    print('test №3 failed')
