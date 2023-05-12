from console import get_iteration_limit
from util import derivative, double_derivative, partial_derivative_x, partial_derivative_y


# ---------------------------------Уравнения---------------------------------
def bisection(f, a, b, eps):
    if f(a) * f(b) >= 0:
        return None, None, None, None

    n = 0
    x = (a + b) / 2
    deviation = abs(a - b)
    iter_table = ['№,a,b,x,f(a),f(b),f(x),|a - b|'.split(','), [n, a, b, x, f(a), f(b), f(x), deviation]]

    while deviation > eps or abs(f(x)) > eps:
        n += 1

        if f(a) * f(x) < 0:
            b = x
        else:
            a = x

        deviation = abs(a - b)
        x = (a + b) / 2
        iter_table.append([n, a, b, x, f(a), f(b), f(x), deviation])

    return x, f(x), n + 1, iter_table


def find_initial_approximation(f, a, b, eps):
    d2a = double_derivative(f, a)
    d2b = double_derivative(f, b)
    if f(a) * d2a > 0:
        return a, a + eps
    elif f(b) * d2b > 0:
        return b, b - eps
    else:
        if abs(f(a)) <= abs(f(b)):
            return a, a + eps
        else:
            return b, b - eps


def check_condition_for_convergence(d1, d2):
    iter_limit = float("inf")
    if abs(d1) >= 1 or abs(d2) >= 1:
        print('Условие сходимости не выполняется')
        iter_limit = get_iteration_limit()
    return iter_limit


def secant(f, a, b, eps):
    a, b = find_initial_approximation(f, a, b, eps)

    n = 0
    fa, fb = f(a), f(b)
    x = b - fb * (b - a) / (fb - fa)
    fx = f(x)
    deviation = abs(x - b)
    iter_table = ['№,x_(i-1),x_i,x_(i+1),f(x_(i+1)),|x_(i+1) - x_i|'.split(','), [n, a, b, x, fx, deviation]]

    while abs(fx) > eps or deviation > eps:
        n += 1
        a, b = b, x
        fa, fb = fb, fx
        x = b - fb * (b - a) / (fb - fa)
        fx = f(x)
        deviation = abs(x - b)
        iter_table.append([n, a, b, x, fx, deviation])

    return x, f(x), n + 1, iter_table


def simple_iteration(f, a, b, eps):
    dfa = derivative(f, a)
    dfb = derivative(f, b)
    lambda_coefficient = -1 / max(abs(dfa), abs(dfb))

    dphia = 1 + lambda_coefficient * dfa
    dphib = 1 + lambda_coefficient * dfb
    print(f'\ndphia = {dphia}; dphib = {dphib}')
    iter_limit = check_condition_for_convergence(dphia, dphib)

    n = 0
    x = a if abs(dfa) >= abs(dfb) else b
    phix = x + lambda_coefficient * f(x)
    fphix = f(phix)
    deviation = abs(phix - x)
    iter_table = ['№,x_i,x_(i+1),f(x_(i+1)),|x_(i+1) - x_i|'.split(','), [n, x, phix, fphix, deviation]]

    while (abs(fphix) > eps or deviation > eps) and n < iter_limit:
        n += 1
        x = phix
        phix = x + lambda_coefficient * f(x)
        fphix = f(phix)
        deviation = abs(phix - x)
        iter_table.append([n, x, phix, fphix, deviation])

    if n == iter_limit:
        print('\nПревышен лимит итераций')

    return phix, fphix, n + 1, iter_table


# ---------------------------------Системы---------------------------------
def newton(system, x0, y0, eps):
    x, y = x0, y0

    f = system[0]
    g = system[1]

    n = 0
    delta_x, delta_y = float('inf'), float('inf')

    iter_limit = get_iteration_limit()
    iter_table = ['№,x,y,x^(i+1) - x^i,y^(i+1) - y^i'.split(',')]

    while (abs(delta_x) > eps or abs(delta_y) > eps) and n < iter_limit:
        n += 1

        matrix = [[partial_derivative_x(f, x, y), partial_derivative_y(f, x, y)],
                  [partial_derivative_x(g, x, y), partial_derivative_y(g, x, y)]]

        constant_terms = [-f(x, y), -g(x, y)]

        det = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

        if det == 0:
            print('Определитель матрицы равен нулю')
            return None, None, None, None, None, None

        delta_x = (constant_terms[0] * matrix[1][1] - constant_terms[1] * matrix[0][1]) / det
        delta_y = (constant_terms[1] * matrix[0][0] - constant_terms[0] * matrix[1][0]) / det
        x += delta_x
        y += delta_y

        iter_table.append([n, x, y, abs(delta_x), abs(delta_y)])

    return x, y, f(x, y), g(x, y), n + 1, iter_table


# ---------------------------------Общее---------------------------------
equation_methods = {
    1: (bisection, 'Метод половинного деления'),
    2: (secant, 'Метод секущих'),
    3: (simple_iteration, 'Метод простой итерации')
}

system_methods = {
    1: (newton, 'Метод Ньютона')
}
