import numpy as np
import matplotlib.pyplot as plt
import random
from prettytable import PrettyTable


# функция
def f1(x):
    return x * x * np.e ** (np.sin(x))


def f2(x):
    return x * x * np.e ** (np.sin(x)) * np.sin(5 * x)


x = np.linspace(8, 15, 100)
f1_plot = x * x * np.e ** (np.sin(x))
f2_plot = x * x * np.e ** (np.sin(x)) * np.sin(5 * x)
plt.plot(x, f1_plot)
plt.title("x*x*eps[sin(x)]")
plt.ylabel('Y')
plt.xlabel('X')
plt.grid(True)
plt.savefig('lab02-function1.png')
plt.show()
plt.title("x*x*eps[sin(x)]* sin(5x)")
plt.ylabel('Y')
plt.xlabel('X')
plt.grid(True)
plt.plot(x, f2_plot)
plt.savefig('lab02-function2.png')
plt.show()

a = 9
b = 14
v = float(b - a)
P = [0.90 + (i / 100) for i in range(10)]
q = [0.005 * (i + 1) for i in range(20)]
e = []
for i in range(len(q)):
    e_current = (b - a) * q[i]
    e.append(e_current)
P1 = []
for i in range(len(e)):
    P_1 = 1 - (e[i] / v)
    P1.append(P_1)
print("Вероятность непопадания в случае одного испытания:")
mytable1 = PrettyTable()
mytable1.field_names = ["e", "P"]
for j in range(len(e)):
    mytable1.add_row([round(e[j], 5), round(P1[j], 5)])
print(mytable1, "\n")

N = []
for i in range(len(q)):
    for j in range(len(P)):
        N_cur = np.math.ceil(np.math.log(1 - P[j]) / np.math.log(1 - q[i]))
        N.append(N_cur)

mytable2 = PrettyTable()
# имена полей таблицы
mytable2.field_names = ["q/P", *P]
i = 0
for j in range(len(q)):
    mytable2.add_row([q[j], *N[i:i + 10]])
    i += 10
print("необходимое  число  испытаний  N")
print(mytable2, "\n")
# создадим пустой  массив
cur = []

for i in range(len(N)):  # len(N)=200
    for j in range(N[i]):
        result = float(f1(random.uniform(a, b)))
        if j == 0:
            min = result
        if result < min:
            min = result
    cur.append(float(min))

mytable3 = PrettyTable()
# имена полей таблицы
mytable3.field_names = ["q/P", *P]
i = 0
for j in range(len(q)):
    mytable3.add_row([q[j], *cur[i:i + 10]])
    i += 10
print("для функции x*x*exp[sin(x)]")
mytable3.float_format = '.4'
print(mytable3, "\n")

cur2 = []

for i in range(len(N)):  # len(N)=200
    for j in range(N[i]):
        result = float(f2(random.uniform(a, b)))
        if j == 0:
            min = result
        if result < min:
            min = result
    cur2.append(float(min))

mytable4 = PrettyTable()
# имена полей таблицы
mytable4.field_names = ["q/P", *P]
mytable4.float_format = '.4'
i = 0
for j in range(len(q)):
    mytable4.add_row([q[j], *cur2[i:i + 10]])
    i += 10
print("для функции x*x*exp[sin(x)]*sin(5*x)")
print(mytable4, "\n")

# график зависимостей погрешности от числа точек N
# на одно значение q -одно значение е ,но 10 значений N  - вся строка
N_average = []
k = N_sum = 0

for i in range(len(q)):  # len(q)=20 - номер строки
    for j in range(len(P)):  # len(P)=10 - вся строка
        N_sum += N[10 * k + j]
    k += 1
    N_average.append(N_sum / len(P))
    N_sum = 0
delta = []  # погрешность
for i in range(len(e)):
    delta_current = e[i] / 2
    delta.append(delta_current)
plt.plot(N_average, delta)
plt.title("Зависимость погрешности от числа точек N")
plt.ylabel('∆')
plt.xlabel('N')
plt.grid(True)
plt.savefig('lab02-addiction.png')
plt.show()
