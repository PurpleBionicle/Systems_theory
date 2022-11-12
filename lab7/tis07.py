import math
import numpy as np
import matplotlib.pyplot as plt
import random
from prettytable import PrettyTable

# функция 15 вариант
"""Среднее гармоническое"""
"""Метрика Чебышева"""

a = 1 / 4


def f1(x):
    return 0.5 + np.sin(x)


def f2(x):
    return f1(x) + random.uniform(-a, a)


K = 100
x_min = 0
x_max = np.pi
x = [x_min + k * (x_max - x_min) / K for k in range(K)]

f1_plot = []
f2_plot = []
for i in range(K):
    f1_plot.append(f1(x[i]))
    f2_plot.append(f2(x[i]))

"""График функции"""
plt.plot(x, f1_plot, label="clear", color=(1, 0.7, 0))
plt.plot(x, f2_plot, label=" interference", color=(1, 0, 0))
plt.ylabel('Y')
plt.xlabel('X')
plt.grid(True)
plt.legend()
plt.savefig('lab07-1.png')
plt.show()


def Harmonic_mean(f, K, r):
    M = int((r - 1) / 2)
    f_harm = []
    alfa = [0 for g in range(2 * M + 1)]
    alfa[M] = random.uniform(0, 1)
    if M >= 2:
        for m in range(M - 1):
            """Веса"""
            sum_ = 0
            for s in range(r - 1 - 2):
                s_ = s + 2
                sum_ += alfa[s_]

            m_ = m + 2
            alfa[m_ - 1] = 0.5 * random.uniform(0, 1 - sum_)
            alfa[r - m_] = alfa[m_ - 1]

    alfa[0] = 0.5 * (1 - sum(alfa))
    alfa[len(alfa) - 1] = alfa[0]

    for k in range(K - 2 * M):
        res = 0
        k_ = k + M
        for i in range(2 * M + 1):
            i_ = k_ - M + i - 1
            res += (alfa[i_ + 1 + M - k_]) / f[i_]
        res = res ** (-1)
        f_harm.append(res)
    return alfa, f_harm


def Chebyshev_distance_for_interference(f):
    max = 0
    for i in range(len(f) - 1):
        i_ = i + 1
        if abs(f[i_ - 1] - f[i_]) >= max:
            max = abs(f[i_ - 1] - f[i_])
    return max


def Chebyshev_distance_for_difference(f_harmonic, f_inter):
    max = 0
    for i in range(len(f_harmonic)):
        if abs(f_harmonic[i] - f_inter[i]) >= max:
            max = abs(f_harmonic[i] - f_inter[i])
    return max


# скольщяее окно
r = [3, 5]
P = 0.95  # вероятность попадания в окрестность экстремума
L = 10
lyambda = [l / L for l in range(L + 1)]  # веса свертки
e = 0.01  # интервал неопределенности

N = math.ceil((np.log(1 - P)) / np.log((1 - (e) / (x_max - x_min))))
print("Необходимое число испытаний = ", N, '\n')

alfa, f_harmonic = Harmonic_mean(f2_plot, K, r[0])
w = Chebyshev_distance_for_interference(f_harmonic)
delta = Chebyshev_distance_for_difference(f_harmonic, f2_plot)

for qq in range(len(r)):
    mytable1 = PrettyTable()
    mytable1.field_names = ["lymbda", "dist", "alfa", "w", "d", "J"]
    mytable1.float_format = '.4'
    answer_harmonic = []
    answer_j = 1
    answer_d = 1
    answer_dist = 1
    answer_w = 1
    answer_lyambda = 1
    for i in range(len(lyambda)):

        min = 1
        min_w = 1
        min_delta = 1
        dist = 1
        alfa_min = []
        for j in range(N):
            alfa, f_harmonic = Harmonic_mean(f2_plot, K, r[qq])
            w = Chebyshev_distance_for_interference(f_harmonic)

            delta = Chebyshev_distance_for_difference(f_harmonic, f2_plot)

            J = lyambda[i] * w + (1 - lyambda[i]) * delta
            if J < min:
                min = J
                min_w = w
                min_delta = delta
                alfa_min = np.round(alfa, 4)
                dist = max(min_w, min_delta)
        mytable1.add_row([lyambda[i], dist, alfa_min, min_w, min_delta, min])
        if dist < answer_dist:
            answer_dist = dist
            answer_j = min
            answer_harmonic = f_harmonic
            answer_d = min_delta
            answer_w = min_w
            answer_lyambda = lyambda[i]
    print("для r=", r[qq])
    print(mytable1, "\n")
    mytable2 = PrettyTable()
    mytable2.field_names = ["lyambda", "J", "w", "d"]
    mytable2.add_row([answer_lyambda, answer_j, answer_w, answer_d])
    print(mytable2, "\n")

    plt.plot(x, f1_plot, label="clear", color=(1, 0.7, 0))
    plt.plot(x, f2_plot, label=" interference", color=(1, 0, 0))
    plt.plot(x[0:len(answer_harmonic)], answer_harmonic, label="filter", color=(0, 1, 0))
    plt.ylabel('Y')
    plt.xlabel('X')
    plt.legend()
    plt.grid(True)
    plt.savefig('lab07-2.png')
    plt.show()
