# Task 4.1

import numpy as np


# Ввод матрицы 3 на 3
def enterMatrix():
    while True:
        enter_matrix = []
        print("Введите элементы через пробел, следующая строка через enter")
        for i in range(3):
            enter_matrix.append(list(map(int, input("").split())))

        if len(enter_matrix[0]) == 3 and len(enter_matrix[1]) == 3 and len(enter_matrix[2]) == 3:
            return enter_matrix
        else:
            print("Введите по три элемента в каждой строке. Должна получиться матрица 3 на 3")


# Вычисляем определитель матрицы
def getDeterminant(matrix, mul=1):
    width = len(matrix)
    if width == 1:
        return mul * matrix[0][0]
    else:
        sign = -1
        answer = 0
        for i in range(width):
            m = []
            for j in range(1, width):
                buff = []
                for k in range(width):
                    if k != i:
                        buff.append(matrix[j][k])
                m.append(buff)
            sign *= -1
            answer = answer + mul * getDeterminant(m, sign * matrix[0][i])
    return answer


# Транспонирование
def transposition(matrix):
    rows = 3
    columns = 3

    trans_matrix = [[0 for row in range(rows)] for column in range(columns)]

    for row in range(rows):
        for column in range(columns):
            trans_matrix[column][row] = matrix[row][column]

    return trans_matrix


# Нахождение минора
def getMinor(m, i, j):
    return [row[:j] + row[j + 1:] for row in (m[:i] + m[i + 1:])]


# Находим обратную матрицу
def getInvMatrix(matrix):
    determinant = getDeterminant(matrix)

    if determinant == 0:
        return False

    cofactors = []
    for r in range(len(matrix)):
        cofactorRow = []
        for c in range(len(matrix)):
            minor = getMinor(matrix, r, c)
            cofactorRow.append(((-1) ** (r + c)) * getDeterminant(minor))
        cofactors.append(cofactorRow)

    cofactors = transposition(cofactors)

    for r in range(len(cofactors)):
        for c in range(len(cofactors)):
            cofactors[r][c] = cofactors[r][c] / determinant

    return cofactors


# Начало программы
print("#НАХОЖДЕНИЕ ОБРАТНОЙ МАТРИЦЫ#")
enter_matrix = enterMatrix()
matrix_inverse = getInvMatrix(enter_matrix)

if not matrix_inverse:
    print("Определитель матрицы равен нулю. Найти обратную невозможно")
else:
    print("Ваша матрица:")
    print(enter_matrix)

    print("Обратная матрица, высчитанная с помощью кода, написанного вручную:")
    print(matrix_inverse)

    print("Обратная матрица, высчитанная с помощью numpy:")
    print(np.linalg.inv(enter_matrix))
