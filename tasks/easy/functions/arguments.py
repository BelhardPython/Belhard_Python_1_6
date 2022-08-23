"""
Написать функцию dict_from_args, которая принимает неограниченное
количество позиционных аргументов и неограниченное количество аргументов
ключевых-слов.

Если все позиционные аргументы - целые числа, то рассчитать их сумму. Если
нет, то кинуть ошибку TypeError("Все позиционные аргументы должны быть целыми").
Проверить, что все аргументы целые можно с помощью функции all:
https://pyneng.readthedocs.io/ru/latest/book/10_useful_functions/all_any.html

Если все аргументы - ключевые слова являются строками, то найти максимальную
длину слова. Если нет, то кинуть ошибку TypeError("Все аргументы - ключевые
слова должны быть строками").

Функция должна вернуть словарь, вида:
{
    "args_sum": 13,
    "kwargs_max_len": 7
}
"""


def dict_from_args(*args, **kwargs):
    res_1 = 0
    res_2 = 0
    for i in args:
        if (isinstance(i, int)) is True:
            res_1 += i
        elif i is None:
            res_1 = res_1
        else:
            raise TypeError("Все позиционные аргументы должны быть целыми")
    for j in kwargs.items():
        if isinstance(j, str) is True:
            res_2 = max(len(j))
        elif j is None:
            res_2 = res_2
        else:
            raise TypeError("Все аргументы - ключевые слова должны быть строками")
    return(f"args_sum: {res_1}, kwargs_max_len: {res_2}")


print(dict_from_args(7, 9, 10))
