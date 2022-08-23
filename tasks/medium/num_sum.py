"""
Написать рекурсивную функцию sum_of_numbers, которая будет вычислять сумму
цифр целого числа.

Можно пользоваться только функциями, операторами и условиями.
"""


def sum_of_numbers(n):
    list_1 = []
    res = 0
    list_1 = list(str(n))
    for i in list_1:
        res += int(i)
    return res


print(sum_of_numbers(179))
