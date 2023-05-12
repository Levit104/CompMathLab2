from common import *
from console import print_dictionary, get_value, get_interval
from equations_systems import equations, systems
from methods import equation_methods, system_methods
from graph import draw_equation_graph, draw_system_graph
from util import find_root_intervals

EQUATIONS_NUMBER = len(equations)
SYSTEMS_NUMBER = len(systems)
EQUATION_METHODS_NUMBER = len(equation_methods)
SYSTEM_METHODS_NUMBER = len(system_methods)


def solve_equation():
    print_dictionary('Нелинейные уравнения', equations, value_is_tuple=True)
    equation_id = int(get_value('Выберите уравнение', max_value=EQUATIONS_NUMBER))
    equation, equation_string = equations[equation_id]

    draw_equation_graph(equation, equation_string, -5, 5)

    print_dictionary('Методы', equation_methods, value_is_tuple=True)
    method_id = int(get_value('Выберите метод', max_value=EQUATION_METHODS_NUMBER))
    method, method_string = equation_methods[method_id]

    print_dictionary('Режимы ввода', input_output_modes)
    input_id = int(get_value('Укажите откуда вводить данные'))
    get_data = get_data_for_equation[input_id]
    accuracy, interval = get_data()

    root_interval = find_root_intervals(equation, interval, accuracy)
    while root_interval is None:
        interval = get_interval()
        root_interval = find_root_intervals(equation, interval, accuracy)

    a, b = root_interval[0], root_interval[1]

    draw_equation_graph(equation, equation_string, a, b)

    x, fx, iter_count, iter_table = method(equation, a, b, accuracy)

    print_dictionary('Режимы вывода', input_output_modes)
    output_id = int(get_value('Укажите куда вывести результат'))
    print_results_function = print_equation_results[output_id]
    print_results_function(x, fx, iter_count, iter_table)


def solve_system():
    print_dictionary('Системы нелинейных уравнений', systems, value_is_tuple=True, systems=True)
    system_id = int(get_value('Выберите систему', max_value=SYSTEMS_NUMBER))
    system, system_string = systems[system_id]
    system = system()

    draw_system_graph(system, system_string)

    # print_dictionary('Методы', system_methods, value_is_tuple=True)
    # method_id = int(get_value('Выберите метод', max_value=SYSTEM_METHODS_NUMBER))
    method_id = 1
    method, method_string = system_methods[method_id]

    print_dictionary('Режимы ввода', input_output_modes)
    input_id = int(get_value('Укажите откуда вводить данные'))
    get_data = get_data_for_system[input_id]
    accuracy, approximations = get_data()

    x0, y0 = approximations[0], approximations[1]
    x, y, fxy, gxy, iter_count, iter_table = method(system, x0, y0, accuracy)

    print_dictionary('Режимы вывода', input_output_modes)
    output_id = int(get_value('Укажите куда вывести результат'))
    print_results_function = print_system_results[output_id]
    print_results_function(x, y, fxy, gxy, iter_count, iter_table)

    if abs(system[0](x, y)) <= accuracy and abs(system[1](x, y)) <= accuracy:
        print('Решение корректно')
    else:
        print('Решение некорректно')


if __name__ == '__main__':
    while True:
        try:
            print('\nЧтобы выйти из программы введите exit на любом этапе')

            print_dictionary('Виды уравнений', tasks)
            task = int(get_value('Укажите, что решать'))

            if task == EQUATION:
                solve_equation()
            else:
                solve_system()

        except (EOFError, KeyboardInterrupt):
            print("\nВыход из программы")
            break
