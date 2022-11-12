import numpy as np
import matplotlib.pyplot as plt

"""5 вариант"""

vec_of_wood = ['A-береза', 'B-сосна', 'C-дуб', 'D-лиственница']
wood = [[7, 8, 7, 2], [6, 5, 8, 6], [3, 4, 9, 3], [4, 3, 10, 7]]  # ХАРАКТЕРИСТИКИ
weights = [6, 5, 8, 4]  # ВЕСА


def rationing(param):
    """Нормализация вектора весов критериев"""
    sum = 0
    for i in range(len(param)):
        sum += param[i]
    for i in range(len(param)):
        param[i] /= sum
    return param


def max_min(wood):
    """Нахождение макс и мин по всем критериям """
    min = []
    max = []

    for j in range(4):
        min_current = 10
        max_current = 0
        for i in range(len(wood)):
            if wood[i][j] < min_current:
                min_current = wood[i][j]
            if wood[i][j] > max_current:
                max_current = wood[i][j]
        max.append(max_current)
        min.append(min_current)
    return max, min


def main_argument():
    def matrix_rationing():
        max, min = (max_min(wood))
        for i in range(len(wood)):
            for j in range(len(wood[i])):
                if j != 2:
                    wood[i][j] = (wood[i][j] - min[j]) / (max[j] - min[j])
        print("Нормированная матрица оценок альтернатив \n", wood[0], "\n",
              wood[1], "\n", wood[2], "\n", wood[3])
        max, min = (max_min(wood))
        answer = wood[0]
        index = 0
        limit_price = 0.5 * max[0]
        limit_proccesing = 0.2 * max[1]
        limit_resistance = 0.3 * max[3]
        for i in range(len(wood)):
            if wood[i][2] >= answer[2] and wood[i][0] >= limit_price and wood[i][1] >= limit_proccesing and \
                    wood[i][
                        3] >= limit_resistance:
                answer = wood[i]
                index = i
        for i in range((len(woods))):
            if i == index:
                print("ответ методом замены критериев ограничениями:")
                print(vec_of_wood[i], "\n")
                break

    """0-береза  1- сосна   2 - дуб   3- лиственница """
    """ вектор  весов  критериев """
    params = [6, 5, 8, 4]
    print("Исходная матрица критериев \n", wood[0], "\n", wood[1], "\n", wood[2], "\n", wood[3])
    rationing(params)
    print("Нормированные веса =", round(params[0], 2), round(params[1], 2), round(params[2], 2), round(params[3], 2))
    # Выберем в качестве главного критерия  долговечность (критерий 3- индекс 2 ).
    matrix_rationing()


def pareto():
    def chebyshev_distance(first_values, third_values):
        utopia_point_x = 10
        utopia_point_y = 10
        answer = 0
        min = utopia_point_x
        for i in range(len(first_values)):
            min_current = max(utopia_point_x - first_values[i], utopia_point_y - third_values[i])
            if min_current <= min:
                answer = i
                min = min_current
        return answer

    wood = [[7, 8, 7, 2], [6, 5, 8, 6], [3, 4, 9, 3], [4, 3, 10, 7]]
    """Выберим критерии  1(0) и 3(2) как главные"""
    first_values = [wood[0][0], wood[1][0], wood[2][0], wood[3][0]]
    third_values = [wood[0][2], wood[1][2], wood[2][2], wood[3][2]]

    plt.plot(first_values, third_values)
    plt.xlabel('Cheap')
    plt.ylabel('Durability')
    plt.grid(True)
    plt.savefig('lab06.png')
    plt.show()
    print("ответ методом формирования множества Парето:")
    print(vec_of_wood[chebyshev_distance(first_values, third_values)], "\n")


def weighing_combining_criteria():
    def rationing(criteria):
        """Нормализуем их"""
        sum = 0
        for i in range(len(criteria)):
            sum += i + 1
        for i in range(len(criteria)):
            criteria[i] /= sum
        return criteria

    print("Методом взвешивания коэффициентов:")
    """Расставим веса методом ранжирования """
    weight_criteria = [3, 2, 4, 1]
    sum_ = sum(weight_criteria)
    for i in range(len(weight_criteria)):
        weight_criteria[i] /= sum_
    print("нормированный вектор коэффициентов:", weight_criteria)
    matrix_params = np.array([weight_criteria[0], weight_criteria[1], weight_criteria[2], weight_criteria[3]])
    wood = [[7, 8, 7, 2], [6, 5, 8, 6], [3, 4, 9, 3], [4, 3, 10, 7]]
    max, min = (max_min(wood))
    for i in range(len(wood)):
        for j in range(len(wood[i])):
            wood[i][j] = round((wood[i][j] - min[j]) / (max[j] - min[j]), 2)

    wood_matrix = np.array([wood[0], wood[1], wood[2], wood[3]])
    print("нормированный матрица:\n", wood_matrix)
    a = wood_matrix.dot(matrix_params)
    answer = 0
    for i in range(len(a)):
        if a[i] > a[answer]:
            answer = i

    print("Ответ:", a, "\n", vec_of_wood[answer], "\n")


def analysis_hierarchies(woods):
    sums = []
    norm_matrix = []
    matrix_normal_sums = []

    def lymba_max(norm_matrix):
        e = np.array([1, 1, 1, 1])
        matrix_sum = np.array([norm_matrix[0], norm_matrix[1], norm_matrix[2], norm_matrix[3]])
        buf = e.dot(matrix_sum)
        res = buf.dot(normal_sum)
        return res

    for k in range(len(woods[0])):
        print("матрица по критерию:", k + 1)
        print("A\t  B\t   C\t   D  сумма ")
        for i in range(len(woods)):
            f = []
            sum = 0
            for j in range(len(woods)):
                wood = [[7, 8, 7, 2], [6, 5, 8, 6], [3, 4, 9, 3], [4, 3, 10, 7]]
                f.append(round(wood[i][k] / wood[j][k], 3))
                sum += round(f[j], 2)
            sums.append(sum)
            norm_matrix.append(f)
            print(f, sum)
        print("Нормированная сумма")

        all_sums = 0
        normal_sum = []
        for i in range(len(woods)):
            all_sums += sums[i]
        for i in range(len(woods)):
            round_normal = round(sums[i] / all_sums, 2)
            normal_sum.append(round_normal)
            matrix_normal_sums.append(round_normal)
            print(round_normal)

        print("Отношение согласованности=", (lymba_max(norm_matrix) - len(woods)) / (len(woods) - 1))
        sums.clear()

    print("Оценка вектора критериев:")
    norm1_matrix = []
    weight = [6, 5, 8, 4]
    for i in range(len(weight)):
        f = []
        sum = 0
        for j in range(len(weight)):
            f.append(round(weight[i] / weight[j], 3))
            sum += round(f[j], 3)
        sums.append(sum)
        norm1_matrix.append(f)

        print(f, sum)
    all_sums = 0
    normal_sum = []
    for i in range(len(woods)):
        all_sums += sums[i]
    for i in range(len(woods)):
        """Нормируем сумму по строке """
        round_normal = round(sums[i] / all_sums, 2)
        normal_sum.append(round_normal)

    print("Нормированная сумма  ", normal_sum)
    print("Отношение согласованности=", -(lymba_max(norm1_matrix) - len(woods)) / (len(woods) - 1))
    mat = np.array([[matrix_normal_sums[0], matrix_normal_sums[4], matrix_normal_sums[8], matrix_normal_sums[12]],
                    [matrix_normal_sums[1], matrix_normal_sums[5], matrix_normal_sums[9], matrix_normal_sums[13]],
                    [matrix_normal_sums[2], matrix_normal_sums[6], matrix_normal_sums[10], matrix_normal_sums[14]],
                    [matrix_normal_sums[3], matrix_normal_sums[7], matrix_normal_sums[11], matrix_normal_sums[15]]
                    ])
    print(mat)
    result = mat.dot(normal_sum)
    print("Итого:", result)
    answer = 0
    for i in range(len(result)):
        if result[i] >= result[answer]:
            answer = i
    print("Ответ методом анализа иерархий:")
    print(vec_of_wood[answer], "\n")


woods = [[7, 8, 7, 2], [6, 5, 8, 6], [3, 4, 9, 3], [4, 3, 10, 7]]
main_argument()
pareto()
weighing_combining_criteria()
analysis_hierarchies(woods)
