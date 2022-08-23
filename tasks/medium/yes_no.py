"""
Напишите функцию yes_or_no, которая принимает список из целых чисел,
проходит по нему и выводит Yes, если число уже встречалось и No, если нет
"""


def yes_or_no(list_1):
    list_2 = []
    for i in list_1:
        if i in list_2:
            yield "Yes"
            list_2.append(i)
        else:
            yield "No"
            list_2.append(i)


list_1 = [1, 3, 5, 6, 7, 1, 3]
for item in yes_or_no(list_1):
    print(item)

yes_or_no_gen = yes_or_no(list_1)
next(yes_or_no_gen)
