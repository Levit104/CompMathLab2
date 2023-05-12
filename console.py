from validation import valid_value, valid_accuracy_params, valid_interval_or_approximation_params


def get_value(description, min_value=1.0, max_value=2.0, is_strict=False):
    value = input(f'\n{description}: ').strip()

    while not valid_value(value, min_value, max_value, is_strict):
        print('Невалидное значение')
        value = input('Повторите ввод: ').strip()

    return value


def get_data_for_equation_from_console():
    return get_accuracy(), get_interval()


def get_data_for_system_from_console():
    return get_accuracy(), get_initial_approximation()


def get_accuracy():
    return float(get_value('Введите точность', *valid_accuracy_params))


def get_interval():
    left_bound = get_value('Введите левую границу интервала', *valid_interval_or_approximation_params)
    right_bound = get_value('Введите правую границу интервала', *valid_interval_or_approximation_params)
    return [float(left_bound), float(right_bound)]


def get_initial_approximation():
    x0 = get_value('Введите начальное приближение x', *valid_interval_or_approximation_params)
    y0 = get_value('Введите начальное приближение y', *valid_interval_or_approximation_params)
    return [float(x0), float(y0)]


def get_iteration_limit():
    return int(get_value('Введите лимит итераций', min_value=1, max_value=float('inf'))) - 1


def print_dictionary(name, dictionary, value_is_tuple=False, value_tuple_index=1, systems=False):
    print(f'\n{name}:', end='')
    for key, value in dictionary.items():
        if value_is_tuple:
            value = value[value_tuple_index]

        if not systems:
            print(f'\n\t{key}. {value}', end='')
        else:
            print(f'\n\t{key}. {value[0]}\n\t\t{value[1]}', end='')
    print()


def print_equation_results_to_console(x, fx, iter_count, iter_table):
    print_iteration_table_to_console(iter_table)
    print()
    print(f'Кол-во итераций: {iter_count}')
    print(f'Корень уравнения: {x}')
    print(f'Значение функции в корне: {fx}')


def print_system_results_to_console(x, y, fxy, gxy, iter_count, iter_table):
    print_iteration_table_to_console(iter_table)
    print()
    print(f'Кол-во итераций: {iter_count}')
    print(f'Корни системы: x = {x}, y = {y}')
    print(f'Значений ф-ций системы в корнях: f(x, y) = {fxy}, g(x, y) = {gxy}')


def print_iteration_table_to_console(iter_table):
    print('\nТаблица итераций:')
    for row in iter_table:
        for val in row:
            if row == iter_table[0]:
                print(f'{val:>10}\t', end='')
            else:
                print(f'{round(val, 5):>10}\t', end='')
        print()
