import numpy as np
import matplotlib.pyplot as plt
from prettytable import PrettyTable


# функция 15 вариант
def f(x, y):
    return np.sin(x) * np.exp(-y ** 2) / (1 + x ** 2 + y ** 2)

all_max_fits=[]
x1 = 0
x2 = 2
y1 = -2
y2 = 2
x_array = [i * 0.01 for i in range(200)]
y_array = [-2 + i * 0.01 for i in range(400)]

# график
X, Y = np.meshgrid(x_array, y_array)
Z = f(X, Y)

fig, ax = plt.subplots(subplot_kw=dict(projection='3d'))
ax.plot_surface(X, Y, Z, cmap=plt.get_cmap('plasma'))


plt.savefig('lab05-function.png')
plt.show()


def average_fit(fits):
    # Подсчет среднего значения фитнес-функции
    return sum(fits) / len(fits)

def add_row(generation, fits, k):

    for i in range(len(generation)):
        if i != (len(generation) - 1):
            mytable1.add_row(["", generation[i][0],
                              generation[i][1], fits[i], "", ""])
        else:
            mytable1.add_row([k, generation[i][0],
                              generation[i][1], fits[i],
                              fits[i], average_fit(fits)])
            mytable1.add_row(["", "", "", "", "", ""])


def generate_xy():
    x_ = np.random.uniform(x1, x2)
    y_ = np.random.uniform(y1, y2)
    return [x_, y_]


def crossover(generation, fits):
    points = list(generation)
    new_points = [[points[3][0], points[2][1]], [points[2][0], points[3][1]], [points[3][0], points[1][1]],
                  [points[1][0], points[3][1]]]
    # так как generation отсортировано ,то 0 не трогаем- худший
    # 3 - лучший - скрещиваем

    generation.clear()
    fits.clear()
    for point in new_points:
        fit = f(point[0], point[1])
        fits.append(fit)
        generation.append(point)
    fits.sort()
    generation = sort_generation(generation, fits)
    return [generation, fits]


def mutation(generation, fits):
    def mutation_point(point):
        delta_x = np.random.uniform(-0.05, 0.05)
        delta_y = np.random.uniform(-0.05, 0.05)

        new_x = delta_x + point[0]
        new_y = delta_y + point[1]
        return [new_x, new_y]

    for i in range(len(generation)):
        # мутация с вероятностью 10%
        probability = np.random.uniform(0, 1)
        if probability > 0.9:
            new_point = mutation_point(generation[i])
            generation[i] = new_point
            fits[i] = f(new_point[0], new_point[1])
    return [generation, fits]


def sort_generation(generation, fits):
    new_generation = []
    for i in range(len(fits)):
        for j in range(len(generation)):
            if f(generation[j][0], generation[j][1]) == fits[i]:
                new_generation.append(generation[j])
                break
    return new_generation


# 0 поколение
generation = []
fits = []
for i in range(4):
    point = generate_xy()
    fit = f(point[0], point[1])
    generation.append(point)
    fits.append(fit)

fits.sort()
generation = sort_generation(generation, fits)
all_max_fits.append(average_fit(fits))
mytable1 = PrettyTable()
mytable1.field_names = ["N", "X", "Y", "FIT",
                        "максимальный результат", "средний результат"]
mytable1.float_format = '.8'
i = 0
add_row(generation, fits, i)
# генетический алгоритм c 10 поколениями
for i in range(100):
    population = crossover(generation, fits)
    generation = population[0]
    fits = population[1]
    fits.sort()
    generation = sort_generation(generation, fits)
    mutation(generation, fits)
    fits.sort()
    generation = sort_generation(generation, fits)
    if i!=99:
        all_max_fits.append(average_fit(fits))
    i += 1
    if i % 10 == 0  or i<=10:
        add_row(generation, fits, i)

print(mytable1, "\n")


plt.ylabel('FIT')
plt.xlabel('N')
plt.grid(True)
k=[i for i in range(100)]
plt.plot(k,all_max_fits)
plt.savefig('lab05-2.png')
plt.show()
