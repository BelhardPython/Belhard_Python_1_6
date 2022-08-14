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
    data_list = {}
    if not all(isinstance(i, int) for i in args):
        raise TypeError('Все позиционные аргументы должны быть целыми')
    data_list['args_sum'] = sum(args)
    if not all(isinstance(i, str) for i in kwargs.values()):
        raise TypeError('Все аргументы - ключевые слова должны быть строками')
    data_list['kwargs_max_len'] = len(max(kwargs.values(), key=len))
    return data_list


print(dict_from_args(1, 2, 3, k='aratdghd', a='rtu'))
