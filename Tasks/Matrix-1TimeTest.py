# Task 4.2

import numpy as np
import timeit

print("\n#ВРЕМЯ#")

code_to_test = """
import numpy as np

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

test_matrix = np.random.randint(-20, 20, (3, 3)).tolist()

a = getInvMatrix(test_matrix)
"""

code_to_test_np = """
import numpy as np

test_matrix = np.random.randint(-20, 20, (3, 3))

a = np.linalg.inv(test_matrix)
"""

code_to_test_np_without_np_array = """
import numpy as np

test_matrix = np.random.randint(-20, 20, (3, 3))

a = np.linalg.inv(test_matrix)
"""

print("Тесты по времени проходили для матрицы:")
test_matrix = np.array([[2, 5, 7], [6, 3, 4], [5, -2, -3]])
print(test_matrix)

print()

elapsed_time = timeit.timeit(code_to_test, number=100) / 100
print(str(elapsed_time) + " времени заняло выполнение кода, написанного вручную")

elapsed_time_np = timeit.timeit(code_to_test_np, number=100) / 100
print(str(elapsed_time_np) + " времени заняло определение обратной матрицы с помощью numpy")

elapsed_time_np = timeit.timeit(code_to_test_np_without_np_array, number=100) / 100
print(
    str(elapsed_time_np) + " времени заняло определение обратной матрицы с помощью numpy без использования конструкции np.array()")
