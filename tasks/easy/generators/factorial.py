"""
Написать генератор factorial, который возвращает подряд значения факториала

Например:

factorial_gen = factorial()

next(factorial_gen) -> 1
next(factorial_gen) -> 2
next(factorial_gen) -> 6
next(factorial_gen) -> 24
"""
def factorial(n):
    item = 1
    for i in range(2, n+1):
        yield item *=  i
for item in factorial(3):
    print(item)

factorial_gen = factorial(3)
next(factorial_gen)