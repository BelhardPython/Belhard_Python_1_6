"""
Написать рекурсивную функцию factorial, которая будет возвращать n-ый элемент

5! = 1 * 2 * 3 * 4 * 5 = 125
"""


def factorial(n):
    if (n <= 1):
        result = 1
    else:
        result = n * factorial(n - 1)
    return result

# n = int(input("Введите число:"))
# print("Факториал числа равен:")
# print(factorial(n))
