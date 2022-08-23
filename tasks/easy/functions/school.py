"""
Написать композицию из функций (не чистых функций)

Имеется словарь SCHOOL_DATA с данными школы класс-количество учеников

- Функция incr_students, которая принимает SCHOOL_DATA, название класса и
    увеличивает количество учеников на 1
- Функция decr_students, которая принимает SCHOOL_DATA, название класса и
    уменьшает количество учеников на 1, но не меньше 0
- Функция add_class, которая принимает SCHOOL_DATA, название класса и добавляет
    класс в словарь с количеством учеников 0
- Функция remove_class, которая принимает SCHOOL_DATA, название класса и удаляет
    класс из словаря
- Функция calc_students, которая принимает SCHOOL_DATA и возвращает кол-во
    учеников во всей школе
"""
school_data = {
    '1a': 15,
    '1b': 23,
    '2a': 13,
    '2b': 30
}


def incr_students(collection):
    res = {}
    for value in collection.values():
        for key in collection.keys():
            value = collection.get(key)
            res[key] = value + 1
    return res


print(incr_students(school_data))


def decr_students(collection):
    res = {}
    for value in collection.values():
        for key in collection.keys():
            value = collection.get(key)
            if value == 0:
                res[key] = 0
            else:
                res[key] = value - 1
    return res


print(decr_students(school_data))


def add_class(collection, str_1):
    res = collection.update({str_1: 0})
    return res


print(add_class(school_data, "5A"))


def calc_students(collection):
    res = sum(collection.values())
    return res


print(calc_students(school_data))


def remove_class(collection, str_3):
    res = collection.pop(str_3)
    return res


print(add_class(school_data, "1a"))
