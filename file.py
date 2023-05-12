from validation import valid_file, valid_accuracy, valid_interval_or_approximation


def get_data_from_file():
    path = get_file()

    with open(path, 'r') as file:
        data = file.read().split()

        if len(data) != 3:
            print('Неверное кол-во строк в файле')
            return get_data_from_file()

        accuracy = data.pop(0)
        interval_or_approximation = data

        if not valid_accuracy(accuracy):
            print('Точность не валидна')
            return get_data_from_file()
        if not valid_interval_or_approximation(interval_or_approximation):
            print('Границы интервала/Начальные приближения не валидны')
            return get_data_from_file()

        return float(accuracy), [float(val) for val in interval_or_approximation]


def get_file(validate=True):
    path = input('\nВведите путь до файла: ').strip()

    if validate:
        while not valid_file(path):
            print('Файла не существует или он пустой')
            path = input('Повторите ввод: ').strip()

    return path


def print_equation_results_to_file(x, fx, iter_count, iter_table):
    path = get_file(validate=False)
    with open(path, 'w', encoding='utf-8') as file:
        print_iteration_table_to_file(iter_table, file)
        file.write('\n')
        file.write(f'Кол-во итераций: {iter_count}\n')
        file.write(f'Корень уравнения: {x}\n')
        file.write(f'Значение функции в корне: {fx}\n')


def print_system_results_to_file(x, y, fxy, gxy, iter_count, iter_table):
    path = get_file(validate=False)
    with open(path, 'w', encoding='utf-8') as file:
        print_iteration_table_to_file(iter_table, file)
        file.write('\n')
        file.write(f'Кол-во итераций: {iter_count}\n')
        file.write(f'Корни системы: x = {x}, y = {y}\n')
        file.write(f'Значений ф-ций системы в корнях: f(x, y) = {fxy}, g(x, y) = {gxy}\n')


def print_iteration_table_to_file(iter_table, file):
    file.write('Таблица итераций:\n')
    for row in iter_table:
        for val in row:
            if row == iter_table[0]:
                file.write(f'{val:>10}\t')
            else:
                file.write(f'{round(val, 5):>10}\t')
        file.write('\n')
