import numpy as np
import matplotlib.pyplot as plt
import random
from prettytable import PrettyTable


# функция 15 вариант
def f1(x):
    return x * x * np.sin(x)


def f2(x):
    return x * x * np.sin(x) * np.sin(5 * x)


x = np.linspace(8, 13, 100)
f1_plot = x * x * np.sin(x)
f2_plot = x * x * np.sin(x) * np.sin(5 * x)
plt.plot(x, f1_plot)
plt.title("x*x*sin(x)")
plt.ylabel('Y')
plt.xlabel('X')
plt.grid(True)
plt.savefig('lab03-function1.png')
plt.show()
plt.title("x*x*sin(x)* sin(5x)")
plt.ylabel('Y')
plt.xlabel('X')
plt.grid(True)
plt.plot(x, f2_plot)
plt.savefig('lab03-function2.png')
plt.show()

a = 9
b = 12
Tmax = 10000
Tmin = 0.1
T_current = Tmax
x_current = random.uniform(a, b)
f_x_current = float(f1(x_current))
i = 1

mytable1 = PrettyTable()
mytable1.field_names = ["N", "T", "x", "f(x)", "P", "accept?",
                        "    ", "x best", "f(x) best"]
mytable1.add_row([i, T_current, x_current, f_x_current, 1, "Y",
                  "", x_current, f_x_current])

while T_current > Tmin:
    i += 1
    x_new = random.uniform(a, b)
    f_x_new = float(f1(x_new))
    delta_f = f_x_new - f_x_current

    if delta_f <= 0:
        x_current = x_new
        P = 1
    else:
        # вероятность выбора
        P = np.e ** (-delta_f / T_current)
        x_current = np.float_(random.choices([float(x_new), float(x_current)],
                                             weights=[P, 1 - P]))
    f_x_current = float(f1(x_current))
    T_current *= 0.95

    if x_current == x_new:
        accept = "Y"
    else:
        accept = "-"
    mytable1.add_row([i, T_current, x_new, f_x_new, P, accept,
                      "", np.float_(x_current), f_x_current])

print("Для функции x*x*sin(x):")
mytable1.float_format = '.3'
print(mytable1, "\n")
print("Результат: x= ", "%.3f" % np.float_(x_current),
      "\tf(x)= ", "%.3f" % f_x_current, "\n")

# для мультимодальной функции :
T_current = Tmax
x_current = random.uniform(a, b)
f_x_current = float(f2(x_current))
i = 1

mytable2 = PrettyTable()
mytable2.field_names = ["N", "T", "x", "f(x)", "P", "accept?",
                        "    ", "x best", "f(x) best"]
mytable2.add_row([i, T_current, x_current, f_x_current, 1, "Y",
                  "", x_current, f_x_current])

while T_current > Tmin:
    i += 1
    x_new = random.uniform(a, b)
    f_x_new = float(f2(x_new))
    delta_f = f_x_new - f_x_current

    if delta_f <= 0:
        x_current = x_new
        P = 1
    else:
        # вероятность выбора
        P = np.e ** (-delta_f / T_current)
        x_current = np.float_(random.choices([float(x_new), float(x_current)],
                                             weights=[P, 1 - P]))
    f_x_current = float(f2(x_current))
    T_current *= 0.95

    if x_current == x_new:
        accept = "Y"
    else:
        accept = "-"
    mytable2.add_row([i, T_current, x_new, f_x_new, P, accept,
                      "", np.float_(x_current), f_x_current])

print("Для функции x*x*sin(x)*sin(5x):")
mytable2.float_format = '.3'
print(mytable2, "\n")
print("Результат: x= ", "%.3f" % np.float_(x_current),
      "\tf(x)= ", "%.3f" % f_x_current, "\n")
