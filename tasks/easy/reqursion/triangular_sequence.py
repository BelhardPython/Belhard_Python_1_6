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


def triangular_sequence(n: object) -> object:
    if (n <= 1):
        return n
    else:
        return triangular_sequence(n - 1), str(n) * n
    for i in range(n):
        print(f"{triangular_sequence(i)}\n")


print(triangular_sequence(5))
