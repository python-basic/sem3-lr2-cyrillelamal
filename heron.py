import math


def get_sides():
    a = float(input('a side: '))
    b = float(input('b side: '))
    c = float(input('c side: '))
    return heron(a, b, c)


def heron(a, b, c):
    p = 1/2 * (a + b + c)
    return math.sqrt(p*(p-a)*(p-b)*(p-c))


print(get_sides())
