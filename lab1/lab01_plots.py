import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(8, 15, 100)
f1_plot = x * x * np.e ** (np.sin(x))
plt.title("x*x*eps[sin(x)]")
plt.ylabel('Y')
plt.xlabel('X')
plt.grid(True)
plt.plot(x, f1_plot)
plt.savefig('lab01-function.png')
plt.show()
N = [i for i in range(100)]  # число точек
b = 14
a = 9  # границы отрезка
e = []
inaccuracy = []
for i in range(len(N)):
    e_current = float((2 * (b - a)) / (N[i] + 1))  # интервал неопределенности
    inaccuracy_curent = float(e_current / 2)
    inaccuracy.append(inaccuracy_curent)

plt.plot(N, inaccuracy, label="passive")
e_dichotomy = [5, 2.51, 1.265, 0.6425, 0.33125, 0.175625]  # значения взяты из lab1.cpp
inaccuracy_dichotomy = []
N = [i for i in range(6)]
for i in range(len(e_dichotomy)):
    inaccuracy_curent = float(e_dichotomy[i] / 2)
    inaccuracy_dichotomy.append(inaccuracy_curent)

plt.plot(N, inaccuracy_dichotomy, label="dichotomy")
plt.legend()
plt.ylabel('∆')
plt.xlabel('N')
plt.grid(True)
plt.savefig('addiction.png')
plt.show()
