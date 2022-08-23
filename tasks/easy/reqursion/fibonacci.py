"""
Написать рекурсивную функцию fibonacci, которая будет возвращать n-ый элемент
"""


def fibonacci(n):
    if n <= 1:
        return n
    else:
        return (fibonacci(n - 1) + fibonacci(n - 2))


n = int(input("Введите число членов последовательности:"))
print("Последовательность Фибоначчи:")
print(fibonacci(n - 1))
