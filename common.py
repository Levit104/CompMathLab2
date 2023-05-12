from console import get_data_for_equation_from_console, print_equation_results_to_console, \
    print_system_results_to_console, get_data_for_system_from_console
from file import get_data_from_file, print_equation_results_to_file, print_system_results_to_file

CONSOLE = 1
FILE = 2

input_output_modes = {
    CONSOLE: 'Консоль',
    FILE: 'Файл'
}

get_data_for_equation = {
    CONSOLE: get_data_for_equation_from_console,
    FILE: get_data_from_file
}

get_data_for_system = {
    CONSOLE: get_data_for_system_from_console,
    FILE: get_data_from_file
}

print_equation_results = {
    CONSOLE: print_equation_results_to_console,
    FILE: print_equation_results_to_file
}

print_system_results = {
    CONSOLE: print_system_results_to_console,
    FILE: print_system_results_to_file
}

EQUATION = 1
SYSTEM = 2

tasks = {
    EQUATION: 'Нелинейное уравнение',
    SYSTEM: 'Система нелинейных уравнений'
}
