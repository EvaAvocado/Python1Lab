# Task 3

import numpy as np


# Функции, применяемые в работе
# Ввод количества строк в матрице
def enterRows():
    while True:
        try:
            a = int(int(input("Введите количество строк в матрице\n")))
            if a <= 0:
                print("Введите число, которое больше 0")
            else:
                return a
        except ValueError:
            print("Вы ввели неправильно, введите целое число")


# Ввод матрицы
def enterMatrix(a):
    enter_matrix = []
    print("Введите элементы через пробел, следующая строка через enter")
    for i in range(a):
        enter_matrix.append(list(map(int, input("").split())))
    return enter_matrix


isChoose = False
while not isChoose:
    choice = input("Что вы хотите сделать?\n1)Транспонировать матрицу\n2)Умножить матрицы\n3)Определить ранг матрицы\n")
    try:
        choice = int(choice)
        if choice != 1 and choice != 2 and choice != 3:
            print("Введите число 1, 2 или 3")
        else:
            isChoose = True
    except ValueError:
        print("Вы ввели неправильно, введите целое число")

# Если было выбрано транспонирование
if choice == 1:
    rows = enterRows()
    matrix = enterMatrix(rows)
    matrix = np.array(matrix)

    trans_matrix = np.array(matrix).transpose()

    # Выводим матрицы
    print("Вы ввели:")
    print(matrix)

    print("\nТранспонированная матрица:")
    print(trans_matrix)

# Если было выбрано умножение
if choice == 2:
    isEnterTwoMatrix = False
    while not isEnterTwoMatrix:
        print("ВВЕДИТЕ ПЕРВУЮ МАТРИЦУ")
        rows1 = enterRows()
        matrix1 = enterMatrix(rows1)
        columns1 = len(matrix1[0])
        matrix1 = np.array(matrix1)

        print("ВВЕДИТЕ ВТОРУЮ МАТРИЦУ")
        rows2 = enterRows()
        matrix2 = enterMatrix(rows2)
        columns2 = len(matrix2[0])
        matrix2 = np.array(matrix2)

        if columns1 != rows2:
            print("Такие матрицы перемножить нельзя! Попробуйте снова\n")
        else:
            isEnterTwoMatrix = True

    matrix_product = np.dot(matrix1, matrix2)

    print("Вы ввели матрицы:")
    print(matrix1)
    print("")
    print(matrix2)

    print("\nПри умножении матриц получается:")
    print(matrix_product)

# Если было выбрано определение ранга матрицы
if choice == 3:
    rows = enterRows()
    rank_matrix = enterMatrix(rows)
    columns = len(rank_matrix[0])
    rank_matrix = np.array(rank_matrix)

    print("Вы ввели матрицу:")
    print(rank_matrix)

    rank = np.linalg.matrix_rank(rank_matrix)

    print("\nРанг данной матрицы = " + str(rank))
