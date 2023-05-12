import math
import numpy as np


def f1(x):
    return x ** 3 - x + 4


def f2(x):
    return x ** 2 + 20 * np.cos(x)


def f3(x):
    return x ** 3 - 0.5 * x ** 2 - 1.5 * x + 0.4


def system1():
    def f(x, y):
        return x ** 2 + y ** 2 - 4

    def g(x, y):
        return -3 * x ** 2 + y

    return [f, g]


def system2():
    def f(x, y):
        return 0.2 * x ** 2 + 0.3 * y ** 2 + x - 0.5

    def g(x, y):
        return 0.4 * x ** 2 - 0.2 * x * y + y - 0.5

    return [f, g]


equations = {
    1: (f1, 'x^3 - x + 4 = 0'),
    2: (f2, 'x^2 + 20cos(x)'),
    3: (f3, 'x^3 - 0.5 * x^2 - 1.5 * x + 0.4')
}

systems = {
    1: (system1, ['x^2 + y^2 - 4 = 0', '-3x^2 + y = 0']),
    2: (system2, ['0.2 * x^2 + 0.3 * y^2 + x - 0.5', '0.4 * x^2 - 0.2 * x * y + y - 0.5'])
}
