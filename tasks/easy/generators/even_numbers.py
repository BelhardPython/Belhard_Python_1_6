"""
Написать генератор get_even_number, который возвращает подряд четные числа

Например:

even_gen = get_even_number()

next(even_gen) -> 2
next(even_gen) -> 4
next(even_gen) -> 6
"""


def get_even_number(n):
    for i in range(n):
        yield 2 * i


for item in get_even_number(3):
    print(item)

even_gen = get_even_number(3)
next(even_gen)
