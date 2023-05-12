import numpy as np
import matplotlib.pyplot as plt


def draw_equation_graph(f, f_string, a, b):
    x = np.linspace(a - 1, b + 1, 100)
    y = f(x)

    plt.grid()
    plt.axvline(x=0, color='black')
    plt.axhline(y=0, color='black')
    plt.title(f'График функции ${f_string}$')
    plt.xlabel('x')
    plt.ylabel('y')

    plt.plot(x, y)
    plt.show()


def draw_system_graph(system, system_string):
    x, y = np.meshgrid(np.linspace(-6, 6, 120), np.linspace(-6, 6, 120))
    f = system[0](x, y)
    g = system[1](x, y)

    plt.grid()
    plt.axvline(x=0, color='black')
    plt.axhline(y=0, color='black')
    plt.title(f'График системы ${system_string[0]}$\n\t\t\t${system_string[1]}$')
    plt.xlabel('x')
    plt.ylabel('y')

    plt.contour(x, y, f, levels=[0], colors='dodgerblue')
    plt.contour(x, y, g, levels=[0], colors='red')
    plt.show()
