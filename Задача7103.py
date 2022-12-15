"""
Подвиг 3. Используя замыкания функций, объявите внутреннюю функцию, которая заключает в тег h1 строку s
(s - строка, параметр внутренней функции). Далее, на вход программы поступает строка и ее нужно поместить
в тег h1 с помощью реализованного замыкания. Результат выведите на экран.
P. S. Пример добавления тега h1 к строке "Python": <h1>Python</h1>

Sample Input:
Balakirev

Sample Output:
<h1>Balakirev</h1>
"""


def format_str():

    def add_tag_to_string(str):
        print(f'<h1>{str}</h1>')
    
    return add_tag_to_string


str1 = format_str()
str1('Balakirev')