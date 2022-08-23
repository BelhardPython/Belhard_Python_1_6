"""
Написать генератор fibonacci, которая принимает номер значения num_count
из чисел Фибоначчи и выводит на экран результат до заданного значения.

Номер значения нужно проверить

Пример:

fibonacci(0) -> raise ValueError('Введите значение больше 1')
fibonacci(5)
1
2
3
5
8
Traceback (most recent call last):
File «C:/Python/Python3/python_generator.py», line 29, in
print(next(fib))
StopIteration
"""


def fibonacci(num_count):
    if num_count == 0:
        raise ValueError('Введите значение больше 1')
    else:
        fib1, fib2 = 0, 1
        for i in range(num_count):
            fib1, fib2 = fib2, fib1 + fib2
            yield fib1


for fib1 in fibonacci(10):
    print(fib1)

fibonacci_gen = fibonacci(10)
next(fibonacci_gen)
