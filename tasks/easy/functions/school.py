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


def incr_students(school_data, class_name):
    key_value = school_data.get(class_name) + 1
    school_data.update({class_name: key_value})


def decr_students(school_data, class_name):
    key_value = school_data.get(class_name) - 1
    if key_value >= 0:
        school_data.update({class_name: key_value})


def add_class(school_data, class_name):
    school_data[class_name] = 0


def remove_class(school_data, class_name):
    school_data.pop(class_name)


def calc_students(school_data):
    number_of_students = sum(school_data.values())
    return number_of_students
