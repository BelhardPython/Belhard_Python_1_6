"""
Написать функцию count_char, которая принимает строковое значение STR_VAL,
из которого создает и возвращает словарь, следующего вида:
{
    'буква': количество-вхождений-в-строку
}

например: {
    'p': 2,
    'y': 1,
    ...
}

Нельзя пользоваться collections.Counter!
"""
from collections import defaultdict

STR_VAL = 'python is the fastest-growing major programming language'


def count_char(STR_VAL):
    res = defaultdict(int)
    for i in STR_VAL:
        res[i] += 1
    return res


print(count_char(STR_VAL)