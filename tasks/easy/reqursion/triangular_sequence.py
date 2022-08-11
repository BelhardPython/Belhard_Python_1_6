"""
Написать функцию triangular_sequence, которая принимает n и возвращает
последовательность следующего вида:

1
22
333
4444
55555
...

Например:

n = 3:
1
22
333

n = 6:
1
22
333
4444
55555
666666
"""

def triangular_sequence(n):
    if n == 0:
        return n
    triangular_sequence(n - 1)
    return print(str(n) * n)

# n = int(input("Введите число членов последовательности:"))
# print(triangular_sequence(n))
