# Task 2

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


# Замена двух строк матрицы
def swapRows(swap_matrix, row1, row2, col):
    for i in range(col):
        temp = swap_matrix[row1][i]
        swap_matrix[row1][i] = swap_matrix[row2][i]
        swap_matrix[row2][i] = temp


# Начало программы
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
    columns = len(matrix[0])

    # Инициализуем новую матрицу, которая в будущем станет транспонированной
    trans_matrix = [[0 for row in range(rows)] for column in range(columns)]

    # Делаем транспонированную матрицу, меняя строки со столбцами
    for row in range(rows):
        for column in range(columns):
            trans_matrix[column][row] = matrix[row][column]

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

        print("ВВЕДИТЕ ВТОРУЮ МАТРИЦУ")
        rows2 = enterRows()
        matrix2 = enterMatrix(rows2)
        columns2 = len(matrix2[0])

        if columns1 != rows2:
            print("Такие матрицы перемножить нельзя! Попробуйте снова\n")
        else:
            isEnterTwoMatrix = True

    # Умножаем матрицы
    matrix_product = []

    for i in range(rows1):
        row = []
        for j in range(columns2):
            product = 0
            for k in range(len(matrix1[i])):
                product += matrix1[i][k] * matrix2[k][j]
            row.append(product)

        matrix_product.append(row)

    print("Вы ввели матрицы:")
    print(matrix1)
    print(matrix2)

    print("\nПри умножении матриц получается:")
    print(matrix_product)

# Если было выбрано определение ранга матрицы
if choice == 3:
    rows = enterRows()
    rank_matrix = enterMatrix(rows)
    columns = len(rank_matrix[0])

    print("Вы ввели матрицу:")
    print(rank_matrix)

    rank = columns

    for row in range(0, rank, 1):
        diagonal_el = 0
        try:
            diagonal_el = rank_matrix[row][row]
        except IndexError:
            continue
        finally:
            # Диагональный элемент не ноль
            if diagonal_el != 0:
                for col in range(0, rows, 1):
                    if col != row:

                        # Преобразовываем все записи текущего столбца в ноль, кроме matrix[row][row]
                        multiplier = (rank_matrix[col][row] /
                                      rank_matrix[row][row])
                        for i in range(rank):
                            rank_matrix[col][i] -= (multiplier *
                                                    rank_matrix[row][i])
            else:
                reduce = True

                # Найти ненулевой элемент в текущем столбце
                for i in range(row + 1, rows, 1):
                    if rank_matrix[i][row] != 0:
                        # Поменять местами строку с ненулевым элементом с этой строкой
                        swapRows(rank_matrix, row, i, rank)
                        reduce = False
                        break

                if reduce:
                    # Уменьшить количество столбцов
                    rank -= 1
                    for i in range(0, rows, 1):
                        rank_matrix[i][row] = rank_matrix[i][rank]

                row -= 1

    print("\nРанг данной матрицы = " + str(rank))
