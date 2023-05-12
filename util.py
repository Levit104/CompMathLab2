from console import get_value


def derivative(f, x, h=0.00000001):
    return (f(x + h) - f(x)) / h


def double_derivative(f, x, h=0.00000001):
    return (f(x + h) - 2 * f(x) + f(x - h)) / (h ** 2)


def partial_derivative_x(f, x, y, h=0.00000001):
    return (f(x + h, y) - f(x, y)) / h


def partial_derivative_y(f, x, y, h=0.00000001):
    return (f(x, y + h) - f(x, y)) / h


def find_root_intervals(f, interval, eps):
    a, b = interval[0], interval[1]
    root_count = 0
    left_y = f(a)
    root_intervals = [a]
    x = a
    while x < b + eps:
        right_y = f(x)
        if left_y * right_y < 0:
            root_count += 1
            root_intervals.append(x)
            left_y = right_y
        x += eps
    root_intervals[-1] = b

    if root_count == 0:
        print('\nНа данном интервале нет корней')
        return None
    elif root_count == 1:
        print('\nНа данном интервале один корень')
        return root_intervals
    else:
        print(f'\nНа данном интервале несколько корней (найдено {root_count})')
        for i in range(root_count):
            print(f'{i + 1}. [{root_intervals[i]:.5f}, {root_intervals[i + 1]:.5f}]')

        root_interval_id = int(get_value('Выберите интервал', max_value=root_count))
        return [root_intervals[root_interval_id - 1], root_intervals[root_interval_id]]
